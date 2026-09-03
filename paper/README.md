# Paper source

**Author:** Bruce J. Swihart

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

The tracked PDF is `degree3_spectral_refinement.pdf`.

## AI-assistance declaration

The manuscript identifies the system used as OpenAI ChatGPT (GPT-5.6 Pro),
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
