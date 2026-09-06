# Reproducibility guide

**Release:** v0.1.0 (September 6, 2026)\
**Canonical repository:** https://github.com/swihart/minvol-degree3-spectral-bound\
**Versioned release:** https://github.com/swihart/minvol-degree3-spectral-bound/releases/tag/v0.1.0

This guide explains how to reproduce the symbolic checks, numerical
cross-checks, manuscript build, and typeset Markdown documentation from a fresh
clone.

## Continuous-integration environments

The GitHub Actions workflow uses:

- Ubuntu 24.04;
- Python 3.13;
- the exact Python package versions in `requirements.txt`;
- R 4.6.1, using base R only;
- Pandoc 3.10.1;
- XeLaTeX, `latexmk`, and the TeX packages installed by the workflow; and
- `pdfinfo`, `pdffonts`, and `pdftotext` from Poppler for PDF preflight.

The workflow file is `.github/workflows/verification.yml`.

## Recorded fresh-clone tests

A clean-clone reproduction was completed on 2026-09-04 for commit
`96cea57275070f21babf30477ab1b128ec0f5eb6`. The isolated clone ran the Python
and R suites, rebuilt the manuscript and every Markdown-derived PDF, passed the
metadata and local checksum checks, and remained byte-clean afterward.

A second fresh-clone smoke test was completed on 2026-09-06 for release-candidate
commit `ff5118cc05ada29d26631c82d0cbf69613ed88c1`. Every mathematical check,
document build, metadata preflight, and PDF-validity/checksum check passed. The
only binary differences were two-byte changes in two secondary rendered
Markdown PDFs, with corresponding updates to the checksum manifest. No source,
release metadata, or mathematical output changed. This is treated as documented
renderer-level variation rather than a release blocker.

The full Poppler PDF preflight was delegated to the green GitHub Actions
document jobs. The complete environments and interpretation are recorded in
[`CLEAN_CLONE_CHECK.md`](CLEAN_CLONE_CHECK.md).

## Fresh-clone procedure

To reproduce the fixed v0.1.0 release, clone the tag and enter the repository:

```sh
git clone --branch v0.1.0 --depth 1 \
  https://github.com/swihart/minvol-degree3-spectral-bound.git
cd minvol-degree3-spectral-bound
```

To inspect later development instead, clone the default branch without the
`--branch v0.1.0` option. Results should always be reported with the exact tag
or commit used.

### 1. Python checks

Create and activate a virtual environment if desired, then install the pinned
requirements and run the suite:

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
./run_python_checks.sh
```

A successful run ends with all of the following:

```text
EXACT DEGREE-3 IDENTITY CHECK: PASS
ALTERNATIVE COMPACT-FORM CHECK: PASS
PAIRING-COUNT CHECK: PASS
BOUND ARITHMETIC CHECK: PASS
NUMERICAL STRESS TESTS: PASS
```

### 2. R checks

The R scripts use base R only:

```sh
./run_r_checks.sh
```

A successful run contains:

```text
R PAIRING-COUNT CHECK: PASS
R NUMERICAL STRESS TESTS: PASS
```

The runner records both outputs and the R session information in `expected/`.

### 3. Manuscript build

With Python 3, `latexmk`, and a standard LaTeX installation available:

```sh
./build_paper.sh
```

The resulting manuscript is:

```text
paper/degree3_spectral_refinement.pdf
```

### 4. Markdown-derived PDFs

With Pandoc, Python 3, and XeLaTeX available:

```sh
./build_markdown_pdfs.sh
```

The rendered files are written beneath `rendered/markdown/`, preserving the
source directory structure. Their SHA-256 hashes are written to:

```text
rendered/markdown/SHA256SUMS.txt
```

On macOS, verify the tracked files with:

```sh
shasum -a 256 -c rendered/markdown/SHA256SUMS.txt
```

On systems with GNU coreutils, use:

```sh
sha256sum -c rendered/markdown/SHA256SUMS.txt
```

### 5. Metadata and PDF preflight

Check consistency of the author name, AI-system identification, citation file,
licensing declaration, release version, release date, and public URLs:

```sh
./ci/preflight_metadata.sh
./ci/preflight_release.sh
```

With Poppler installed, validate the manuscript and every Markdown-derived PDF:

```sh
./ci/preflight_pdfs.sh
```

The PDF check confirms that each PDF is nonempty and readable, has at least one
page, contains extractable text, uses embedded fonts, and has a valid checksum
when applicable. It also confirms that the manuscript contains the full author
name, candidate coefficient, AI-assistance disclosure, and model designation.

## What is exact and what is numerical

The general degree-3 tensor identities are checked with exact symbolic
arithmetic by the Python/SymPy programs. The R programs are independently
written numerical and finite-enumeration cross-checks. Agreement between the
two languages helps detect implementation and convention errors, but it is not
a substitute for mathematical review of the proof.

## PDF reproducibility

The build scripts fix the source-date epoch and canonicalize several known
volatile PDF fields, including embedded-font subset prefixes, metadata dates,
and the trailer identifier. The regression test in
`ci/check_pdf_canonicalizer.sh` verifies those specific canonicalizations.
These measures improve repeatability, but they do not guarantee byte-for-byte
identity across every TeX/Pandoc invocation, filesystem context, or platform.

The release standard for generated PDFs is successful compilation, valid and
extractable content, embedded fonts, consistent release metadata, and a passing
hosted Poppler preflight. The checksum manifest authenticates the PDF files
supplied with the release and verifies a single generated collection; it is not
a promise that independently rebuilt PDFs will always have the same binary
hashes.

The 2026-09-04 clean-clone run reproduced all tracked outputs byte for byte. In
the 2026-09-06 release-candidate smoke test, all mathematical checks and builds
passed, while two secondary rendered documentation PDFs differed from their
committed copies by two bytes. No source or mathematical output changed. The
Markdown and LaTeX files are the editable source files; the tracked PDFs are
rendered counterparts provided for convenient reading.

## GitHub Actions

The workflow runs automatically on pushes to `main`, pushes of version tags, pull
requests, and manual requests from the Actions tab. It stores the Python and R logs and the generated
PDFs as temporary workflow artifacts for inspection. A green run means that the
repository's checks and builds completed in the declared environments; it is
not an independent proof review.

## Release-candidate verification

Before the `v0.1.0` tag is created, the exact release-candidate commit must pass:

1. all three GitHub Actions jobs on `main`;
2. the release and authorship metadata preflights; and
3. successful local or hosted execution of the mathematical and document-build
   workflows.

A fresh-clone smoke test has additionally confirmed that the declared
dependencies are sufficient and that every substantive check and build runs
outside the development checkout. Binary differences confined to generated PDF
artifacts are diagnostic information, not a release-blocking condition, when
the sources are unchanged and all PDF validity and content preflights pass.

The tag must point to the reviewed commit with green `main` checks. Pushing the
tag starts the same three-job workflow for the tagged ref; that run must also
pass before the GitHub release is published. The release page should record the
commit hash and the verification scope accurately.

## Reporting a discrepancy

Record the following when reporting a failed or differing run:

- commit hash;
- operating system and architecture;
- Python, SymPy, NumPy, R, Pandoc, and TeX versions;
- the full command used; and
- the complete console output beginning at the first warning or error.
