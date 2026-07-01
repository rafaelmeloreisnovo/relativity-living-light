# Real Data Addition Ledger — 2026-07

Status: `governance_record / source_registration / claim_blocked`

## Purpose

This ledger records additional real-data source targets for the RLL cosmology pipeline without turning source registration into scientific validation.

The repository already contains real-data paths and source checks for H(z), DESI DR2 BAO, growth/fσ8, CMB shift, and a Pantheon+ downloader. This ledger adds a stricter July 2026 queue for source registration, provenance, and future materialization.

## Boundary

Source registration is not validation.

A source becomes usable for scientific model comparison only after:

1. primary source is identified;
2. exact local file is materialized;
3. checksum/hash is recorded;
4. schema and column semantics are validated;
5. covariance or uncertainty policy is declared;
6. baseline/adversary comparison is run;
7. output artifact and manifest are written;
8. claim boundary remains explicit.

Until then, the state remains `SOURCE_REGISTERED_ONLY`, `DOWNLOAD_READY`, or `REAL_VALIDATED_BLOCKED`.

## Registry added

New registry:

```text
 data/real/cosmology/real_data_addition_registry_2026_07.json
```

It records these source targets:

| dataset_id | domain | state | safe use now |
|---|---|---|---|
| `pantheon_plus_sh0es_official_release` | supernovae | `DOWNLOAD_READY` | download/materialize with checksum; no validation claim |
| `desi_dr2_bao_official_measurements` | BAO | `REAL_VALIDATED_BLOCKED` | compare source and local covariance semantics |
| `desi_dr2_lya_and_extended_bao_context` | BAO/Lyα context | `SOURCE_REGISTERED_ONLY` | literature context only |
| `union31_supernova_compilation_context` | supernovae context | `SOURCE_REGISTERED_ONLY` | future dataset branch only |
| `des_dovekie_recalibration_context` | supernova calibration context | `SOURCE_REGISTERED_ONLY` | systematic/calibration context only |
| `planck_2018_cmb_reference_or_likelihood` | CMB | `REAL_VALIDATED_BLOCKED` | clarify prior/likelihood/chain semantics |

## What this adds

This patch adds real-data source governance, not new scientific proof.

It is useful because it prevents these errors:

- treating a paper citation as a materialized dataset;
- treating a source page as a covariance matrix;
- merging Pantheon+, DES/Dovekie, Union3.1, DESI and Planck semantics without separate labels;
- using a compressed CMB-shift number as if it were a full Planck likelihood;
- claiming RLL validation before `Os0`, CPL comparison, covariance, posterior and multi-seed tests are settled.

## Claim boundary

Allowed:

> The repository has registered additional real-data sources and future materialization targets.

Blocked:

> RLL is validated by these sources.

> DESI confirms RLL.

> Pantheon+ confirms RLL.

> Planck/CMB validates RLL.

> Literature context is equivalent to a local dataset.

## Next materialization order

1. Pantheon+ official files via `scripts/download_real_cosmology_inputs.sh`.
2. DESI DR2 BAO table/covariance exact-file audit.
3. Multi-seed joint likelihood with identical optimizer policy for LCDM, wCDM, CPL and RLL.
4. Pantheon+/CosmoSIS likelihood-semantics cross-check.
5. Supernova branch comparison: Pantheon+ vs DES/Dovekie vs Union3.1, only after machine-readable data and covariance are located.
6. Planck/CMB branch clarification: compressed prior vs official likelihood vs chain.

## Scientific status

`CLAIM_BLOCKED`

The added registry improves reproducibility and future data acquisition. It does not change the current scientific conclusion: RLL remains a falsifiable candidate under test, not a validated replacement for ΛCDM or CPL.
