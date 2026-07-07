# CONTRATO DE FALSIFICADORES — RLL v0.1.0

**Data**: 20260707 | **Pipeline**: rll-validacao-cientifica-completa | **Run**: 28860351117 | **Commit**: 3f436f0c

> *"Um modelo científico que não pode ser falsificado não é ciência — é dogma."* — RAFAELIA

## Status Geral

| PASS | FAIL | TOKEN_VAZIO |
|------|------|-------------|
| 3/5 | 0 | 2 |

## Falsificadores Ativos

| ID | Descrição | Threshold | Resultado | Status |
|----|-----------|-----------|---------|--------|
| F-COS-01 | ΔAIC(RLL−ΛCDM) < +10 — Pantheon+SH0ES | `ΔAIC < 10` | 3.805 | ✅ PASS [E — FASE 4] |
| F-COS-02 | χ²_Pantheon/dof < 1.05 — RLL original | `χ²_red < 1.05` | 0.4386 | ✅ PASS [E — FASE 4] |
| F-COS-03 | z_t ∈ [0.5, 1.5] — scan C01 slingshot | `0.5 ≤ z_t ≤ 1.5` | TOKEN_VAZIO | ⚠️ P0 aguarda MCMC joint (G1) |
| F-COS-04 | ln(B₁₀) RLL/ΛCDM > −5 — escala Jeffreys | `ln(B₁₀) > −5` | TOKEN_VAZIO | ⚠️ P0 aguarda pipeline Bayes (G2) |
| F-COS-05 | χ²_DESI DR2 BAO < 150 (parâmetros nominais) | `χ²_nominal < 150` | 93.81 | ✅ PASS [E] |

## P0 Desbloqueadores

| Gap | Status | Método |
|-----|--------|--------|
| Joint MCMC Pantheon+ + DESI BAO | ⚠️ TOKEN_VAZIO | Disparar `rll-validacao-cientifica-completa` modo=completo → job `joint_mcmc_p0` |
| Fator de Bayes RLL/ΛCDM | ⚠️ TOKEN_VAZIO | Mesmo pipeline → job `bayes_factor_p0` (dynesty/Laplace) |

## Análise w_eff — FASE 11 (2026-07-07)

Verificação numérica dos setores RLL vs CPL DESI (χ² com σ=0.05 sobre 6 pontos BAO):

| Variante | χ²_melhor | Parâmetros ótimos | w_eff < 0 sempre? |
|----------|-----------|------------------|-------------------|
| Padrão (f + matéria) | 1162.3 | nominais | Não (cruza em z~0.45) |
| Opção A (1-f + matéria) | 2232.2 | nominais | Não (cruza em z<0) |
| **Opção B** (DE puro bimodal) | **14.8** | w2=−0.50, w_t=0.50 | **Sim** |
| Opção C (setor duplo α·f) | 104.0 | α=0.50, r=0.05 | Depende de r |

**Nota**: Opção B não é um novo falsificador — é uma análise exploratória de compatibilidade arquitetural.  
Nenhuma das variantes atingiu χ²<10 no scan discreto. P-RLL-05 prediz que otimização contínua pode cruzar esse limiar.

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
*Versão inicial gerada em 2026-07-07T10:51:50.836622+00:00 por rll-validacao-cientifica-completa (run 28860351117).*  
*Atualizado em FASE 12 (2026-07-07): F-COS-01/02 refletidos com valores reais de FASE 4; análise w_eff FASE 11 adicionada.*