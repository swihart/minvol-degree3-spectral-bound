#!/usr/bin/env python3
"""Exact symbolic verification of the degree-3 tensor identities.

This script does not assume the key constants.  It constructs a general
seven-parameter symmetric trace-free rank-3 tensor T, forms the spherical
harmonic Y(u)=T[u,u,u], constructs A_Y = Hess_{S^2}Y + Y I as a 3x3 tangent
extension, integrates exact polynomials over S^2, and solves for the
invariant coefficients.
"""

from __future__ import annotations

from itertools import permutations
from typing import Dict, Tuple

import sympy as sp

Index3 = Tuple[int, int, int]


def build_stf_tensor(params: tuple[sp.Symbol, ...]) -> Dict[Index3, sp.Expr]:
    """Return all components of a general symmetric trace-free rank-3 tensor."""
    if len(params) != 7:
        raise ValueError("Exactly seven independent parameters are required.")
    a, b, c, d, e, f, g = params
    independent = {
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
    for key, value in independent.items():
        for permuted in set(permutations(key)):
            tensor[permuted] = value
    if len(tensor) != 27:
        raise RuntimeError("Tensor construction did not fill all 27 components.")
    return tensor


def sphere_monomial_integral(exponents: tuple[int, int, int]) -> sp.Expr:
    """Exact integral of x^i y^j z^k over the unit sphere S^2."""
    i, j, k = exponents
    if i % 2 or j % 2 or k % 2:
        return sp.Integer(0)
    a, b, c = i // 2, j // 2, k // 2
    numerator = (
        4
        * sp.pi
        * sp.factorial2(2 * a - 1)
        * sp.factorial2(2 * b - 1)
        * sp.factorial2(2 * c - 1)
    )
    denominator = sp.factorial2(2 * (a + b + c) + 1)
    return sp.cancel(numerator / denominator)


def sphere_integral(expr: sp.Expr, xyz: tuple[sp.Symbol, ...]) -> sp.Expr:
    """Integrate a polynomial exactly over S^2 using monomial moments."""
    if len(xyz) != 3:
        raise ValueError("Expected three Cartesian variables.")
    poly = sp.Poly(sp.expand(expr), *xyz)
    total = sp.Integer(0)
    for exponents, coefficient in poly.terms():
        total += coefficient * sphere_monomial_integral(exponents)
    return sp.expand(total)


def derive_scalar_multiple(lhs: sp.Expr, rhs_basis: sp.Expr, params: tuple[sp.Symbol, ...]) -> sp.Expr:
    """Solve lhs = alpha*rhs_basis as a polynomial identity."""
    alpha = sp.Symbol("alpha")
    equations = sp.Poly(sp.expand(lhs - alpha * rhs_basis), *params).coeffs()
    solutions = sp.solve(equations, [alpha], dict=True)
    if len(solutions) != 1 or alpha not in solutions[0]:
        raise RuntimeError("Could not derive a unique scalar coefficient.")
    value = sp.factor(solutions[0][alpha])
    residual = sp.Poly(sp.expand(lhs - value * rhs_basis), *params)
    if not residual.is_zero:
        raise AssertionError("Derived scalar coefficient leaves a nonzero residual.")
    return value


def derive_two_invariant_coefficients(
    lhs: sp.Expr,
    invariant_1: sp.Expr,
    invariant_2: sp.Expr,
    params: tuple[sp.Symbol, ...],
) -> tuple[sp.Expr, sp.Expr]:
    """Solve lhs = alpha*invariant_1 + beta*invariant_2 exactly."""
    alpha, beta = sp.symbols("alpha beta")
    equations = sp.Poly(
        sp.expand(lhs - alpha * invariant_1 - beta * invariant_2), *params
    ).coeffs()
    solutions = sp.solve(equations, [alpha, beta], dict=True)
    if len(solutions) != 1 or alpha not in solutions[0] or beta not in solutions[0]:
        raise RuntimeError("Could not derive unique invariant coefficients.")
    alpha_value = sp.factor(solutions[0][alpha])
    beta_value = sp.factor(solutions[0][beta])
    residual = sp.Poly(
        sp.expand(lhs - alpha_value * invariant_1 - beta_value * invariant_2),
        *params,
    )
    if not residual.is_zero:
        raise AssertionError("Invariant decomposition leaves a nonzero residual.")
    return alpha_value, beta_value


def main() -> None:
    x, y, z = sp.symbols("x y z", real=True)
    xyz = (x, y, z)
    params = sp.symbols("a0:7", real=True)
    tensor = build_stf_tensor(params)
    u = sp.Matrix(xyz)

    # Y(u) = T_{ijk} u_i u_j u_k.
    harmonic = sp.expand(
        sum(
            tensor[i, j, k] * u[i] * u[j] * u[k]
            for i in range(3)
            for j in range(3)
            for k in range(3)
        )
    )
    laplacian = sp.expand(sum(sp.diff(harmonic, variable, 2) for variable in xyz))
    if laplacian != 0:
        raise AssertionError("The general cubic is not harmonic.")

    # For a homogeneous cubic restricted to S^2:
    # Hess_{S^2}Y + Y I = P D^2Y P - 2Y P.
    matrix_tu = sp.Matrix(
        3,
        3,
        lambda j, k: sum(tensor[i, j, k] * u[i] for i in range(3)),
    )
    projection = sp.eye(3) - u * u.T
    curvature = projection * (6 * matrix_tu) * projection - 2 * harmonic * projection

    trace_curvature = sp.expand(sp.trace(curvature))
    frobenius_sq = sp.expand(sp.trace(curvature * curvature))

    # The 3x3 extension has eigenvalues lambda_1, lambda_2, 0 on S^2.
    # Hence 4 det_{u^perp}(C) = 2[(tr C)^2 - tr(C^2)].
    q = sp.expand(2 * (trace_curvature**2 - frobenius_sq))

    integrated_norm_without_pi = sp.expand(sphere_integral(frobenius_sq, xyz) / sp.pi)
    integrated_q_sq_without_pi = sp.expand(sphere_integral(q**2, xyz) / sp.pi)

    tau = sp.expand(
        sum(
            tensor[i, j, k] ** 2
            for i in range(3)
            for j in range(3)
            for k in range(3)
        )
    )
    contraction_b = sp.Matrix(
        3,
        3,
        lambda i, j: sum(
            tensor[i, k, ell] * tensor[j, k, ell]
            for k in range(3)
            for ell in range(3)
        ),
    )
    b0 = contraction_b - sp.eye(3) * tau / 3
    b0_sq = sp.expand(sp.trace(b0 * b0))

    norm_coefficient = derive_scalar_multiple(
        integrated_norm_without_pi, tau, params
    )
    q_tau_coefficient, q_b0_coefficient = derive_two_invariant_coefficients(
        integrated_q_sq_without_pi, tau**2, b0_sq, params
    )

    if q_b0_coefficient >= 0:
        raise AssertionError("The B0 coefficient must be negative for the upper bound.")

    determinant_ratio = sp.factor(q_tau_coefficient / norm_coefficient**2)
    s = sp.sqrt(determinant_ratio)
    volume_coefficient = sp.factor(sp.pi * (sp.Rational(1, 6) - (20 + 9 * s) / 638))
    nishioka_coefficient = sp.Rational(4, 33) * sp.pi
    improvement = sp.simplify(volume_coefficient - nishioka_coefficient)

    expected_ratio = sp.Rational(15183, 17303)
    if determinant_ratio != expected_ratio:
        raise AssertionError(
            f"Unexpected determinant ratio: {determinant_ratio} != {expected_ratio}"
        )

    print("EXACT DEGREE-3 IDENTITY CHECK: PASS")
    print(f"harmonic Laplacian                       = {laplacian}")
    print(f"integral |A_Y|^2 / (pi*tau)             = {norm_coefficient}")
    print(f"tau^2 coefficient in integral q^2 / pi  = {q_tau_coefficient}")
    print(f"|B0|^2 coefficient in integral q^2 / pi = {q_b0_coefficient}")
    print(f"determinant ratio                        = {determinant_ratio}")
    print(f"candidate volume coefficient             = {volume_coefficient}")
    print(f"candidate decimal                        = {sp.N(volume_coefficient, 18)}")
    print(f"Nishioka decimal                         = {sp.N(nishioka_coefficient, 18)}")
    print(f"absolute improvement                     = {sp.N(improvement, 18)}")


if __name__ == "__main__":
    main()
