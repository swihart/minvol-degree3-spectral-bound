#!/usr/bin/env python3
"""Independent numerical stress tests for tensor conventions and integrals."""

from __future__ import annotations

from itertools import permutations

import numpy as np


def build_tensor(values: np.ndarray) -> np.ndarray:
    if values.shape != (7,):
        raise ValueError("Expected seven tensor parameters.")
    a, b, c, d, e, f, g = values
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
    tensor = np.zeros((3, 3, 3), dtype=float)
    for key, value in seeds.items():
        for p in set(permutations(key)):
            tensor[p] = value
    return tensor


def evaluate_quantities(tensor: np.ndarray, u: np.ndarray) -> tuple[float, float, float]:
    harmonic = np.einsum("ijk,i,j,k->", tensor, u, u, u)
    matrix_tu = np.einsum("ijk,i->jk", tensor, u)
    vector_tuu = np.einsum("ijk,i,j->k", tensor, u, u)
    projection = np.eye(3) - np.outer(u, u)
    curvature = projection @ (6.0 * matrix_tu) @ projection - 2.0 * harmonic * projection
    norm_sq = float(np.trace(curvature @ curvature))
    q_projected = float(2.0 * (np.trace(curvature) ** 2 - norm_sq))
    q_compact = float(
        64.0 * harmonic**2
        + 144.0 * np.dot(vector_tuu, vector_tuu)
        - 72.0 * np.trace(matrix_tu @ matrix_tu)
    )
    return norm_sq, q_projected, q_compact


def gauss_legendre_sphere(n_z: int = 24, n_phi: int = 64) -> tuple[np.ndarray, np.ndarray]:
    z, w_z = np.polynomial.legendre.leggauss(n_z)
    phi = 2.0 * np.pi * np.arange(n_phi) / n_phi
    points = []
    weights = []
    for zi, wi in zip(z, w_z, strict=True):
        radius = np.sqrt(max(0.0, 1.0 - zi * zi))
        for angle in phi:
            points.append([radius * np.cos(angle), radius * np.sin(angle), zi])
            weights.append(wi * 2.0 * np.pi / n_phi)
    return np.asarray(points), np.asarray(weights)


def tensor_invariants(tensor: np.ndarray) -> tuple[float, float]:
    tau = float(np.einsum("ijk,ijk->", tensor, tensor))
    b_matrix = np.einsum("ikl,jkl->ij", tensor, tensor)
    b0 = b_matrix - np.eye(3) * tau / 3.0
    b0_sq = float(np.trace(b0 @ b0))
    return tau, b0_sq


def random_rotation(rng: np.random.Generator) -> np.ndarray:
    q, _ = np.linalg.qr(rng.normal(size=(3, 3)))
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    return q


def rotate_tensor(tensor: np.ndarray, rotation: np.ndarray) -> np.ndarray:
    return np.einsum("ia,jb,kc,abc->ijk", rotation, rotation, rotation, tensor)


def main() -> None:
    rng = np.random.default_rng(20260902)
    sphere_points, sphere_weights = gauss_legendre_sphere()

    max_pointwise_error = 0.0
    max_norm_relative_error = 0.0
    max_q_relative_error = 0.0
    max_rotation_error = 0.0

    for _ in range(12):
        tensor = build_tensor(rng.normal(size=7))
        tau, b0_sq = tensor_invariants(tensor)
        predicted_norm = np.pi * (176.0 / 7.0) * tau
        predicted_q_sq = np.pi / 1001.0 * (555264.0 * tau**2 - 2265600.0 * b0_sq)

        integrated_norm = 0.0
        integrated_q_sq = 0.0
        for point, weight in zip(sphere_points, sphere_weights, strict=True):
            norm_sq, q_direct, q_compact = evaluate_quantities(tensor, point)
            max_pointwise_error = max(max_pointwise_error, abs(q_direct - q_compact))
            integrated_norm += weight * norm_sq
            integrated_q_sq += weight * q_direct**2

        max_norm_relative_error = max(
            max_norm_relative_error,
            abs(integrated_norm - predicted_norm) / max(1.0, abs(predicted_norm)),
        )
        max_q_relative_error = max(
            max_q_relative_error,
            abs(integrated_q_sq - predicted_q_sq) / max(1.0, abs(predicted_q_sq)),
        )

        rotation = random_rotation(rng)
        rotated = rotate_tensor(tensor, rotation)
        tau_rotated, b0_sq_rotated = tensor_invariants(rotated)
        max_rotation_error = max(
            max_rotation_error,
            abs(tau - tau_rotated),
            abs(b0_sq - b0_sq_rotated),
        )

    if max_pointwise_error > 2e-10:
        raise AssertionError(f"Pointwise determinant mismatch: {max_pointwise_error}")
    if max_norm_relative_error > 2e-12:
        raise AssertionError(f"Norm integral mismatch: {max_norm_relative_error}")
    if max_q_relative_error > 2e-11:
        raise AssertionError(f"q^2 integral mismatch: {max_q_relative_error}")
    if max_rotation_error > 2e-11:
        raise AssertionError(f"Rotation-invariance mismatch: {max_rotation_error}")

    print("NUMERICAL STRESS TESTS: PASS")
    print(f"maximum pointwise determinant error = {max_pointwise_error:.3e}")
    print(f"maximum norm relative error          = {max_norm_relative_error:.3e}")
    print(f"maximum q^2 relative error           = {max_q_relative_error:.3e}")
    print(f"maximum invariant rotation error     = {max_rotation_error:.3e}")


if __name__ == "__main__":
    main()
