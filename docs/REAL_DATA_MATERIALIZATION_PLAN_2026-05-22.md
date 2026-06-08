# REAL DATA MATERIALIZATION PLAN — RLL

Date: 2026-05-22
Status: operational plan
Scope: real-data ingestion, provenance, hashing, and model-comparison readiness

## 1. Objective

Organize the real-data layer needed to move RLL from synthetic/partial-real status toward reproducible real-data comparison.

The immediate priority is Pantheon+ / SH0ES because it is the minimal cosmological dataset required by the current RLL-vs-LCDM comparison path.

## 2. Data layers

### 2.1 Primary minimal cosmology validation

Dataset:

```text
pantheon_plus_shoes
```

Required local files:

```text
data/pantheon/lcparam_full_long_zhel.txt
data/pantheon/Pantheon+SH0ES_STAT+SYS.cov
```

Purpose:

```text
RLL vs LCDM expansion-history comparison using chi2/AIC/BIC under a declared covariance-aware Pantheon+ likelihood.
```

### 2.2 Secondary cosmological cross-validation

Dataset:

```text
desi_dr2_bao
```

Purpose:

```text
Independent BAO cross-check for expansion-history behavior and dynamic dark-energy compatibility.
```

Rule:

```text
Do not mix DESI into a Pantheon-only result unless the final artifact explicitly declares the combined likelihood.
```

### 2.3 Baseline priors / external comparison

Dataset:

```text
planck_2018_pr4
```

Purpose:

```text
CMB parameter comparison or prior usage only when explicitly declared.
```

Rule:

```text
No silent Planck prior injection into Pantheon-only model comparisons.
```

### 2.4 Auxiliary non-cosmology validation

Dataset:

```text
omni_space_weather
```

Purpose:

```text
Heliospheric-radiative and plasma/magnetic RLL blocks, not direct LCDM model preference.
```

## 3. Materialization command

Dry run:

```bash
python scripts/materialize_real_data.py --dataset pantheon_plus_shoes --dry-run
```

Real materialization:

```bash
python scripts/materialize_real_data.py --dataset pantheon_plus_shoes
```

Output manifest:

```text
data/real_sources/real_data_manifest.json
```

## 4. Verification and real run

After materialization:

```bash
python scripts/verify_pantheon_inputs.py --json
python -m rll.cli preflight-real --json
python -m rll.cli run --data real --model both --with-covariance
python scripts/run_real_pantheon_validation.py
```

Required final artifact:

```text
data/results/model_comparison.json
```

## 5. Required model-comparison metrics

The final artifact must include:

- `n_obs`
- `k_rll = 5`
- `k_lcdm = 2`
- `chi2_rll`
- `chi2_lcdm`
- `AIC_rll`
- `AIC_lcdm`
- `BIC_rll`
- `BIC_lcdm`
- `delta_chi2_rll_minus_lcdm`
- `delta_aic_rll_minus_lcdm`
- `delta_bic_rll_minus_lcdm`
- `interpretation_label`
- `claim_boundary`
- `command_used`
- `git_commit_hash`
- `environment`
- `real_data_files_sha256`

## 6. Interpretation boundary

Allowed labels:

```text
inconclusive
lcdm_preferred
rll_preferred_tentative
rll_preferred_strong
```

These labels are local model-comparison outcomes, not universal cosmological conclusions.

## 7. Publication-safe language

Before complete real-data run:

```text
RLL is a candidate effective dynamic-transition cosmology under real-data evaluation.
```

After complete real-data run:

```text
Under the declared dataset, covariance, command, environment, and assumptions, the RLL-vs-LCDM comparison produced the reported chi2/AIC/BIC deltas. Broader cosmological interpretation requires independent replication and cross-dataset validation.
```

## 8. Bare-metal / freestanding boundary

The freestanding/bare-metal layer is valuable for deterministic runtime, hashing, checksums, and low-level reproducibility helpers.

It must not replace the scientific likelihood layer. The correct boundary is:

```text
freestanding runtime = deterministic support layer
Pantheon+/DESI/Planck likelihoods = scientific inference layer
model_comparison.json = claim boundary layer
```

## 9. Next action

Run the materializer, inspect `real_data_manifest.json`, run the Pantheon+ preflight, and generate the normalized model-comparison artifact.
