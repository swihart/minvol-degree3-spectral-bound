# Verification status

**Last updated:** September 3, 2026

**Current designation:** AI-assisted, non-peer-reviewed research draft seeking
independent mathematical verification.

## Candidate statement

The repository studies the proposed lower bound

\[
\operatorname{Vol}(K) \ge
\frac{\pi}{1914}
\left(259-27\sqrt{\frac{15183}{17303}}\right)d^3
\approx 0.383602704709068\,d^3
\]

for every three-dimensional convex body of constant width \(d\).

This coefficient is larger than Nishioka's published coefficient
\(4\pi/33\approx0.380799109526\), but it is numerically weaker than the much
newer public HYRA claims. The proposed contribution is the independent
degree-3 spectral mechanism, not the strongest currently claimed coefficient.

## Evidence currently in the repository

| Layer | Evidence | Status |
|---|---|---|
| Published framework | Nishioka's support-function formulation, volume identity, spectral mode calculation, and smooth approximation | Sourced |
| Exact tensor algebra | General seven-parameter trace-free cubic checked by exact SymPy arithmetic | Passed internally |
| Independent exact formulation | A second determinant formulation checked symbolically on the sphere | Passed internally |
| Pairing enumeration | All contraction pairings for the six quartic moments counted exhaustively | Passed in Python; matching R implementation included |
| Numerical convention checks | Deterministic quadrature, random tensors, and rotational tests | Passed independently in Python and R |
| Human-readable proof | Bridge lemmas and the degree-3 tensor identity are written line by line | Drafted and internally audited |
| Integrated manuscript | Complete LaTeX research note compiles to PDF | Passed internally |
| External mathematical review | Review by an independent subject-matter expert | Not yet completed |
| Peer review | Journal or conference peer review | Not yet completed |

The detailed claim-by-claim record is in `proof/PROOF_LEDGER.md`. The dependency
structure is in `proof/CLAIM_DEPENDENCIES.md`, and the internal audit is in
`proof/PROOF_AUDIT.md`.

## What a green GitHub Actions run means

The workflow in `.github/workflows/verification.yml` runs three jobs:

1. exact and numerical Python checks;
2. independent base-R checks; and
3. clean builds and preflight checks of the manuscript and all
   Markdown-derived PDFs.

A green workflow establishes that the checked computations and document builds
run successfully in the recorded CI environments. It does **not** establish that
the theorem has been independently proved, certified, or peer reviewed.

## Language approved for public use

Use:

> AI-assisted, non-peer-reviewed research draft seeking independent
> mathematical verification.

Do not use:

> Peer-reviewed theorem, certified proof, independently verified theorem, or
> accepted result.

## Correction policy

The public version history should preserve every released draft. If an error is
found, document it promptly, retain the earlier release, and issue a corrected
version with a new tag. Material corrections should be summarized in the
release notes and in the repository README.
