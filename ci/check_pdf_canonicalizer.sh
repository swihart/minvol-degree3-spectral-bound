#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
cd "$ROOT"

TMP=$(mktemp -d "${TMPDIR:-/tmp}/minvol-pdf-canonicalizer.XXXXXX")
trap 'rm -rf "$TMP"' EXIT HUP INT TERM

cat > "$TMP/a.pdf" <<'EOF'
%PDF-1.5
1 0 obj
<< /CreationDate (D:20260906123456Z)
   /BaseFont /ABCDEF+LMRoman10-Regular
   /FontName /GHIJKL+LMRoman10-Bold
   /CMapName /ABCDEF+LMRoman10-Regular-UTF16 >>
endobj
trailer
<< /ID [<11111111111111111111111111111111> <22222222222222222222222222222222>] >>
%%EOF
EOF

cat > "$TMP/b.pdf" <<'EOF'
%PDF-1.5
1 0 obj
<< /CreationDate (D:20260906235959Z)
   /BaseFont /UVWXYZ+LMRoman10-Regular
   /FontName /MNOPQR+LMRoman10-Bold
   /CMapName /UVWXYZ+LMRoman10-Regular-UTF16 >>
endobj
trailer
<< /ID [<AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA> <BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB>] >>
%%EOF
EOF

SOURCE_DATE_EPOCH=1788652800 python3 \
  tools/markdown_pdf/normalize_pdf_id.py "$TMP/a.pdf"
SOURCE_DATE_EPOCH=1788652800 python3 \
  tools/markdown_pdf/normalize_pdf_id.py "$TMP/b.pdf"

cmp -s "$TMP/a.pdf" "$TMP/b.pdf" || {
  echo "PDF CANONICALIZER CHECK: FAIL" >&2
  diff -u "$TMP/a.pdf" "$TMP/b.pdf" >&2 || true
  exit 1
}

if grep -Eq 'ABCDEF\+|GHIJKL\+|UVWXYZ\+|MNOPQR\+' "$TMP/a.pdf"; then
  echo "PDF CANONICALIZER CHECK: FAIL - volatile font prefixes remain" >&2
  exit 1
fi

if ! grep -Fq 'D:20260906000000Z' "$TMP/a.pdf"; then
  echo "PDF CANONICALIZER CHECK: FAIL - source date was not normalized" >&2
  exit 1
fi

echo "PDF CANONICALIZER CHECK: PASS"
