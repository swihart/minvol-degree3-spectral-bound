#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"

fail() {
  echo "Metadata preflight failed: $*" >&2
  exit 1
}

for file in AI_ASSISTANCE.md CITATION.cff LICENSE \
  paper/degree3_spectral_refinement.tex VERIFICATION_STATUS.md; do
  [ -s "$file" ] || fail "missing or empty file: $file"
done

grep -F "Bruce J. Swihart" paper/degree3_spectral_refinement.tex >/dev/null || \
  fail "paper source does not contain the full author name"
grep -F "pdfauthor={Bruce J. Swihart}" paper/degree3_spectral_refinement.tex >/dev/null || \
  fail "paper PDF metadata author is inconsistent"
grep -F "GPT-5.6 Pro" paper/degree3_spectral_refinement.tex >/dev/null || \
  fail "paper source does not identify the AI model"
grep -F "GPT-5.6 Pro" AI_ASSISTANCE.md >/dev/null || \
  fail "AI_ASSISTANCE.md does not identify the AI model"
grep -F 'given-names: "Bruce J."' CITATION.cff >/dev/null || \
  fail "CITATION.cff does not contain the author's given names"
grep -F 'family-names: "Swihart"' CITATION.cff >/dev/null || \
  fail "CITATION.cff does not contain the author's family name"
grep -F "CC BY 4.0" LICENSE >/dev/null || \
  fail "LICENSE does not declare the documentation license"
grep -F "MIT License" LICENSE >/dev/null || \
  fail "LICENSE does not declare the software license"

# A light structural check that uses only Python's standard library. Full CFF
# schema validation can be added later without making the research runtime
# depend on a citation-metadata package.
python3 - <<'PY'
from pathlib import Path
text = Path("CITATION.cff").read_text(encoding="utf-8")
required = (
    "cff-version: 1.2.0",
    "message:",
    "title:",
    "authors:",
    "preferred-citation:",
    "type: unpublished",
)
missing = [item for item in required if item not in text]
if missing:
    raise SystemExit("CITATION.cff is missing: " + ", ".join(missing))
print("CITATION METADATA CHECK: PASS")
PY

echo "METADATA PREFLIGHT: PASS"
