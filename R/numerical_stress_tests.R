#!/usr/bin/env Rscript
# Independent base-R numerical checks of the degree-3 tensor conventions.
# This is a numerical cross-check; the Python/SymPy scripts perform the exact proof.

build_tensor <- function(values) {
  stopifnot(length(values) == 7)
  a <- values[1]; b <- values[2]; c <- values[3]; d <- values[4]
  e <- values[5]; f <- values[6]; g <- values[7]
  T <- array(0, dim = c(3, 3, 3))

  set_sym <- function(indices, value) {
    perms <- unique(rbind(
      indices,
      indices[c(1, 3, 2)],
      indices[c(2, 1, 3)],
      indices[c(2, 3, 1)],
      indices[c(3, 1, 2)],
      indices[c(3, 2, 1)]
    ))
    for (row in seq_len(nrow(perms))) {
      T[perms[row, 1], perms[row, 2], perms[row, 3]] <<- value
    }
  }

  set_sym(c(1, 1, 1), a)
  set_sym(c(1, 1, 2), b)
  set_sym(c(1, 1, 3), c)
  set_sym(c(1, 2, 2), d)
  set_sym(c(1, 2, 3), e)
  set_sym(c(2, 2, 2), f)
  set_sym(c(2, 2, 3), g)
  set_sym(c(1, 3, 3), -a - d)
  set_sym(c(2, 3, 3), -b - f)
  set_sym(c(3, 3, 3), -c - g)
  T
}

contract_Tuuu <- function(T, u) {
  total <- 0
  for (i in 1:3) for (j in 1:3) for (k in 1:3) {
    total <- total + T[i, j, k] * u[i] * u[j] * u[k]
  }
  total
}

matrix_Tu <- function(T, u) {
  M <- matrix(0, 3, 3)
  for (j in 1:3) for (k in 1:3) for (i in 1:3) {
    M[j, k] <- M[j, k] + T[i, j, k] * u[i]
  }
  M
}

vector_Tuu <- function(T, u) {
  v <- numeric(3)
  for (k in 1:3) for (i in 1:3) for (j in 1:3) {
    v[k] <- v[k] + T[i, j, k] * u[i] * u[j]
  }
  v
}

evaluate_quantities <- function(T, u) {
  Y <- contract_Tuuu(T, u)
  M <- matrix_Tu(T, u)
  v <- vector_Tuu(T, u)
  P <- diag(3) - tcrossprod(u)
  C <- P %*% (6 * M) %*% P - 2 * Y * P
  norm_sq <- sum(diag(C %*% C))
  q_direct <- 2 * (sum(diag(C))^2 - norm_sq)
  q_compact <- 64 * Y^2 + 144 * sum(v^2) - 72 * sum(diag(M %*% M))
  c(norm_sq = norm_sq, q_direct = q_direct, q_compact = q_compact)
}

gauss_legendre <- function(n) {
  i <- seq_len(n - 1)
  beta <- i / sqrt(4 * i^2 - 1)
  J <- matrix(0, n, n)
  J[cbind(i, i + 1)] <- beta
  J[cbind(i + 1, i)] <- beta
  eig <- eigen(J, symmetric = TRUE)
  ord <- order(eig$values)
  list(nodes = eig$values[ord], weights = 2 * eig$vectors[1, ord]^2)
}

sphere_grid <- function(n_z = 24, n_phi = 64) {
  gl <- gauss_legendre(n_z)
  phi <- 2 * pi * (0:(n_phi - 1)) / n_phi
  points <- matrix(0, n_z * n_phi, 3)
  weights <- numeric(n_z * n_phi)
  row <- 1
  for (iz in seq_len(n_z)) {
    z <- gl$nodes[iz]
    r <- sqrt(max(0, 1 - z^2))
    for (angle in phi) {
      points[row, ] <- c(r * cos(angle), r * sin(angle), z)
      weights[row] <- gl$weights[iz] * 2 * pi / n_phi
      row <- row + 1
    }
  }
  list(points = points, weights = weights)
}

tensor_invariants <- function(T) {
  tau <- sum(T^2)
  B <- matrix(0, 3, 3)
  for (i in 1:3) for (j in 1:3) for (k in 1:3) for (ell in 1:3) {
    B[i, j] <- B[i, j] + T[i, k, ell] * T[j, k, ell]
  }
  B0 <- B - diag(3) * tau / 3
  c(tau = tau, b0_sq = sum(diag(B0 %*% B0)))
}

set.seed(20260902)
grid <- sphere_grid()
max_pointwise <- 0
max_norm_rel <- 0
max_q_rel <- 0

for (trial in 1:12) {
  T <- build_tensor(rnorm(7))
  inv <- tensor_invariants(T)
  predicted_norm <- pi * (176 / 7) * inv["tau"]
  predicted_q_sq <- pi / 1001 * (555264 * inv["tau"]^2 - 2265600 * inv["b0_sq"])

  norm_integral <- 0
  q_integral <- 0
  for (row in seq_len(nrow(grid$points))) {
    values <- evaluate_quantities(T, grid$points[row, ])
    max_pointwise <- max(max_pointwise, abs(values["q_direct"] - values["q_compact"]))
    norm_integral <- norm_integral + grid$weights[row] * values["norm_sq"]
    q_integral <- q_integral + grid$weights[row] * values["q_direct"]^2
  }
  max_norm_rel <- max(max_norm_rel, abs(norm_integral - predicted_norm) / max(1, abs(predicted_norm)))
  max_q_rel <- max(max_q_rel, abs(q_integral - predicted_q_sq) / max(1, abs(predicted_q_sq)))
}

stopifnot(max_pointwise < 5e-9)
stopifnot(max_norm_rel < 5e-11)
stopifnot(max_q_rel < 5e-10)

ratio <- 15183 / 17303
candidate <- pi / 1914 * (259 - 27 * sqrt(ratio))
nishioka <- 4 * pi / 33
meissner <- pi * (2 / 3 - sqrt(3) / 4 * acos(1 / 3))
stopifnot(nishioka < candidate, candidate < meissner)

cat("R NUMERICAL STRESS TESTS: PASS\n")
cat(sprintf("maximum pointwise determinant error = %.3e\n", max_pointwise))
cat(sprintf("maximum norm relative error          = %.3e\n", max_norm_rel))
cat(sprintf("maximum q^2 relative error           = %.3e\n", max_q_rel))
cat(sprintf("candidate coefficient                = %.15f\n", candidate))
