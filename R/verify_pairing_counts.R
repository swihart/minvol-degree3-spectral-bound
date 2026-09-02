#!/usr/bin/env Rscript
# Base-R combinatorial check of the pairing table in
# proof/DEGREE3_TENSOR_IDENTITY.md.

pairings <- function(items) {
  if (length(items) == 0) return(list(list()))
  first <- items[[1]]
  output <- list()
  cursor <- 1
  for (index in 2:length(items)) {
    second <- items[[index]]
    keep <- setdiff(seq_along(items), c(1, index))
    tails <- pairings(items[keep])
    for (tail in tails) {
      output[[cursor]] <- c(list(list(first, second)), tail)
      cursor <- cursor + 1
    }
  }
  output
}

edge_key <- function(a, b) paste(sort(c(a, b)), collapse = "-")

classify_graph <- function(edges) {
  keys <- vapply(edges, function(edge) edge_key(edge[1], edge[2]), character(1))
  if (any(vapply(edges, function(edge) edge[1] == edge[2], logical(1)))) return("loop")
  counts <- table(keys)

  adjacency <- lapply(0:3, function(x) integer())
  for (edge in edges) {
    a <- edge[1] + 1
    b <- edge[2] + 1
    adjacency[[a]] <- unique(c(adjacency[[a]], b))
    adjacency[[b]] <- unique(c(adjacency[[b]], a))
  }
  seen <- 1L
  frontier <- 1L
  while (length(frontier) > 0) {
    current <- frontier[1]
    frontier <- frontier[-1]
    new_nodes <- setdiff(adjacency[[current]], seen)
    seen <- unique(c(seen, new_nodes))
    frontier <- c(frontier, new_nodes)
  }
  if (length(seen) < 4) return("D")
  if (length(counts) == 6 && all(as.integer(counts) == 1)) return("K")
  "J"
}

count_case <- function(free_degrees, fixed_edges) {
  items <- list()
  cursor <- 1
  for (vertex in 0:3) {
    degree <- free_degrees[vertex + 1]
    if (degree > 0) {
      for (slot in 0:(degree - 1)) {
        items[[cursor]] <- c(vertex, slot)
        cursor <- cursor + 1
      }
    }
  }
  counts <- c(loop = 0L, D = 0L, J = 0L, K = 0L)
  for (matching in pairings(items)) {
    moment_edges <- lapply(matching, function(pair) c(pair[[1]][1], pair[[2]][1]))
    type <- classify_graph(c(fixed_edges, moment_edges))
    counts[type] <- counts[type] + 1L
  }
  counts
}

odd_double_factorial <- function(n) {
  stopifnot(n > 0, n %% 2 == 1)
  prod(seq(1, n, by = 2))
}

cases <- list(
  "Y^4" = list(c(3, 3, 3, 3), list()),
  "Y^2|v|^2" = list(c(3, 3, 2, 2), list(c(2, 3))),
  "Y^2|M|^2" = list(c(3, 3, 1, 1), list(c(2, 3), c(2, 3))),
  "|v|^4" = list(c(2, 2, 2, 2), list(c(0, 1), c(2, 3))),
  "|v|^2|M|^2" = list(c(2, 2, 1, 1), list(c(0, 1), c(2, 3), c(2, 3))),
  "|M|^4" = list(c(1, 1, 1, 1), list(c(0, 1), c(0, 1), c(2, 3), c(2, 3)))
)

expected <- list(
  "Y^4" = c(D = 108, J = 1944, K = 1296, tau = 756, Jred = 648),
  "Y^2|v|^2" = c(D = 12, J = 216, K = 144, tau = 84, Jred = 72),
  "Y^2|M|^2" = c(D = 6, J = 36, K = 0, tau = 6, Jred = 36),
  "|v|^4" = c(D = 4, J = 40, K = 16, tau = 12, Jred = 24),
  "|v|^2|M|^2" = c(D = 2, J = 8, K = 0, tau = 2, Jred = 8),
  "|M|^4" = c(D = 1, J = 2, K = 0, tau = 1, Jred = 2)
)

cat("R PAIRING-COUNT CHECK\n")
for (name in names(cases)) {
  values <- cases[[name]]
  counts <- count_case(values[[1]], values[[2]])
  stopifnot(sum(counts) == odd_double_factorial(sum(values[[1]]) - 1))
  n_tau <- counts["D"] + counts["K"] / 2
  j_reduced <- counts["J"] - counts["K"]
  actual <- c(D = counts["D"], J = counts["J"], K = counts["K"], tau = n_tau, Jred = j_reduced)
  stopifnot(all(actual == expected[[name]]))
  cat(sprintf("%-17s D=%4d J=%4d K=%4d => tau^2=%4d, J=%4d\n",
              name, as.integer(counts["D"]), as.integer(counts["J"]),
              as.integer(counts["K"]), as.integer(n_tau), as.integer(j_reduced)))
}
cat("R PAIRING-COUNT CHECK: PASS\n")
