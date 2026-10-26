#!/usr/bin/env python3
"""Separate prime-field implementation using determinant-one matrices.

Does not import verify.py or share its arithmetic/group construction.
"""
import argparse
import hashlib
import itertools
import json
from pathlib import Path


def compute(p):
    triples = set()
    sl_count = 0
    for a, b, c in itertools.product(range(p), repeat=3):
        if a:
            ds = [((1 + b * c) * pow(a, -1, p)) % p]
        elif (b * c) % p == p - 1:
            ds = range(p)
        else:
            continue
        for d in ds:
            assert (a * d - b * c) % p == 1
            sl_count += 1
            image = []
            for x in (p, 0, 1):
                if x == p:
                    image.append(p if c == 0 else (a * pow(c, -1, p)) % p)
                else:
                    den = (c * x + d) % p
                    image.append(p if den == 0 else ((a * x + b) * pow(den, -1, p)) % p)
            assert len(set(image)) == 3
            triples.add(tuple(image))
    assert sl_count == p * (p * p - 1)
    assert len(triples) == sl_count // (1 if p == 2 else 2)
    cubes = []
    checked = 0
    for u, v, w in itertools.permutations(range(2, p), 3):
        checked += 1
        valid = True
        for bits in itertools.product((0, 1), repeat=3):
            image = (u if bits[0] else p, v if bits[1] else 0, w if bits[2] else 1)
            if image not in triples:
                valid = False
                break
        if valid:
            cubes.append((u, v, w))
    digest = hashlib.sha256(json.dumps(cubes, separators=(",", ":")).encode()).hexdigest()
    return {"q": p, "SL2_matrix_count": sl_count, "group_order": len(triples),
            "normalized_candidate_triples": checked, "normalized_3_cube_count": len(cubes),
            "all_cubes_sha256": digest}


def main():
    parser = argparse.ArgumentParser()
    reproduction = Path(__file__).resolve().parent.parent / "No42_reproduction"
    parser.add_argument("--reference", default=str(reproduction / "verification.json"),
                        help="Fresh verify.py result to compare against")
    parser.add_argument("--output", default=str(reproduction / "independent_prime_verification.json"),
                        help="JSON output; default is outside the package")
    args = parser.parse_args()
    rows = [compute(p) for p in (2, 3, 5, 7, 11, 13, 17, 19, 23)]
    original = json.loads(Path(args.reference).read_text(encoding="utf-8"))
    source = {row["q"]: row for row in original["fields"]}
    for row in rows:
        for key in ("group_order", "normalized_candidate_triples", "normalized_3_cube_count", "all_cubes_sha256"):
            assert row[key] == source[row["q"]][key], (row["q"], key)
        print(f"q={row['q']}: independent determinant-one enumeration agrees PASS")
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps({"status": "PASS", "independence": "separate source; modular prime arithmetic; det=1 matrices", "fields": rows}, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
