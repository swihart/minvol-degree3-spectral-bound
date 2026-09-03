# Proof ledger

Status labels:

- **Sourced**: stated and proved in an identified reference.
- **Hand-checked**: algebra reviewed in the project notes.
- **Exact-code checked**: a symbolic identity was verified over general symbolic parameters.
- **Numerically cross-checked**: deterministic quadrature/random tests agree.
- **Formal write-up drafted**: a line-by-line proof is in the repository, but has not received outside review.
- **Integrated manuscript drafted**: the claim has been merged into the LaTeX research note and compiled.
- **Hosted CI passed**: all configured GitHub Actions jobs completed successfully in a clean hosted environment.
- **Needs local rerun**: a matching check exists but should be rerun and preserved in the current repository state.
- **Needs external review**: no independent subject-matter expert has checked it.

| ID | Claim | Current evidence | Status |
|---|---|---|---|
| N1 | Support-function constraints and volume formula | Nishioka, Sections 2--4 | Sourced |
| N2 | Smooth approximation and volume continuity | Nishioka, Lemma 2; Martini--Montejano--Oliveros, Theorem 8.5.1; limiting argument in `BRIDGE_LEMMAS.md` | Sourced; formal write-up drafted |
| S1 | Degree-3 coefficient is 1/22; tail coefficient is at most 1/58 | Nishioka, Lemma 4 and Proposition 1; explicit derivation in `BRIDGE_LEMMAS.md` | Sourced; formal write-up drafted |
| S2 | Tensor quadratic form is orthogonal across harmonic degrees | Polarized Bochner calculation in `BRIDGE_LEMMAS.md`, Lemmas 2.1--2.2 | Hand-checked; formal write-up drafted; needs external review |
| T1 | General cubic tensor is harmonic iff symmetric trace-free | `DEGREE3_TENSOR_IDENTITY.md`, Section 2; symbolic Laplacian check | Exact-code checked; formal write-up drafted; needs external review |
| T2 | `||A_Y||_2^2 = (176*pi/7) tau` | Moment derivation in `DEGREE3_TENSOR_IDENTITY.md`, Section 5; general symbolic integration | Exact-code checked; formal write-up drafted; needs external review |
| T3 | Exact formula for `||4 det A_Y||_2^2` | Quartic contraction derivation in `DEGREE3_TENSOR_IDENTITY.md`, Sections 6--8; general symbolic integration | Exact-code checked by two formulations; formal write-up drafted; needs external review |
| T4 | Compact pointwise determinant formula | `DEGREE3_TENSOR_IDENTITY.md`, Sections 3--4; matrix formula compared modulo `x^2+y^2+z^2-1` | Exact-code checked; hand-checked; needs external review |
| T5 | Rotational invariance and random convention checks | Deterministic sphere quadrature and random rotations | Numerically cross-checked independently in Python and R; both earlier runs pass |
| T6 | Pairing counts for the six quartic moments | Hand count in `DEGREE3_TENSOR_IDENTITY.md`, Section 7; exhaustive exact pairing enumeration | Exact-count checks passed independently in Python and R |
| F1 | Nuclear-norm identity and Cauchy--Schwarz step | `BRIDGE_LEMMAS.md`, Lemmas 4.1--4.2 | Hand-checked; formal write-up drafted; needs external review |
| F2 | Projection/duality step `||C||_2^2 = <A_h,C> <= (d/2) integral ||C||_*` | `BRIDGE_LEMMAS.md`, Corollary 2.3 and Lemmas 5.1--5.2 | Hand-checked; formal write-up drafted; needs external review |
| A1 | Final exact coefficient, decimal, and strict improvement | SymPy exact arithmetic; `BRIDGE_LEMMAS.md`, Theorem 6.2 and Corollary 6.3 | Exact-code checked; hand-checked; integrated manuscript drafted |
| R1 | Passage to nonsmooth bodies | Nishioka's approximation lemma; `BRIDGE_LEMMAS.md`, Theorem 7.1 | Sourced; formal write-up drafted; needs external review |
| P1 | Complete paper source compiles without unresolved references | `paper/degree3_spectral_refinement.tex`; `build_paper.sh` | Integrated manuscript drafted; runtime-tested in project environment |
| P2 | PDF has no visible clipping, overlap, or broken glyphs | Eight rendered pages inspected at 180 dpi | Render-checked |
| C1 | Hosted clean-environment checks for Python, R, the paper, metadata, and Markdown PDFs | `.github/workflows/verification.yml`; three green jobs reported on September 3, 2026 | Hosted CI passed |
| D1 | Public-facing verification and reproduction instructions | `VERIFICATION_STATUS.md`; `REPRODUCIBILITY.md` | Drafted and integrated |
| M1 | Authorship, AI provenance, citation, and licensing metadata | `AI_ASSISTANCE.md`; `CITATION.cff`; `LICENSE`; manuscript declaration; metadata preflight | Drafted and integrated; public release URL/version pending |
| L1 | Exact constant/decimal not found in a targeted web search | Search terms and limitations recorded in `PROOF_AUDIT.md` | Preliminary only; not a systematic novelty review |
| E1 | Full theorem has been independently reviewed | None yet | Needs external review |

## Current bottleneck

The internal proof chain, integrated manuscript, hosted verification workflow,
and authorship/provenance metadata are complete. The remaining internal gates
are:

1. have the named author finish reading and approve the manuscript;
2. perform and record a fresh-clone test before public release; and
3. add the public repository URL, release version, and release date to
   `CITATION.cff` when the first public release is prepared.

## Release rule

Do not describe the candidate bound as peer reviewed, certified, or
independently verified while `E1` remains open. The first public GitHub release
may be labeled **public research draft seeking verification** after all internal
gates above pass.
