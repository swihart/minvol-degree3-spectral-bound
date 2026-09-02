# Claim dependency graph

## Candidate theorem

For every three-dimensional convex body of constant width `d`,

\[
\operatorname{Vol}(K) \ge
\frac{\pi}{1914}
\left(259-27\sqrt{\frac{15183}{17303}}\right)d^3
\approx 0.3836027047\,d^3.
\]

This repository checkpoint does **not** yet label the statement an externally
verified theorem.

## Dependencies

1. **Nishioka support-function framework**
   - `h` is odd after centering.
   - `A_h = nabla^2 h + h I` satisfies `-dI/2 <= A_h <= dI/2`.
   - `Vol(K) = pi*d^3/6 - d*E(h)/2`.
   - Smooth constant-width bodies approximate arbitrary ones in Hausdorff
     distance, with volume convergence.

2. **Refined spectral split**
   - Write `h = h_3 + h_{>=5}`.
   - Orthogonality for the tensor quadratic form gives
     `||A_h||_2^2 = ||A_{h_3}||_2^2 + ||A_{h_{>=5}}||_2^2`.
   - Degree 3 has coefficient `1/22`; all odd degrees at least 5 have
     coefficient at most `1/58`.
   - Therefore
     `E(h) <= ||A_h||_2^2/58 + (9/319)||A_{h_3}||_2^2`.

3. **New degree-3 determinant identity**
   - Represent `h_3(u) = T[u,u,u]` by a symmetric trace-free rank-3 tensor.
   - For `C = A_{h_3}` and `B_ij = T_ikl T_jkl`, with
     `B0 = B - tr(B)I/3`, prove

     \[
     \|C\|_2^2 = \frac{176\pi}{7}\,\tau,
     \]

     \[
     \|4\det C\|_2^2 =
     \frac{\pi}{1001}
     \left(555264\tau^2-2265600\|B_0\|_F^2\right).
     \]

   - Hence

     \[
     \|4\det C\|_2^2
     \le \frac{15183}{17303\pi}\|C\|_2^4.
     \]

4. **Operator/nuclear-norm bridge**
   - For a symmetric `2 x 2` matrix,
     `||C||_*^2 = |C|_F^2 + 2|det C|`.
   - Use Cauchy-Schwarz and the determinant estimate to bound
     `integral ||C||_*^2`.
   - Use tensor-harmonic orthogonality and
     `||A_h(u)||_op <= d/2` to bound `||C||_2^2`.

5. **Final arithmetic**
   - Insert the global bound `||A_h||_2^2 <= 2*pi*d^2` and the refined
     degree-3 bound into the spectral split.
   - Apply Nishioka's volume identity.

6. **Regularity passage**
   - Prove the smooth case first.
   - Pass to arbitrary constant-width bodies using the cited smooth
     approximation and volume continuity.
