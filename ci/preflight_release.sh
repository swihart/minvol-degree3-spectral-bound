#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"

fail() {
  echo "Release preflight failed: $*" >&2
  exit 1
}

EXPECTED_VERSION=v0.1.0
EXPECTED_DATE=2026-09-06
DISPLAY_DATE="September 6, 2026"
REPOSITORY_URL="https://github.com/swihart/minvol-degree3-spectral-bound"
RELEASE_URL="$REPOSITORY_URL/releases/tag/$EXPECTED_VERSION"

for file in VERSION RELEASE_DATE RELEASE_NOTES.md README.md CITATION.cff \
  REPRODUCIBILITY.md VERIFICATION_STATUS.md AI_ASSISTANCE.md LICENSE \
  paper/README.md paper/degree3_spectral_refinement.tex; do
  [ -s "$file" ] || fail "missing or empty file: $file"
done

version=$(tr -d '\r\n' < VERSION)
release_date=$(tr -d '\r\n' < RELEASE_DATE)
[ "$version" = "$EXPECTED_VERSION" ] || \
  fail "VERSION is '$version', expected '$EXPECTED_VERSION'"
[ "$release_date" = "$EXPECTED_DATE" ] || \
  fail "RELEASE_DATE is '$release_date', expected '$EXPECTED_DATE'"

for file in README.md RELEASE_NOTES.md REPRODUCIBILITY.md \
  VERIFICATION_STATUS.md paper/README.md \
  paper/degree3_spectral_refinement.tex CITATION.cff LICENSE; do
  grep -F "$EXPECTED_VERSION" "$file" >/dev/null || \
    fail "$file does not contain $EXPECTED_VERSION"
done

for file in README.md RELEASE_NOTES.md REPRODUCIBILITY.md \
  VERIFICATION_STATUS.md paper/README.md \
  paper/degree3_spectral_refinement.tex LICENSE; do
  grep -F "$DISPLAY_DATE" "$file" >/dev/null || \
    fail "$file does not contain $DISPLAY_DATE"
done

grep -F 'date-released: "2026-09-06"' CITATION.cff >/dev/null || \
  fail "CITATION.cff release date is missing or inconsistent"
grep -F 'version: "0.1.0"' CITATION.cff >/dev/null || \
  fail "CITATION.cff version is missing or inconsistent"
grep -F 'status: preprint' CITATION.cff >/dev/null || \
  fail "CITATION.cff preferred-citation status is missing or inconsistent"

grep -F "$REPOSITORY_URL" README.md >/dev/null || \
  fail "README.md does not contain the canonical repository URL"
grep -F "$RELEASE_URL" README.md >/dev/null || \
  fail "README.md does not contain the versioned release URL"
grep -F "$REPOSITORY_URL" CITATION.cff >/dev/null || \
  fail "CITATION.cff does not contain the canonical repository URL"
grep -F "$RELEASE_URL" CITATION.cff >/dev/null || \
  fail "CITATION.cff does not contain the versioned release URL"
grep -F "$REPOSITORY_URL" paper/degree3_spectral_refinement.tex >/dev/null || \
  fail "paper source does not contain the canonical repository URL"
grep -F "$RELEASE_URL" paper/degree3_spectral_refinement.tex >/dev/null || \
  fail "paper source does not contain the versioned release URL"

grep -F "public research draft" README.md >/dev/null || \
  fail "README.md does not use public research-draft wording"
grep -F "public research draft" RELEASE_NOTES.md >/dev/null || \
  fail "RELEASE_NOTES.md does not identify the public research draft"

for obsolete in \
  "private, pre-release verification project" \
  "not yet ready for public release" \
  "release URL and version still pending" \
  "What remains before public release" \
  "editable source of truth"; do
  if grep -R -F "$obsolete" README.md REPRODUCIBILITY.md \
      VERIFICATION_STATUS.md paper/README.md proof/PROOF_AUDIT.md \
      proof/PROOF_LEDGER.md >/dev/null 2>&1; then
    fail "obsolete pre-release wording remains: $obsolete"
  fi
done

if grep -R -F "YOUR_REPOSITORY_URL" README.md REPRODUCIBILITY.md \
    RELEASE_NOTES.md paper/README.md >/dev/null 2>&1; then
  fail "placeholder repository URL remains"
fi

echo "RELEASE PREFLIGHT: PASS"
echo "Version: $EXPECTED_VERSION"
echo "Release date: $EXPECTED_DATE"
echo "Canonical repository: $REPOSITORY_URL"
echo "Versioned release: $RELEASE_URL"
