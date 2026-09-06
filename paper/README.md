# Paper source

**Author:** Bruce J. Swihart\
**Release:** v0.1.0 (September 6, 2026)\
**Canonical repository:** https://github.com/swihart/minvol-degree3-spectral-bound\
**Versioned release:** https://github.com/swihart/minvol-degree3-spectral-bound/releases/tag/v0.1.0

The manuscript source is `degree3_spectral_refinement.tex`. To keep the build
self-contained on minimal TeX installations, the short bibliography is included
inside the TeX source.

Build from the repository root with:

```sh
./build_paper.sh
```

or directly inside this directory with:

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error degree3_spectral_refinement.tex
```

The tracked PDF is `degree3_spectral_refinement.pdf`. The visible front matter
and PDF metadata identify this manuscript as release `v0.1.0`, dated September
5, 2026.

## Supporting proof documentation

For a deeper audit of the two nonroutine parts of the argument, see:

- [`../proof/DEGREE3_TENSOR_IDENTITY.md`](../proof/DEGREE3_TENSOR_IDENTITY.md)
  for the expanded cubic-tensor and quartic-moment derivation; and
- [`../proof/BRIDGE_LEMMAS.md`](../proof/BRIDGE_LEMMAS.md) for the expanded
  projection, nuclear-norm, duality, and smooth-approximation steps.

Typeset PDF versions are available under `../rendered/markdown/proof/`.

## AI-assistance declaration

The manuscript identifies the system used as OpenAI ChatGPT (GPT-5.6 Sol Pro),
accessed August-September 2026, and distinguishes computational reproducibility
from independent mathematical review. The fuller repository-level account is in
[`../AI_ASSISTANCE.md`](../AI_ASSISTANCE.md).

## Status language

Use:

> AI-assisted, non-peer-reviewed research draft seeking independent mathematical verification.

Do not describe the draft as peer reviewed, certified, or independently verified.

The repository-wide status and reproduction instructions are maintained in
[`../VERIFICATION_STATUS.md`](../VERIFICATION_STATUS.md) and
[`../REPRODUCIBILITY.md`](../REPRODUCIBILITY.md).
