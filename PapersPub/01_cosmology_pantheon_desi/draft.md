# Relativity Living Light as a Falsifiable Candidate Cosmology: A Conservative Joint Real-Data Smoke Comparison against LCDM, wCDM and CPL

**Status:** `draft_paper_v0.1`  
**Repository:** `instituto-Rafael/relativity-living-light`  
**Paper track:** `PapersPub/01_cosmology_pantheon_desi`  
**Prepared:** `2026-06-16`  
**Authors:** Instituto Rafael / Rafael Melo Reis  
**Claim gate:** `claim_allowed = false`  
**Numerical artifact used:** `results/structure_d/joint_real_likelihood.json`  
**Important scope note:** this manuscript draft reports the current repository state and the current smoke/sanity run. It does not report a final cosmological fit, posterior inference, or model confirmation.

---

## Abstract

Relativity Living Light (RLL) is treated here as a candidate effective dynamic-transition cosmology rather than as a confirmed physical replacement for the standard model. This paper draft presents the current reproducible repository state for a joint real-data smoke comparison of LCDM, wCDM, CPL/w0waCDM and RLL using the available likelihood artifact in `results/structure_d/joint_real_likelihood.json`. The run combines observational blocks for H(z), DESI DR2 BAO primary points with materialized BAO covariance, fσ8/growth proxy data, and a compressed CMB-shift block, with a shared optimizer policy based on `scipy.optimize.differential_evolution`, seed `42`, tolerance `0.001`, and `maxiter=3` for all models. The smoke result contains `N=64` effective points. In this execution, CPL/w0waCDM is favored by chi2 and by information criteria. RLL reaches a LCDM-like limit with `Os0=0.0`, producing chi2 effectively indistinguishable from LCDM while being penalized by AIC, AICc and BIC because of the larger parameter count. Therefore, strong claims remain blocked: RLL is not confirmed, does not beat LCDM, does not beat CPL, and cannot yet be claimed to resolve dark energy, H0 or S8 tensions. The contribution of the current work is methodological and epistemic: it converts a symbolic/phenomenological cosmology into an auditable object with explicit gates separating concept, data, computation, missing evidence, falsification conditions and publication language.

**Keywords:** Relativity Living Light; RLL; cosmology; LCDM; wCDM; CPL; DESI DR2 BAO; H(z); information criteria; falsifiability; reproducibility; TOKEN_VAZIO.

---

## 1. Scientific position and claim boundary

The present manuscript adopts a conservative scientific posture. RLL is not presented as established cosmology. It is presented as a structured hypothesis that must survive comparison against standard and flexible baselines under real observational data, reproducible scripts, explicit parameter accounting, documented datasets and falsifiable gates.

The current repository policy is:

```text
claim_allowed = false
```

This state is not a failure of the project. It is the correct scientific state while robust-fit, posterior, complete covariance, growth backends and full data materialization remain incomplete. In the language of the project, unresolved evidence is not treated as proof. It is marked as `TOKEN_VAZIO`, meaning an honest missing measurement, missing backend, missing covariance, missing posterior or missing reproducibility object.

The allowed scientific statement at this stage is:

> RLL remains a candidate effective dynamic-transition cosmology under real-data evaluation, with an auditable pipeline and conservative claim gates.

The prohibited scientific statements at this stage are:

- RLL is confirmed.
- RLL wins against LCDM.
- RLL wins against CPL/w0waCDM.
- RLL resolves dark energy.
- RLL resolves the H0 tension.
- RLL resolves the S8 tension.
- A symbolic metaphor or incomplete output is observational evidence.

This boundary is central to the paper: the work is valuable precisely because it makes the difference between hypothesis, computation, data, lacuna and claim explicit.

---

## 2. Conceptual model

RLL is treated as a phenomenological extension/transition structure. Its present computational representation introduces parameters that can activate or suppress the RLL sector. In the current joint smoke artifact, the RLL row contains:

```text
Os0 = 0.0
zt  = 0.48913585347939664
wt  = 0.5725207843474277
```

The value `Os0=0.0` is the key diagnostic. It means that the current optimizer found the best smoke-test solution by deactivating the additional RLL sector, making the RLL prediction effectively collapse to a LCDM-like limit while still carrying a larger parameter count. This creates an important falsifiability signal:

```text
If RLL reduces to LCDM-like behavior while using more parameters, information criteria should penalize RLL.
```

That is exactly what the current artifact reports.

This is scientifically useful because it gives the project a non-rhetorical test. A live model must be able to lose. A model that cannot lose is not yet a scientific model; it is only language. In the current state, RLL does not receive a victory claim. It receives a clear next-test route.

---

## 3. Data blocks and provenance

The joint real-data smoke artifact records the following data paths:

| Block | Repository path | Role |
|---|---|---|
| H(z) | `data/real/Hz_data_real.csv` | Expansion-rate observations |
| DESI DR2 BAO primary | `data/real/cosmology/desi_dr2_bao_primary_points.csv` | BAO observables |
| DESI DR2 BAO covariance | `data/real/desi_dr2_bao_covariance.csv` | Full BAO covariance in current artifact |
| fσ8/growth | `data/real/cosmology/fsigma8_growth_real.csv` | Structure-growth proxy block |
| CMB shift | `data/real/CMB_shift_real.json` | Compressed CMB-shift block |
| Parameter registry | `data/inputs/cosmology_joint/parameter_origin_registry.json` | Parameter provenance and accounting |

The artifact classifies the dataset type as:

```text
dataset_type = real_observational
```

However, two important limits remain:

1. `Pantheon+` is not promoted here as a completed joint-likelihood block in the current artifact.
2. Growth remains blocked for strong claims because the artifact reports the external CLASS/CAMB benchmark as unavailable in the execution environment.

Therefore, the title track may reference the broader Pantheon+/DESI paper route, but the numerical result in this draft must be described only as the currently materialized joint smoke run.

---

## 4. Methods

### 4.1 Model set

The smoke comparison includes four model classes:

1. `LCDM_joint_real`
2. `wCDM_joint_real`
3. `CPL_w0waCDM_joint_real`
4. `RLL_joint_real`

LCDM functions as the standard baseline. wCDM introduces a constant dark-energy equation-of-state freedom. CPL/w0waCDM introduces a time-varying dark-energy parameterization. RLL introduces its own dynamic-transition sector and is therefore expected to be penalized by information criteria unless its fit improvement compensates for the extra degrees of freedom.

### 4.2 Optimization policy

The current artifact uses:

```text
optimizer = scipy.optimize.differential_evolution
seed      = 42
tol       = 0.001
maxiter   = 3 for LCDM, wCDM, CPL and RLL
```

The shared low `maxiter=3` is important. It makes the run useful as a smoke/sanity comparison, but not as a final model-ranking result. A robust fit must use substantially larger iteration budgets and multiple seeds.

### 4.3 Metrics

For each model, the artifact reports:

- total chi2;
- AIC;
- AICc;
- BIC;
- effective number of data points `N`;
- number of parameters `k`;
- degrees of freedom `dof`;
- chi2 contributions by data block.

The information criteria are essential because models with additional parameters can reduce chi2 by flexibility alone. A model only earns stronger support when the improvement is large enough to survive complexity penalty.

---

## 5. Results

### 5.1 Main model-ranking table

| Model | chi2 | AIC | AICc | BIC | N | k | dof | Current status |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| LCDM | 84.48241222580135 | 94.48241222580135 | 95.51689498442204 | 105.27682764259971 | 64 | 5 | 59 | baseline |
| wCDM | 83.71037717797158 | 95.71037717797158 | 97.1840613884979 | 108.66367567812961 | 64 | 6 | 58 | slightly lower chi2, worse information criteria |
| CPL/w0waCDM | 62.071708706289364 | 76.07170870628937 | 78.07170870628937 | 91.18389028980707 | 64 | 7 | 57 | favored in the current smoke run |
| RLL | 84.48241222572261 | 100.48241222572261 | 103.10059404390444 | 117.75347689259999 | 64 | 8 | 56 | not favored; collapses to `Os0=0.0` |

The current smoke artifact favors CPL/w0waCDM. LCDM remains stronger than RLL under information criteria because RLL does not improve chi2 while carrying additional parameters. wCDM slightly improves chi2 relative to LCDM but does not survive the AIC/AICc/BIC penalties in this execution.

### 5.2 Blockwise chi2 decomposition

| Model | chi2_Hz | chi2_DESI_DR2_BAO | chi2_fsigma8 | chi2_CMB_shift |
|---|---:|---:|---:|---:|
| LCDM | 19.430741008634875 | 20.575030662200746 | 23.630658522602975 | 20.845982032362752 |
| wCDM | 19.365634730204704 | 17.48883027438094 | 22.797439542715814 | 24.058472630670114 |
| CPL/w0waCDM | 19.220020703366146 | 12.082522240097463 | 18.87551935235649 | 11.893646410469268 |
| RLL | 19.43074096832219 | 20.575029041552828 | 23.630658584576636 | 20.84598363127095 |

CPL/w0waCDM improves the BAO, growth-proxy and CMB-shift blocks in this smoke run. RLL closely tracks LCDM in all blocks, consistent with the `Os0=0.0` diagnostic.

### 5.3 Deltas against LCDM

| Comparison | delta_chi2 | delta_AIC | delta_AICc | delta_BIC | Interpretation |
|---|---:|---:|---:|---:|---|
| wCDM - LCDM | -0.7720350478297746 | 1.2279649521702254 | 1.6671664040758571 | 3.386848035529894 | chi2 improves slightly, but complexity penalty dominates |
| CPL - LCDM | -22.41070351951199 | -18.410703519511983 | -17.445186278132667 | -14.092937352792646 | favored by chi2 and information criteria in this smoke artifact |
| RLL - LCDM | -7.87423459769343e-11 | 5.999999999921258 | 7.583699059482399 | 12.476649250000278 | chi2 effectively unchanged; ICs worsen due to larger `k` |

These deltas enforce the current claim boundary. RLL cannot be reported as preferred. The correct statement is that the pipeline is functioning and that the current RLL parameterization falls back to the LCDM-like sector under the smoke configuration.

---

## 6. Interpretation

The present result should be read as a diagnostic, not as a terminal verdict.

Three findings matter:

1. **The joint comparison object exists.**  
   The repository contains a structured artifact comparing LCDM, wCDM, CPL and RLL under the same smoke-run framework.

2. **The current RLL execution is not competitive.**  
   RLL reaches `Os0=0.0`, making it effectively LCDM-like in prediction while receiving additional complexity penalties.

3. **CPL is the required adversary baseline.**  
   Because CPL/w0waCDM is favored in the current run, any future RLL claim must compare not only against LCDM but also against CPL.

This transforms the next phase from broad narrative into precise engineering:

```text
Can RLL remain active with Os0 > 0 while improving chi2 enough to survive AIC/AICc/BIC against LCDM and CPL under robust seeds, complete covariance and external growth validation?
```

Until that question is answered, the model remains a candidate under test.

---

## 7. Falsifiability conditions

### 7.1 Conditions that block a strong RLL claim

A strong RLL claim remains blocked if any of the following persist:

- RLL is worse than LCDM in AIC/AICc/BIC.
- RLL is effectively equal to LCDM but has larger `k`.
- CPL remains better than RLL under robust settings.
- Pantheon+ or equivalent supernova likelihood remains unmaterialized.
- CMB covariance remains partial or undocumented.
- Growth validation lacks CLASS/CAMB or an equivalent external benchmark.
- Results depend on a single seed or a smoke-level optimizer budget.
- Posterior inference is absent.

### 7.2 Conditions that would keep RLL alive as a candidate

RLL remains scientifically alive if:

- it is implemented reproducibly;
- it remains falsifiable;
- its additional sector can be ablated;
- `Os0 > 0` can be tested under constrained and unconstrained regimes;
- failures are recorded rather than hidden;
- the claim gate remains conservative.

### 7.3 Conditions that would allow stronger discussion

A stronger RLL discussion becomes possible only if future runs show:

- robust multi-seed convergence;
- no dependence on smoke optimizer settings;
- improvement against LCDM and CPL in chi2;
- improvement or competitive behavior under AIC/AICc/BIC;
- complete data/covariance provenance;
- posterior or nested-sampling evidence;
- external growth validation;
- reproducible commands, hashes and outputs.

---

## 8. Limitations

| Limitation | Current state | Consequence |
|---|---|---|
| Optimizer budget | `maxiter=3` | Smoke/sanity only; not a final fit |
| Seeds | single seed `42` | No robustness across random initializations |
| Pantheon+ | not promoted in current joint artifact | Broad cosmological claim blocked |
| Growth benchmark | CLASS/CAMB unavailable in current environment | Growth block remains internally approximated |
| CMB covariance | compressed/partial status requires further audit | CMB claim remains limited |
| Posterior inference | absent | No robust parameter uncertainty or evidence |
| RLL activation | `Os0=0.0` | RLL sector deactivated in current optimum |
| Information criteria | RLL worse than LCDM and CPL | Victory claim blocked |

These limitations are not editorial weaknesses; they are the scientific safeguards that make the repository auditable.

---

## 9. Reproducibility and audit trail

The paper is grounded in the following repository artifacts:

- `results/structure_d/joint_real_likelihood.json`
- `docs/RLL_CURRENT_RESULTS_PAPER_TABLE.md`
- `docs/RLL_CLAIM_GATE_LEDGER.md`
- `PapersPub/01_cosmology_pantheon_desi/data_manifest.md`
- `PapersPub/01_cosmology_pantheon_desi/reproducibility.md`
- `PapersPub/01_cosmology_pantheon_desi/references.md`

No new numerical execution is claimed in this draft update. The document is an editorial/scientific synthesis of the current repository state.

A future reproducibility upgrade should include:

```bash
# Example target pattern; exact script/CLI may change after audit.
python data/pipelines/structure_d/joint_real_likelihood.py \
  --seed 1 --maxiter 100 \
  --output results/structure_d/robust/joint_real_likelihood_seed001.json
```

Required future artifact policy:

1. never overwrite the current canonical smoke artifact without backup;
2. store each robust run by seed and configuration;
3. record environment, command, input hashes and output hashes;
4. produce a summary table comparing seeds;
5. rerun all models under the same policy;
6. include CPL as a mandatory baseline;
7. keep `claim_allowed=false` until all gates pass.

---

## 10. Discussion: why a negative result is useful

The current artifact is scientifically valuable because it prevents premature triumph. RLL is not protected from failure; it is exposed to measurable loss. In this smoke run, the optimizer chooses the LCDM-like limit for RLL. This can mean several things:

1. the RLL sector is unnecessary for the present data/configuration;
2. the current parameterization is too flexible but not predictive enough;
3. the optimizer budget is too shallow to find an active RLL basin;
4. the current data blocks do not constrain the intended transition feature;
5. the model needs ablation, priors, reparameterization or a different observable before any claim can be made.

The next scientific act is not to hide the result. The next act is to sharpen it.

A rigorous RLL program should ask:

- Does fixing `Os0 > 0` worsen the fit, improve it, or expose degeneracy?
- Does RLL improve any block while damaging another?
- Is the LCDM-like collapse stable across seeds?
- Does CPL remain preferred after robust optimization?
- Do posterior constraints force `Os0` to zero?
- Does adding Pantheon+ reinforce or weaken the current outcome?
- Does an external growth backend change the fσ8 interpretation?

That is the transition from symbolic cosmology to testable cosmology.

---

## 11. Minimal paper-ready conclusion

This paper draft reports a conservative repository-grounded smoke comparison of LCDM, wCDM, CPL/w0waCDM and RLL. In the current artifact, CPL/w0waCDM is favored by chi2, AIC, AICc and BIC. RLL is not favored: it reaches the `Os0=0.0` limit, becomes effectively LCDM-like in chi2, and is penalized by information criteria because of its larger parameter count. Therefore, RLL remains a falsifiable candidate under evaluation, not a confirmed model.

The principal contribution at this stage is not a claim of cosmological victory. It is the construction of an auditable claim-gated path: symbolic hypothesis → computational model → real-data artifact → baseline comparison → negative result → falsifiable next step. This is the correct scientific posture for a living theory: it must be able to transform under evidence, and it must allow the data to say no.

---

## 12. Next work items

### Immediate engineering tasks

- Add a robust output path/stem option to avoid overwriting canonical smoke artifacts.
- Run multi-seed fits with `maxiter >= 100`.
- Store every seed/configuration output separately.
- Generate a robust summary table with mean, median, best, worst and variance.
- Add ablation runs for RLL parameters, especially `Os0`.

### Immediate science tasks

- Materialize Pantheon+ or mark it explicitly as `TOKEN_VAZIO_DATASET` in this paper route.
- Complete CMB covariance documentation.
- Add CLASS/CAMB or equivalent external growth benchmark.
- Run posterior inference after robust optimization.
- Compare RLL not only against LCDM, but also against CPL/w0waCDM.

### Immediate manuscript tasks

- Add external bibliographic references with DOI/arXiv/ADS identifiers.
- Add generated figures only after robust runs exist.
- Add a Methods appendix with exact command, environment and hash ledger.
- Promote status only after data and reproducibility gates pass.

---

## 13. Internal references

This draft is linked to the following internal repository references:

- `results/structure_d/joint_real_likelihood.json`
- `results/structure_d/joint_real_likelihood.csv`
- `docs/RLL_CURRENT_RESULTS_PAPER_TABLE.md`
- `docs/RLL_CLAIM_GATE_LEDGER.md`
- `docs/RLL_VS_CPL_DIAGNOSTIC.md`
- `docs/RLL_OS0_ZERO_ROOT_CAUSE.md`
- `docs/RLL_ROBUST_FIT_CHECKLIST.md`
- `docs/RLL_NEXT_ROBUST_FIT_PLAN.md`
- `PapersPub/01_cosmology_pantheon_desi/data_manifest.md`
- `PapersPub/01_cosmology_pantheon_desi/reproducibility.md`
- `PapersPub/01_cosmology_pantheon_desi/references.md`

---

## 14. R3 — retrofeedback

```text
F_ok   = paper draft now states the real current result without overclaim: CPL favored, RLL not favored, claim gate closed.
F_gap  = robust fit, posterior, Pantheon+, CMB covariance and external growth backend remain unresolved.
F_next = implement robust multi-seed route and update this draft only after reproducible artifacts exist.
```
