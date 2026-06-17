# Pantheon+ × DESI DR2 — Master Data Table for RLL Filtering

Status: `claim_allowed=false` until provenance, hashes, full covariance handling, and reproducible likelihood runs are complete.

Purpose: create a clean, auditable table of the decent observational inputs to use later for RLL / LCDM / wCDM / CPL calculations without mixing real data, inferred data, and symbolic/metaphoric interpretation.

---

## 1. Rule of use

1. Numbers without source, file, hash, covariance policy, and command are `TOKEN_VAZIO_NUMERIC_ORIGIN`.
2. Plot-only diagonal errors must not be used for cosmological fitting when full covariance exists.
3. DESI BAO rows are usable now as local materialized BAO points when matched to the committed covariance matrix.
4. Pantheon+ is ingestion-ready by protocol only after the two official files are present and hashed locally.
5. Any filtering choice must be logged before the run, not after seeing which model wins.

---

## 2. Current canonical files in this repository

| dataset | local path | current status | role | claim gate |
|---|---|---|---|---|
| DESI DR2 BAO primary points | `data/real/cosmology/desi_dr2_bao_primary_points.csv` | materialized | 13 BAO observables: BGS, LRG, ELG, QSO, LyA | usable if covariance dimensions/order match |
| DESI DR2 BAO covariance | `data/real/desi_dr2_bao_covariance.csv` | materialized | 13×13 covariance matrix aligned to primary BAO vector | required for fair chi2 |
| DESI DR2 covariance summary | `data/real/cosmology/desi_dr2_bao_covariance_summary.csv` | materialized | audit helper / block summary | supportive, not likelihood by itself |
| Pantheon+ required directory | `data/pantheon/` | protocol present | user-supplied official files only | must fail if files absent |
| Pantheon+ distance table | `data/pantheon/Pantheon+SH0ES.dat` or `data/pantheon/lcparam_full_long_zhel.txt` | TOKEN_VAZIO until downloaded/hashed | SN distance/modulus data | full provenance + SHA256 required |
| Pantheon+ full covariance | `data/pantheon/Pantheon+SH0ES_STAT+SYS.cov` | TOKEN_VAZIO until downloaded/hashed | full SN stat+systematic covariance | mandatory for fitting |

---

## 3. DESI DR2 BAO primary vector currently staged

Order matters: this order must match the covariance rows/columns.

| index | tracer | z_eff | observable | value | sigma | covariance block | paired observable | corr | filter tier | notes |
|---:|---|---:|---|---:|---:|---|---|---:|---|---|
| 0 | BGS | 0.295 | `DV_over_rd` | 7.942 | 0.075 | `DESI_DR2_BGS_DV` | — | — | keep/core | isotropic BAO point |
| 1 | LRG1 | 0.510 | `DM_over_rd` | 13.588 | 0.167 | `DESI_DR2_LRG1_DM_DH` | `DH_over_rd` | -0.459 | keep/core | transverse BAO |
| 2 | LRG1 | 0.510 | `DH_over_rd` | 21.863 | 0.425 | `DESI_DR2_LRG1_DM_DH` | `DM_over_rd` | -0.459 | keep/core | radial BAO |
| 3 | LRG2 | 0.706 | `DM_over_rd` | 17.351 | 0.177 | `DESI_DR2_LRG2_DM_DH` | `DH_over_rd` | -0.404 | keep/core | transverse BAO |
| 4 | LRG2 | 0.706 | `DH_over_rd` | 19.455 | 0.330 | `DESI_DR2_LRG2_DM_DH` | `DM_over_rd` | -0.404 | keep/core | radial BAO |
| 5 | LRG3_PLUS_ELG1 | 0.934 | `DM_over_rd` | 21.576 | 0.152 | `DESI_DR2_LRG3_ELG1_DM_DH` | `DH_over_rd` | -0.416 | keep/core | combined-bin transverse BAO |
| 6 | LRG3_PLUS_ELG1 | 0.934 | `DH_over_rd` | 17.641 | 0.193 | `DESI_DR2_LRG3_ELG1_DM_DH` | `DM_over_rd` | -0.416 | keep/core | combined-bin radial BAO |
| 7 | ELG2 | 1.321 | `DM_over_rd` | 27.601 | 0.318 | `DESI_DR2_ELG2_DM_DH` | `DH_over_rd` | -0.434 | keep/core | transverse BAO |
| 8 | ELG2 | 1.321 | `DH_over_rd` | 14.176 | 0.221 | `DESI_DR2_ELG2_DM_DH` | `DM_over_rd` | -0.434 | keep/core | radial BAO |
| 9 | QSO | 1.484 | `DM_over_rd` | 30.512 | 0.760 | `DESI_DR2_QSO_DM_DH` | `DH_over_rd` | -0.500 | keep/core | transverse BAO |
| 10 | QSO | 1.484 | `DH_over_rd` | 12.817 | 0.516 | `DESI_DR2_QSO_DM_DH` | `DM_over_rd` | -0.500 | keep/core | radial BAO |
| 11 | LyA | 2.330 | `DM_over_rd` | 38.988 | 0.531 | `DESI_DR2_LYA_DM_DH` | `DH_over_rd` | -0.431 | keep/high-z | Lyman-alpha transverse BAO |
| 12 | LyA | 2.330 | `DH_over_rd` | 8.632 | 0.101 | `DESI_DR2_LYA_DM_DH` | `DM_over_rd` | -0.431 | keep/high-z | Lyman-alpha radial BAO |

Recommended first filters:

| filter id | data kept | why | risk |
|---|---|---|---|
| `DESI_ALL_13` | all 13 BAO observables | full current BAO vector | depends on covariance alignment |
| `DESI_LOW_MID_11` | indices 0–10 | isolate galaxy/QSO BAO without LyA | removes high-z anchor |
| `DESI_ANISO_ONLY_12` | indices 1–12 | use only DM/DH anisotropic points | drops BGS DV point |
| `DESI_DVLESS_LOW_MID_10` | indices 1–10 | clean anisotropic low/mid-z vector | no BGS, no LyA |
| `DESI_LYA_ONLY_2` | indices 11–12 | test high-z LyA anchor | not enough alone for model ranking |

---

## 4. Pantheon+ files and column dictionary

Official source repository: `PantheonPlusSH0ES/DataRelease`.

Official distance/covariance directory: `Pantheon+_Data/4_DISTANCES_AND_COVAR`.

Required fitting files from that directory:

| official file | local target | meaning | fitting status |
|---|---|---|---|
| `Pantheon+SH0ES.dat` | `data/pantheon/Pantheon+SH0ES.dat` | nominal SN and Cepheid-host distances | use with full covariance only |
| `Pantheon+SH0ES_STAT+SYS.cov` | `data/pantheon/Pantheon+SH0ES_STAT+SYS.cov` | full statistical + systematic covariance, N=1701 | mandatory for cosmology fitting |
| `Pantheon+SH0ES_STATONLY.cov` | optional local audit copy | statistical covariance only | diagnostic only unless explicitly chosen |
| `sytematic_groupings/` | optional local audit copy | grouped systematic covariance components | ablation/systematics analysis |

Core columns to stage for filtering:

| column | meaning | initial filter use | notes |
|---|---|---|---|
| `CID` | candidate ID | dedupe / traceability | never drop provenance |
| `IDSURVEY` | source survey code | survey ablation | compare survey-dependent residuals |
| `zHD` | Hubble-diagram redshift | main cosmology redshift | CMB/VPEC corrected |
| `zHDERR` | zHD uncertainty | redshift error propagation | not replacement for full covariance |
| `zCMB` | CMB-corrected redshift | frame ablation | compare redshift frame sensitivity |
| `zHEL` | heliocentric redshift | low-z/local-flow checks | not default cosmology redshift |
| `m_b_corr` | standardized corrected magnitude | SN residual target | covariance required |
| `m_b_corr_err_DIAG` | diagonal plotting uncertainty | plotting only | do not fit cosmology with this alone |
| `MU_SH0ES` | SH0ES-calibrated distance modulus | H0/distance ladder diagnostic | covariance required |
| `MU_SH0ES_ERR_DIAG` | diagonal plotting uncertainty for MU | plotting only | do not fit cosmology with this alone |
| `CEPH_DIST` | Cepheid host distance | calibrator diagnostics | covariance includes host component |
| `IS_CALIBRATOR` | Cepheid-host flag | calibrator split | 1/0 binary |
| `USED_IN_SH0ES_HF` | Hubble-flow flag | HF-only filter | 1/0 binary |
| `c` | SALT2 color | quality/systematics filter | use with uncertainties/covariances |
| `cERR` | SALT2 color uncertainty | quality filter | |
| `x1` | SALT2 stretch | quality/systematics filter | |
| `x1ERR` | stretch uncertainty | quality filter | |
| `mB` | uncorrected SALT2 brightness | audit only | raw light-curve fit output |
| `mBERR` | mB uncertainty | audit only | |
| `RA` / `DEC` | sky position | anisotropy/dipole/systematics | preserve for directional tests |
| `HOST_RA` / `HOST_DEC` | host position | host matching | |
| `HOST_ANGSEP` | SN-host angular separation | host association quality | |
| `VPEC` / `VPECERR` | peculiar velocity and uncertainty | low-z flow filter | crucial for z < 0.1 |
| `MWEBV` | Milky Way reddening | dust/systematics filter | |
| `HOST_LOGMASS` | host stellar mass | mass-step systematics | |
| `PKMJD` | peak date | temporal audit | survey/epoch checks |
| `NDOF` | fit degrees of freedom | quality filter | |
| `FITCHI2` | SALT2 fit chi-squared | quality filter | |
| `FITPROB` | SNANA fit probability | quality filter | |
| `biasCor_m_b` | brightness bias correction | selection-effect audit | |
| `biasCorErr_m_b` | bias correction uncertainty | selection-effect audit | |

Recommended Pantheon+ first filters:

| filter id | predicate | reason | claim gate |
|---|---|---|---|
| `PPLUS_ALL_1701` | all rows with full covariance | reproduce official baseline | full covariance required |
| `PPLUS_HF_ONLY` | `USED_IN_SH0ES_HF == 1` | Hubble-flow diagnostic | cannot replace full SN likelihood |
| `PPLUS_NON_CALIBRATOR` | `IS_CALIBRATOR == 0` | remove Cepheid host calibration coupling | covariance submatrix required |
| `PPLUS_CALIBRATOR_ONLY` | `IS_CALIBRATOR == 1` | distance-ladder diagnostic | not cosmology alone |
| `PPLUS_ZHD_GT_001` | `zHD > 0.01` | avoid extreme local-flow sensitivity | document cutoff |
| `PPLUS_ZHD_GT_0023` | `zHD > 0.0233` | common Hubble-flow cut | document cutoff |
| `PPLUS_LOWZ_001_015` | `0.01 <= zHD <= 0.15` | local anisotropy / H0 drift checks | not enough for full DE claim |
| `PPLUS_DESI_OVERLAP_Z` | redshift range overlapping DESI BAO | compare shape consistency | not same observable |
| `PPLUS_QUALITY_SALT2` | finite `x1,c,mB`, acceptable `FITCHI2/FITPROB` | remove pathological fits | thresholds must be declared before run |

---

## 5. Joint DESI × Pantheon+ calculation plan

| stage | action | output | fail condition |
|---|---|---|---|
| 1 | verify DESI vector and covariance order | `desi_vector_audit.json` | mismatch between 13 rows and 13×13 matrix |
| 2 | download/hash Pantheon+ official files | `pantheon_provenance.json` | missing SHA256 / size / source URL |
| 3 | read Pantheon+ with full covariance | `pantheon_preflight.json` | covariance N not equal data rows |
| 4 | create filter masks before fitting | `filter_manifest.json` | filter defined after seeing model deltas |
| 5 | run LCDM/wCDM/CPL/RLL on identical masks | `joint_fit_results.json` | unequal dataset between models |
| 6 | compute chi2, AIC, AICc, BIC, deltas | `model_comparison_table.md` | missing k/N/provenance |
| 7 | run robustness battery | seed/timestamped outputs | overwritten canonical result |

---

## 6. TOKEN_VAZIO ledger for this stage

| object | current state | why | next measure |
|---|---|---|---|
| Pantheon+ local SHA256 | `TOKEN_VAZIO_SHA256` | official files not yet hashed in repo context | run `scripts/verify_pantheon_inputs.py --json` after download |
| Pantheon+ full SN likelihood output | `TOKEN_VAZIO_RUN` | no current joint Pantheon+ result in this table | run preflight + likelihood with covariance |
| DESI/Pantheon combined filters | `TOKEN_VAZIO_FILTER_RUN` | filters proposed but not executed | create filter manifest and run |
| RLL claim with Pantheon+ | `TOKEN_VAZIO_CLAIM` | no full covariance SN result yet | fit robust battery with fixed claim gates |

---

## 7. Minimal commands once files are present

```bash
python scripts/verify_pantheon_inputs.py --json
python -m rll.cli preflight-real --json
python -m data.pipelines.structure_d.joint_real_likelihood
```

The robust run must write to seed/timestamped output files, not overwrite the current canonical smoke result.
