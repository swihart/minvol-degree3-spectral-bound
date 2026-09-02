# Degree-3 spectral refinement: verification checkpoint

This is an **internal verification checkpoint**, not yet a public theorem package.
It tests a candidate refinement of Nishioka's lower bound for the
three-dimensional Blaschke-Lebesgue problem.

## Candidate coefficient

The proposed bound is

$$
{Vol}(K) \ge
\frac{\pi}{1914}
\left(259-27\sqrt{\frac{15183}{17303}}\right)d^3
\approx 0.3836027047d^3.
$$



Nishioka's published coefficient is `4*pi/33 ~= 0.3807991095`.
The candidate is numerically weaker than the much newer HYRA claims; its
possible contribution is the independent degree-3 spectral mechanism.

## What has been checked at this checkpoint

- A general degree-3 spherical harmonic is represented by a seven-parameter
  symmetric trace-free tensor.
- The central norm and determinant identities are integrated exactly over
  `S^2` with SymPy rational arithmetic.
- The crucial constants are derived from polynomial identities rather than
  inserted as final answers.
- A second exact formulation checks the determinant identity independently.
- Deterministic numerical quadrature and random tensor tests check conventions.
- Independent Python and base-R numerical implementations both pass; see `expected/CROSS_LANGUAGE_COMPARISON.md`.
- The final coefficient is simplified and evaluated exactly.

## What remains before public release

- Write a complete human-readable proof of the determinant identity.
- Formalize the harmonic projection/orthogonality lemma.
- Formalize the operator/nuclear-norm step.
- State the smooth-approximation passage carefully.
- Preserve a clean command-line record of the R cross-check and R session metadata.
- Add automated continuous integration and a complete AI-assistance statement.
- Obtain outside mathematical review after the first public research-draft release.

See `proof/PROOF_LEDGER.md` and `proof/CLAIM_DEPENDENCIES.md`.

## Run the exact Python checks

From the repository root:

```sh
python -m pip install -r requirements.txt
./run_python_checks.sh
```

The exact symbolic scripts are:

- `python/verify_degree3_identity.py`
- `python/verify_degree3_identity_alt.py`
- `python/verify_bound_arithmetic.py`

The numerical stress test is:

- `python/numerical_stress_tests.py`

## Run the R cross-check

The R script uses base R only:

```sh
Rscript R/numerical_stress_tests.R
```

The R script is an independent numerical cross-check.  The exact symbolic
verification is performed by the Python/SymPy scripts.

## Current verification language

Until external review, use:

> AI-assisted public research draft seeking verification.

Do not use:

> Peer-reviewed, certified, or independently verified theorem.
