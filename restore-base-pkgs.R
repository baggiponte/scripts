#! /usr/bin/env Rscript

pkgs_to_remove <- installed.packages() |>
  as.data.frame() |>
  # select all packages that are not the default ones and select only the package names
  subset(!(Priority %in% c("base", "recommended")))

# get path where the packages are installed
lib_path <- unique(pkgs_to_remove$LibPath)

# get unique package names
pkgs_names <- pkgs_to_remove[, "Package"]

# remove packages
sapply(pkgs_names, remove.packages, lib = lib_path)
