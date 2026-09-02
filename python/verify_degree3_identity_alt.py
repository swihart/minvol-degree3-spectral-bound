#!/usr/bin/env python3
"""Alternative exact check of the cubic determinant formula.

This script compares the projected-matrix determinant with the compact
contraction formula

  4 det A_Y = 64 Y^2 + 144 |T(u,u,.)|^2 - 72 |T(u,.,.)|^2

on S^2, and independently integrates the compact formula.
"""

from __future__ import annotations

from itertools import permutations
from typing import Dict, Tuple

import sympy as sp

Index3 = Tuple[int, int, int]


def build_tensor(params: tuple[sp.Symbol, ...]) -> Dict[Index3, sp.Expr]:
    a, b, c, d, e, f, g = params
    seeds = {
        (0, 0, 0): a,
        (0, 0, 1): b,
        (0, 0, 2): c,
        (0, 1, 1): d,
        (0, 1, 2): e,
        (1, 1, 1): f,
        (1, 1, 2): g,
        (0, 2, 2): -a - d,
        (1, 2, 2): -b - f,
        (2, 2, 2): -c - g,
    }
    tensor: Dict[Index3, sp.Expr] = {}
    for key, value in seeds.items():
        for p in set(permutations(key)):
            tensor[p] = value
    return tensor


def sphere_integral(expr: sp.Expr, x: sp.Symbol, y: sp.Symbol, z: sp.Symbol) -> sp.Expr:
    total = sp.Integer(0)
    for (i, j, k), coefficient in sp.Poly(sp.expand(expr), x, y, z).terms():
        if i % 2 or j % 2 or k % 2:
            continue
        a, b, c = i // 2, j // 2, k // 2
        moment = (
            4
            * sp.pi
            * sp.factorial2(2 * a - 1)
            * sp.factorial2(2 * b - 1)
            * sp.factorial2(2 * c - 1)
            / sp.factorial2(2 * (a + b + c) + 1)
        )
        total += coefficient * moment
    return sp.expand(total)


def main() -> None:
    x, y, z = sp.symbols("x y z", real=True)
    params = sp.symbols("b0:7", real=True)
    tensor = build_tensor(params)
    u = sp.Matrix([x, y, z])
    radius_relation = x**2 + y**2 + z**2 - 1

    harmonic = sp.expand(
        sum(
            tensor[i, j, k] * u[i] * u[j] * u[k]
            for i in range(3)
            for j in range(3)
            for k in range(3)
        )
    )
    matrix_tu = sp.Matrix(
        3,
        3,
        lambda j, k: sum(tensor[i, j, k] * u[i] for i in range(3)),
    )
    vector_tuu = sp.Matrix(
        [
            sum(
                tensor[i, j, k] * u[i] * u[j]
                for i in range(3)
                for j in range(3)
            )
            for k in range(3)
        ]
    )

    projection = sp.eye(3) - u * u.T
    curvature = projection * (6 * matrix_tu) * projection - 2 * harmonic * projection
    q_projected = sp.expand(
        2 * (sp.trace(curvature) ** 2 - sp.trace(curvature * curvature))
    )
    q_compact = sp.expand(
        64 * harmonic**2
        + 144 * vector_tuu.dot(vector_tuu)
        - 72 * sp.trace(matrix_tu * matrix_tu)
    )

    difference = sp.expand(q_projected - q_compact)
    remainder = sp.rem(sp.Poly(difference, z), sp.Poly(radius_relation, z)).as_expr()
    if not sp.Poly(sp.expand(remainder), x, y, z, *params).is_zero:
        raise AssertionError("The two determinant formulas disagree on S^2.")

    tau = sp.expand(
        sum(
            tensor[i, j, k] ** 2
            for i in range(3)
            for j in range(3)
            for k in range(3)
        )
    )
    b_matrix = sp.Matrix(
        3,
        3,
        lambda i, j: sum(
            tensor[i, k, ell] * tensor[j, k, ell]
            for k in range(3)
            for ell in range(3)
        ),
    )
    b0 = b_matrix - sp.eye(3) * tau / 3
    b0_sq = sp.expand(sp.trace(b0 * b0))

    integrated = sphere_integral(q_compact**2, x, y, z)
    target = (
        sp.pi
        / 1001
        * (sp.Integer(555264) * tau**2 - sp.Integer(2265600) * b0_sq)
    )
    residual = sp.Poly(sp.expand((integrated - target) / sp.pi), *params)
    if not residual.is_zero:
        raise AssertionError("Compact-form integration does not match the invariant identity.")

    print("ALTERNATIVE COMPACT-FORM CHECK: PASS")
    print("projected determinant equals compact determinant modulo x^2+y^2+z^2-1")
    print("compact determinant integration reproduces the invariant identity exactly")


if __name__ == "__main__":
    main()
