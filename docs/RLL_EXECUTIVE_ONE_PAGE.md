# RLL — Executive One Page

**Status:** síntese executiva conservadora para leitura rápida.  
**Escopo:** resumo do estado atual; não altera dados, fórmulas, resultados ou claims.

---

## 1. O que é o RLL neste repositório

O `relativity-living-light` contém um framework de pesquisa para transformar a hipótese RLL em objeto computacional auditável. O repositório separa:

- hipótese e motivação;
- modelo executável;
- dados reais e sintéticos;
- métricas de comparação;
- lacunas explícitas;
- gates de claim científico.

A tese operacional atual não é “RLL está confirmado”.

A tese segura é:

> RLL é uma hipótese cosmológica fenomenológica testável, com pipeline reprodutível em desenvolvimento e comparação contra LCDM, wCDM e CPL/w0waCDM.

---

## 2. Resultado atual

O artefato canônico atual compara quatro modelos:

| Modelo | Estado no smoke atual |
|---|---|
| LCDM | baseline |
| wCDM | melhora pouco chi2, mas piora critérios de informação |
| CPL/w0waCDM | preferido no smoke atual |
| RLL | não preferido; `Os0=0.0` desativa camada RLL |

A execução atual usa `maxiter=3`, portanto é um smoke/sanity test. Ela prova que o pipeline roda e gera comparação auditável; não prova ranking cosmológico final.

---

## 3. Por que isso é valioso

O valor principal do repositório é metodológico e científico-operacional:

1. hipótese convertida em cálculo;
2. comparação com baselines adequados;
3. uso de critérios de informação;
4. separação real/sintético;
5. documentação de lacunas;
6. política explícita de claims permitidos/proibidos;
7. preservação de `TOKEN_VAZIO` em vez de inferência falsa.

---

## 4. O que ainda falta

| Lacuna | Estado |
|---|---|
| robust fit com seeds e maxiter maior | `TOKEN_VAZIO_ROBUST_FIT` |
| Pantheon+ completo | `TOKEN_VAZIO_DATASET` |
| CMB compressed covariance completa | `TOKEN_VAZIO_COVARIANCE` |
| growth externo CLASS/CAMB | `TOKEN_VAZIO_BACKEND` |
| posterior/MCMC/nested sampling | `TOKEN_VAZIO_POSTERIOR` |
| output versionado para robust fit | `TOKEN_VAZIO_CLI_OUTPUT_STEM` |

---

## 5. Claims seguros hoje

Permitido dizer:

- o pipeline existe;
- RLL é candidato testável;
- CPL é o adversário técnico principal no estado atual;
- o resultado atual é preliminar;
- claims fortes estão corretamente bloqueados.

Não permitido dizer:

- RLL venceu;
- RLL está confirmado;
- RLL resolve energia escura;
- RLL resolve H0/S8;
- RLL substitui LCDM/CPL.

---

## 6. Próximo ato correto

Antes de rodar robust fit, corrigir ou contornar o output stem para impedir sobrescrita dos resultados canônicos.

Depois disso:

1. executar seeds 1..10 com `maxiter>=100`;
2. gerar tabela robusta;
3. rodar ablações;
4. comparar `w_eff_RLL(z)` contra `w_CPL(z)`;
5. completar Pantheon+/CMB/growth;
6. só então reavaliar claim.

---

## 7. Frase executiva

> O RLL ainda não é uma cosmologia comprovada; mas o repositório já é uma infraestrutura séria para testar, falsificar, comparar e proteger a hipótese contra overclaim.

---

## 8. R3

```text
F_ok   = síntese executiva criada; valor e limite do estado atual expressos em uma página.
F_gap  = faltam robust fit, datasets/backends completos e posterior.
F_next = criar risk register científico-operacional.
```
