# Proof ledger

Status labels:

- **Sourced**: stated and proved in an identified reference.
- **Hand-checked**: algebra reviewed in the project notes.
- **Exact-code checked**: a symbolic identity was verified over general symbolic parameters.
- **Numerically cross-checked**: deterministic quadrature/random tests agree.
- **Needs formal write-up**: mathematically plausible but not yet in publication-ready form.
- **Needs external review**: no independent subject-matter expert has checked it.

| ID | Claim | Current evidence | Status |
|---|---|---|---|
| N1 | Support-function constraints and volume formula | Nishioka, Sections 2-4 | Sourced |
| N2 | Smooth approximation and volume continuity | Nishioka, Lemma 2 | Sourced |
| S1 | Degree-3 coefficient is 1/22; tail coefficient is at most 1/58 | Nishioka, Lemma 4 and Proposition 1; direct arithmetic | Sourced; hand-checked |
| S2 | Tensor quadratic form is orthogonal across harmonic degrees | Bilinearized Bochner calculation | Hand-checked; needs formal write-up |
| T1 | General cubic tensor is harmonic iff symmetric trace-free | Direct tensor construction and Laplacian check | Exact-code checked |
| T2 | `||A_Y||_2^2 = (176*pi/7) tau` | General seven-parameter symbolic integration | Exact-code checked by `verify_degree3_identity.py` |
| T3 | Exact formula for `||4 det A_Y||_2^2` | General seven-parameter symbolic integration | Exact-code checked by two formulations |
| T4 | Compact pointwise determinant formula | Matrix formula compared modulo `x^2+y^2+z^2-1` | Exact-code checked |
| T5 | Rotational invariance and random convention checks | Deterministic sphere quadrature and random rotations | Numerically cross-checked independently in Python and R; both runs pass |
| F1 | Nuclear-norm identity and Cauchy-Schwarz step | Elementary matrix algebra | Hand-checked; needs formal write-up |
| F2 | Projection/duality step `||C||_2^2 = <A_h,C> <= (d/2) integral ||C||_*` | Follows from S2 and operator/nuclear duality | Hand-checked; needs formal write-up |
| A1 | Final exact coefficient and decimal | SymPy exact arithmetic | Exact-code checked |
| R1 | Passage to nonsmooth bodies | Nishioka's approximation lemma | Sourced; needs explicit application in note |
| E1 | Full theorem has been independently reviewed | None yet | Needs external review |

## Release rule

Do not call the candidate bound an externally verified theorem until every row
except `E1` is in publication-ready form.  The first public GitHub release may
be labeled **public research draft seeking verification** while `E1` remains open.
