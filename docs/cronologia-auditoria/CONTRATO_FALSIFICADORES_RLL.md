# CONTRATO DE FALSIFICADORES — RLL v0.1.0

**Data**: 20260709 | **Pipeline**: rll-validacao-cientifica-completa | **Run**: 28995165927 | **Commit**: f1e5354d

> *"Um modelo científico que não pode ser falsificado não é ciência — é dogma."* — RAFAELIA

## Status Geral

| PASS | FAIL | TOKEN_VAZIO |
|------|------|-------------|
| 2/5 | 2/5 | 1/5 |

> **Nota (FASE 15, 2026-07-10)**: versão anterior gerada pelo CI (2026-07-09) continha TOKEN_VAZIO
> incorreto em F-COS-01, F-COS-02, F-COS-03. Valores corrigidos abaixo com fontes de dados.
> F-COS-03 FAIL (resultado honesto) — ver `14_ZT_SCAN_RESULTADO_REAL.md` para detalhes.

## Falsificadores Ativos

| ID | Descrição | Threshold | Resultado | Status | Fonte |
|----|-----------|-----------|---------|--------|-------|
| F-COS-01 | ΔAIC(RLL−ΛCDM) < +10 — Pantheon+SH0ES | `ΔAIC < 10` | **3.805** | ✅ PASS [E] | `results/pantheon_plus_resultado_real.txt` |
| F-COS-02 | χ²_Pantheon/dof < 1.05 — RLL original | `χ²_red < 1.05` | **0.4387** | ✅ PASS [E] | `results/pantheon_plus_resultado_real.txt` |
| F-COS-03 | z_t ∈ [0.5, 1.5] — scan slingshot | `0.5 ≤ z_t ≤ 1.5` | **z_t_BAO=0.3** | ✗ FAIL [E] | `results/zt_scan/summary.json` |
| F-COS-04 | ln(B₁₀) RLL/ΛCDM > −5 — escala Jeffreys | `ln(B₁₀) > −5` | **−6.24 (proxy BIC)** | ✗ FAIL [C proxy] | `results/bayes_factor_bic_proxy.json` |
| F-COS-05 | χ²_DESI DR2 BAO < 150 (parâmetros nominais) | `χ²_nominal < 150` | **93.81** | ✅ PASS [E] | `results/desi_dr2_bao_covariance_chi2.json` |

## P0 Desbloqueadores

| Gap | Status | Método |
|-----|--------|--------|
| Joint MCMC Pantheon+ + DESI BAO | ⚠️ TOKEN_VAZIO P0 | Disparar `rll-validacao-cientifica-completa` modo=completo |
| Fator de Bayes RLL/ΛCDM (definitivo) | ⚠️ TOKEN_VAZIO P0 | Pipeline → job `bayes_factor_p0` (dynesty/nested sampling) |

## Rastreabilidade de Artefatos

| Artefato | Job | Arquivo CI |
|----------|-----|------------|
| Fit Pantheon+ | fit_pantheon_rll | artifacts/pantheon_fit/pantheon_fit_result.json |
| DESI BAO χ² | fit_desi_bao | artifacts/desi_bao/desi_bao_result.json |
| w_eff CPL | weff_cpl_mapping | artifacts/weff_mapping/weff_cpl_mapping.json |
| Scan z_t | zt_falsification | artifacts/zt_falsification/zt_result.json |
| MCMC conjunto | joint_mcmc_p0 | artifacts/joint_mcmc/joint_mcmc_summary.json |
| Bayes Factor | bayes_factor_p0 | artifacts/bayes_factor/bayes_factor_result.json |

## Claim Boundary

> Documento gerado automaticamente pelo pipeline CI. Resultados `TOKEN_VAZIO` indicam
> gaps epistêmicos ainda não fechados. Nenhuma afirmação de superioridade do modelo RLL
> pode ser feita sem revisão por pares dos artefatos completos.
> Referência canônica: `.github/workflows/real-data-complete-execution.yml`

---
*Gerado em 2026-07-09T05:08:11.573798+00:00 por rll-validacao-cientifica-completa*