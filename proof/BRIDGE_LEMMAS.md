# Bridge lemmas for the degree-3 spectral refinement

## Status

This file gives a line-by-line proof of the **noncomputational bridge** from the
new degree-3 determinant estimate to the proposed volume bound.  It does not
prove the determinant estimate itself; that remains the central algebraic lemma
and is isolated explicitly below.

The argument is for smooth support functions first and then passes to arbitrary
convex bodies of constant width by Nishioka's smooth-approximation lemma.

## 1. Notation and sourced input

Fix a width `d > 0` and put

\[
c:=\frac d2.
\]

Let `h` be the centered support function of a smooth convex body of constant
width `d`, translated so that its degree-one spherical-harmonic component is
zero.  Thus

\[
h(-u)=-h(u),\qquad h\perp \mathcal H_1.
\]

On the unit sphere \(S^2\), define the self-adjoint tangent endomorphism

\[
A_h:=\nabla^2h+hI.
\]

Nishioka's support-function formulation gives the pointwise constraint

\[
-cI\preceq A_h(u)\preceq cI\qquad(u\in S^2),
\tag{1.1}
\]

and the volume identity

\[
\operatorname{Vol}(K)=\frac{\pi d^3}{6}-\frac d2 E(h),
\qquad
E(h):=\int_{S^2}\left(\frac12|\nabla h|^2-h^2\right)d\sigma.
\tag{1.2}
\]

For tangent endomorphism fields `A` and `B`, write

\[
\langle A,B\rangle_2:=\int_{S^2}\operatorname{tr}(AB)\,d\sigma,
\qquad
\|A\|_2^2:=\langle A,A\rangle_2.
\]

Decompose the odd spherical-harmonic expansion as

\[
h=h_3+h_{\ge5},
\qquad
h_{\ge5}:=\sum_{\substack{\ell\ge5\\ \ell\text{ odd}}}h_\ell,
\]

and set

\[
C:=A_{h_3},\qquad
N:=\|A_h\|_2^2,\qquad
N_3:=\|C\|_2^2.
\tag{1.3}
\]

The proof below uses the following central degree-3 estimate, whose exact
symbolic verification is already implemented in the repository and whose
human-readable derivation is to be supplied separately.

**Degree-3 determinant estimate.** For every \(Y\in\mathcal H_3\), with
\(C=A_Y\) and determinant taken on the tangent plane,

\[
\|4\det C\|_2^2
\le
\frac{15183}{17303\pi}\,\|C\|_2^4.
\tag{1.4}
\]

Define

\[
s:=\sqrt{\frac{15183}{17303}}.
\tag{1.5}
\]

Then (1.4) is equivalently

\[
\|4\det C\|_2\le \frac{s}{\sqrt\pi}N_3.
\tag{1.6}
\]

## 2. Tensor-valued harmonic orthogonality

### Lemma 2.1 (polarized Bochner identity)

For smooth real-valued functions \(f,g\) on \(S^2\),

\[
\int_{S^2}\langle\nabla^2f,\nabla^2g\rangle\,d\sigma
=
\int_{S^2}(\Delta f)(\Delta g)\,d\sigma
-
\int_{S^2}\langle\nabla f,\nabla g\rangle\,d\sigma.
\tag{2.1}
\]

#### Proof

Nishioka uses the integrated Bochner identity

\[
\int_{S^2}|\nabla^2q|^2\,d\sigma
=
\int_{S^2}(\Delta q)^2\,d\sigma
-
\int_{S^2}|\nabla q|^2\,d\sigma
\tag{2.2}
\]

for every smooth `q`.  Apply (2.2) to `q=f+g` and to `q=f-g`, subtract the
second equality from the first, and divide by four.  The three quadratic terms
polarize respectively to

\[
\langle\nabla^2f,\nabla^2g\rangle,
\qquad
(\Delta f)(\Delta g),
\qquad
\langle\nabla f,\nabla g\rangle.
\]

This gives (2.1).  \(\square\)

### Lemma 2.2 (orthogonality of the curvature tensors)

If \(f\in\mathcal H_\ell\) and \(g\in\mathcal H_m\) with \(\ell\ne m\), then

\[
\langle A_f,A_g\rangle_2=0.
\tag{2.3}
\]

If instead \(f,g\in\mathcal H_\ell\), and
\(\lambda_\ell=\ell(\ell+1)\), then

\[
\langle A_f,A_g\rangle_2
=(\lambda_\ell-1)(\lambda_\ell-2)
\int_{S^2}fg\,d\sigma.
\tag{2.4}
\]

#### Proof

Expand the pointwise Frobenius product:

\[
\begin{aligned}
\langle A_f,A_g\rangle
&=\langle\nabla^2f+fI,\nabla^2g+gI\rangle\\
&=\langle\nabla^2f,\nabla^2g\rangle
  +g\,\Delta f+f\,\Delta g+2fg,
\end{aligned}
\tag{2.5}
\]

because `tr(I)=2` on the two-dimensional tangent plane.  Integrating and using
Lemma 2.1 yields

\[
\begin{aligned}
\langle A_f,A_g\rangle_2
={}&\int_{S^2}(\Delta f)(\Delta g)\,d\sigma
 -\int_{S^2}\langle\nabla f,\nabla g\rangle\,d\sigma\\
&+\int_{S^2}g\Delta f\,d\sigma
 +\int_{S^2}f\Delta g\,d\sigma
 +2\int_{S^2}fg\,d\sigma.
\end{aligned}
\tag{2.6}
\]

For spherical harmonics,

\[
-\Delta f=\lambda_\ell f,
\qquad
-\Delta g=\lambda_m g.
\]

Also, integration by parts gives

\[
\int_{S^2}\langle\nabla f,\nabla g\rangle\,d\sigma
=-\int_{S^2}f\Delta g\,d\sigma
=\lambda_m\int_{S^2}fg\,d\sigma.
\tag{2.7}
\]

If \(\ell\ne m\), then \(\int fg=0\) by orthogonality of distinct harmonic
degrees.  Every term on the right of (2.6) is therefore zero, proving (2.3).

If \(\ell=m\), write \(\lambda=\lambda_\ell\).  Substitution in (2.6) gives

\[
\begin{aligned}
\langle A_f,A_g\rangle_2
&=(\lambda^2-\lambda-2\lambda+2)
  \int_{S^2}fg\,d\sigma\\
&=(\lambda-1)(\lambda-2)
  \int_{S^2}fg\,d\sigma,
\end{aligned}
\]

which is (2.4).  \(\square\)

### Corollary 2.3 (projection identity)

With the notation (1.3),

\[
N=\sum_{\substack{\ell\ge3\\\ell\text{ odd}}}\|A_{h_\ell}\|_2^2,
\tag{2.8}
\]

and

\[
\boxed{
N_3=\langle A_h,C\rangle_2.
}
\tag{2.9}
\]

#### Proof

Because `h` is smooth, its spherical-harmonic expansion converges in every
Sobolev norm, in particular in `H^2(S^2)`.  Since
`f -> A_f = nabla^2 f + fI` is continuous from `H^2` to tensor-valued `L^2`,

\[
A_h=\sum_{\substack{\ell\ge3\\\ell\text{ odd}}}A_{h_\ell}
\quad\text{in }L^2.
\]

Lemma 2.2 makes the summands pairwise orthogonal, proving (2.8).  Taking the
inner product with `C=A_{h_3}` leaves only the degree-three term:

\[
\langle A_h,C\rangle_2
=\langle A_{h_3},A_{h_3}\rangle_2=N_3.
\]

This proves (2.9).  \(\square\)

## 3. Refined spectral split

### Lemma 3.1

For every smooth admissible `h`,

\[
\boxed{
E(h)\le \frac1{58}N+\frac9{319}N_3.
}
\tag{3.1}
\]

#### Proof

Nishioka's harmonic calculation gives, for
\(h_\ell\in\mathcal H_\ell\),

\[
E(h_\ell)=\frac{\lambda_\ell-2}{2}\|h_\ell\|_2^2,
\qquad
\|A_{h_\ell}\|_2^2
=(\lambda_\ell-1)(\lambda_\ell-2)\|h_\ell\|_2^2.
\tag{3.2}
\]

Hence

\[
E(h_\ell)
=\frac{1}{2(\lambda_\ell-1)}\|A_{h_\ell}\|_2^2.
\tag{3.3}
\]

For degree three, \(\lambda_3=12\), so the coefficient in (3.3) is `1/22`.
For every remaining odd degree \(\ell\ge5\), one has
\(\lambda_\ell\ge\lambda_5=30\), so

\[
\frac{1}{2(\lambda_\ell-1)}\le\frac1{58}.
\tag{3.4}
\]

Using Corollary 2.3 and orthogonality of `E` across harmonic degrees,

\[
\begin{aligned}
E(h)
&\le \frac1{22}N_3+\frac1{58}(N-N_3)\\
&=\frac1{58}N+
  \left(\frac1{22}-\frac1{58}\right)N_3.
\end{aligned}
\]

Finally,

\[
\frac1{22}-\frac1{58}
=\frac{36}{1276}=\frac9{319},
\]

which proves (3.1).  \(\square\)

## 4. From the determinant estimate to a nuclear-norm estimate

For a self-adjoint endomorphism `M` of a two-dimensional Euclidean space,
write `|M|` for its Frobenius norm, `||M||_op` for its operator norm, and
`||M||_*` for its nuclear norm.

### Lemma 4.1 (two-dimensional nuclear-norm identity)

For every real symmetric `2 x 2` matrix `M`,

\[
\boxed{
\|M\|_*^2=|M|^2+2|\det M|.
}
\tag{4.1}
\]

#### Proof

Let \(\mu_1,\mu_2\) be the eigenvalues of `M`.  Then

\[
\|M\|_*=|\mu_1|+|\mu_2|,
\qquad
|M|^2=\mu_1^2+\mu_2^2,
\qquad
|\det M|=|\mu_1\mu_2|.
\]

Therefore

\[
\|M\|_*^2
=(|\mu_1|+|\mu_2|)^2
=\mu_1^2+\mu_2^2+2|\mu_1\mu_2|,
\]

which is (4.1).  \(\square\)

### Lemma 4.2 (integrated nuclear-norm bound for the cubic mode)

Assume the degree-3 determinant estimate (1.4).  Then

\[
\boxed{
\int_{S^2}\|C(u)\|_*^2\,d\sigma(u)
\le (1+s)N_3,
}
\tag{4.2}
\]

and consequently

\[
\boxed{
\left(\int_{S^2}\|C(u)\|_*\,d\sigma(u)\right)^2
\le 4\pi(1+s)N_3.
}
\tag{4.3}
\]

#### Proof

Put

\[
q(u):=4\det C(u).
\]

By Lemma 4.1,

\[
\|C(u)\|_*^2=|C(u)|^2+\frac12|q(u)|.
\tag{4.4}
\]

Integrating gives

\[
\int_{S^2}\|C\|_*^2\,d\sigma
=N_3+\frac12\|q\|_{L^1}.
\tag{4.5}
\]

Since \(\sigma(S^2)=4\pi\), Cauchy--Schwarz yields

\[
\|q\|_{L^1}
\le (4\pi)^{1/2}\|q\|_{L^2}
=2\sqrt\pi\,\|q\|_{L^2}.
\tag{4.6}
\]

Using (1.6),

\[
\|q\|_{L^1}
\le 2\sqrt\pi\left(\frac{s}{\sqrt\pi}N_3\right)
=2sN_3.
\tag{4.7}
\]

Substitution in (4.5) proves (4.2).  A second application of
Cauchy--Schwarz, now to the nonnegative function `||C||_*`, gives

\[
\left(\int_{S^2}\|C\|_*\,d\sigma\right)^2
\le 4\pi\int_{S^2}\|C\|_*^2\,d\sigma.
\]

Combining this with (4.2) proves (4.3).  \(\square\)

## 5. The degree-3 curvature budget

### Lemma 5.1 (elementary operator/nuclear duality)

If `A` and `M` are self-adjoint endomorphisms of a two-dimensional Euclidean
space, then

\[
|\operatorname{tr}(AM)|\le \|A\|_{\mathrm{op}}\|M\|_*.
\tag{5.1}
\]

#### Proof

Choose an orthonormal eigenbasis \(e_1,e_2\) of `M`, with eigenvalues
\(\mu_1,\mu_2\).  Then

\[
\operatorname{tr}(AM)
=\mu_1\langle Ae_1,e_1\rangle
 +\mu_2\langle Ae_2,e_2\rangle.
\]

Because
\(|\langle Ae_i,e_i\rangle|\le\|A\|_{\mathrm{op}}\),

\[
|\operatorname{tr}(AM)|
\le \|A\|_{\mathrm{op}}(|\mu_1|+|\mu_2|)
=\|A\|_{\mathrm{op}}\|M\|_*.
\]

This proves (5.1).  \(\square\)

### Lemma 5.2 (improved bound on the cubic component)

Assume the degree-3 determinant estimate (1.4).  Then every smooth admissible
`h` satisfies

\[
\boxed{
N_3\le \pi d^2(1+s).
}
\tag{5.2}
\]

#### Proof

The pointwise matrix constraint (1.1) implies

\[
\|A_h(u)\|_{\mathrm{op}}\le c=\frac d2.
\tag{5.3}
\]

By the projection identity (2.9), Lemma 5.1, and (5.3),

\[
\begin{aligned}
N_3
&=\int_{S^2}\operatorname{tr}(A_hC)\,d\sigma\\
&\le \int_{S^2}|\operatorname{tr}(A_hC)|\,d\sigma\\
&\le c\int_{S^2}\|C\|_*\,d\sigma.
\end{aligned}
\tag{5.4}
\]

If \(N_3=0\), then (5.2) is immediate.  Suppose \(N_3>0\).  Squaring (5.4)
and applying (4.3),

\[
N_3^2
\le c^2\left(\int_{S^2}\|C\|_*\,d\sigma\right)^2
\le 4\pi c^2(1+s)N_3.
\]

Divide by `N_3` and use \(c=d/2\):

\[
N_3\le4\pi\left(\frac d2\right)^2(1+s)
=\pi d^2(1+s).
\]

This proves (5.2).  \(\square\)

## 6. Final assembly in the smooth class

### Lemma 6.1 (global curvature budget)

Every smooth admissible `h` satisfies

\[
\boxed{
N\le2\pi d^2.
}
\tag{6.1}
\]

#### Proof

At each `u`, the two eigenvalues of `A_h(u)` lie in `[-c,c]` by (1.1).
Therefore

\[
|A_h(u)|^2\le2c^2=\frac{d^2}{2}.
\]

Integrating over the sphere of area `4*pi` gives

\[
N\le4\pi\frac{d^2}{2}=2\pi d^2.
\]

\(\square\)

### Theorem 6.2 (smooth candidate bound, conditional only on (1.4))

Every smooth convex body `K` of constant width `d` satisfies

\[
\boxed{
\operatorname{Vol}(K)
\ge
\frac{\pi}{1914}
\left(259-27\sqrt{\frac{15183}{17303}}\right)d^3.
}
\tag{6.2}
\]

#### Proof

Combine Lemma 3.1, Lemma 5.2, and Lemma 6.1:

\[
\begin{aligned}
E(h)
&\le \frac1{58}N+\frac9{319}N_3\\
&\le \frac{2\pi d^2}{58}
 +\frac9{319}\pi d^2(1+s)\\
&=\frac{\pi d^2}{319}(20+9s).
\end{aligned}
\tag{6.3}
\]

Insert (6.3) in the volume identity (1.2):

\[
\begin{aligned}
\operatorname{Vol}(K)
&\ge \frac{\pi d^3}{6}
 -\frac d2\frac{\pi d^2}{319}(20+9s)\\
&=\pi d^3\left(\frac16-\frac{20+9s}{638}\right)\\
&=\frac{\pi d^3}{1914}(259-27s).
\end{aligned}
\]

Substitute the definition (1.5) of `s` to obtain (6.2).  \(\square\)

### Corollary 6.3 (strict improvement over Nishioka, conditional on (1.4))

The coefficient in (6.2) is strictly larger than `4*pi/33`.

#### Proof

Since `15183 < 17303`, one has `s < 1`.  Direct subtraction gives

\[
\frac{1}{1914}(259-27s)-\frac4{33}
=\frac9{638}(1-s)>0.
\]

Multiplying by `pi` proves the claim.  \(\square\)

## 7. Passage to arbitrary constant-width bodies

### Theorem 7.1

Assume the degree-3 determinant estimate (1.4).  Then (6.2) holds for every
three-dimensional convex body of constant width `d`, without a smoothness
assumption.

#### Proof

Let `K` be an arbitrary convex body of constant width `d`.  Nishioka's Lemma 2
states that `K` can be approximated in the Hausdorff metric by convex bodies
`K_j` of the same constant width with smooth support functions, and that volume
is continuous for Hausdorff convergence.  Thus

\[
K_j\longrightarrow K
\quad\text{and}\quad
\operatorname{Vol}(K_j)\longrightarrow\operatorname{Vol}(K).
\]

Theorem 6.2 applies to every `K_j`, so

\[
\operatorname{Vol}(K_j)
\ge
\frac{\pi}{1914}
\left(259-27\sqrt{\frac{15183}{17303}}\right)d^3.
\]

Pass to the limit as `j -> infinity`.  The right-hand side is independent of
`j`, and volume convergence gives the same inequality for `K`.  \(\square\)

## 8. What this file establishes

Subject only to the degree-3 determinant estimate (1.4), the complete bridge
from Nishioka's support-function framework to the proposed volume coefficient is
now explicit.  The only new mathematical dependency not proved in this file is
(1.4), together with the stronger exact identity from which it follows.

The next proof file should therefore establish the degree-3 tensor identity:

\[
\|A_Y\|_2^2=\frac{176\pi}{7}\tau,
\]

\[
\|4\det A_Y\|_2^2
=
\frac{\pi}{1001}
\left(555264\tau^2-2265600\|B_0\|_F^2\right).
\]

That derivation must use exactly the tensor and determinant conventions tested
by the Python and R programs.

## Source used for the inherited framework

Akatsuki Nishioka, "An improved lower bound for the three-dimensional
Blaschke--Lebesgue problem from spectral and dual perspectives," Journal of
Mathematical Analysis and Applications 566 (2027), 131038, especially Sections
2--4 and Lemma 2.
