# Claim dependency graph

**Release:** v0.1.0 (September 6, 2026)\
**Status:** AI-assisted, non-peer-reviewed research draft seeking independent
mathematical verification

## Candidate theorem

For every three-dimensional convex body of constant width `d`,

\[
\operatorname{Vol}(K) \ge
\frac{\pi}{1914}
\left(259-27\sqrt{\frac{15183}{17303}}\right)d^3
\approx 0.3836027047\,d^3.
\]

The integrated proof is in:

```text
paper/degree3_spectral_refinement.tex
```

The repository does **not** label the statement a peer-reviewed,
independently verified, certified, or accepted theorem.

## Dependencies

1. **Nishioka support-function framework**
   - `h` is odd after subtracting `d/2` from the support function.
   - A translation removes the degree-one harmonic component.
   - `A_h = nabla^2 h + h I` satisfies `-dI/2 <= A_h <= dI/2`.
   - `Vol(K) = pi*d^3/6 - d*E(h)/2`.
   - Smooth same-width bodies approximate arbitrary constant-width bodies in
     Hausdorff distance, with volume convergence.

2. **Refined spectral split**
   - Write `h = h_3 + h_{>=5}`.
   - Tensor-valued harmonic orthogonality gives
     `||A_h||_2^2 = ||A_{h_3}||_2^2 + ||A_{h_{>=5}}||_2^2`.
   - Degree 3 has coefficient `1/22`; all odd degrees at least 5 have
     coefficient at most `1/58`.
   - Therefore
     `E(h) <= ||A_h||_2^2/58 + (9/319)||A_{h_3}||_2^2`.
   - Complete proof: `proof/BRIDGE_LEMMAS.md`, Sections 2--3.

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

   - Human-readable derivation: `proof/DEGREE3_TENSOR_IDENTITY.md`.
   - Exact symbolic verification: `python/verify_degree3_identity.py` and
     `python/verify_degree3_identity_alt.py`.
   - Exact contraction-graph count: `python/verify_pairing_counts.py`, with a
     matching base-R implementation in `R/verify_pairing_counts.R`.

4. **Operator/nuclear-norm bridge**
   - For a symmetric `2 x 2` matrix,
     `||C||_*^2 = |C|_F^2 + 2|det C|`.
   - Cauchy--Schwarz and the determinant estimate bound
     `integral ||C||_*^2`.
   - Tensor-harmonic orthogonality and
     `||A_h(u)||_op <= d/2` bound `||C||_2^2`.
   - Complete proof: `proof/BRIDGE_LEMMAS.md`, Sections 4--5.

5. **Final arithmetic**
   - Insert `||A_h||_2^2 <= 2*pi*d^2` and the refined degree-3 bound into the
     spectral split.
   - Apply Nishioka's volume identity.
   - Complete proof: `proof/BRIDGE_LEMMAS.md`, Section 6.
   - Exact arithmetic check: `python/verify_bound_arithmetic.py`.

6. **Regularity passage**
   - Prove the smooth case first.
   - Pass to arbitrary constant-width bodies using same-width smooth
     approximation and volume continuity.
   - Complete proof: `proof/BRIDGE_LEMMAS.md`, Section 7.

7. **Integrated publication draft**
   - All dependencies above are assembled in
     `paper/degree3_spectral_refinement.tex`.
   - The compiled PDF is `paper/degree3_spectral_refinement.pdf`.
   - The internal line-by-line audit is `proof/PROOF_AUDIT.md`.
   - Build instructions are in `paper/README.md` and `build_paper.sh`.

8. **Still external to the proof package**
   - Independent mathematical review.
   - A systematic literature/novelty review.
   - Verification of HYRA's stronger public claims.
