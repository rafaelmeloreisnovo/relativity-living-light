# CONTRATO DE FALSIFICADORES — RLL v0.1.0

**Data**: 20260707 | **Versão**: baseline estático pré-CI  
**Fonte**: resultados conhecidos de `results/pantheon_plus_resultado_real.txt` + `scripts/check_desi_dr2_bao_covariance.py`

> *"Um modelo científico que não pode ser falsificado não é ciência — é dogma."* — RAFAELIA

> **NOTA**: Este é o baseline estático criado em FASE 8 com valores reais disponíveis.
> Será sobrescrito automaticamente quando o pipeline `rll-validacao-cientifica-completa.yml`
> rodar com `commit_resultados=true`. O valor final de referência é o gerado pelo CI.

---

## Status Geral

| PASS | FAIL | TOKEN_VAZIO |
|------|------|-------------|
| 3/5 | 0 | 2 |

---

## Falsificadores Ativos

| ID | Descrição | Threshold | Resultado | Status | Fonte |
|----|-----------|-----------|-----------|--------|-------|
| F-COS-01 | ΔAIC(RLL−ΛCDM) < +10 — Pantheon+SH0ES | `ΔAIC < 10` | **3.805** | ✅ PASS | `results/pantheon_plus_resultado_real.txt` [E] |
| F-COS-02 | χ²_Pantheon/dof < 1.05 — RLL original | `χ²_red < 1.05` | **0.4386** (710.613/1620) | ✅ PASS | `results/pantheon_plus_resultado_real.txt` [E] |
| F-COS-03 | z_t ∈ [0.5, 1.5] — scan slingshot C01 | `0.5 ≤ z_t ≤ 1.5` | TOKEN_VAZIO | ⚠️ TOKEN_VAZIO | aguarda Job 5 (`zt_falsification`) |
| F-COS-04 | ln(B₁₀) RLL/ΛCDM > −5 — escala Jeffreys | `ln(B₁₀) > −5` | TOKEN_VAZIO P0 | ⚠️ TOKEN_VAZIO | aguarda Job 7 (`bayes_factor_p0`) |
| F-COS-05 | χ²_DESI DR2 BAO < 150 (parâmetros nominais) | `χ²_nominal < 150` | **93.81** | ✅ PASS | `scripts/check_desi_dr2_bao_covariance.py` [E] |

---

## Notas sobre os Resultados Conhecidos

### F-COS-01 e F-COS-02 — Pantheon+ SH0ES (N=1624 SNe)

Calculados em FASE 4 (2026-07-06) com `scripts/pantheon/run_rll_vs_pantheon.py`:

| Modelo | χ² | k | AIC | ΔAIC vs ΛCDM |
|--------|----|---|-----|-------------|
| ΛCDM | 710.808 | 2 | 714.808 | — |
| CPL | 710.390 | 4 | 718.390 | +3.582 |
| RLL original | 710.613 | 4 | 718.613 | **+3.805** |
| RLL Opção A | 710.613 | 4 | 718.613 | +3.805 |

**dof** = 1624 − 4 = 1620; χ²_red_RLL = 710.613 / 1620 = **0.4386** ✅

**Interpretação**: ΔAIC=+3.805 < 10 → RLL não é falsificado por Pantheon+ no sentido AIC.
Atenção: o ΔAIC é positivo (RLL é penalizado por 2 parâmetros extras), não indicando superioridade.

### F-COS-05 — DESI DR2 BAO (N=13 pontos)

Calculado em FASE 2 com `scripts/check_desi_dr2_bao_covariance.py` (covariância 13×13 completa):

| Modelo | χ²_BAO |
|--------|--------|
| ΛCDM | 28.97 |
| RLL (params nominais) | **93.81** |

**Aviso**: χ²_RLL=93.81 < 150 passa o threshold de F-COS-05, mas χ²_RLL/χ²_ΛCDM = 3.24 indica
que os parâmetros nominais RLL não são otimizados para BAO. O threshold de 150 é um critério conservador.

---

## P0 Desbloqueadores

| Gap | Status | Método Previsto |
|-----|--------|----------------|
| Joint MCMC Pantheon+ + DESI BAO | ⚠️ TOKEN_VAZIO P0 | Structure-D inference: `python -m data.pipelines.structure_d.run_all --bayes-mode inference --bayes-nwalkers 32 --bayes-nsteps 1000` |
| Fator de Bayes ln(B₁₀) RLL/ΛCDM | ⚠️ TOKEN_VAZIO P0 | `scripts/slingshot_zt_falsification.py --bayes-factor` (BIC proxy ou dynesty) |

---

## Rastreabilidade de Artefatos (pré-CI)

| Falsificador | Arquivo | Hash evidência |
|-------------|---------|----------------|
| F-COS-01 | `results/pantheon_plus_resultado_real.txt` | FASE 4, auditado em `09_PANTHEON_RESULTADO_REAL.md` |
| F-COS-02 | `results/pantheon_plus_resultado_real.txt` | idem |
| F-COS-03 | — | aguarda pipeline |
| F-COS-04 | — | aguarda pipeline |
| F-COS-05 | `scripts/check_desi_dr2_bao_covariance.py` | FASE 2, auditado em `08_ARVORE_CONCEITUAL_RLL.md §NÍVEL3` |

---

## Rastreabilidade de Artefatos (pós-CI, quando disponível)

| Artefato | Job | Arquivo CI |
|----------|-----|------------|
| Fit Pantheon+ | `fit_pantheon_rll` | `artifacts/pantheon_fit/pantheon_fit_result.json` |
| DESI BAO χ² | `fit_desi_bao` | `artifacts/desi_bao/desi_bao_result.json` |
| w_eff CPL | `weff_cpl_mapping` | `artifacts/weff_mapping/weff_cpl_mapping.json` |
| Scan z_t | `zt_falsification` | `artifacts/zt_falsification/zt_result.json` |
| MCMC conjunto | `joint_mcmc_p0` | `artifacts/joint_mcmc/joint_mcmc_summary.json` |
| Bayes Factor | `bayes_factor_p0` | `artifacts/bayes_factor/bayes_factor_result.json` |

---

## Claim Boundary

> Baseline estático gerado em FASE 8. Valores F-COS-01/02/05 são resultados reais de
> execuções documentadas (FASE 2 e FASE 4). Valores TOKEN_VAZIO aguardam execução do
> pipeline CI `rll-validacao-cientifica-completa.yml`.
>
> Nenhuma afirmação de superioridade do modelo RLL pode ser feita sem:
> (a) F-COS-04 ≥ −5 em escala Jeffreys (Bayes Factor não desfavorável)
> (b) Parâmetros otimizados em joint MCMC (não apenas nominais)
>
> Referência canônica: `.github/workflows/real-data-complete-execution.yml`
> Pipeline de validação: `.github/workflows/rll-validacao-cientifica-completa.yml`

---

*Baseline estático — FASE 8 (2026-07-07). Será sobrescrito pelo primeiro run CI com commit_resultados=true.*
