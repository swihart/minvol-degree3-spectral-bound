# Cross-language numerical comparison

The Python stress test was executed in the assistant's container. The matching
base-R stress test was executed by Bruce Swihart in his local R environment.
The two programs are independent implementations and use language-specific
random-number generators, so they do not test the same random tensors even
though both runs are deterministic within their own language.

| Check | Python | R | Interpretation |
|---|---:|---:|---|
| Maximum pointwise determinant discrepancy | `1.819e-12` | `2.046e-12` | Direct projected-matrix determinant and compact tensor-contraction formula agree to floating-point precision. |
| Maximum relative error in `integral |A_Y|^2` | `2.829e-15` | `2.038e-15` | Numerical quadrature agrees with `(176*pi/7)*tau`. |
| Maximum relative error in `integral (4 det A_Y)^2` | `3.427e-15` | `5.107e-15` | Numerical quadrature agrees with the proposed quartic invariant identity. |
| Candidate volume coefficient | `0.383602704709067716` | `0.383602704709068` | Agreement to all 15 digits printed by R. |

All programmed acceptance thresholds passed in both languages.

This is strong cross-language numerical evidence for the tensor conventions and
constants. It is not a proof of the full lower bound. In particular, the exact
symbolic proof is currently implemented only in Python/SymPy, and the
harmonic-projection, nuclear-norm, and nonsmooth-approximation arguments still
require a publication-ready mathematical write-up and outside review.
