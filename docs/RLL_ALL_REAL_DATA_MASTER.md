# RLL all real data master ledger

Status date: 2026-06-23

## Why this exists

This file stops the fragmentation of real-data requests. The single master registry is:

```text
data/real/cosmology/RLL_ALL_REAL_DATA_MASTER.csv
```

Everything real-data related must map to that file.

## Non-negotiable rule

No RLL scientific claim may bypass this registry.

```text
if dataset_or_backend_not_in_master:
    claim_status = TOKEN_VAZIO
```

## What the master now includes

### Already existing or partially existing repository assets

- `data/real/cosmology/fsigma8_growth.csv`
- `data/inputs/cosmology_joint/joint_real_inputs_manifest.json`
- `results/audit/real_data_materialization_audit.json`
- `results/audit/real_source_signature_verification.md`
- open PR `#385`: real-validation bundle and DESI DR2 Cobaya materialization

### Required serious real datasets

- cosmic chronometers `H(z)`
- DESI DR1 BAO
- DESI DR2 BAO
- SDSS BOSS/eBOSS DR16 BAO/RSD
- Pantheon+ supernovae
- Planck 2018 CMB likelihood or distance priors
- ACT DR6 CMB lensing
- Planck PR4 CMB lensing
- f sigma 8 full covariance

### Required computational backends

- native CLASS RLL backend
- native CAMB RLL backend
- Halofit/HMcode nonlinear matter validation
- Cobaya/MontePython/emcee/dynesty chains

### Required provenance

- source URL or bibliographic ID
- license/access condition
- source date
- SHA256 for every materialized file
- loader script path
- test path
- claim gate

## P0 items

The master marks these as P0:

1. PR #385 must be resolved or extracted.
2. f sigma 8 must be upgraded from diagonal-only to full covariance.
3. joint real inputs manifest must be audited against this master.
4. DESI DR1/DR2 BAO must have covariance-aware loaders.
5. SDSS/eBOSS DR16 must be loaded as the legacy BAO/RSD baseline.
6. Pantheon+ must be added with full covariance.
7. Planck 2018 must be added as CMB baseline.
8. Cobaya/MontePython chains must be defined.
9. hashes/licenses/source dates must be added.
10. public claim language must be checked against gate status.

## Invariant content

The formal invariant remains:

```text
I_RLL = (M, B, P, D, C, L, S, T, G, V)
```

Where:

- `M` = model equations
- `B` = backend
- `P` = perturbations and transfer functions
- `D` = real data
- `C` = covariance
- `L` = likelihood/evidence
- `S` = systematics
- `T` = tests
- `G` = gates/TOKEN_VAZIO
- `V` = versioning/provenance

## What is not allowed anymore

- A dataset mentioned in chat but absent from the master.
- A claim based on a dataset without covariance status.
- A market or academic claim without gate status.
- A backend claim when CLASS/CAMB native integration is still absent.
- A public statement saying RLL is confirmed while CMB and nonlinear P(k) remain TOKEN_VAZIO.

## Next command path

The next engineering work must follow this order:

1. Merge or extract PR #385.
2. Materialize DESI DR2 BAO + Cobaya files.
3. Add Pantheon+ covariance loader.
4. Add Planck 2018 distance-prior or likelihood loader.
5. Upgrade f sigma 8 covariance.
6. Run joint likelihood/MCMC.
7. Generate claim report from master gate statuses.
