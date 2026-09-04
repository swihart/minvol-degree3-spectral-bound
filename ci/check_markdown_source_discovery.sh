#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"

fail() {
  echo "Markdown source discovery check failed: $*" >&2
  exit 1
}

scratch=.venv/markdown-source-discovery-check
source_list=$(mktemp)
trap 'rm -rf "$scratch"; rm -f "$source_list"' EXIT HUP INT TERM

mkdir -p "$scratch"
printf '# Ignored environment file\n' > "$scratch/SHOULD_NOT_RENDER.md"

sh tools/markdown_pdf/list_markdown_sources.sh > "$source_list"

grep -Fx 'README.md' "$source_list" >/dev/null || \
  fail 'README.md was not discovered'
grep -Fx 'proof/DEGREE3_TENSOR_IDENTITY.md' "$source_list" >/dev/null || \
  fail 'proof/DEGREE3_TENSOR_IDENTITY.md was not discovered'

if grep -F '.venv/' "$source_list" >/dev/null; then
  cat "$source_list" >&2
  fail 'an ignored virtual-environment Markdown file was discovered'
fi

echo 'MARKDOWN SOURCE DISCOVERY CHECK: PASS'
