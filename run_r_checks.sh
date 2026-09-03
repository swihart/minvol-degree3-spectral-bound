#!/bin/sh
set -eu

mkdir -p expected

run_and_record() {
  output=$1
  shift
  temporary=$(mktemp)

  if "$@" >"$temporary" 2>&1; then
    cat "$temporary"
    {
      cat "$temporary"
      printf '\nProvenance: generated locally by run_r_checks.sh.\n'
    } >"$output"
    rm -f "$temporary"
  else
    status=$?
    cat "$temporary" >&2
    {
      cat "$temporary"
      printf '\nProvenance: failed local run recorded by run_r_checks.sh.\n'
    } >"$output"
    rm -f "$temporary"
    return "$status"
  fi
}

run_and_record expected/R_pairing_counts_output.txt \
  Rscript R/verify_pairing_counts.R
run_and_record expected/R_numerical_stress_output.txt \
  Rscript R/numerical_stress_tests.R
Rscript -e 'sessionInfo()' > expected/R_session_info.txt
