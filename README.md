# Exact Natarajan Dimension of the Natural PSL(2,q) Action

Research No.42. Unreviewed public preprint, version 1.0, 27 October 2026.

Author: Ryutaro Yonezu, Yonezu Research Lab.

For every prime power q, the Natarajan dimension of the natural action of
PSL(2,q) on the projective line is:

| q | Natarajan dimension |
| --- | ---: |
| 2 | 1 |
| 3, 4, 5, 7, 11 | 2 |
| Every other prime power | 3 |

The proof is in [PROOF.md](PROOF.md) and the formatted preprint is in
[paper/No42_PSL2_Natarajan_Preprint_v1_0.pdf](paper/No42_PSL2_Natarajan_Preprint_v1_0.pdf).

## Scope and status

The statement concerns the natural degree-(q+1) action, not all actions of the
abstract group. Natarajan dimension, determinant square classes, Paley
structures, and several small cases are known. The even-characteristic part
is a direct consequence of sharp triple transitivity and label counting.

This is an unreviewed preprint. Model, proof and computations have been
rechecked by AI in another session of the same workflow. This is **not
independent third-party confirmation or human peer review**. Separate code
implementations are described as such, without implying institutional or
third-party validation. The additional custom checker mentioned in the
received review was not supplied with raw code or logs.

**REFERENCES: PARTIAL. NOVELTY: INCONCLUSIVE. No priority claim is made.**
The exact all-field classification was not located in the checked primary
sources. That limited observation does not establish novelty. See
[NOVELTY_RECHECK_JA.md](NOVELTY_RECHECK_JA.md),
[CITATION_CHECK_JA.md](CITATION_CHECK_JA.md), and [sources.json](sources.json).
Earlier audit requests and reports are retained as workflow records; their
use of "independent" must be read with the restriction above.

## Verification

Python 3.10 or newer, standard library only. No network, model API, payment,
GPU, or third-party package is needed for the verifiers. From this directory:

```text
python check_hashes.py
python verify.py
python verify_prime_independent.py
python check_hashes.py
```

The default results go outside this directory into `../No42_reproduction/`.
The packaged evidence is preserved. Optional `--output PATH` and, on the
separate prime checker, `--reference PATH` select alternate locations.

The finite-field sweep covers q=2,3,4,5,7,8,9,11,13,16,17,19,23,25,27:
15 fields and 43,290 normalized candidate triples. The separate modular
prime implementation covers 2,3,5,7,11,13,17,19,23 and agrees on full cube-set
counts and hashes. The two original evidence JSON files are unchanged from
the audited candidate. Finite checks support the implementation; the proof
is the basis for the claim over all prime powers.

Infinity is represented by q in the JSON. Extension-field labels encode
polynomial coefficients, not integers modulo q. Their irreducible
polynomials are recorded with coefficients in ascending degree.

## Materials and rights

- Repository: https://github.com/yonezaemon1-hub/no42-psl2-natarajan-dimension
- Zenodo DOI: https://doi.org/10.5281/zenodo.23677132
- The TeX source uses standard LaTeX packages and can be compiled with pdfLaTeX.
- Rights statement: Copyright (c) 2026 Ryutaro Yonezu. All rights reserved.

Research contact: yonezaemon1+research@gmail.com.
