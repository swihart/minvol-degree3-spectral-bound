#!/usr/bin/env python3
"""Exact arithmetic check from the determinant ratio to the volume bound."""

from __future__ import annotations

import sympy as sp


def main() -> None:
    ratio = sp.Rational(15183, 17303)
    s = sp.sqrt(ratio)

    # Nishioka gives N <= 2*pi*d^2.  The refined degree-3 estimate gives
    # N3 <= pi*d^2*(1+s).  The spectral split is
    # E <= N/58 + (9/319)N3.
    energy_coefficient = sp.factor(sp.pi * (20 + 9 * s) / 319)
    volume_coefficient = sp.factor(sp.pi / 6 - energy_coefficient / 2)
    displayed_form = sp.pi / 1914 * (259 - 27 * s)
    if sp.simplify(volume_coefficient - displayed_form) != 0:
        raise AssertionError("Equivalent forms of the candidate coefficient disagree.")

    nishioka = 4 * sp.pi / 33
    meissner = sp.pi * (
        sp.Rational(2, 3) - sp.sqrt(3) / 4 * sp.acos(sp.Rational(1, 3))
    )
    if not (sp.N(nishioka) < sp.N(volume_coefficient) < sp.N(meissner)):
        raise AssertionError("Expected numerical ordering failed.")

    print("BOUND ARITHMETIC CHECK: PASS")
    print(f"energy coefficient E/d^2 <= {energy_coefficient}")
    print(f"candidate volume coefficient = {volume_coefficient}")
    print(f"candidate decimal            = {sp.N(volume_coefficient, 20)}")
    print(f"Nishioka decimal             = {sp.N(nishioka, 20)}")
    print(f"Meissner decimal              = {sp.N(meissner, 20)}")
    print(f"improvement over Nishioka     = {sp.N(volume_coefficient - nishioka, 20)}")


if __name__ == "__main__":
    main()
