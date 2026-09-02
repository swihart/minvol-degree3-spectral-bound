#!/bin/sh
set -eu
mkdir -p expected
{
  Rscript R/verify_pairing_counts.R
  printf '\nProvenance: generated locally by run_r_checks.sh.\n'
} | tee expected/R_pairing_counts_output.txt
{
  Rscript R/numerical_stress_tests.R
  printf '\nProvenance: generated locally by run_r_checks.sh.\n'
} | tee expected/R_numerical_stress_output.txt
Rscript -e 'sessionInfo()' > expected/R_session_info.txt
