#!/bin/sh
set -eu

ROOT=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
cd "$ROOT"

export SOURCE_DATE_EPOCH=${SOURCE_DATE_EPOCH:-1788652800}
export FORCE_SOURCE_DATE=${FORCE_SOURCE_DATE:-1}

cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error degree3_spectral_refinement.tex
python3 ../tools/markdown_pdf/normalize_pdf_id.py degree3_spectral_refinement.pdf
latexmk -c degree3_spectral_refinement.tex
