# RLL — Inspection Rate Math and Knowledge Test

**Status:** métrica de inspeção científico-operacional para Structure-D/RLL.  
**Escopo:** calcula noção quantitativa de prontidão, conhecimento documentado, operação executável, controle de risco e risco residual.  
**Regra:** esta métrica é governança diagnóstica; não é resultado cosmológico e não autoriza `claim_allowed=true`.

---

## 1. Por que isto existe

O repositório já possui muitos objetos diferentes:

```text
resultado canônico
claim gate
wrapper seguro
CI corrigido
dinâmica efetiva
ablações documentadas
robust fit pendente
posterior pendente
Pantheon+/CMB/growth pendentes
```

Sem uma taxa de inspeção, esses objetos ficam qualitativos. A taxa de inspeção cria uma noção objetiva de:

```text
o que existe
o que só está documentado
o que executa
o que tem teste
o que ainda é TOKEN_VAZIO
o que é risco crítico se for afirmado cedo demais
```

---

## 2. Arquivos criados

| Arquivo | Função |
|---|---|
| `data/inputs/structure_d_inspection/inspection_items.json` | ledger ponderado de itens a inspecionar |
| `scripts/analysis/structure_d_inspection_rate.py` | calculadora da taxa de inspeção |
| `tests/test_structure_d_inspection_rate.py` | testes matemáticos da fórmula |

---

## 3. Fórmula principal

Cada item recebe quatro dimensões:

| Dimensão | Intervalo | Significado |
|---|---:|---|
| `evidence` | 0 a 1 | quanto existe de evidência/documentação/artefato |
| `operation` | 0 a 1 | quanto está executável/testado/verificado |
| `risk_control` | 0 a 1 | quanto há gate, trava, checklist ou proteção |
| `risk_severity` | 0 a 1 | gravidade se o item for mal interpretado |

A nota de inspeção do item é:

```math
S_i = 100\times(0.40E_i + 0.35O_i + 0.25C_i)
```

onde:

```text
E_i = evidence
O_i = operation
C_i = risk_control
```

A taxa global de inspeção é uma média ponderada:

```math
IR = \frac{\sum_i w_i S_i}{\sum_i w_i}
```

O risco residual ponderado é:

```math
RE = 100\times\frac{\sum_i w_i R_i (1-S_i/100)}{\sum_i w_i R_i}
```

onde:

```text
w_i = peso do item
R_i = risk_severity
```

---

## 4. Interpretação da taxa

| Taxa | Classe | Leitura |
|---:|---|---|
| `>=85` | `operational_high_confidence` | alto grau de inspeção, ainda não claim cosmológico |
| `70–84` | `operational_but_needs_hardening` | operacional, mas precisa endurecer |
| `50–69` | `partial_inspection` | existe estrutura parcial |
| `30–49` | `early_scaffold` | estrutura inicial, lacunas fortes |
| `<30` | `critical_gap` | risco alto / pouca inspeção |

---

## 5. Matemática aplicada ao conhecimento

Esta métrica separa três coisas que costumam ser misturadas:

### 5.1 Conhecimento

```math
KR = 100\times\frac{\sum_i w_i E_i}{\sum_i w_i}
```

Mostra quanto do sistema está documentado, materializado ou evidenciado.

### 5.2 Operação

```math
OR = 100\times\frac{\sum_i w_i O_i}{\sum_i w_i}
```

Mostra quanto do sistema pode realmente ser executado/testado.

### 5.3 Controle de risco

```math
CR = 100\times\frac{\sum_i w_i C_i}{\sum_i w_i}
```

Mostra quanto há de trava contra erro, overclaim, sobrescrita ou falsa conclusão.

---

## 6. Comando de uso

```bash
python scripts/analysis/structure_d_inspection_rate.py
```

Saídas esperadas:

```text
results/structure_d/inspection/structure_d_inspection_rate_items.csv
results/structure_d/inspection/structure_d_inspection_rate_categories.csv
results/structure_d/inspection/structure_d_inspection_rate_manifest.json
```

---

## 7. Como ler o resultado

Se a taxa de conhecimento for alta, mas a operação for baixa:

```text
há muita documentação, mas pouca execução
```

Se a operação for alta, mas o controle de risco for baixo:

```text
há execução perigosa
```

Se o controle de risco for alto, mas a evidência/operação forem baixas:

```text
há TOKEN_VAZIO protegido corretamente
```

Se o risco residual for alto:

```text
não usar como claim; priorizar na próxima rodada
```

---

## 8. Exemplos de leitura no RLL atual

| Item | Leitura provável |
|---|---|
| smoke canônico | existe e é auditável, mas não final |
| claim gate | forte, protege contra overclaim |
| output stem wrapper | mitiga sobrescrita canônica |
| CI fix | corrigido, mas precisa confirmação de PASS |
| effective dynamics | implementado, precisa execução dos derivados |
| robust fit | lacuna crítica |
| posterior | lacuna crítica |
| GEDE baseline | lacuna de fronteira |
| Pantheon+/CMB/growth | lacunas de dataset/backend |

---

## 9. O que esta taxa não significa

Não significa:

```text
RLL venceu
RLL está confirmado
RLL resolve energia escura
RLL resolve H0/S8
```

Significa:

```text
temos uma métrica de inspeção da maturidade científico-operacional do pipeline
```

---

## 10. Testes matemáticos adicionados

O arquivo:

```text
tests/test_structure_d_inspection_rate.py
```

cobre:

```text
fórmula do item_score
média ponderada
risco residual
agrupamento por categoria
validação de scores fora de [0,1]
escrita de CSV/manifesto
claim_allowed=false no manifesto
```

---

## 11. R3

```text
F_ok   = taxa de inspeção criada com ledger, script e testes matemáticos.
F_gap  = outputs ainda precisam ser gerados por execução local/CI.
F_next = executar a calculadora e usar o risco residual para priorizar robust fit, posterior, GEDE, Pantheon+, CMB e growth backend.
```
