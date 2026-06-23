# PR385 safe extraction status

Status date: 2026-06-23

PR #385 is useful but not mergeable as-is. Extraction must be additive only: no workflow overwrite, no directory moves, no deletions.

## Extracted now

- `data/real/cosmology/desi_bao_dr2_cobaya/README.md`
- `data/real/cosmology/desi_bao_dr2_cobaya/desi_gaussian_bao_ALL_GCcomb_mean.tsv`
- `data/real/cosmology/desi_bao_dr2_cobaya/desi_gaussian_bao_ALL_GCcomb_cov.tsv`

## Claim boundary

DESI DR2 core data are present, but RLL claims stay limited until a covariance-aware loader runs on current `main` and writes model-comparison results.

## Still remaining from PR385

- full manifest and hashes
- subset mean/cov files
- download helper
- materialization test adapted to current main
- workflow changes only after isolated review
