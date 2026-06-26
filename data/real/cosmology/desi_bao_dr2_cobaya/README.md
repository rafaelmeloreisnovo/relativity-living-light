# DESI DR2 BAO public likelihood files

This directory materializes the small public DESI DR2 BAO mean/covariance files used by the Cobaya BAO likelihood, plus source/provenance metadata.

## Why this exists

PR #385 contains a wider workflow/data refactor that is not mergeable as-is. To avoid regression, this directory extracts only the safe real-data core needed for validation.

## Sources

- DESI DR2 Results II paper: `https://arxiv.org/abs/2503.14738`
- DESI DR2 papers page: `https://data.desi.lbl.gov/doc/papers/dr2/`
- Public BAO likelihood files: `https://github.com/CobayaSampler/bao_data/tree/master/desi_bao_dr2`
- Official supplementary record: `https://zenodo.org/records/16644577`

## Core files

- `desi_gaussian_bao_ALL_GCcomb_mean.txt`
- `desi_gaussian_bao_ALL_GCcomb_cov.txt`

Those two files provide the 13 DESI DR2 BAO observables and their covariance matrix. The validation layer may map `*_over_rs` labels to RLL `*_over_rd` convention while preserving numerical values and covariance.

## Claim boundary

These are real public likelihood data files, but RLL claims remain limited until a covariance-aware likelihood and model comparison are run on current `main`.
