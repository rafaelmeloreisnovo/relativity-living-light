# RLL — TOKEN_VAZIO Priority Ledger

**Gerado**: 2026-07-05  
**Método**: Sistematização de lacunas documentadas em auditoria  
**Princípio**: "Lacuna marcada vira ciência" — preservação honesta de incertezas

---

## Legenda de Prioridades

| Nível | Critério | Impacto | Ação |
|-------|----------|--------|------|
| **P0** | Crítico para validação central | Bloqueia afirmação de modelo | Requer resolução antes de paper |
| **P1** | Alto impacto em confiança | Afeta interpretação | Requere investigação documentada |
| **P2** | Médio impacto em robustez | Afeta generalização | Nice-to-have para completude |
| **P3** | Baixo impacto prático | Afeta performance | Melhorias secundárias |

---

## P0: Crítico para Validação Central

### Gap 1: Reprodutibilidade dos Notebooks

**Questão**: Os notebooks da tag v1.0.0 realmente reproduzem H(z) e os gráficos documentados?

**Por que P0**: Se notebooks não executam ou produzem outputs diferentes, toda a cronologia é questionável.

**Status**: ⚠️ **TOKEN_VAZIO** — arquivos existem, execução não validada

**Comando para resolver**:
```bash
cd data/
nbconvert --execute --to notebook Hz_superposicao.ipynb --output /tmp/Hz_exec.ipynb
nbconvert --execute --to notebook density_decomp.ipynb --output /tmp/density_exec.ipynb
# Comparar outputs contra figs/*.png
```

**Próximo passo**: Executar em ambiente Termux ARM32 + documentar outputs

---

### Gap 2: Primeiro Commit Exato com "DESI"

**Questão**: Qual é o commit absoluto que INTRODUZ "DESI" pela primeira vez (não just o que o contém)?

**Por que P0**: Rastreabilidade cronológica depende de haver um "primeiro" bem-definido.

**Status**: ⚠️ **TOKEN_VAZIO** — temos hash 207013741... mas requer análise de diff

**Comando para resolver**:
```bash
git show 207013741ac55db5a1bc6f3d61f72c4d31791c47 | grep -A5 -B5 "DESI" | head -20
# Mostrar contexto da introdução
```

**Próximo passo**: Analisar diffs de cada commit para encontrar o que adiciona "DESI" pela primeira vez

---

### Gap 3: Validação χ² Contra DESI DR2 Real

**Questão**: Qual é o χ² real (não marginal, não aproximado) do RLL vs. ΛCDM comparando contra dados DESI DR2 brutos?

**Por que P0**: Afirmação central do modelo é que reproduz observações; isso requer cálculo concreto.

**Status**: ⚠️ **TOKEN_VAZIO** — scripts existem, execução completa não documentada

**Arquivo relevante**: `scripts/rll_vs_lcdm.py`

**Comando para resolver**:
```bash
python3 scripts/rll_vs_lcdm.py \
  --bao data/real/cosmology/desi_dr2_bao_primary_points.csv \
  --adversary both --h0 67.4 --omega-m 0.315 \
  --omega-s0 0.05 --zt 0.8 --wt 0.3 \
  --out-json results/rll_vs_lcdm_final.json
```

**Próximo passo**: Executar e documentar resultado (χ² RLL vs. χ² ΛCDM)

---

## P1: Alto Impacto em Confiança

### Gap 4: Origem de Constantes (H₀, Ωm, etc.)

**Questão**: De onde vieram os valores iniciais H₀, Ωm, Ωb, Ωr?

**Por que P1**: Determina se modelo é baseado em literatura padrão ou escolhas ad hoc.

**Status**: ⚠️ **TOKEN_VAZIO** — provavelmente Planck 2018, mas não documentado

**Fontes candidatas**:
- Planck 2018 + WMAP + Baryon Acoustic Oscillations (BAO)
- SH0ES (H₀ local)
- Compilation Moresco 2023

**Próximo passo**: Citar fonte explícita no código (comments) e documentação

---

### Gap 5: Autoridade das Equações (Reformulação vs. Original)

**Questão**: As equações do RLL são originalmente derivadas pelo autor, ou reformulação de trabalhos publicados?

**Por que P1**: Determina precedência científica e inovação.

**Status**: ⚠️ **TOKEN_VAZIO** — sem citação de trabalho anterior similar

**Possibilidades**:
- Extensão original de Friedmann (mais provável)
- Inspiração em f(R) gravity ou Finsler (menos provável)
- Reformulação de trabalho anterior não citado (improvável mas TOKEN_VAZIO)

**Próximo passo**: Comparação explícita com f(R), Finsler, EDE em literatura revisada por pares

---

### Gap 6: Correlação de Parâmetros (zt, wt, Ωs0)

**Questão**: Os parâmetros (zt=1.0, wt=0.3, Ωs0=0.02) têm justificativa física ou são ajustes?

**Por que P1**: Determina se modelo é mecanístico (parâmetros têm significado) ou fenomenológico.

**Status**: ⚠️ **TOKEN_VAZIO** — não há derivação teórica clara de "por que esses valores"

**Possível justificativa**:
- zt ~ redshift de equivalência matéria/radiação? Não documentado.
- wt ~ escala de transição Hubble? Não documentado.
- Ωs0 ~ fração observada de "setor novo"? Requer validação DESI.

**Próximo passo**: Investigar se há motivação teórica nos papers anteriores de Rafael

---

## P2: Médio Impacto em Robustez

### Gap 7: Reprodução de Gráficos Numéricos

**Questão**: Os valores de H(z), σ8(z), etc. nos gráficos coincidem com os calculados pelos notebooks?

**Por que P2**: Afeta precisão da apresentação, não do modelo per se.

**Status**: ⚠️ **TOKEN_VAZIO** — gráficos .png existem, mas origem (hand-drawn vs. gerada) não documentada

**Próximo passo**: Comparar outputs de nbconvert com .png pixel-by-pixel

---

### Gap 8: Performance em Diferentes Ambientes

**Questão**: O modelo e scripts executam em Termux ARM32, colab, servidor standard?

**Por que P2**: Afeta replicabilidade pelos usuários.

**Status**: ⚠️ **TOKEN_VAZIO** — executável em x86, ARM32 não testado

**Próximo passo**: Testar em Termux e documentar incompatibilidades

---

## P3: Baixo Impacto Prático

### Gap 9: Documentação de Commits Antigos

**Questão**: Commits anteriores a v1.0.0 têm histórico documentado?

**Por que P3**: Afeta história de projeto, não validação científica.

**Status**: ⚠️ **TOKEN_VAZIO** — shallow clone, histórico anterior desconhecido

**Nota**: Não é crítico para auditoria, mais para "background".

---

## Plano de Resolução Proposto

| Gap | P | Resolução | Responsável | Prazo |
|-----|---|-----------|-------------|-------|
| Reprodutibilidade notebooks | P0 | Executar nbconvert + documentar | user | semana 1 |
| Primeiro commit DESI exact | P0 | Analisar diffs de commit | user | semana 1 |
| χ² real DESI | P0 | Rodar scripts, capturar JSON | user | semana 2 |
| Origem constantes | P1 | Citar fonte em código | user | semana 1 |
| Autoridade equações | P1 | Comparar com f(R), Finsler | user | semana 3 |
| Justificativa parâmetros | P1 | Investigar papers anteriores | user | semana 2 |
| Gráficos numéricos | P2 | Comparar pixel-level | automation | semana 3 |
| Performance ARM32 | P2 | Testar em Termux | user | semana 4 |
| Histórico antigo | P3 | Documentar se possível | user | semana 4+ |

---

## GAPS RESOLVIDOS — Fase 4 (2026-07-06)

### Gap G0: Pantheon+SH0ES ausente do pipeline RLL → FECHADO [E]

**Questão original**: χ² do RLL contra dataset Pantheon+ SNe Ia não calculado.

**Status**: ✅ **FECHADO** — `docs/cronologia-auditoria/09_PANTHEON_RESULTADO_REAL.md`

**Resultado real**:
| Modelo | χ² | AIC | ΔAIC vs ΛCDM |
|--------|-----|-----|-------------|
| ΛCDM (k=2) | 710.808 | 714.808 | — |
| CPL (k=4) | 710.390 | 718.390 | +3.582 |
| RLL original (k=4) | 710.613 | 718.613 | +3.805 |
| RLL Opção A (k=4) | 710.613 | 718.613 | +3.805 |

N=1624 SNe cosmológicas. Ratio RLL_original/RLL_optionA = 1.0000 (degenerados em Pantheon+).

**Classificação**: [E] cálculo direto contra dado observacional real.

**Scripts**: `scripts/pantheon/load_pantheon.py`, `models_pantheon.py`, `run_rll_vs_pantheon.py`  
**Dados**: `validacao_real/data/pantheon_data.dat` (1702 linhas, 1624 amostra cosmológica)  
**Resultado**: `results/pantheon_plus_resultado_real.txt`

---

---

## GAPS ATUALIZADOS — Fase 7 (2026-07-07)

### Gap P0-3 (χ² DESI Real): PRONTO PARA EXECUÇÃO

**Status anterior**: ⚠️ TOKEN_VAZIO — scripts existem, execução completa não documentada

**Status atual**: ⏳ **PRONTO PARA EXECUÇÃO** — pipeline `rll-validacao-cientifica-completa.yml` existe (PR #506 merged)

**Para fechar**: Disparar o workflow em GitHub Actions → modo=completo. Job `fit_desi_bao` calcula χ² com parâmetros otimizados. Job `joint_mcmc_p0` fecha o joint MCMC P0.

**Referência**: `.github/workflows/rll-validacao-cientifica-completa.yml` (11 jobs, PR #506)

---

### Gap G1: Pipeline Joint MCMC — Primeiro Run Pendente [NOVO P0]

**Questão**: Qual é o χ² RLL real com parâmetros otimizados conjuntamente (Pantheon+ + DESI BAO)?

**Por que P0**: O joint MCMC é o teste definitivo da viabilidade do modelo — sem ele, não há afirmação de superioridade sobre ΛCDM com parâmetros livres.

**Status**: ⚠️ **TOKEN_VAZIO P0** — pipeline existe (Job 6: `joint_mcmc_p0`), primeiro run não executado

**Para fechar**:
```bash
# GitHub Actions → rll-validacao-cientifica-completa → Run workflow
# Inputs: modo=completo, commit_resultados=true
# Job joint_mcmc_p0 usa: python -m data.pipelines.structure_d.run_all \
#   --profile structure_d_real_validation --bayes --bayes-mode inference \
#   --bayes-nwalkers 32 --bayes-nsteps 1000
```

**Resultado esperado**: `results/ci/joint_mcmc_*/joint_mcmc_summary.json` com posteriors {H₀, Ωm, Ωs0, z_t, w_t}

---

### Gap G2: Fator de Bayes RLL/ΛCDM [NOVO P0]

**Questão**: ln(B₁₀) RLL vs ΛCDM — positivo, negativo, ou inconclusivo?

**Por que P0**: Falsificador F-COS-04 ainda TOKEN_VAZIO. Sem Bayes Factor, não há resposta à pergunta "o RLL é preferido Bayesianamente?"

**Status**: ⚠️ **TOKEN_VAZIO P0** — Job 7 (`bayes_factor_p0`) no pipeline; aguarda primeiro run

**Para fechar**: Mesmo run do Gap G1. Job `bayes_factor_p0` depende de `joint_mcmc_p0`.

---

### CONTRATO_FALSIFICADORES — Baseline Estático Criado [FASE 7]

**Status**: ✅ `docs/cronologia-auditoria/CONTRATO_FALSIFICADORES_RLL.md` criado como baseline estático

**Valores conhecidos (pré-CI)**:
- F-COS-01: ✅ PASS — ΔAIC=3.805 (resultados/pantheon_plus_resultado_real.txt)
- F-COS-02: ✅ PASS — χ²_red=0.4386 (710.613/1620)
- F-COS-05: ✅ PASS — χ²_DESI_nominal=93.81 < 150

**Valores TOKEN_VAZIO (aguardam pipeline)**:
- F-COS-03: z_t scan — aguarda Job 5 (`zt_falsification`)
- F-COS-04: ln(B₁₀) — aguarda Job 7 (`bayes_factor_p0`)

---

## GAPS RESOLVIDOS — FASE 11 (2026-07-07)

### Gap H1-WEFF: Opção B numericamente testada → FECHADO [E]

**Questão original**: Setor DE puro com dois estados logisticamente interpolados poderia compatibilizar w_eff com CPL DESI?

**Status**: ✅ **EXECUTADO** — `scripts/verify_weff_opcao_b.py` — scan 36 combinações (w2, w_t)

**Resultado**: Melhor χ²=14.8 (w2=−0.5, w_t=0.5). Não passa threshold<10, mas melhora drasticamente vs padrão (1162.3) e Opção A (2232.2). w_eff sempre negativo ✅.

**Implicação**: Opção B é a variante mais promissora. Otimização contínua pode cruzar χ²<10 (TOKEN_VAZIO P1 acionável).

---

### Gap H2-WEFF: Opção C numericamente testada → FECHADO [E]

**Status**: ✅ **EXECUTADO** — `scripts/verify_weff_opcao_c.py` — scan 35 combinações (α, r)

**Resultado**: Melhor χ²=104.0 (α=0.5, r=0.05). Opção C inferior à Opção B; espaço (α,r) com z_t fixo é insuficiente.

---

### Gap P0 PRED: Predição datada RLL → FECHADA [C]

**Status**: ✅ **CRIADO** — `docs/canonicos/PREDICAO_DATADA_RLL.md`

**Predições registradas** (antes de DESI DR3 e Euclid DR1):
- P-RLL-01: w_eff > 0 em z~0.7–1.3 (setor padrão) — disfavorecida por DR2, distinguível futuramente
- P-RLL-02: Transição E(z) em z~1.0 — aguarda MCMC (G1)
- P-RLL-03: Ωs0 < 0.05 — aguarda MCMC (G1)
- P-RLL-04: Degeneração padrão/Opção A ✅ verificada em FASE 4
- P-RLL-05: Opção B cruzará χ²<10 com otimização — pendente

---

### Gap P1-WEFF-B-OPT: Otimização contínua Opção B [NOVO P1]

**Questão**: Um scipy.minimize sobre (z_t, w2, w_t) pode levar χ²_Opção_B abaixo de 10?

**Por que P1**: χ²=14.8 no scan discreto é ~50% acima do threshold. Otimização contínua é acionável sem dados externos.

**Como fechar**: Criar `scripts/optimize_weff_opcao_b.py` com `scipy.optimize.minimize(chi2_b, x0=[1.0, -0.5, 0.5], bounds=[(0.3,1.5),(-0.95,-0.05),(0.1,0.8)], method='L-BFGS-B')`

**Status**: ⚠️ **TOKEN_VAZIO P1** — scan feito, otimização pendente

---

## Conclusão (atualizada FASE 11)

**Token Total**: 9 gaps originais + G0/G1/G2 + novos FASE 11
**P0 (bloqueador)**: G1 (MCMC joint) + G2 (Bayes Factor) — ambos requerem pipeline manual
**P1 (confiança)**: 3 originais + Gap 6 (justificativa parâmetros) + P1-WEFF-B-OPT
**P2 (robustez)**: 2 originais
**P3 (polish)**: 1 original

**Fechados**:
- G0 Pantheon+: ✅ FASE 4
- H1-WEFF (Opção B): ✅ FASE 11 — χ²=14.8, melhora estrutural confirmada
- H2-WEFF (Opção C): ✅ FASE 11 — χ²=104.0, Opção C inferior
- Predição datada: ✅ FASE 11 — 5 predições registradas em `PREDICAO_DATADA_RLL.md`

**Pendentes (requerem ação)**:
- G1 (Pipeline MCMC): Disparar `rll-validacao-cientifica-completa.yml` modo=completo
- G2 (Bayes Factor): Idem (Job 7)
- P1-WEFF-B-OPT: Criar e rodar `scripts/optimize_weff_opcao_b.py`
- Gap 6 (justificativa parâmetros): Ver `docs/canonicos/JUSTIFICATIVA_PARAMETROS_RLL.md` (FASE 12)

**Método**: TOKEN_VAZIO preserva honestidade enquanto trabalho prossegue.

---

*"Lacuna marcada vira ciência. Lacuna ocultada vira propaganda." — RAFAELIA*
