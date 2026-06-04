# Cosmology joint real-input feeding directory

This directory is the lightweight routing layer for the four-axis real-data likelihood requested for RLL validation:

1. `H(z)` expansion data from `data/real/Hz_data_real.csv`.
2. DESI DR2 BAO primary points from `data/real/cosmology/desi_dr2_bao_primary_points.csv`.
3. DESI DR2 BAO covariance summary from `data/real/cosmology/desi_dr2_bao_covariance_summary.csv`.
4. Growth `fσ8` points from `data/real/cosmology/fsigma8_growth_real.csv` (real RSD/growth compilation).
5. Planck 2018 CMB shift summary from `data/real/CMB_shift_real.json`.

The manifest here does **not** duplicate the data. It pins the intended feeding paths so the executable joint likelihood can remain local-first, reproducible, and rollback-safe.

## Executable consumer

Run from the repository root:

```bash
python -m data.pipelines.structure_d.joint_real_likelihood
```

Expected outputs:

- `results/structure_d/joint_real_likelihood.csv`
- `results/structure_d/joint_real_likelihood.json`
- `results/structure_d/joint_real_likelihood_covariance_manifest.json`

## Failsafe and rollback policy

The consumer writes through a temporary file and replaces outputs atomically. If an output already exists, a sibling `*.bak` file is written before replacement. If a downstream check fails, restore the matching `*.bak` file over the generated artifact.

## Boundary

This directory only routes real, locally committed inputs. It does not claim that RLL is superior to ΛCDM; the output AIC/BIC table is the decision artifact.

## Live source-signature verification

Run:

```bash
python tools/verify_real_source_signatures.py
```

The verifier records bounded HTTP source signatures, required-term matches, local SHA256 hashes, and explicit failover status in:

- `data/real/cosmology/real_source_signatures.json`
- `results/audit/real_source_signature_verification.json`
- `results/audit/real_source_signature_verification.md`

A blocked source is not silently replaced; the committed local file remains the fallback until manual review.
