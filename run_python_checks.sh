#!/bin/sh
set -eu
python python/verify_degree3_identity.py
python python/verify_degree3_identity_alt.py
python python/verify_pairing_counts.py
python python/verify_bound_arithmetic.py
python python/numerical_stress_tests.py
