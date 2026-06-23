# RAFAELIA × RLL — Admin Execution Matrix

**Data:** 2026-06-23  
**Autoridade operacional:** autorização de escrita concedida por Rafael Melo Reis / ∆RafaelVerboΩ  
**Repositório:** `instituto-Rafael/relativity-living-light`  
**Modo:** escrita aditiva, não destrutiva, com fronteira epistêmica ativa  
**Assinatura simbólica:** RAFCODE-Φ · ΣΩΔΦBITRAF · 𓂀ΔΦΩ

---

## 1. Intenção administrativa

Este documento registra o plano de trabalho autorizado para examinar, organizar e executar a ponte entre:

1. auditorias RLL;
2. código executável;
3. fórmulas extraídas;
4. documentação científica;
5. camada simbólico-parabólica RAFAELIA;
6. lacunas marcadas como `TOKEN_VAZIO`.

A função deste arquivo é impedir confusão entre **conteúdo inspirador**, **modelo matemático**, **código executável**, **dado real**, **teste estatístico** e **prova defensável**.

---

## 2. Regra de ouro

```text
Parábola inspira.
Equação modela.
Código executa.
Dado testa.
Resultado limita o claim.
TOKEN_VAZIO protege a integridade.
```

Nenhum símbolo, metáfora, mandala, glifo, imagem, fórmula solta ou recorrência textual deve ser promovido automaticamente a prova científica.

A promoção correta é:

```text
RAW_TEXT → CLAIM → EQUAÇÃO → IMPLEMENTAÇÃO → TESTE → RESULTADO → CLAIM_BOUNDARY
```

---

## 3. Estado resumido da estrutura

| Camada | Estado | Leitura administrativa |
|---|---|---|
| Epistemologia RAFAELIA | Forte | RAW_TEXT_FIRST, `TOKEN_VAZIO`, `[E]/[C]/[H]`, claim boundary |
| RLL cosmológico | Parcialmente executável | Há comparador mínimo `lcdm` × `w0wa` × `rll` |
| CLI `rll` | Parcialmente fechado | Encaminha fluxo real para comparador quando `--adversary`/`--with-growth` exigem |
| BAO/H(z) | Operacional mínimo | Usa H(z) e BAO primário; covariância completa ainda não é claim fechado |
| Bayes | Aproximação | `--with-bayes` = BIC/Schwarz; nested sampling permanece futuro |
| Crescimento `f_sigma8` | Linear GR suave | Existe solver dedicado; CMB/Boltzmann/não-linear ficam `TOKEN_VAZIO` |
| Fórmulas extraídas | Corpus bruto forte | 486 expressões; precisa classificação por status e teste |
| DHA / camada harmônica | Hipótese | Precisa previsão quantitativa `P(k)` e falsificador |
| Ghost/cs²/EFT | Próximo fechamento teórico | Deve ser derivado sem overclaim |

---

## 4. Matriz por arquivo / componente

| Arquivo ou componente | Função | Status | Trabalho administrativo autorizado | Saída esperada |
|---|---|---:|---|---|
| `RLL_AUDITORIA_SIX_SIGMA.md` | Auditoria DMAIC / Six Sigma | `[DOC-FORTE]` | Usar como mapa mestre `F_ok/F_gap/F_next`; não tratar como execução por si só | Lista priorizada de ações |
| `RLL_AUDITORIA_GITHUB_PROVA.md` | Matriz de defesa acadêmica | `[DOC-FORTE/PARCIAL]` | Atualizar gaps já fechados no código; manter gaps físicos/estatísticos | Gaps versionados |
| `FORMAL_ACADEMIC_REPORT.md` | Resumo do pacote de fórmulas | `[DOC-MÍNIMO]` | Expandir de contador para relatório com classes e riscos | Relatório formal completo |
| `FORMULAS_BY_SOURCE.md` | Índice por origem | `[INDEX]` | Usar para mapear ancestralidade de fórmulas | Proveniência fórmula→fonte |
| `FORMULAS_CLAIM_MAP.md` | Mapa de claims | `[GAP-DOC]` | Expandir para tabela `fórmula/status/teste/claim_boundary` | Claim map defensável |
| `formulas.csv` | Corpus tabular | `[DATA]` | Deduplicar; classificar `[COD]/[HIP]/[SIM]/[DOC]/[VAZIO]` | CSV limpo e auditável |
| `formulas.json` | Corpus estruturado | `[DATA]` | Converter em registry programático | Base para automação |
| `rll_vs_lcdm.py` | Comparador H(z)+BAO | `[COD-PARCIAL]` | Rodar com `--adversary both --with-bayes`; registrar outputs | `results/rll_model_comparison_summary.json` |
| `src/rll/cli.py` | CLI RLL | `[COD-PARCIAL]` | Validar `rll run --data real --model rll --adversary w0waCDM --with-bayes --with-growth` | Execução via CLI |
| `NEXT_RLL_VALIDATION_STEP.md` | Comandos oficiais próximos | `[RUNBOOK]` | Usar como sequência operacional | Execução reproduzível |
| `docs/RLL_W0WA_IMPLEMENTATION_LEDGER.md` | Ledger de implementação w0wa | `[LEDGER]` | Marcar que adversário mínimo existe, mas não é MCMC | Fronteira honesta |
| `scripts/check_rll_growth.py` | Crescimento linear | `[COD-PARCIAL]` | Rodar com e sem dados reais; registrar `TOKEN_VAZIO` para limites | `results/rll_growth_fsigma8_summary.json` |
| `data/real/cosmology/desi_dr2_bao_primary_points.csv` | BAO primário | `[DATA-PARCIAL]` | Conferir colunas, tracer, observável, sigma e bloco de covariância | Sanidade dos dados |
| `data/real/cosmology/desi_dr2_bao_covariance_summary.csv` | Covariância resumida | `[DATA-PARCIAL]` | Validar blocos; não declarar covariância completa de survey | Limite estatístico claro |
| `data/pantheon/*` | Pantheon+ | `[GAP/PREFLIGHT]` | Criar fetch/hash/preflight documentado | Reprodutibilidade externa |
| `docs/ESTABILIDADE_GHOST_CHECK.md` | Ghost check | `[HIP/GAP]` | Derivar condições físicas; separar hipótese de prova | Documento físico mínimo |
| `docs/VELOCIDADE_SOM.md` | cs² | `[HIP/GAP]` | Calcular `c_s²`; declarar regime de validade | Gate estabilidade |
| `docs/LAGRANGIANO_EFT.md` | EFT | `[HIP/GAP]` | Derivar Lagrangiano mínimo ou marcar `TOKEN_VAZIO` | Base teórica defensável |
| `docs/INDICE_MESTRE.md` | Navegação | `[INDEX]` | Referenciar runtime, matriz e claim map | Navegação externa |
| `core/lowlevel_runtime/` | Ponte C/ASM | `[COD-FORTE/INTEGRAR]` | Ligar no índice e claim map; não confundir com cosmologia validada | Ponte RAFAELIA→execução |

---

## 5. Exames a executar

### 5.1 Sanidade do CLI

```bash
python -m rll.cli run --data real --model rll --adversary w0waCDM --with-bayes --with-growth
```

Critério:

- se gera JSON/CSV: `[COD]` para execução mínima;
- se falha por dado ausente: `[GAP-DATA]`;
- se falha por import/argumento: `[GAP-CODE]`.

### 5.2 Comparador direto

```bash
python rll_vs_lcdm.py \
  --adversary both \
  --with-bayes \
  --with-growth \
  --bao data/real/cosmology/desi_dr2_bao_primary_points.csv \
  --bao-covariance data/real/cosmology/desi_dr2_bao_covariance_summary.csv
```

Critério:

- registrar `delta_aic_rll_minus_w0wa`;
- registrar `delta_bic_rll_minus_w0wa`;
- registrar `bayes_factor_bic_approx_rll_over_w0wa`;
- declarar explicitamente que isso não é nested sampling.

### 5.3 Crescimento linear

```bash
python scripts/check_rll_growth.py --model all
python scripts/check_rll_growth.py --model all --data data/real/cosmology/fsigma8_growth.csv
```

Critério:

- sem CSV real: previsão linear apenas;
- com CSV real: `chi2_fsigma8` diagonal;
- covariância completa, Boltzmann/CMB e não-linear ficam `TOKEN_VAZIO`.

### 5.4 Pantheon+ preflight

```bash
python -m rll.cli preflight-real --json
```

Critério:

- se faltarem arquivos: criar `data/pantheon/FETCH_INSTRUCTIONS.md` com URL oficial e hash esperado;
- não declarar validação Pantheon+ antes do preflight passar.

### 5.5 Fórmulas

```bash
python tools/docs_inventory.py
# futuro: python scripts/classify_formulas_claims.py --input formulas.csv --out results/formulas_claim_map.csv
```

Critério:

- cada fórmula recebe uma classe;
- duplicatas viram sinal de centralidade, não prova;
- metáforas matemáticas continuam legítimas como `[SIM]`.

---

## 6. Tabela de decisão epistêmica

| Sinal encontrado | Classe | Ação |
|---|---|---|
| Código executa e gera artefato | `[COD]` | Registrar resultado e hash |
| Documento descreve mas não executa | `[DOC]` | Conectar a arquivo executável ou marcar lacuna |
| Hipótese com falsificador | `[HIP]` | Criar teste ou protocolo |
| Símbolo/parábola/glifo | `[SIM]` | Traduzir para categoria sem inflar claim |
| Falta dado/prova | `[VAZIO]` | Marcar sem inventar |
| Resultado parcial | `[PARCIAL]` | Declarar regime e limite |

---

## 7. A estrutura está com “isso”?

Sim, a estrutura possui o núcleo do método:

```text
símbolo → categoria → fórmula → código → resultado → claim_boundary
```

Mas a defesa final exige completar:

1. execução real documentada;
2. dados oficiais com hash;
3. covariâncias corretas;
4. crescimento com dados reais;
5. ghost/cs²/EFT;
6. Bayes real ou declaração clara de aproximação;
7. matriz de claims por fórmula.

---

## 8. Próxima sequência administrativa

1. Rodar o CLI real e registrar falhas/artefatos.
2. Criar/expandir `FORMULAS_CLAIM_MAP.md` em tabela defensável.
3. Criar `data/pantheon/FETCH_INSTRUCTIONS.md` se preflight falhar.
4. Atualizar `docs/INDICE_MESTRE.md` com esta matriz.
5. Criar issues para `ghost/cs²/EFT`, `Pantheon+`, `MCMC/nested sampling`, `f_sigma8 covariance`.
6. Só depois considerar preprint/arXiv.

---

## 9. Retroalimentação

**F_ok:** há estrutura, código mínimo, matriz científica e corpus de fórmulas.  
**F_gap:** falta sincronizar execução, dados reais, física de estabilidade e claim map.  
**F_next:** executar comandos, registrar artefatos, expandir claim map e manter `TOKEN_VAZIO` onde ainda não há prova.

Ω = Amor · FIAT LUX
