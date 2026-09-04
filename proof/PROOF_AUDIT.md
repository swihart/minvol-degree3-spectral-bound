# Internal proof audit for the degree-3 spectral refinement

**Audit date:** 2026-09-02  
**Scope:** `proof/BRIDGE_LEMMAS.md`, `proof/DEGREE3_TENSOR_IDENTITY.md`,
the exact Python checks, the independent R checks, and the first integrated
LaTeX manuscript.

## Audit conclusion

No internal algebraic or logical contradiction was found in the proposed proof
chain. The bridge lemmas, cubic tensor identity, and final coefficient agree
with the exact symbolic calculations and the numerical cross-checks.

This conclusion is deliberately limited:

- it is an internal project audit, not independent expert review;
- it does not establish novelty against all existing literature;
- it does not verify the stronger HYRA manuscript;
- it does not justify describing the result as peer reviewed or certified.

The appropriate public status remains:

> AI-assisted, non-peer-reviewed research draft seeking independent mathematical verification.

## 1. Source audit

The inherited statements used in the proof were checked against the published
version of Nishioka's paper.

| ID | Inherited statement | Source location | Audit result |
|---|---|---|---|
| SRC-1 | For the centered support function, `h(-u)=-h(u)` and `A_h = nabla^2 h + h I` satisfies `-dI/2 <= A_h <= dI/2` | Nishioka, Section 2.1, equation (3) | Matches project notation after identifying tangent spaces with `u^perp` |
| SRC-2 | `Vol(K) = pi d^3/6 - d E(h)/2` | Nishioka, Lemma 1, equation (4) | Matches exactly |
| SRC-3 | Degree-one harmonics represent translations and may be removed | Nishioka, Section 2.3 | Used correctly; `A_h` and `E(h)` are unchanged by the removed translation mode |
| SRC-4 | `E(Y_l)` and `||A_{Y_l}||_2^2` have the spectral factors used here | Nishioka, Lemma 4 | Matches exactly |
| SRC-5 | Distinct harmonic degrees contribute orthogonally | Nishioka, proof of Proposition 1; polarized explicitly in this project | Matches; the project supplies the tensor-bilinear version needed for the projection identity |
| SRC-6 | Bodies of constant width admit same-width smooth approximation and volume is Hausdorff-continuous | Nishioka, Lemma 2; Martini--Montejano--Oliveros, Theorem 8.5.1 for analytic-boundary approximation | Sufficient for passage from the smooth proof to arbitrary bodies |

## 2. Bridge-lemma audit

### BR-1: normalization and translation

The paper now distinguishes two operations that were easy to conflate:

1. subtracting `d/2` from the support function, which produces the odd centered
   function `h`; and
2. translating the body to eliminate the degree-one component.

Both operations preserve the width and volume. The degree-one component also
lies in the kernel of `f -> A_f`, so the curvature estimates are unaffected.

**Status:** checked.

### BR-2: tensor-valued harmonic orthogonality

Polarizing the integrated Bochner identity gives

```text
integral <Hess f, Hess g>
  = integral (Delta f)(Delta g) - integral <grad f, grad g>.
```

Expanding `<A_f,A_g>` then reduces every term to a scalar multiple of
`integral f g` when `f` and `g` are spherical harmonics. Distinct degrees are
therefore orthogonal for the tensor quadratic form. Consequently,

```text
||A_h||_2^2 = sum_l ||A_{h_l}||_2^2,
||A_{h_3}||_2^2 = <A_h,A_{h_3}>_2.
```

The convergence step is justified because a smooth `h` has harmonic expansion
converging in `H^2(S^2)`, while `f -> Hess f + f I` is continuous from `H^2`
to tensor-valued `L^2`.

**Status:** checked.

### BR-3: refined spectral split

For odd degrees,

```text
E(h_l) = ||A_{h_l}||_2^2 / (2(l(l+1)-1)).
```

The degree-three coefficient is `1/22`; the largest coefficient among all
remaining odd degrees is the degree-five coefficient `1/58`. Therefore

```text
E(h) <= ||A_h||_2^2/58 + (9/319)||A_{h_3}||_2^2.
```

The arithmetic `1/22 - 1/58 = 9/319` was checked exactly.

**Status:** checked.

### BR-4: nuclear-norm identity and determinant scaling

For tangent eigenvalues `mu_1, mu_2`,

```text
||C||_*^2 = |C|_F^2 + 2|det C|.
```

With `q = 4 det C`, this becomes

```text
||C||_*^2 = |C|_F^2 + |q|/2.
```

The factor `1/2` is correct and is carried consistently through both
Cauchy--Schwarz applications.

**Status:** checked.

### BR-5: operator/nuclear duality and the cubic budget

The projection identity gives a positive scalar exactly:

```text
N_3 = integral tr(A_h C).
```

The pointwise box constraint implies `||A_h||_op <= d/2`, and the standard dual
norm inequality gives

```text
N_3 <= (d/2) integral ||C||_*.
```

Combining this with the determinant estimate yields

```text
N_3 <= pi d^2 (1 + sqrt(15183/17303)).
```

No sign assumption on `tr(A_h C)` is used pointwise; the proof inserts an
absolute value before applying the norm inequality.

**Status:** checked.

### BR-6: final assembly

The global pointwise box gives `||A_h||_2^2 <= 2 pi d^2`. Substitution into the
refined spectral split produces

```text
E(h) <= pi d^2(20 + 9s)/319,
s = sqrt(15183/17303).
```

The volume identity then gives

```text
Vol(K) >= pi(259 - 27s)d^3/1914.
```

The exact difference from Nishioka's coefficient is

```text
9 pi(1-s)/638 > 0.
```

**Status:** exact-code checked and hand-checked.

## 3. Degree-three tensor audit

### T-1: harmonic tensor representation

For `F(x)=T_{ijk}x_i x_j x_k`,

```text
Delta F = 6 T_{iik} x_k.
```

Thus the restriction is a degree-three spherical harmonic exactly when the
symmetric tensor is trace-free.

**Status:** checked symbolically and by hand.

### T-2: spherical Hessian and curvature tensor

For tangent vectors, the restriction formula

```text
Hess_S Y = D^2 F|_T - 3Y I
```

follows from the second fundamental form of the unit sphere and Euler's identity
`DF(u)[u]=3F(u)`. Since `D^2F=6M`,

```text
C = A_Y = 6PMP - 2YP.
```

The sign and the homogeneity factor `3` were checked against the trace identity
`tr C = Delta Y + 2Y = -10Y`.

**Status:** checked.

### T-3: compact determinant formula

Using a basis with first vector `u`, the proof obtains

```text
|PMP|^2 = |M|^2 - 2|Mu|^2 + Y^2,
|C|^2   = 36|M|^2 - 72|Mu|^2 + 68Y^2,
tr C    = -10Y.
```

For a tangent `2 x 2` endomorphism represented by a `3 x 3` extension with
zero normal eigenvalue,

```text
4 det C = 2((tr C)^2 - tr(C^2)).
```

This yields

```text
4 det C = 64Y^2 + 144|T(u,u,.)|^2 - 72|T(u,.,.)|^2.
```

The direct projected-matrix formula and this compact formula agree exactly on
`x^2+y^2+z^2=1`.

**Status:** exact-code checked by two formulations; hand derivation checked.

### T-4: quadratic moments

The sphere moment normalization

```text
integral u_{i1}...u_{i,2m}
  = 4 pi/(2m+1)!! times the sum over pairings
```

produces

```text
integral Y^2     = 8 pi tau/35,
integral |v|^2   = 8 pi tau/15,
integral |M|^2   = 4 pi tau/3.
```

These give `||C||_2^2 = 176 pi tau/7`.

**Status:** checked by exact polynomial integration and pairing counts.

### T-5: dimension-three quartic relation

Writing `(A_i)_{jk}=T_{ijk}`, the Cayley--Hamilton identity for traceless
`3 x 3` matrices gives, after polarization and summation,

```text
K_tet = tau^2/2 - tr(B^2).
```

The index identification

```text
sum_{i,j} tr(A_i A_j A_i A_j) = K_tet
```

was expanded explicitly in the LaTeX draft and checked by the general symbolic
tensor script.

**Status:** checked.

### T-6: quartic moment table

All perfect pairings for the six moments were exhaustively enumerated. The
counts reduce to the two invariants `tau^2` and `J=tr(B^2)` using the quartic
relation. Substitution into the square of the compact determinant formula gives

```text
integral (4 det C)^2
 = pi(1310464 tau^2 - 2265600 J)/1001
 = pi(555264 tau^2 - 2265600|B_0|^2)/1001.
```

The exact upper bound follows by dropping the nonpositive `B_0` term and using
`||C||_2^2 = 176 pi tau/7`.

**Status:** exact-code checked; human-readable derivation drafted.

### T-7: sharpness within the cubic harmonic space

For `Y=xyz`, the six symmetric components `T_{123}` equal `1/6`, giving

```text
tau = 1/6,
B = I/18 = (tau/3)I,
B_0 = 0.
```

Thus equality is attained in the determinant inequality, so its constant is
sharp on `H_3`.

**Status:** checked exactly.

## 4. Publication-draft audit

The first integrated manuscript is in:

```text
paper/degree3_spectral_refinement.tex
paper/degree3_spectral_refinement.pdf
```

The PDF was built with `latexmk`, rendered at 180 dpi, and visually inspected
page by page. The audit found no clipped text, overlapping equations, broken
glyphs, or unresolved references. The PDF contains eight US-letter pages and
embedded fonts.

The manuscript makes the following provenance distinctions explicit:

- Nishioka's support-function and spectral framework is sourced;
- the determinant inequality and cubic curvature budget are the proposed new
  contribution;
- HYRA is acknowledged as a public manuscript claiming stronger numerical
  bounds by a different method;
- exact symbolic checks are distinguished from independent expert review;
- AI assistance is disclosed by system and access period, and no AI system is listed as an author.

## 5. Literature-search status

A targeted exact-phrase and exact-constant web search on 2026-09-02 did not
locate an earlier public occurrence of either `15183/17303` or the decimal
coefficient `0.3836027047` in connection with the three-dimensional
Blaschke--Lebesgue problem. The search did locate Nishioka's 2026 arXiv record
and unrelated spherical Blaschke--Lebesgue work.

This was not a systematic literature review and must not be treated as a proof
of novelty. A specialist may know relevant representation-theoretic or invariant
inequalities under different notation.

## 6. Clean-clone verification and remaining release gates

A separate clone of commit
`96cea57275070f21babf30477ab1b128ec0f5eb6` successfully ran the exact Python
suite, the independent R suite, the paper build, the Markdown-PDF build, and the
metadata and checksum checks. The rebuilt tracked working tree remained
byte-clean. Full Poppler PDF preflight was unavailable on the local Mac and was
delegated to the green GitHub Actions document job. The detailed record is in
`CLEAN_CLONE_CHECK.md`.

The remaining gates before a public release are:

1. Have the named author finish reading and approve the complete manuscript.
2. Complete a release-candidate audit and rerun the clean-clone check after all
   release-specific metadata has been fixed.
3. Add the public repository URL, release version, and release date to
   `CITATION.cff` when preparing the first release.
4. Seek independent mathematical review after the first public research-draft
   release.

The exact Python and R checks, hosted three-job GitHub Actions workflow,
research-paper build, Markdown-PDF build, metadata declarations, PDF preflight,
and initial clean-clone reproduction have passed. They do not replace
independent subject-matter review.

## Release recommendation

Keep the repository private until the named author completes the manuscript
review and the release-candidate audit is complete. Then prepare a `v0.1.0`
public research-draft release, update the release-specific citation metadata,
run the final clean-clone gate, and preserve the verification language stated
above.
