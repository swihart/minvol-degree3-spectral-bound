# Recorded clean-clone verification

**Result:** PASS with the full Poppler PDF preflight delegated to GitHub Actions  
**UTC timestamp:** 2026-09-04 10:05:19  
**Tested commit:** `96cea57275070f21babf30477ab1b128ec0f5eb6`  
**Repository:** `swihart/minvol-degree3-spectral-bound`

## Purpose

This record documents a successful reproduction attempt from a newly cloned
copy of the repository. The test was designed to detect hidden local files,
uncommitted dependencies, machine-specific build assumptions, and generated
outputs that differ from the versions tracked in Git.

The tested commit preceded this documentation commit. The result therefore
applies exactly to commit
`96cea57275070f21babf30477ab1b128ec0f5eb6`; later commits require their own
verification when a final release candidate is prepared.

## Recorded result

```text
CLEAN CLONE CHECK: PASS WITH PDF PREFLIGHT DELEGATED TO GITHUB ACTIONS
Commit: 96cea57275070f21babf30477ab1b128ec0f5eb6
Repository: swihart/minvol-degree3-spectral-bound
PDF validation: basic local PDF and checksum checks passed; full PDF preflight delegated to GitHub Actions
Tracked working tree after all checks and rebuilds: clean
```

Machine-specific temporary-directory and artifact-directory paths have been
omitted from this public-facing record. They were retained in the local ignored
`ci-artifacts/` directory when the test was run.

## Procedure completed

Starting from a clean checkout whose `HEAD` matched `origin/main`, the helper:

1. cloned the repository into a new temporary directory;
2. created an isolated Python virtual environment outside the clone;
3. installed the pinned Python dependencies;
4. ran every exact and numerical Python check;
5. ran both independent base-R checks;
6. rebuilt the LaTeX manuscript;
7. rebuilt every Markdown-derived PDF;
8. ran the metadata preflight;
9. performed local PDF-header and checksum validation; and
10. confirmed that all tracked files remained byte-for-byte unchanged after the
    checks and rebuilds.

The same tested commit also had all three GitHub Actions jobs green. The hosted
document job supplied the full Poppler-based PDF preflight that was unavailable
on the local Mac.

## Environment

| Component | Recorded value |
|---|---|
| Operating system | macOS 26.2, Darwin 25.2.0, `x86_64` |
| Git | 2.50.1 (Apple Git-155) |
| Python | 3.13.15 |
| NumPy | 2.3.5 |
| SymPy | 1.14.0 |
| R | 4.6.0 |
| Pandoc | 2.19.2 |
| XeTeX | 3.141592653-2.6-0.999994, TeX Live 2022 |
| `latexmk` | 4.77 |
| Poppler tools | Not installed locally; full preflight delegated to GitHub Actions |

The clean result is particularly useful because the local document toolchain
differed from the pinned Ubuntu CI toolchain. Despite those differences, the
tracked manuscript, rendered documentation PDFs, checksum manifest, and
recorded verification outputs were reproduced without changing a tracked byte.

## Interpretation and limits

This test supports the following claims:

- the committed computational checks run successfully from a fresh clone;
- the committed document sources rebuild successfully in the recorded local
  environment;
- the regenerated tracked outputs match the committed outputs byte for byte;
- no uncommitted local source file was needed for the successful run; and
- the full PDF preflight also passed in the clean hosted GitHub Actions
  environment.

It does **not** constitute independent subject-matter review, peer review, or a
certification that the proposed mathematical theorem is correct. The current
status remains:

> AI-assisted, non-peer-reviewed research draft seeking independent
> mathematical verification.

See [`REPRODUCIBILITY.md`](REPRODUCIBILITY.md) for the reproduction procedure
and [`VERIFICATION_STATUS.md`](VERIFICATION_STATUS.md) for the boundary between
computational reproducibility and mathematical verification.
