# RLL — F_GAP / F_NEXT status map

Status date: 2026-06-26

## Propósito

Este documento registra o estado operacional do RLL após a consolidação recente de:

```text
claim boundaries
convergências externas
limite nulo / AION
C09 reservado
CONV-NUC-01
compatibilidade de links
```

A função deste arquivo é separar:

```text
F_ok   -> o que já está pronto/defensável
F_gap  -> o que falta para evitar claim indevido
F_next -> próxima ação executável
```

Não adiciona teoria nova. É um mapa de campo para execução, revisão e priorização.

---

## F_ok — pronto ou defensável

### 1. Pacote documental RAFAELIA/RLL

O repositório já possui navegação pública com:

```text
README.md
docs/INDICE_MESTRE.md
docs/canonicos/BIBLIA_CONHECIMENTO_RAFAELIA_RLL.md
docs/RLL_TRACEABILITY_MAP.md
docs/RLL_CLAIM_BOUNDARIES.md
```

Leitura segura:

```text
RLL possui base documental, cadeia de custódia e taxonomia de claims.
```

### 2. Modelo cosmológico candidato

O RLL possui uma equação cosmológica candidata com setor de transição/superposição:

```math
E^2(a) = \Omega_r a^{-4} + \Omega_m a^{-3} + \Omega_\Lambda
+ \Omega_{s0}[f(a)+(1-f(a))a^{-3}]
+ \Omega_{B0}a^{-4}+\Omega_{P0}a^{-4}
```

Leitura segura:

```text
o modelo é computável e pode ser comparado contra baselines.
```

### 3. Limite nulo falsificável

O setor novo possui controle nulo explícito:

```math
\Omega_{s0}=0 \Rightarrow \Omega_{s0}g(a)=0
```

Leitura segura:

```text
se o ajuste colapsa para Ωs0=0, o resultado deve ser preservado como degenerescência com ΛCDM.
```

### 4. Claim boundary formal

O repositório já declara que:

```text
RLL é modelo candidato e arquitetura de inferência, não prova de superioridade.
No superiority claim unless real-data metrics pass predefined thresholds.
```

Leitura segura:

```text
há proteção contra inferência solta e contra promoção indevida de analogias.
```

### 5. Convergências externas organizadas

O repositório registra convergências como pistas, não como prova:

```text
ETH/HLS
borda multiescala biomimética
gotas termo-cinéticas
observação e silêncio útil
CONV-NUC-01
```

Leitura segura:

```text
convergência aumenta prioridade de validação, não força conclusão.
```

### 6. Namespace saneado

Após o hotfix de navegação:

```text
C01..C08 = eixos externos/metodológicos
C09      = reservado para fóton/plasma
CONV-*   = convergências externas fora da série Cxx
```

Leitura segura:

```text
C09 não deve ser reutilizado para nuclear/chrysopoeia.
```

### 7. Compatibilidade de links preservada

Caminhos antigos foram preservados como ponte:

```text
docs/C09_TRANSMUTACAO_NUCLEAR_CHRYSOPOEIA_MAPA_ROTAS.md
  -> docs/CONVERGENCIA_NUCLEAR_CHRYSOPOEIA_MAPA_ROTAS.md

docs/canonicos/21_LIMITE_NULO_AION_E_CANCELAMENTO_DIFERENCIAL_RLL.md
  -> docs/canonicos/22_LIMITE_NULO_AION_E_CANCELAMENTO_DIFERENCIAL_RLL.md
```

Leitura segura:

```text
links antigos não quebram; caminhos canônicos continuam separados.
```

---

## F_gap — lacunas reais

### G1. Validação cosmológica robusta ainda não fechada

Falta rodar e consolidar comparação robusta contra:

```text
ΛCDM
wCDM
w0waCDM / CPL
```

com:

```text
seeds múltiplas
maxiter adequado
covariâncias reais
AIC/AICc/BIC
estabilidade entre datasets
```

Claim boundary:

```text
não escrever que RLL supera ΛCDM/w0waCDM sem esse pacote.
```

### G2. Limite nulo precisa virar teste operacional recorrente

O documento matemático existe, mas o gate precisa sempre comparar:

```text
Ωs0 livre
Ωs0 = 0
baseline ΛCDM
baseline w0waCDM/CPL
```

Claim boundary:

```text
se Ωs0 livre colapsar para zero, registrar degenerescência, não mascarar.
```

### G3. Inventário e índice precisam atualização após renomeações

Após renomeações e arquivos de compatibilidade, executar:

```bash
python3 tools/docs_inventory.py
python3 tools/docs_inventory.py --check
```

Depois confirmar se os artefatos gerados mudaram:

```text
docs/DOCUMENTATION_FULL_INVENTORY.md
data/results/repo_inventory_summary.json
```

### G4. C09 / CONV-NUC-01 precisa permanecer sem colisão

Risco:

```text
usar C09 como convergência nuclear de novo
```

Regra:

```text
C09 = fóton/plasma
CONV-NUC-01 = nuclear/chrysopoeia
```

### G5. Convergências externas ainda não são validação física

ETH/HLS, biomimética, gotas, silêncio útil e CONV-NUC-01 ainda são:

```text
rotas de leitura
mapas de pendência
hipóteses operacionais
```

Não são:

```text
prova de RLL
prova de T7
prova de BITRAF
prova de RAFAELIA
```

### G6. Pipeline CLI precisa auditoria de roteamento

Houve indicação anterior de risco no roteamento:

```text
rll run --data real --adversary lcdm
```

poder cair em fluxo legado, ignorando opções do comparador.

Falta verificar se a CLI chama corretamente o caminho moderno de comparação contra baseline.

### G7. Resultados negativos precisam aparecer no mesmo nível que positivos

O projeto deve preservar:

```text
χ² pior
AIC/BIC pior
degenerescência com ΛCDM
TOKEN_VAZIO
CONTRADICTION
```

como resultado científico, não como falha documental.

---

## F_next — próximas ações executáveis

### N1. Rodar saneamento documental pós-merge

```bash
python3 tools/docs_inventory.py
python3 tools/docs_inventory.py --check
```

Saída esperada:

```text
inventário atualizado
contagem consistente
sem link morto canônico
```

### N2. Criar teste/gate do limite nulo

Adicionar ou consolidar teste que compare:

```text
Ωs0 livre vs Ωs0=0
```

Critério mínimo:

```text
quando Ωs0=0, setor RLL deve anular matematicamente e retornar ao baseline esperado.
```

### N3. Criar relatório `RLL_NULL_LIMIT_DIAGNOSTIC.md`

Relatório esperado:

```text
configuração do teste
datasets usados
priors
χ²
AIC/AICc/BIC
interpretação
claim_state
```

### N4. Criar relatório `RLL_VS_W0WACDM_DIAGNOSTIC.md`

O adversário forte deve ser explícito:

```text
ΛCDM é baseline mínimo;
w0waCDM/CPL é adversário dinâmico.
```

### N5. Auditar CLI de comparação

Verificar se comandos de alto nível chamam o comparador correto:

```text
rll run --data real --adversary lcdm
rll run --data real --adversary cpl
rll run --data real --adversary w0wa
```

Saída esperada:

```text
sem fallback silencioso para fluxo legado
opções de covariância/diagonal respeitadas
logs de rota claros
```

### N6. Promover convergências externas para YAML quando houver fonte/artefato

Futuro catálogo sugerido:

```text
data/rll_convergences/external_convergences.yml
```

Campos mínimos:

```yaml
id:
name:
source_type:
source_url_or_ref:
claim_state:
required_metric:
validation_path:
notes:
```

### N7. Manter comunicação pública com frase segura

Frase recomendada:

> RLL é uma arquitetura cosmológica candidata e falsificável, com limite nulo explícito, cadeia documental e mapa de convergências. O projeto possui rotas de validação reais, mas não reivindica superioridade cosmológica sem métricas robustas contra ΛCDM e w0waCDM/CPL.

---

## Prioridade operacional

| Prioridade | Ação | Motivo |
|---|---|---|
| P0 | `docs_inventory.py --check` | impede drift documental |
| P1 | teste Ωs0 livre vs Ωs0=0 | protege falsificabilidade |
| P1 | comparação contra w0waCDM/CPL | evita adversário fraco |
| P2 | auditoria CLI | evita resultado por rota errada |
| P2 | YAML de convergências externas | transforma narrativa em artefato |
| P3 | paper/README público | só após métricas e gates limpos |

---

## Estado final resumido

```text
F_ok:
  RLL possui documentação, equação, limite nulo, claim boundary, convergências e cadeia de custódia.

F_gap:
  falta validação robusta contra baselines fortes, inventário pós-renomeação, auditoria CLI e relatórios negativos/positivos lado a lado.

F_next:
  rodar inventário, criar diagnóstico de limite nulo, comparar contra w0waCDM/CPL e garantir que a CLI usa o caminho correto.
```
