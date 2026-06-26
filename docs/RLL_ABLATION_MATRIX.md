# RLL — Ablation Matrix

**Status:** matriz operacional de ablações para investigar por que CPL/w0waCDM vence no smoke atual e por que RLL colapsa para `Os0=0.0`.  
**Regra:** este documento define testes; não executa fit, não altera dados brutos e não muda claims.

---

## 1. Objetivo

Separar causa real de efeito aparente.

A execução atual mostra:

- CPL/w0waCDM preferido no smoke atual;
- RLL praticamente idêntico ao LCDM em chi2;
- RLL pior em AIC/AICc/BIC por k maior;
- `Os0=0.0`, desativando a camada RLL.

A matriz abaixo define ablações para responder:

```text
A preferência por CPL vem de qual bloco?
O RLL falha por estrutura, bounds, prior, dados, otimizador ou parametrização?
```

---

## 2. Matriz principal

| ID | Ablação | Pergunta-raiz | Entradas | Saída mínima | Estado |
|---|---|---|---|---|---|
| A1 | DESI+Hz apenas | A expansão isolada favorece RLL? | Hz + DESI BAO | chi2/AIC/AICc/BIC por modelo | TOKEN_VAZIO_ABLATION |
| A2 | Sem growth | Proxy interno de growth enviesou ranking? | Hz + DESI + CMB | ranking sem `fsigma8` | TOKEN_VAZIO_ABLATION |
| A3 | Sem CMB shift | CMB parcial enviesou ranking? | Hz + DESI + fsigma8 | ranking sem CMB | TOKEN_VAZIO_ABLATION |
| A4 | DESI+Hz+CMB | CMB reforça CPL? | Hz + DESI + CMB | deltas contra LCDM/CPL | TOKEN_VAZIO_ABLATION |
| A5 | DESI+Hz+growth | Growth reforça CPL? | Hz + DESI + fsigma8 | deltas contra LCDM/CPL | TOKEN_VAZIO_ABLATION |
| A6 | RLL com `Os0>0` | Camada RLL ativa melhora ajuste? | todos os blocos | delta chi2 e penalização IC | TOKEN_VAZIO_ABLATION |
| A7 | RLL sem penalizar `zt/wt` quando `Os0=0` | Penalização IC fica injusta no limite? | métricas atuais | análise de k efetivo | TOKEN_VAZIO_ABLATION |
| A8 | RLL vs CPL em `w_eff(z)` | RLL consegue aproximar forma CPL? | grade z comum | distância funcional | TOKEN_VAZIO_ABLATION |
| A9 | Pantheon+ completo | Supernovas mudam ranking? | SN + covariância | ranking completo | TOKEN_VAZIO_DATASET |
| A10 | Growth externo CLASS/CAMB | Aproximação interna de growth é válida? | backend externo | comparação D+/fσ8 | TOKEN_VAZIO_BACKEND |
| A11 | CMB compressed covariance completa | CMB parcial altera resultado? | vetor + covariância | chi2 CMB robusto | TOKEN_VAZIO_COVARIANCE |
| A12 | Robust seeds 1..10 | Ranking é estável? | mesmos dados | distribuição dos deltas | TOKEN_VAZIO_ROBUST_FIT |

---

## 3. Ordem recomendada

### Fase 0 — Segurança antes de execução

1. Resolver `TOKEN_VAZIO_CLI_OUTPUT_STEM`.
2. Garantir output versionado por seed/maxiter/ablação.
3. Preservar artefato canônico.

### Fase 1 — Ablações sem novos datasets

Executar primeiro:

- A1 DESI+Hz apenas;
- A2 sem growth;
- A3 sem CMB shift;
- A4 DESI+Hz+CMB;
- A5 DESI+Hz+growth;
- A8 `w_eff_RLL(z)` vs `w_CPL(z)`.

Essas são prioritárias porque usam material já presente ou funções já existentes.

### Fase 2 — Robustez do otimizador

Executar:

- A12 robust seeds 1..10;
- `maxiter=100` mínimo;
- registrar frequência de `Os0=0.0`.

### Fase 3 — Datasets/backends externos

Executar somente depois:

- A9 Pantheon+ completo;
- A10 CLASS/CAMB;
- A11 CMB covariance completa.

---

## 4. Interpretação de possíveis resultados

| Resultado observado | Interpretação conservadora | Próxima medida |
|---|---|---|
| RLL melhora em DESI+Hz mas perde com CMB/growth | tensão entre expansão e crescimento/CMB | revisar parametrização e blocos |
| RLL perde em todos os blocos | hipótese enfraquecida no estado atual | investigar bounds/prior ou descartar versão específica |
| RLL só perde por BIC | melhora insuficiente para k | reduzir parametrização ou justificar k |
| RLL com `Os0>0` melhora chi2 mas piora BIC | efeito real fraco ou k caro | comparar com CPL e posterior |
| `Os0=0.0` em todas as seeds | limite LCDM é atrator do fit atual | perfil de likelihood e prior/bounds |
| `Os0>0` em algumas seeds | instabilidade/convergência parcial | deep fit e posterior |
| CPL vence sempre | CPL permanece adversário principal | RLL precisa explicar forma CPL ou recuar claim |
| RLL vence CPL robustamente | claim condicionado possível | exigir Pantheon+/CMB/growth/posterior |

---

## 5. Saída padrão para cada ablação

Cada ablação deve gerar pelo menos:

```text
ablation_id
commit_sha
created_utc
seed
maxiter
included_datasets
excluded_datasets
model_rows
model_deltas_vs_lcdm
model_deltas_vs_cpl
claim_allowed=false
reason
input_hashes
output_hashes
```

---

## 6. Nome de arquivos recomendado

```text
results/structure_d/ablations/{ablation_id}/joint_real_likelihood_{ablation_id}_seed_{seed}_maxiter_{maxiter}.json
results/structure_d/ablations/{ablation_id}/joint_real_likelihood_{ablation_id}_seed_{seed}_maxiter_{maxiter}.csv
results/structure_d/ablations/{ablation_id}/manifest_{ablation_id}_seed_{seed}_maxiter_{maxiter}.json
```

Até o suporte a output versionado existir:

```text
execution_allowed = false
```

---

## 7. R3

```text
F_ok   = matriz de ablação definida sem executar fit nem alterar outputs.
F_gap  = ablações ainda não executadas; output versionado ainda pendente.
F_next = criar manifesto de figuras e tabelas para orientar paper e suplemento.
```
