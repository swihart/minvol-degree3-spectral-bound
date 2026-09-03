# Degree-3 spectral refinement: research-draft verification package

This is a **private, pre-release verification project** for a candidate
refinement of Nishioka's lower bound for the three-dimensional
Blaschke--Lebesgue problem. The repository now contains an integrated LaTeX
research draft, but it is not yet ready for public release.

## Candidate coefficient

The proposed bound is

\[
\operatorname{Vol}(K) \ge
\frac{\pi}{1914}
\left(259-27\sqrt{\frac{15183}{17303}}\right)d^3
\approx 0.3836027047\,d^3.
\]

Nishioka's published coefficient is `4*pi/33 ~= 0.3807991095`.
The candidate is numerically weaker than the much newer HYRA claims; its
possible contribution is the independent degree-3 spectral mechanism.

## What has been checked

- A general degree-3 spherical harmonic is represented by a seven-parameter
  symmetric trace-free tensor.
- The central norm and determinant identities are integrated exactly over
  `S^2` with SymPy rational arithmetic.
- The crucial constants are derived from polynomial identities rather than
  inserted as final answers.
- A second exact formulation checks the determinant identity independently.
- Deterministic numerical quadrature and random tensor tests check conventions.
- Independent Python and base-R numerical implementations both pass; see
  `expected/CROSS_LANGUAGE_COMPARISON.md`.
- The final coefficient is simplified and evaluated exactly.
- The noncomputational bridge from the determinant estimate to the candidate
  volume bound has a line-by-line draft in `proof/BRIDGE_LEMMAS.md`.
- The degree-3 tensor identity now has a human-readable derivation in
  `proof/DEGREE3_TENSOR_IDENTITY.md`, including a contraction-graph count for
  all six quartic moments.
- The contraction-graph table is independently enumerated by exact Python code;
  a matching base-R script is included for cross-language checking.
- An internal line-by-line audit is recorded in `proof/PROOF_AUDIT.md`.
- The complete proof has been merged into an eight-page LaTeX manuscript in
  `paper/degree3_spectral_refinement.tex`; the tracked PDF was built and
  visually inspected in this project environment.

## What remains before public release

- Run and preserve the base-R pairing-count and numerical outputs plus R session
  metadata after applying the current patch.
- Have the named author read and approve the complete manuscript, especially
  the authorship, responsibility, and AI-assistance language.
- Add automated continuous integration for Python, R, and the LaTeX build.
- Add public-facing repository metadata: `LICENSE`, `CITATION.cff`, and
  `VERIFICATION_STATUS.md`.
- Perform a fresh-clone reproducibility test.
- Obtain outside mathematical review after the first public research-draft
  release.

See `proof/PROOF_LEDGER.md`, `proof/CLAIM_DEPENDENCIES.md`,
`proof/PROOF_AUDIT.md`, `proof/BRIDGE_LEMMAS.md`, and
`proof/DEGREE3_TENSOR_IDENTITY.md`.

## Build the paper

The manuscript source and tracked PDF are in `paper/`. Build from the repository
root with:

```sh
./build_paper.sh
```

The build requires `latexmk` and a standard LaTeX installation. See
`paper/README.md`.

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
- `python/verify_pairing_counts.py`

The numerical stress test is:

- `python/numerical_stress_tests.py`

## Run the R cross-check

The R scripts use base R only:

```sh
Rscript R/verify_pairing_counts.R
Rscript R/numerical_stress_tests.R
```

The first script independently checks the finite pairing-count table; the second
is an independent numerical tensor cross-check. The general exact symbolic
integration is performed by the Python/SymPy scripts.

## Current verification language

Use:

> AI-assisted, non-peer-reviewed research draft seeking independent mathematical verification.

Do not use:

> Peer-reviewed, certified, or independently verified theorem.
