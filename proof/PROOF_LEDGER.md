# Proof ledger

Status labels:

- **Sourced**: stated and proved in an identified reference.
- **Hand-checked**: algebra reviewed in the project notes.
- **Exact-code checked**: a symbolic identity was verified over general symbolic parameters.
- **Numerically cross-checked**: deterministic quadrature/random tests agree.
- **Formal write-up drafted**: a line-by-line proof is now in the repository, but has not received outside review.
- **Needs formal write-up**: mathematically plausible but not yet in publication-ready form.
- **Needs external review**: no independent subject-matter expert has checked it.

| ID | Claim | Current evidence | Status |
|---|---|---|---|
| N1 | Support-function constraints and volume formula | Nishioka, Sections 2-4 | Sourced |
| N2 | Smooth approximation and volume continuity | Nishioka, Lemma 2; explicit limiting argument in `BRIDGE_LEMMAS.md` | Sourced; formal write-up drafted |
| S1 | Degree-3 coefficient is 1/22; tail coefficient is at most 1/58 | Nishioka, Lemma 4 and Proposition 1; explicit derivation in `BRIDGE_LEMMAS.md` | Sourced; formal write-up drafted |
| S2 | Tensor quadratic form is orthogonal across harmonic degrees | Polarized Bochner calculation in `BRIDGE_LEMMAS.md`, Lemmas 2.1-2.2 | Formal write-up drafted; needs external review |
| T1 | General cubic tensor is harmonic iff symmetric trace-free | Direct tensor construction and Laplacian check | Exact-code checked |
| T2 | `||A_Y||_2^2 = (176*pi/7) tau` | General seven-parameter symbolic integration | Exact-code checked by `verify_degree3_identity.py`; needs human-readable derivation |
| T3 | Exact formula for `||4 det A_Y||_2^2` | General seven-parameter symbolic integration | Exact-code checked by two formulations; needs human-readable derivation |
| T4 | Compact pointwise determinant formula | Matrix formula compared modulo `x^2+y^2+z^2-1` | Exact-code checked; needs human-readable derivation |
| T5 | Rotational invariance and random convention checks | Deterministic sphere quadrature and random rotations | Numerically cross-checked independently in Python and R; both runs pass |
| F1 | Nuclear-norm identity and Cauchy-Schwarz step | `BRIDGE_LEMMAS.md`, Lemmas 4.1-4.2 | Formal write-up drafted; needs external review |
| F2 | Projection/duality step `||C||_2^2 = <A_h,C> <= (d/2) integral ||C||_*` | `BRIDGE_LEMMAS.md`, Corollary 2.3 and Lemmas 5.1-5.2 | Formal write-up drafted; needs external review |
| A1 | Final exact coefficient, decimal, and strict improvement | SymPy exact arithmetic; `BRIDGE_LEMMAS.md`, Theorem 6.2 and Corollary 6.3 | Exact-code checked; formal write-up drafted |
| R1 | Passage to nonsmooth bodies | Nishioka's approximation lemma; `BRIDGE_LEMMAS.md`, Theorem 7.1 | Sourced; formal write-up drafted; needs external review |
| E1 | Full theorem has been independently reviewed | None yet | Needs external review |

## Current bottleneck

The noncomputational bridge is now drafted in `proof/BRIDGE_LEMMAS.md`.
The principal remaining internal proof task is a readable derivation of T2-T4
that matches the exact symbolic scripts.

## Release rule

Do not call the candidate bound an externally verified theorem until every row
except `E1` is in publication-ready form. The first public GitHub release may
be labeled **public research draft seeking verification** while `E1` remains open.
