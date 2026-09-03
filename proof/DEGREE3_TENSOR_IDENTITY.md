# Human-readable derivation of the degree-3 tensor identity

## Status

This file supplies a hand-auditable derivation of the central algebraic lemma
used in `proof/BRIDGE_LEMMAS.md`.  The derivation is independent of the final
volume arithmetic.  Exact symbolic checks remain in
`python/verify_degree3_identity.py` and
`python/verify_degree3_identity_alt.py`; the purpose here is to explain why the
identities are true rather than merely report a computer expansion.

All indices range over `{1,2,3}` and repeated indices are summed.  The metric is
the Euclidean metric, so raising and lowering indices has no effect.

## 1. Statement of the degree-3 lemma

Let `T` be a real symmetric trace-free rank-3 tensor on `R^3`:

\[
T_{ijk}=T_{(ijk)},
\qquad
T_{iik}=0.
\tag{1.1}
\]

Define the homogeneous cubic

\[
F(x):=T_{ijk}x_i x_j x_k
\tag{1.2}
\]

and let

\[
Y:=F|_{S^2}.
\]

For `u in S^2`, set

\[
C(u):=A_Y(u)=\nabla^2_{S^2}Y(u)+Y(u)I_{T_uS^2}.
\tag{1.3}
\]

Introduce the tensor invariants

\[
\tau:=T_{ijk}T_{ijk},
\qquad
B_{ij}:=T_{ikl}T_{jkl},
\qquad
B_0:=B-\frac{\tau}{3}I.
\tag{1.4}
\]

Since `tr B = tau`, the matrix `B_0` is traceless.

The goal is to prove

\[
\boxed{
\int_{S^2}|C|^2\,d\sigma=\frac{176\pi}{7}\,\tau
}
\tag{1.5}
\]

and, with the determinant taken on the two-dimensional tangent plane,

\[
\boxed{
\int_{S^2}\bigl(4\det C\bigr)^2\,d\sigma
=
\frac{\pi}{1001}
\left(555264\,\tau^2-2265600\,|B_0|^2\right).
}
\tag{1.6}
\]

It follows immediately that

\[
\boxed{
\|4\det C\|_{L^2(S^2)}^2
\le
\frac{15183}{17303\pi}\,\|C\|_{L^2(S^2)}^4.
}
\tag{1.7}
\]

## 2. Harmonic cubics and symmetric trace-free tensors

Because `T` is symmetric,

\[
\partial_a F=3T_{ajk}x_jx_k,
\qquad
\partial_a\partial_b F=6T_{abk}x_k.
\tag{2.1}
\]

Consequently,

\[
\Delta_{\mathbb R^3}F
=6T_{iik}x_k.
\tag{2.2}
\]

Thus `F` is harmonic if and only if `T` is trace-free.  Every degree-3
spherical harmonic is the restriction of a unique harmonic homogeneous cubic,
so (1.2) represents an arbitrary element of `H_3`.

## 3. The spherical curvature tensor

Fix `u in S^2` and write

\[
P:=I-u\otimes u,
\tag{3.1}
\]

the orthogonal projection onto `T_uS^2=u^perp`.  Define

\[
M(u)_{jk}:=T_{ijk}u_i,
\qquad
v(u)_k:=T_{ijk}u_i u_j=M(u)u,
\qquad
Y(u)=u^TM(u)u.
\tag{3.2}
\]

The Euclidean Hessian of `F` at `u` is

\[
D^2F(u)=6M(u).
\tag{3.3}
\]

### Lemma 3.1 (restriction Hessian formula)

For tangent vectors `xi, eta in T_uS^2`,

\[
\nabla^2_{S^2}Y(\xi,\eta)
=D^2F(u)[\xi,\eta]-3Y(u)\langle\xi,\eta\rangle.
\tag{3.4}
\]

#### Proof

Let `X` and `Z` be tangent vector fields with `X(u)=xi` and `Z(u)=eta`.
For the unit sphere,

\[
D_XZ=\nabla^{S^2}_XZ-\langle X,Z\rangle u.
\tag{3.5}
\]

Therefore

\[
\begin{aligned}
\nabla^2_{S^2}Y(\xi,\eta)
&=X(ZF)-\bigl(\nabla^{S^2}_XZ\bigr)F\\
&=D^2F(u)[\xi,\eta]
  +DF(u)\bigl(D_XZ-\nabla^{S^2}_XZ\bigr)\\
&=D^2F(u)[\xi,\eta]
  -\langle\xi,\eta\rangle\,DF(u)[u].
\end{aligned}
\]

Euler's identity for the homogeneous cubic gives `DF(u)[u]=3F(u)=3Y(u)`,
which proves (3.4).  \(\square\)

Adding `Y I` to (3.4) gives the tangent endomorphism

\[
\boxed{
C=6PMP-2YP.
}
\tag{3.6}
\]

Here and below we regard a tangent endomorphism as a `3 x 3` symmetric matrix
that vanishes on the normal direction `u`.  Its nonzero eigenvalues are exactly
the two tangent eigenvalues.

## 4. A compact formula for `4 det C`

Trace-freeness of `T` implies

\[
\operatorname{tr}M=T_{ijj}u_i=0.
\tag{4.1}
\]

Since `P=I-u u^T`,

\[
\operatorname{tr}(PMP)
=\operatorname{tr}(MP)
=\operatorname{tr}M-u^TMu
=-Y.
\tag{4.2}
\]

Choose an orthonormal basis whose first vector is `u`.  In block form,

\[
M=
\begin{pmatrix}
Y&w^T\\
w&N
\end{pmatrix},
\qquad
v=Mu=
\begin{pmatrix}
Y\\w
\end{pmatrix},
\qquad
PMP=
\begin{pmatrix}
0&0\\
0&N
\end{pmatrix}.
\]

It follows that

\[
|PMP|^2=|M|^2-2|v|^2+Y^2.
\tag{4.3}
\]

Using (3.6), (4.2), `|P|^2=tr P=2`, and the fact that `PMP` is tangent,

\[
\begin{aligned}
\operatorname{tr}C
&=6\operatorname{tr}(PMP)-2Y\operatorname{tr}P
=-10Y,
\tag{4.4}\\
|C|^2
&=36|PMP|^2-24Y\langle PMP,P\rangle+4Y^2|P|^2\\
&=36|PMP|^2-24Y\operatorname{tr}(PMP)+8Y^2\\
&=36|M|^2-72|v|^2+68Y^2.
\tag{4.5}
\end{aligned}
\]

If the tangent eigenvalues of `C` are `mu_1,mu_2`, then the `3 x 3`
extension has eigenvalues `mu_1,mu_2,0`.  Hence

\[
4\det C
=2\left((\operatorname{tr}C)^2-\operatorname{tr}(C^2)\right).
\tag{4.6}
\]

Substitution of (4.4)-(4.5) yields

\[
\boxed{
q(u):=4\det C(u)
=64Y(u)^2+144|v(u)|^2-72|M(u)|^2.
}
\tag{4.7}
\]

This is the compact determinant formula checked independently by the two exact
Python scripts and by the Python and R numerical tests.

## 5. Spherical moments

For `2m` indices in dimension three,

\[
\boxed{
\int_{S^2}u_{i_1}\cdots u_{i_{2m}}\,d\sigma
=
\frac{4\pi}{(2m+1)!!}
\sum_{\mathcal P}
\prod_{\{a,b\}\in\mathcal P}\delta_{i_ai_b},
}
\tag{5.1}
\]

where the sum runs over all pairings `P` of `{1,...,2m}`.  Odd moments vanish.
To see (5.1), let `G=RU` be a standard Gaussian vector in `R^3`, with `U`
uniform on `S^2` and independent of the radius `R`.  Wick's Gaussian moment
formula gives

\[
\mathbb E[G_{i_1}\cdots G_{i_{2m}}]
=\sum_{\mathcal P}\prod_{\{a,b\}\in\mathcal P}\delta_{i_ai_b},
\]

while `E[R^(2m)]=(2m+1)!!` and

\[
\mathbb E[U_{i_1}\cdots U_{i_{2m}}]
=\frac1{4\pi}\int_{S^2}u_{i_1}\cdots u_{i_{2m}}\,d\sigma.
\]

Dividing the Gaussian identity by `E[R^(2m)]` proves (5.1).

Three low-order consequences will be used first.  Since a trace formed inside a
single copy of `T` vanishes,

\[
\begin{aligned}
\int_{S^2}Y^2\,d\sigma
&=\frac{4\pi}{7!!}\,(3!)\tau
=\frac{8\pi}{35}\tau,
\tag{5.2}\\
\int_{S^2}|v|^2\,d\sigma
&=\frac{4\pi}{5!!}\,(2)\tau
=\frac{8\pi}{15}\tau,
\tag{5.3}\\
\int_{S^2}|M|^2\,d\sigma
&=\frac{4\pi}{3}\tau.
\tag{5.4}
\end{aligned}
\]

Indeed, in (5.2) all three indices of one copy of `T` must be paired with the
three indices of the other, giving `3!` pairings.  In (5.3), the two nonzero
pairings cross between the two copies of `T`.  Equation (5.4) follows from
`|M|^2=B_{ij}u_i u_j` and `tr B=tau`.

Now integrate (4.5):

\[
\begin{aligned}
\int_{S^2}|C|^2\,d\sigma
&=36\frac{4\pi}{3}\tau
 -72\frac{8\pi}{15}\tau
 +68\frac{8\pi}{35}\tau\\
&=\frac{176\pi}{7}\tau.
\end{aligned}
\tag{5.5}
\]

This proves (1.5).

## 6. The two quartic contractions

Besides `tau^2`, introduce

\[
J:=\operatorname{tr}(B^2)=B_{ij}B_{ij}.
\tag{6.1}
\]

and the tetrahedral contraction

\[
K:=T_{abc}T_{ade}T_{bdf}T_{cef}.
\tag{6.2}
\]

The moment expansion of a product of four copies of `T` naturally produces
three contraction graphs.  Representative index contractions are

\[
D=(T_{abc}T_{abc})(T_{def}T_{def})=\tau^2,
\]

\[
J=T_{abc}T_{dbc}T_{aef}T_{def}=\operatorname{tr}(B^2),
\]

and the complete tetrahedral contraction `K` in (6.2).  By symmetry of `T`
and relabeling of dummy indices, every graph of the same type has the same
value.  In dimension three the three values are related.

### Lemma 6.1 (dimension-three quartic relation)

\[
\boxed{K=\frac12\tau^2-J.}
\tag{6.3}
\]

#### Proof

For each `i`, let `A_i` be the symmetric traceless `3 x 3` matrix

\[
(A_i)_{jk}:=T_{ijk}.
\tag{6.4}
\]

Symmetry of `A_i` follows from symmetry of `T`, and
`tr A_i=T_{ijj}=0` follows from (1.1).

Then

\[
\tau=\sum_i\operatorname{tr}(A_i^2),
\qquad
J=\sum_{i,j}\bigl(\operatorname{tr}(A_iA_j)\bigr)^2,
\tag{6.5}
\]

and symmetry of `T` gives

\[
\sum_i A_i^2=B.
\tag{6.6}
\]

To verify (6.6), compare components:

\[
\left(\sum_iA_i^2\right)_{jk}
=T_{ijl}T_{ilk}
=T_{jil}T_{kil}
=B_{jk}.
\]

For every traceless `3 x 3` matrix `X`, Cayley-Hamilton reads

\[
X^3-\frac12\operatorname{tr}(X^2)X
-\frac13\operatorname{tr}(X^3)I=0.
\]

Multiplying by `X` and taking the trace gives

\[
\operatorname{tr}(X^4)=\frac12\bigl(\operatorname{tr}(X^2)\bigr)^2.
\tag{6.7}
\]

Apply (6.7) to `X=A+tD` and compare the coefficient of `t^2`.  Cyclicity of
trace gives

\[
4\operatorname{tr}(A^2D^2)
+2\operatorname{tr}(ADAD)
=
\operatorname{tr}(A^2)\operatorname{tr}(D^2)
+2\bigl(\operatorname{tr}(AD)\bigr)^2.
\tag{6.8}
\]

Set `A=A_i`, `D=A_j`, and sum over `i,j`.  The left-hand tetrahedral term is

\[
\sum_{i,j}\operatorname{tr}(A_iA_jA_iA_j)=K,
\tag{6.9}
\]

where equality follows by writing out the indices and using the full symmetry
of `T`.  Also, by (6.6),

\[
\sum_{i,j}\operatorname{tr}(A_i^2A_j^2)
=
\operatorname{tr}\left(\left(\sum_iA_i^2\right)^2\right)
=\operatorname{tr}(B^2)=J.
\tag{6.10}
\]

Summing (6.8) therefore gives

\[
4J+2K=\tau^2+2J,
\]

which rearranges to (6.3).  \(\square\)

## 7. Pairing count for the six quartic moments

Write

\[
a:=Y^2,
\qquad
b:=|v|^2,
\qquad
c:=|M|^2.
\tag{7.1}
\]

We need the six integrals of `a^2,ab,ac,b^2,bc,c^2`.

Represent the four copies of `T` by four labeled vertices.  Each tensor has
three index slots, so every complete contraction is a 3-regular multigraph on
those four vertices.  An index contraction within one tensor is a loop and
vanishes because `T` is trace-free.  Every surviving loopless graph is one of:

- `D`: two disjoint pairs joined by three parallel edges, contributing `tau^2`;
- `J`: two opposite doubled edges and two connecting single edges,
  contributing `J`;
- `K`: the simple complete graph on four vertices, contributing `K`.

There are no other possibilities.  A triple edge forces the disconnected type.
If a connected graph has no multiple edge, it is `K_4`.  If it has a double
edge, degree three forces a second opposite double edge and two single
connecting edges.

Some contractions are already present before applying the spherical moment
formula.  In the table, `12` denotes one fixed contraction between tensor
vertices 1 and 2, and `12^2` denotes two such fixed contractions.  The remaining
`u`-indices are paired by (5.1).

| integrand | number `2m` of `u`-indices | fixed edges | `n_D` | `n_J` | `n_K` | after using `K=tau^2/2-J`: `(n_tau,n_J')` |
|---|---:|---|---:|---:|---:|---:|
| `Y^4` | 12 | none | 108 | 1944 | 1296 | `(756,648)` |
| `Y^2 |v|^2` | 10 | `34` | 12 | 216 | 144 | `(84,72)` |
| `Y^2 |M|^2` | 8 | `34^2` | 6 | 36 | 0 | `(6,36)` |
| `|v|^4` | 8 | `12,34` | 4 | 40 | 16 | `(12,24)` |
| `|v|^2 |M|^2` | 6 | `12,34^2` | 2 | 8 | 0 | `(2,8)` |
| `|M|^4` | 4 | `12^2,34^2` | 1 | 2 | 0 | `(1,2)` |

Here

\[
n_{\tau}=n_D+\frac12n_K,
\qquad
n_J'=n_J-n_K.
\tag{7.2}
\]

For completeness, the counts can be obtained directly as follows.

1. **`Y^4`.**  The disconnected type has
   `3(3!)^2=108` pairings.  The tetrahedral type has `(3!)^4=1296`.
   There are six labeled `J` graphs; each has
   `3^4(2!)^2=324` slot assignments, giving `1944`.
2. **`Y^2|v|^2`.**  The fixed edge is `34`.  Type `D` gives
   `3!2!=12`, and type `K` gives `3!3!2!2!=144`.  For type `J`, two
   graphs use `34` as a doubled edge and contribute `72` each; two use it
   as a single edge and contribute `36` each.  Total: `216`.
3. **`Y^2|M|^2`.**  The two fixed `34` edges force either type `D`, with
   `3!=6`, or one of two `J` graphs, each contributing `3*3*2=18`.
4. **`|v|^4`.**  Fixed edges are `12` and `34`.  Type `D` contributes
   `(2!)^2=4`; type `K` contributes `(2!)^4=16`.  Two `J` graphs use the
   fixed matching as doubled edges and contribute `16` each; two use it as
   single edges and contribute `4` each.  Total: `40`.
5. **`|v|^2|M|^2`.**  Fixed edges are `12` and `34^2`.  Type `D`
   contributes `2!=2`; the two possible `J` graphs contribute `4` each.
6. **`|M|^4`.**  Fixed edges are `12^2` and `34^2`.  The three pairings of
   the four remaining slots give one `D` contraction and two `J`
   contractions.

The script `python/verify_pairing_counts.py` enumerates all pairings and checks
this table exactly; `R/verify_pairing_counts.R` is the matching base-R check.

Multiplying the reduced counts by the factor `4*pi/(2m+1)!!` from (5.1) gives

\[
\begin{array}{rcl}
\displaystyle \int Y^4\,d\sigma
&=&\displaystyle \pi\left(\frac{16}{715}\tau^2+\frac{96}{5005}J\right),\\[2mm]
\displaystyle \int Y^2|v|^2\,d\sigma
&=&\displaystyle \pi\left(\frac{16}{495}\tau^2+\frac{32}{1155}J\right),\\[2mm]
\displaystyle \int Y^2|M|^2\,d\sigma
&=&\displaystyle \pi\left(\frac{8}{315}\tau^2+\frac{16}{105}J\right),\\[2mm]
\displaystyle \int |v|^4\,d\sigma
&=&\displaystyle \pi\left(\frac{16}{315}\tau^2+\frac{32}{315}J\right),\\[2mm]
\displaystyle \int |v|^2|M|^2\,d\sigma
&=&\displaystyle \pi\left(\frac{8}{105}\tau^2+\frac{32}{105}J\right),\\[2mm]
\displaystyle \int |M|^4\,d\sigma
&=&\displaystyle \pi\left(\frac{4}{15}\tau^2+\frac{8}{15}J\right).
\end{array}
\tag{7.3}
\]

## 8. Assembly of the quartic identity

From (4.7),

\[
q=64a+144b-72c.
\]

Therefore

\[
q^2
=4096a^2+18432ab-9216ac
 +20736b^2-20736bc+5184c^2.
\tag{8.1}
\]

Substitute the six formulas in (7.3).  Dividing first by `pi`, the coefficient
of `tau^2` is

\[
\begin{aligned}
&4096\frac{16}{715}
+18432\frac{16}{495}
-9216\frac{8}{315}\\
&\qquad
+20736\frac{16}{315}
-20736\frac{8}{105}
+5184\frac{4}{15}
=\frac{1310464}{1001},
\end{aligned}
\tag{8.2}
\]

while the coefficient of `J` is

\[
\begin{aligned}
&4096\frac{96}{5005}
+18432\frac{32}{1155}
-9216\frac{16}{105}\\
&\qquad
+20736\frac{32}{315}
-20736\frac{32}{105}
+5184\frac{8}{15}
=-\frac{2265600}{1001}.
\end{aligned}
\tag{8.3}
\]

Hence

\[
\int_{S^2}q^2\,d\sigma
=
\frac{\pi}{1001}
\left(1310464\tau^2-2265600J\right).
\tag{8.4}
\]

Since

\[
J=|B|^2=|B_0|^2+\frac13\tau^2,
\tag{8.5}
\]

we obtain

\[
\begin{aligned}
\int_{S^2}q^2\,d\sigma
&=
\frac{\pi}{1001}
\left(
\left(1310464-\frac{2265600}{3}\right)\tau^2
-2265600|B_0|^2
\right)\\
&=
\frac{\pi}{1001}
\left(555264\tau^2-2265600|B_0|^2\right).
\end{aligned}
\tag{8.6}
\]

This proves (1.6).

## 9. The determinant estimate and equality case

Because `|B_0|^2>=0`, (8.6) gives

\[
\|q\|_2^2\le \frac{555264\pi}{1001}\tau^2.
\tag{9.1}
\]

From (1.5),

\[
\|C\|_2^4
=\left(\frac{176\pi}{7}\right)^2\tau^2.
\tag{9.2}
\]

Eliminating `tau^2` between (9.1) and (9.2),

\[
\begin{aligned}
\|4\det C\|_2^2
&\le
\frac{555264\pi/1001}{(176\pi/7)^2}\,\|C\|_2^4\\
&=
\frac{15183}{17303\pi}\,\|C\|_2^4.
\end{aligned}
\tag{9.3}
\]

Thus (1.7) is proved.

Equality in (9.3) holds exactly when `B_0=0`.  This condition is nonempty.  For
example, take `Y(x,y,z)=xyz`.  In the normalization (1.2), the six components
`T_{123}` and their permutations equal `1/6`; all other components vanish.  Then

\[
\tau=\frac16,
\qquad
B=\frac1{18}I=\frac{\tau}{3}I,
\]

so `B_0=0`.

## 10. Verification map

The hand derivation corresponds to the code as follows.

| mathematical step | implementation |
|---|---|
| general symmetric trace-free tensor and harmonicity | `python/verify_degree3_identity.py` |
| projected formula `C=6PMP-2YP` | both exact identity scripts |
| compact formula (4.7) | `python/verify_degree3_identity_alt.py` and numerical tests |
| exact sphere moments and identities (1.5)-(1.6) | `python/verify_degree3_identity.py` |
| pairing counts in Section 7 | `python/verify_pairing_counts.py`; matching R script |
| determinant ratio and final simplification | `python/verify_bound_arithmetic.py` |

The exact scripts and this derivation use the same conventions:

- `Y=T[u,u,u]`, with no hidden factorial;
- `C` is represented by a `3 x 3` extension that vanishes on `u`;
- `q=4 det_{u^perp} C`;
- `|C|^2=tr(C^2)`;
- `sigma(S^2)=4*pi`.

## 11. Remaining review status

This file closes the principal internal write-up gap identified as `T1-T4` in
`proof/PROOF_LEDGER.md`. It has been checked against two exact symbolic
implementations and independent Python/R numerical tests, incorporated into
`paper/degree3_spectral_refinement.tex`, and reviewed in
`proof/PROOF_AUDIT.md`. It has not received outside expert review. It should
therefore be described as a **formal derivation in an AI-assisted research
draft**, not as a peer-reviewed or independently certified theorem.
