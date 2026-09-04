#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"

fail() {
  echo "PDF preflight failed: $*" >&2
  exit 1
}

for command_name in pdfinfo pdffonts pdftotext; do
  if ! command -v "$command_name" >/dev/null 2>&1; then
    fail "required command not found: $command_name"
  fi
done

if command -v sha256sum >/dev/null 2>&1; then
  checksum_program=sha256sum
elif command -v shasum >/dev/null 2>&1; then
  checksum_program=shasum
else
  fail "neither sha256sum nor shasum is available"
fi

check_pdf() {
  pdf=$1

  [ -s "$pdf" ] || fail "missing or empty PDF: $pdf"
  pdfinfo "$pdf" >/dev/null || fail "pdfinfo could not read: $pdf"

  pages=$(pdfinfo "$pdf" | awk '/^Pages:/ {print $2; exit}')
  case $pages in
    ''|*[!0-9]*) fail "could not determine page count for: $pdf" ;;
  esac
  [ "$pages" -gt 0 ] || fail "PDF has no pages: $pdf"

  if ! pdffonts "$pdf" | awk '
    NR <= 2 { next }
    NF > 0 && $(NF - 4) != "yes" { bad = 1 }
    END { exit bad }
  '; then
    fail "one or more fonts are not embedded in: $pdf"
  fi

  text_file=$(mktemp)
  if ! pdftotext "$pdf" "$text_file"; then
    rm -f "$text_file"
    fail "pdftotext could not read: $pdf"
  fi
  if [ ! -s "$text_file" ]; then
    rm -f "$text_file"
    fail "PDF has no extractable text: $pdf"
  fi
  rm -f "$text_file"
}

paper_pdf=paper/degree3_spectral_refinement.pdf
check_pdf "$paper_pdf"

paper_text=$(mktemp)
markdown_sources=$(mktemp)
trap 'rm -f "$paper_text" "$markdown_sources"' EXIT HUP INT TERM

pdftotext "$paper_pdf" "$paper_text"
grep -Fi "Bruce J. Swihart" "$paper_text" >/dev/null || \
  fail "paper PDF does not contain the full author name"
grep -F "0.3836027047090677" "$paper_text" >/dev/null || \
  fail "paper PDF does not contain the candidate coefficient"
grep -F "AI-assisted" "$paper_text" >/dev/null || \
  fail "paper PDF does not contain the AI-assistance disclosure"
grep -F "GPT-5.6 Pro" "$paper_text" >/dev/null || \
  fail "paper PDF does not identify the AI model"

sh tools/markdown_pdf/list_markdown_sources.sh > "$markdown_sources"

source_count=$(wc -l < "$markdown_sources" | tr -d ' ')
pdf_count=$(find rendered/markdown -type f -name '*.pdf' | wc -l | tr -d ' ')
[ "$source_count" -eq "$pdf_count" ] || \
  fail "found $source_count Markdown sources but $pdf_count rendered PDFs"

while IFS= read -r source; do
  relative=${source#./}
  pdf=rendered/markdown/${relative%.md}.pdf
  check_pdf "$pdf"
done < "$markdown_sources"

# The checksum manifest stores paths relative to the repository root.
if [ "$checksum_program" = sha256sum ]; then
  sha256sum -c rendered/markdown/SHA256SUMS.txt >/dev/null
else
  shasum -a 256 -c rendered/markdown/SHA256SUMS.txt >/dev/null
fi

echo "PDF PREFLIGHT: PASS"
echo "Paper PDF checked: $paper_pdf"
echo "Markdown source/PDF pairs checked: $source_count"
