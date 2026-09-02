#!/bin/sh
set -eu
mkdir -p expected
Rscript R/numerical_stress_tests.R | tee expected/R_checks_output.txt
Rscript -e 'sessionInfo()' > expected/R_session_info.txt
