# Grafo Epistêmico de Sessão FASE 17–20

**Sessão**: SESSION_FASE17_20_2026-07-14_15
**Método**: ψ→χ→Δ→Σ (reanálise epistêmica)
**Branch**: `claude/rll-cronologia-auditoria-qyvn83`
**claim_allowed**: false

---

## Evolução FASE 17→20: Tabela de Afirmações

| ID | Texto (resumido) | Status | Confiança | Dependências |
|----|-----------------|--------|-----------|--------------|
| C-F17-01 | Ωs0=0.012 era artefato E&H | VERIFICADO_NA_FONTE | 0.97 | C-F18-02, C-F19-01 |
| C-F18-01 | rs_star calib +0.1988 Mpc → chi²_CMB≈0 | VERIFICADO_NA_FONTE | 0.99 | planck_2018_vi, chen_2019 |
| C-F18-02 | Bias E&H: Δrd=+3.614 Mpc | VERIFICADO_NA_FONTE | 0.99 | planck_2018_vi, eisenstein_hu_1998 |
| C-F19-01 | rd calib −3.614 Mpc corrige viés | VERIFICADO_NA_FONTE | 0.99 | C-F18-02 |
| C-F19-02 | Com rd correto, Ωs0→0 | VERIFICADO_NA_FONTE | 0.98 | C-F19-01, C-F17-01 |
| C-F19-03 | ΔBIC=+22.27 → ΛCDM forte | VERIFICADO_NA_FONTE | 0.95 | C-F19-02 |
| C-F20-01 | Ωs0 UL95=0.00178 (MCMC) | VERIFICADO_NA_FONTE | 0.93 | C-F19-01 |
| C-F20-02 | ln(B₁₀)=−6.190±0.691 (dynesty) | VERIFICADO_NA_FONTE | 0.96 | C-F19-01 |
| C-F20-03 | Evidência muito forte para ΛCDM (Jeffreys) | VERIFICADO_NA_FONTE | 0.95 | C-F20-02 |
| C-F20-04 | G4: bias E&H varia em param space | TOKEN_VAZIO | 0.70 | C-F19-01 |

---

## Cadeia paper→claim→código→teste→artefato

```
planck_2018_vi  ──SUPPORTS──► rd_calibration
                                    │
                               IMPLEMENTS
                                    │
                        rll_fase19_rd_calibrado.py
                                    │
                    ┌───────────────┤
                    │           PRODUCES
                    │               │
                 CLOSES        rll_fase19_rd_calibrado.json
                    │               │
                   G2          SUPPORTS──► C-F19-01 (rd calib OK)
                                    │
                               SUPPORTS──► C-F19-02 (Ωs0→0)
                                    │
                               SUPPORTS──► C-F19-03 (ΔBIC=+22.27)

foreman_mackey_2013 ──USED_IN──► rll_fase20_mcmc_bayes.py
speagle_2020        ──USED_IN──► rll_fase20_mcmc_bayes.py
                                          │
                     ┌────────────────────┤
                     │                PRODUCES
                     │                    │
               CLOSES: G1, G3     rll_fase20_mcmc_bayes.json
                                          │
                               SUPPORTS──► C-F20-01 (Ωs0 UL95=0.00178)
                               SUPPORTS──► C-F20-02 (ln(B₁₀)=−6.190)
                               SUPPORTS──► C-F20-03 (Jeffreys: muito forte)

jeffreys_1961 ──SUPPORTS──► C-F20-03

C-F17-01 ──NOT_EVIDENCE_FOR──► [validação do modelo RLL]
           ──DERIVED_FROM──► eh_bias
           ──DERIVED_FROM──► G4 (limitação residual da calibração aditiva)
```

---

## Contradição Resolvida

| ID | Conflito | Mecanismo | Resolução |
|----|----------|-----------|-----------|
| CONTRADICTION-01 | Ωs0=0.012 (FASE18-E) vs Ωs0≈0 (FASE19-20) | rd_EH +3.61 Mpc → otimizador compensava com Ωs0>0 | Calibração rd correta → Ωs0 colapsa a zero; FASE18-E SUPERSEDED |

---

## TOKEN_VAZIO — Estado Final

| ID | Descrição | Status | Resultado |
|----|-----------|--------|-----------|
| G1 | MCMC joint posterior de Ωs0 | ✅ FECHADO | Ωs0 UL95=0.00178 |
| G2 | rd numérico (remove bias E&H) | ✅ FECHADO | calibração −3.614 Mpc |
| G3 | Bayes Factor formal ln(B₁₀) | ✅ FECHADO | −6.190±0.691 (muito forte ΛCDM) |
| G4 | Mapeamento bias E&H em param space | ⬜ TOKEN_VAZIO [H] P3 | Baixa prioridade; impacto estimado ~1-2 ln(B₁₀) |

---

## Heurísticas H1–H8 Aplicadas

| H | Nome | Aplicação |
|---|------|-----------|
| H1 | Proveniência antes de embeddings | Cada C_i tem source, origin, time explícitos |
| H2 | Deduplicação bibliográfica determinística | sources.bib usa DOI/arXivID como chave |
| H3 | Estado epistemológico obrigatório | 9 claims com status; nenhum sem marcação |
| H4 | Ausência tem três valores | gaps.jsonl distingue FECHADO/TOKEN_VAZIO/not_examined |
| H5 | Separar semântica de evidência | NOT_EVIDENCE_FOR para C-F17-01 vs validação RLL |
| H6 | Baseline antes do modelo sofisticado | MCMC (emcee) → nested sampling (dynesty) |
| H7 | Divisão temporal | Experimentos em sequência cronológica FASE 17→18→19→20 |
| H8 | Fórmula só após operacionalização | formulas.yaml tem variáveis+domínio+dados definidos |

---

## Referências Cruzadas

- `results/session_grafo_fase17_20/claims.jsonl` — 10 afirmações atômicas C_i
- `results/session_grafo_fase17_20/sources.bib` — 10 entradas BibTeX
- `results/session_grafo_fase17_20/entities.jsonl` — 44 nós tipados
- `results/session_grafo_fase17_20/relations.jsonl` — 44 arestas tipadas
- `results/session_grafo_fase17_20/graph.graphml` — grafo GraphML completo
- `docs/cronologia-auditoria/20_GRAFO_SESSAO_FASE17_20.md` — documento de auditoria

---

*Gerado por scripts/build_session_grafo_fase17_20.py — claim_allowed: false*
