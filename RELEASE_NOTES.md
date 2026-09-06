# Release notes: v0.1.0

**Release date:** September 6, 2026\
**Author:** Bruce J. Swihart\
**Status:** AI-assisted, non-peer-reviewed research draft seeking independent
mathematical verification

**Canonical repository:**
[github.com/swihart/minvol-degree3-spectral-bound](https://github.com/swihart/minvol-degree3-spectral-bound)

**Versioned release:**
[v0.1.0](https://github.com/swihart/minvol-degree3-spectral-bound/releases/tag/v0.1.0)

**Main manuscript:**
[PDF](paper/degree3_spectral_refinement.pdf) | [LaTeX source](paper/degree3_spectral_refinement.tex)

## Purpose of this release

Version v0.1.0 is the initial public research draft of a proposed degree-3
spectral refinement of Nishioka's lower bound for the three-dimensional
Blaschke-Lebesgue problem.

The proposed bound is

\[
\operatorname{Vol}(K) \ge
\frac{\pi}{1914}
\left(259-27\sqrt{\frac{15183}{17303}}\right)d^3
\approx 0.3836027047d^3.
\]

The proposed contribution is an independent spectral mechanism: the proof
separates the degree-3 curvature energy, derives a new determinant inequality
for that component, and uses it to cap the portion of the total curvature
budget that can receive Nishioka's degree-3 coefficient.

## Included materials

This release contains:

- the integrated LaTeX paper and compiled PDF;
- expanded bridge lemmas and a detailed degree-3 tensor derivation;
- a claim-dependency graph, proof ledger, and internal proof audit;
- exact symbolic Python checks and exhaustive pairing enumeration;
- independent base-R pairing and numerical checks;
- automated GitHub Actions workflows for Python, R, document builds,
  metadata checks, and PDF preflight;
- reproducibility, clean-clone, licensing, citation, and AI-provenance records;
  and
- typeset PDF counterparts of all Markdown documentation.

## Verification status

The finite algebraic identities and constants are checked with exact symbolic
arithmetic. Independent Python and R implementations agree numerically, and the
repository has passed clean hosted builds and a recorded clean-clone
reproduction.

The v0.1.0 release procedure first requires the exact release-candidate commit
to pass the three hosted GitHub Actions jobs on `main` and one final clean-clone
test. That same commit is then tagged `v0.1.0`; the tag-triggered workflow must
also pass before the GitHub release is published. The release page records the
tested commit and the final result.

These checks establish reproducibility of the supplied computations and
artifacts. They do not constitute independent subject-matter review or peer
review of the complete proof.

## Scope and limitations

HYRA publicly claims substantially stronger analytic and computer-assisted
bounds by a different method. This release does not claim the strongest
currently proposed numerical coefficient. It also does not prove the Meissner
conjecture or identify a minimizing body.

Errors, missing hypotheses, normalization issues, and literature references
may still be found. Corrections should preserve the v0.1.0 record and be issued
under a new version tag.

## Preferred citation

Bruce J. Swihart, *A Degree-Three Spectral Refinement of Nishioka's Lower Bound
for the Three-Dimensional Blaschke-Lebesgue Problem*, version v0.1.0, public
research draft, September 6, 2026.

The machine-readable citation is in [`CITATION.cff`](CITATION.cff).
