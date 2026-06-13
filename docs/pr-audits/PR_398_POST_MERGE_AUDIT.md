# PR #398 Post-Merge Audit — Dados

Status: post-merge audit  
PR: #398  
Title: Dados  
Merge commit: b956d02030141ed0dab85d88b4ed7a0bc79add7b  
Scope: inventory, real-validation artifacts, pipeline-run materialization

---

## 1. Executive summary

PR #398 was merged and materialized a reproducibility-oriented result set, including repository inventory updates, real-validation outputs, figures, and a pipeline run folder under:

```text
results/pipeline-runs/27457036990/
```

The PR is useful as a traceability and audit layer. It should not be interpreted as a scientific superiority claim for RLL.

The current validation summary still prefers LCDM over RLL by AIC and BIC for the materialized BAO + H(z) comparison.

---

## 2. PR metadata observed

- State: closed
- Merged: true
- Draft: false
- Base: main
- Head: main
- Title: `Dados`
- Body status: still partially placeholder-like; the PR body does not fully describe the scientific meaning of the changes.
- Comments/reviews: no issue comments, no review submissions, and no review threads were present at audit time.

---

## 3. Main files changed

The PR updated or added the following groups:

### Inventory artifacts

```text
data/results/repo_inventory.json
data/results/repo_inventory.tsv
data/results/repo_inventory_summary.json
docs/DOCUMENTATION_FULL_INVENTORY.md
docs/REAL_NUMBERS_REPORT.md
docs/YML_WORKFLOWS_INDEX.md
```

### Pipeline run artifacts

```text
results/pipeline-runs/27457036990/CHECKSUMS.sha256
results/pipeline-runs/27457036990/CLAIM_REFERENCE_AUDIT.md
results/pipeline-runs/27457036990/COMMIT_SHA.txt
results/pipeline-runs/27457036990/MANIFEST.json
results/pipeline-runs/27457036990/PIPELINE_REPORT.md
results/pipeline-runs/27457036990/RUN_UTC.txt
results/pipeline-runs/27457036990/SOURCES.md
results/pipeline-runs/27457036990/book/BOOK_ROUTE.md
results/pipeline-runs/27457036990/book/CHAPTERS_USED.md
results/pipeline-runs/27457036990/book/FILES_USED.md
```

### Real-validation artifacts

```text
validacao_real/fetched/manifest.json
validacao_real/results/RELATORIO_VALIDACAO.md
validacao_real/results/figures/bao_distances.png
validacao_real/results/figures/hubble_diagram.png
validacao_real/results/figures/model_comparison_bars.png
validacao_real/results/figures/residual_pulls.png
validacao_real/results/validation_summary.json
```

---

## 4. Pipeline run interpretation

The materialized manifest reports:

```text
run_utc: 2026-06-13T04:51:28Z
commit_sha: 8d57899b0f7e9c94a445bf9d8be6e48b6d5a2c63
book_scope: all
dataset_group: all
mode: compute
status: Parcial real em preparação
```

The manifest explicitly keeps the execution under a guarded status rather than promoting it to fully validated real-observational science.

The promotion guard states that the pipeline must not promote the result to real validated status without real execution with data, metrics, and reproducibility.

---

## 5. Claim-reference audit

The claim audit keeps geomagnetic, heliophysics, and cosmology groups as `blocked`.

This is scientifically correct because these tracks require dataset-specific validation before claims are promoted.

| Group | Model reference | Reference set | Status |
|---|---|---|---|
| geomagnetic | M(t), m(t), T_M | NOAA/NCEI IGRF14; WMM2025; ESA Swarm; NASA SAA | blocked |
| heliophysics | Phi_ext, SW, T_M, Phi_eff | NASA OMNI/SPDF; NMDB; GOES; SPENVIS AE9/AP9 | blocked |
| cosmology | E²(a), f(z), w(z), RLL vs LCDM/w0waCDM | DESI DR2 BAO; Pantheon+; Planck 2018; H(z); fσ8 | blocked |

---

## 6. Cosmology validation numbers

The materialized validation summary reports:

| Model | chi2_bao | chi2_hz | chi2_total | n_points | k_params | AIC | BIC |
|---|---:|---:|---:|---:|---:|---:|---:|
| LCDM | 25.0878 | 14.2945 | 39.3823 | 45 | 3 | 45.3823 | 50.8023 |
| RLL | 30.8473 | 14.0420 | 44.8893 | 45 | 5 | 54.8893 | 63.9226 |

Verdict in the JSON:

```json
{
  "compared": "LCDM - RLL",
  "delta_chi2": -5.507,
  "delta_aic": -9.507,
  "delta_bic": -13.1203,
  "preferred_by_aic": "LCDM",
  "preferred_by_bic": "LCDM",
  "reject_sigma": 3.0
}
```

Interpretation:

- LCDM is preferred by AIC and BIC in this run.
- RLL is not shown as falsified by the local BAO/H(z) flags, but it is penalized for worse total fit and more parameters.
- No RLL superiority claim is allowed from this artifact.

---

## 7. What PR #398 adds intellectually

PR #398 adds value by improving:

1. repository-wide inventory tracking;
2. materialized pipeline-run traceability;
3. checksum and manifest discipline;
4. explicit separation between hypothesis, data, model, metric, reference, and status;
5. conservative claim governance.

The strongest point is not model victory. The strongest point is auditability.

---

## 8. Risks / gaps

### Gap 1 — PR body was not descriptive enough

The PR was merged with a generic title and placeholder-like body text. Future PRs should include a short scientific interpretation section.

### Gap 2 — `blocked` status needs next-step routing

The audit correctly marks groups as blocked, but each blocked group should have a next action, such as required dataset, script, metric, or external baseline.

### Gap 3 — real-validation result needs boundary language

The validation summary must be referenced with explicit language:

```text
This is a partial real-data validation artifact. It does not establish RLL superiority over LCDM.
```

### Gap 4 — broad dataset_group=all can obscure which group actually computed

The manifest says `dataset_group: all`, but actual scientific computation currently visible is mainly cosmology BAO + H(z). Future manifests should separate computed groups from declared target groups.

---

## 9. Recommended follow-up PR

Recommended title:

```text
docs: add PR 398 validation boundary and blocked-status routing
```

Recommended changes:

1. Add this audit to the documentation index.
2. Add a `NEXT_ACTIONS.md` inside `results/pipeline-runs/27457036990/`.
3. Add per-group blocked reasons:
   - geomagnetic: requires IGRF/WMM/Swarm ingestion and metric definition;
   - heliophysics: requires OMNI/NMDB/GOES/SPENVIS ingestion and comparison baseline;
   - cosmology: requires Pantheon+/Planck/fσ8 integration and covariance-aware model comparison.
4. Add a claim-boundary paragraph to `validacao_real/results/RELATORIO_VALIDACAO.md` if not already present.

---

## 10. Safe conclusion

PR #398 is a traceability and materialization PR.

It documents a real-validation pipeline state and adds useful artifacts, but the current scientific result remains conservative:

```text
LCDM preferred by AIC/BIC in the visible BAO + H(z) run.
RLL not promoted to superiority claim.
Validation status remains partial / blocked for broader groups.
```

This is a healthy result for operational science: the repository is becoming more honest, more auditable, and harder to confuse with unchecked claims.

---

## Retrofeedback

F_ok: PR #398 strengthens auditability and materialized evidence.  
F_gap: PR body and blocked-status routing need cleanup.  
F_next: create per-group next-action ledgers before promoting any scientific claim.
