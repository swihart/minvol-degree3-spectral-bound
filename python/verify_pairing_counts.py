#!/usr/bin/env python3
"""Exact combinatorial verification of the quartic pairing-count table.

The script enumerates all pairings of the free sphere-moment half-edges for the
six quartic integrands in proof/DEGREE3_TENSOR_IDENTITY.md.  Surviving complete
contractions are classified as D (tau^2), J (tr(B^2)), or K (tetrahedral).
The dimension-three identity K=tau^2/2-J is then applied.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import prod
from typing import Iterable, Iterator

HalfEdge = tuple[int, int]
Edge = tuple[int, int]


def pairings(items: tuple[HalfEdge, ...]) -> Iterator[tuple[tuple[HalfEdge, HalfEdge], ...]]:
    """Generate all perfect pairings of a tuple of labeled half-edges."""
    if not items:
        yield ()
        return
    first = items[0]
    for index in range(1, len(items)):
        second = items[index]
        rest = items[1:index] + items[index + 1 :]
        for tail in pairings(rest):
            yield ((first, second),) + tail


def classify(edges: Iterable[Edge]) -> str:
    """Classify a complete cubic contraction graph on four tensor vertices."""
    counts = Counter(tuple(sorted(edge)) for edge in edges)
    if any(a == b for a, b in counts):
        return "loop"

    adjacency = {vertex: set() for vertex in range(4)}
    for a, b in counts:
        adjacency[a].add(b)
        adjacency[b].add(a)

    seen = {0}
    stack = [0]
    while stack:
        vertex = stack.pop()
        for neighbor in adjacency[vertex]:
            if neighbor not in seen:
                seen.add(neighbor)
                stack.append(neighbor)

    if len(seen) < 4:
        return "D"
    if len(counts) == 6 and all(multiplicity == 1 for multiplicity in counts.values()):
        return "K"
    return "J"


def odd_double_factorial(number: int) -> int:
    if number < 1 or number % 2 == 0:
        raise ValueError("Expected a positive odd integer.")
    return prod(range(1, number + 1, 2))


def count_case(free_degrees: tuple[int, int, int, int], fixed_edges: tuple[Edge, ...]) -> Counter[str]:
    half_edges: list[HalfEdge] = []
    for vertex, degree in enumerate(free_degrees):
        half_edges.extend((vertex, slot) for slot in range(degree))

    result: Counter[str] = Counter()
    for matching in pairings(tuple(half_edges)):
        moment_edges = [(left[0], right[0]) for left, right in matching]
        result[classify((*fixed_edges, *moment_edges))] += 1
    return result


def main() -> None:
    cases = {
        "Y^4": ((3, 3, 3, 3), ()),
        "Y^2|v|^2": ((3, 3, 2, 2), ((2, 3),)),
        "Y^2|M|^2": ((3, 3, 1, 1), ((2, 3), (2, 3))),
        "|v|^4": ((2, 2, 2, 2), ((0, 1), (2, 3))),
        "|v|^2|M|^2": ((2, 2, 1, 1), ((0, 1), (2, 3), (2, 3))),
        "|M|^4": ((1, 1, 1, 1), ((0, 1), (0, 1), (2, 3), (2, 3))),
    }

    expected = {
        "Y^4": (108, 1944, 1296, 756, 648),
        "Y^2|v|^2": (12, 216, 144, 84, 72),
        "Y^2|M|^2": (6, 36, 0, 6, 36),
        "|v|^4": (4, 40, 16, 12, 24),
        "|v|^2|M|^2": (2, 8, 0, 2, 8),
        "|M|^4": (1, 2, 0, 1, 2),
    }

    reduced: dict[str, tuple[int, int, int]] = {}
    print("PAIRING-COUNT CHECK")
    for name, (degrees, fixed) in cases.items():
        counts = count_case(degrees, fixed)
        free_slots = sum(degrees)
        total_expected = odd_double_factorial(free_slots - 1)
        if sum(counts.values()) != total_expected:
            raise AssertionError(f"Pairing total failed for {name}.")

        n_d = counts["D"]
        n_j = counts["J"]
        n_k = counts["K"]
        n_tau = Fraction(n_d) + Fraction(n_k, 2)
        n_j_reduced = n_j - n_k
        if n_tau.denominator != 1:
            raise AssertionError(f"Nonintegral reduced tau count for {name}.")

        actual = (n_d, n_j, n_k, int(n_tau), n_j_reduced)
        if actual != expected[name]:
            raise AssertionError(f"Unexpected counts for {name}: {actual}")
        reduced[name] = (free_slots // 2, int(n_tau), n_j_reduced)
        print(
            f"{name:17s} D={n_d:4d} J={n_j:4d} K={n_k:4d} "
            f"=> tau^2={int(n_tau):4d}, J={n_j_reduced:4d}"
        )

    coefficients: dict[str, tuple[Fraction, Fraction]] = {}
    for name, (m, n_tau, n_j_reduced) in reduced.items():
        denominator = odd_double_factorial(2 * m + 1)
        coefficients[name] = (
            Fraction(4 * n_tau, denominator),
            Fraction(4 * n_j_reduced, denominator),
        )

    expected_coefficients = {
        "Y^4": (Fraction(16, 715), Fraction(96, 5005)),
        "Y^2|v|^2": (Fraction(16, 495), Fraction(32, 1155)),
        "Y^2|M|^2": (Fraction(8, 315), Fraction(16, 105)),
        "|v|^4": (Fraction(16, 315), Fraction(32, 315)),
        "|v|^2|M|^2": (Fraction(8, 105), Fraction(32, 105)),
        "|M|^4": (Fraction(4, 15), Fraction(8, 15)),
    }
    if coefficients != expected_coefficients:
        raise AssertionError("Moment coefficient table failed.")

    weights = {
        "Y^4": 4096,
        "Y^2|v|^2": 18432,
        "Y^2|M|^2": -9216,
        "|v|^4": 20736,
        "|v|^2|M|^2": -20736,
        "|M|^4": 5184,
    }
    tau_coefficient = sum(Fraction(weights[name]) * coefficients[name][0] for name in cases)
    j_coefficient = sum(Fraction(weights[name]) * coefficients[name][1] for name in cases)
    if tau_coefficient != Fraction(1_310_464, 1001):
        raise AssertionError(f"Unexpected tau^2 coefficient: {tau_coefficient}")
    if j_coefficient != Fraction(-2_265_600, 1001):
        raise AssertionError(f"Unexpected J coefficient: {j_coefficient}")

    b0_tau_coefficient = tau_coefficient + j_coefficient / 3
    if b0_tau_coefficient != Fraction(555_264, 1001):
        raise AssertionError(f"Unexpected B0-form tau coefficient: {b0_tau_coefficient}")

    print(f"q^2 / pi coefficient of tau^2 = {tau_coefficient}")
    print(f"q^2 / pi coefficient of J     = {j_coefficient}")
    print(f"B0-form coefficient of tau^2  = {b0_tau_coefficient}")
    print("PAIRING-COUNT CHECK: PASS")


if __name__ == "__main__":
    main()
