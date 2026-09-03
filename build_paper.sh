#!/bin/sh
set -eu
cd paper
latexmk -pdf -interaction=nonstopmode -halt-on-error degree3_spectral_refinement.tex
latexmk -c degree3_spectral_refinement.tex
