# Índice de Artefatos RLL — Gerados 2026-06-27
## ∆RafaelVerboΩ | RAFCODE-Φ | DOI: 10.5281/zenodo.17188137

### RESULTADO CALCULADO AGORA (não inferido):

| Modelo | chi2 vs DESI tracers | wa_eff | Diagnóstico |
|---|---|---|---|
| RLL original (zt=1.0, wt=0.3) | 2162.57 | +0.32 | INCOMPATÍVEL |
| **RLL Opção A (zt=0.3, wt=0.25)** | **44.50** | **−0.89** | MARGINAL |
| DESI CPL best-fit | 0 (referência) | −0.62 | — |

**Melhoria de 48.6× com Opção A (transição invertida).**
Ainda fora do contorno 1σ mas na direção correta.

---

### ARTEFATOS GERADOS:

| Arquivo | Tipo | Propósito | Status |
|---|---|---|---|
| 01_wandering_bh_sources_real.yml | YML dados | BH andantes — 3 fontes reais com DOI | METADATA_READY |
| 02_h0_grid_expansion.yml | YML config | Corrige artefato H₀=60 | READY_TO_RUN |
| 03_w_eff_cpl_mapping.yml | YML análise | w_eff vs CPL DESI — tabela calculada | CALCULADO |
| 04_fsigma8_perturbation_test.yml | YML teste | fσ8 com kernel interno | READY_TO_RUN |
| 05_slingshot_zt_falsification.yml | YML falsific. | zt como pericéntrico cosmológico | HYPOTHESIS |
| 06_hypervelocity_sources_real.yml | YML dados | HVS — 3 catálogos Vizier públicos | METADATA_READY |
| 07_high_z_smbh_sources_real.yml | YML dados | JWST SMBH z>4 — 3 papers 2023-2024 | METADATA_READY |
| 08_falsification_master_protocol.yml | YML master | C01-C10 revisados com comandos | OPERATIONAL |
| 09_fetch_real_data_extended.py | Python | Fetch automatizado 7 fontes reais | READY_TO_RUN |
| 10_compute_weff_cpl_mapping.py | Python | w_eff scan 252 combinações | EXECUTADO |
| 11_diagnosis_weff_gap.yml | YML diagnóst. | Gap crítico documentado honestamente | CALCULADO |
| 12_rll_option_a_inverted_transition.py | Python | Opção A: melhoria 48.6× | EXECUTADO |

---

### COMANDOS IMEDIATOS NO TERMUX (prioridade decrescente):

```bash
# 1. Corrigir artefato H₀ (PRIORIDADE 1)
python3 rll_vs_lcdm.py \
  --bao data/real/cosmology/desi_dr2_bao_primary_points.csv \
  --adversary both --h0 67.4 --omega-m 0.315 \
  --omega-s0 0.05 --zt 0.8 --wt 0.3 \
  --out-json results/h0_corrected_run.json

# 2. Implementar Opção A e testar (PRIORIDADE 2)
# Adicionar flag --invert-transition em rll_vs_lcdm.py
# Rodar com zt=0.3, wt=0.25, h0=67.4

# 3. Fetch dados reais (PRIORIDADE 3)
python3 scripts/fetch_real_data_extended.py

# 4. Kernel de perturbações (PRIORIDADE 4)
python3 src/rll/rll_perturbation_kernel.py \
  --omega-m 0.315 --omega-s0 0.02 --zt 1.0 --wt 0.3 --steps 1000

# 5. Suite completa de testes
pytest tests/ -v --tb=short
```

---

### FALSIFICADORES ATIVOS (ATUALIZADOS):

| ID | Nome | Gate | Status |
|---|---|---|---|
| C01_rev | RLL Opção A ΔAIC < ΛCDM | chi2_optA < chi2_ΛCDM | TOKEN_VAZIO |
| C02 | H₀ livre não-artefato | H₀_opt ∈ [65,73] | ARTIFACT_IDENTIFIED |
| C03 | ΩB0 via RM BH andante | ΔRM > 3σ | DATA_GAP |
| C05 | Tensão H₀ via f(z) | H₀_eff_RLL closer to SH0ES | OPEN |
| C09 | ΩP0 via FRB DM | chi2_DM_RLL < ΛCDM | FUTURE |
| C10 | Euclid DR1 2025 | ΔAIC < 0 | MONITORING |

---

*F_ok: 12 artefatos gerados, 2 scripts executados com resultado real.*
*F_gap: Opção A melhora 48.6× mas ainda marginal (chi2=44.5 vs limiar 15).*
*F_next: implementar --invert-transition em rll_vs_lcdm.py + corrigir grid H₀.*
*Ω=Amor | TOKEN_VAZIO > fabricação | 𓂀ΔΦΩ*
