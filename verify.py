#!/usr/bin/env python3
"""Exact finite checks for the natural PSL(2,q) action. Standard library only.

No network calls, model APIs, or nonstandard dependencies. Python >= 3.10.
The infinite classification is proved separately in PROOF.md.
"""
import argparse
import hashlib
import itertools
import json
import math
from pathlib import Path


def prime_power(q):
    if q < 2:
        raise ValueError(q)
    for p in range(2, math.isqrt(q) + 1):
        if q % p == 0:
            n, degree = q, 0
            while n % p == 0:
                n //= p
                degree += 1
            if n != 1:
                raise ValueError(f"{q} is not a prime power")
            return p, degree
    return q, 1


def digits(n, p, length):
    out = []
    for _ in range(length):
        out.append(n % p)
        n //= p
    return out


def remainder(poly, divisor, p):
    work = list(poly)
    while work and work[-1] == 0:
        work.pop()
    while len(work) >= len(divisor):
        scale, offset = work[-1], len(work) - len(divisor)
        for i, value in enumerate(divisor):
            work[offset + i] = (work[offset + i] - scale * value) % p
        while work and work[-1] == 0:
            work.pop()
    return work


def irreducible_polynomial(p, degree):
    for encoded in range(1, p ** degree):
        coeff = digits(encoded, p, degree) + [1]
        if coeff[0] == 0:
            continue
        irreducible = True
        for d in range(1, degree // 2 + 1):
            for other in range(p ** d):
                divisor = digits(other, p, d) + [1]
                if not remainder(coeff, divisor, p):
                    irreducible = False
                    break
            if not irreducible:
                break
        if irreducible:
            return coeff
    raise AssertionError("No irreducible polynomial found")


class Field:
    def __init__(self, q):
        self.q = q
        self.p, self.degree = prime_power(q)
        p, m = self.p, self.degree
        self.modulus = None if m == 1 else irreducible_polynomial(p, m)
        self.add = [[0] * q for _ in range(q)]
        self.mul = [[0] * q for _ in range(q)]
        reps = [digits(x, p, m) for x in range(q)]
        for x, y in itertools.product(range(q), repeat=2):
            self.add[x][y] = sum(((reps[x][i] + reps[y][i]) % p) * p ** i for i in range(m))
            if m == 1:
                self.mul[x][y] = x * y % p
            else:
                work = [0] * (2 * m - 1)
                for i in range(m):
                    for j in range(m):
                        work[i + j] = (work[i + j] + reps[x][i] * reps[y][j]) % p
                reduced = remainder(work, self.modulus, p)
                self.mul[x][y] = sum(v * p ** i for i, v in enumerate(reduced))
        self.neg = [next(y for y in range(q) if self.add[x][y] == 0) for x in range(q)]
        self.inv = [None] + [next(y for y in range(1, q) if self.mul[x][y] == 1) for x in range(1, q)]
        self.squares = {self.mul[x][x] for x in range(1, q)}

    def sub(self, x, y):
        return self.add[x][self.neg[y]]

    def div(self, x, y):
        assert y != 0
        return self.mul[x][self.inv[y]]

    def chi(self, x):
        assert self.p != 2
        return 0 if x == 0 else (1 if x in self.squares else -1)

    def field_checks(self):
        # Exhaustive associativity and distributivity for these small fields.
        A, M, q = self.add, self.mul, self.q
        checks = 0
        for x, y, z in itertools.product(range(q), repeat=3):
            assert A[A[x][y]][z] == A[x][A[y][z]]
            assert M[M[x][y]][z] == M[x][M[y][z]]
            assert M[x][A[y][z]] == A[M[x][y]][M[x][z]]
            checks += 3
        return checks


def determinant(F, matrix):
    a, b, c, d = matrix
    return F.sub(F.mul[a][d], F.mul[b][c])


def action(F, matrix, x):
    a, b, c, d = matrix
    if x == F.q:  # Infinity is encoded by q.
        return F.q if c == 0 else F.div(a, c)
    denominator = F.add[F.mul[c][x]][d]
    return F.q if denominator == 0 else F.div(F.add[F.mul[a][x]][b], denominator)


def projective_group(F):
    # Normalize the first nonzero entry of an invertible matrix to 1.
    # Its first row is nonzero, so only these two charts are needed.
    candidates = itertools.chain(
        ((1, b, c, d) for b, c, d in itertools.product(range(F.q), repeat=3)),
        ((0, 1, c, d) for c, d in itertools.product(range(F.q), repeat=2)),
    )
    triples = {}
    permutations = set()
    for matrix in candidates:
        det = determinant(F, matrix)
        if det == 0 or (F.p != 2 and det not in F.squares):
            continue
        permutation = tuple(action(F, matrix, x) for x in range(F.q + 1))
        assert len(set(permutation)) == F.q + 1
        triple = tuple(action(F, matrix, x) for x in (F.q, 0, 1))
        assert triple not in triples
        triples[triple] = matrix
        permutations.add(permutation)
    expected = F.q * (F.q * F.q - 1) // math.gcd(2, F.q - 1)
    assert len(triples) == len(permutations) == expected
    return triples


def cube_patterns(q, a, b, c):
    return [tuple(pair[bit] for pair, bit in zip(((q, a), (0, b), (1, c)), bits))
            for bits in itertools.product((0, 1), repeat=3)]


def character_cube(F, a, b, c):
    if F.p == 2:
        return True
    C = F.chi
    if C(c) != 1 or C(F.sub(1, b)) != 1 or C(F.sub(c, b)) != 1:
        return False
    return len({C(a), C(F.sub(a, 1)), C(F.sub(a, b)), C(F.sub(a, c))}) == 1


def predicted_dimension(q):
    return 1 if q == 2 else (2 if q in (3, 4, 5, 7, 11) else 3)


def check_paley_parameters(F):
    if F.p == 2:
        return {"applicable": False}
    q = F.q
    if q % 4 == 1:
        nonneighbors = [x for x in range(1, q) if F.chi(x) == -1]
        degrees = [sum(F.chi(F.sub(y, x)) == 1 for y in nonneighbors) for x in nonneighbors]
        assert len(nonneighbors) == (q - 1) // 2
        assert set(degrees) == {(q - 1) // 4}
        return {"applicable": True, "type": "nonneighbor_induced_graph", "vertices": len(nonneighbors), "regular_degree": degrees[0]}
    counts = []
    for u, v in itertools.combinations(range(q), 2):
        counts.append(sum(F.chi(F.sub(x, u)) == F.chi(F.sub(x, v)) == 1 for x in range(q)))
    assert set(counts) == {(q - 3) // 4}
    return {"applicable": True, "type": "tournament_common_outneighbors", "pairs_checked": len(counts), "common_outneighbors": counts[0]}


def verify_field(q):
    F = Field(q)
    field_checks = F.field_checks()
    paley_parameters = check_paley_parameters(F)
    triples = projective_group(F)
    direct_cubes, character_cubes = [], []
    candidates = 0
    for a, b, c in itertools.permutations(range(2, q), 3):
        candidates += 1
        direct = all(pattern in triples for pattern in cube_patterns(q, a, b, c))
        chars = character_cube(F, a, b, c)
        assert direct == chars, (q, a, b, c, direct, chars)
        if direct:
            direct_cubes.append((a, b, c))
        if chars:
            character_cubes.append((a, b, c))
    assert direct_cubes == character_cubes
    dim = 3 if direct_cubes else (1 if q == 2 else 2)
    assert dim == predicted_dimension(q), (q, dim)
    witness = None
    if direct_cubes:
        a, b, c = direct_cubes[0]
        witness = {
            "input_points": [q, 0, 1],
            "output_pairs": [[q, a], [0, b], [1, c]],
            "matrices": [
                {"output": list(pattern), "matrix": list(triples[pattern])}
                for pattern in cube_patterns(q, a, b, c)
            ],
        }
        for row in witness["matrices"]:
            assert determinant(F, row["matrix"]) in F.squares
            assert [action(F, row["matrix"], x) for x in witness["input_points"]] == row["output"]
    signature = hashlib.sha256(json.dumps(direct_cubes, separators=(",", ":")).encode()).hexdigest()
    return {
        "q": q, "characteristic": F.p, "degree": F.degree,
        "modulus_low_to_high": F.modulus,
        "group_order": len(triples), "field_axiom_checks": field_checks,
        "normalized_candidate_triples": candidates,
        "normalized_3_cube_count": len(direct_cubes),
        "all_cubes_sha256": signature,
        "natarajan_dimension": dim,
        "direct_character_comparison": "PASS", "paley_parameters": paley_parameters, "witness": witness,
    }


def main():
    parser = argparse.ArgumentParser()
    reproduction = Path(__file__).resolve().parent.parent / "No42_reproduction"
    parser.add_argument("--output", default=str(reproduction / "verification.json"),
                        help="JSON output; default is outside the package in ../No42_reproduction")
    parser.add_argument("--q", type=int, nargs="+", default=[2, 3, 4, 5, 7, 8, 9, 11, 13, 16, 17, 19, 23, 25, 27])
    args = parser.parse_args()
    rows = []
    for q in args.q:
        row = verify_field(q)
        rows.append(row)
        print(f"q={q}: Ndim={row['natarajan_dimension']}, cubes={row['normalized_3_cube_count']}, group={row['group_order']} PASS", flush=True)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"status": "PASS", "scope": "finite checks; see PROOF.md for all prime powers", "fields": rows}, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
