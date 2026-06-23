# PR385 safe extraction status

Status date: 2026-06-23

PR #385 is useful but not mergeable as-is. Extraction must be additive only: no workflow overwrite, no directory moves, no deletions.

## Extracted now

- `data/real/cosmology/desi_bao_dr2_cobaya/README.md`
- `data/real/cosmology/desi_bao_dr2_cobaya/desi_gaussian_bao_ALL_GCcomb_mean.tsv`
- `data/real/cosmology/desi_bao_dr2_cobaya/desi_gaussian_bao_ALL_GCcomb_cov.tsv`
- `scripts/check_desi_dr2_bao_covariance.py`
- `tests/test_desi_dr2_bao_covariance_loader.py`

## Claim boundary

DESI DR2 core data and a covariance-aware smoke loader are present. RLL claims stay limited until the produced chi2 artifact is reviewed and integrated into the full joint model-selection pipeline.

## Run

```bash
python scripts/check_desi_dr2_bao_covariance.py
```

Expected output:

```text
results/desi_dr2_bao_covariance_chi2.json
```

## Still remaining from PR385

- full manifest and hashes
- subset mean/cov files
- download helper
- materialization test adapted to current main
- workflow changes only after isolated review
