# RAFAELIA Ω — Referência de Schemas v1.0

**Data:** 2026-07-09  
**Status:** Especificação estrutural / camada de schemas  
**Escopo:** `OmegaArtifact`, `OmegaNode`, `OmegaRelation`, schema agregador Ω, validação local e lacunas remanescentes.

---

## 0. Propósito

Este documento cria a primeira camada formal de schemas derivada de `12_RAFAELIA_OMEGA_MASTER_ARCHITECTURE.md`.

O objetivo não é provar uma hipótese científica, nem ampliar pipelines sensíveis. O objetivo é transformar a arquitetura-mãe RAFAELIA Ω em contratos estruturais mínimos, rastreáveis e validáveis localmente.

```text
schema_parse_success != scientific_validation
schema_parse_success != RLL_confirmed
schema_parse_success != physical_claim
schema_parse_success != peer_review
```

---

## 1. Por que os schemas são o próximo passo natural

O documento 12 define que a arquitetura precisa reduzir entropia, preservar relações coerentes e impedir que código seja produzido antes de uma especificação estável.

A próxima camada natural é, portanto, estrutural:

```text
INTENÇÃO ψ
   ↓
PERGUNTA
   ↓
ARTEFATO
   ↓
SCHEMA
   ↓
VALIDAÇÃO LOCAL
   ↓
GOVERNANÇA
   ↓
KERNEL
```

Schemas entram antes do kernel semântico porque definem a forma mínima dos objetos que o futuro kernel poderá consumir, auditar, rejeitar ou reverter.

---

## 2. Derivação direta do documento 12

O documento 12 estabelece quatro blocos que agora ganham forma inicial:

| Bloco no documento 12 | Artefato formal criado | Função |
|---|---|---|
| Biblioteca Viva | `schemas/omega_artifact.schema.json` | unidade viva de conhecimento |
| Célula semântica | `schemas/omega_node.schema.json` | nó versionado e rastreável |
| Filtro de relação | `schemas/omega_relation.schema.json` | conexão ponderada entre nós |
| Equação canônica Ω | `schemas/omega_schema.json` | agregador estrutural do sistema |

A equação canônica permanece preservada:

```text
Ω(t+1) = F(Ω(t), D(t), E(t), P(t))
```

Onde a transformação `F` deve continuar auditável, reversível e governada.

---

## 3. Separação epistemológica obrigatória

Toda unidade de conhecimento deve ser classificada sem inflar seu grau de verdade.

| Estado | Uso permitido | Bloqueio |
|---|---|---|
| `fact` | dado verificável ou medido | não usar para interpretação sem evidência |
| `hypothesis` | proposta testável | não declarar como resultado |
| `metaphor` | camada didática, simbólica ou parabólica | não converter em fato físico |
| `evidence` | suporte documental, experimental, hash ou fonte | não confundir evidência com conclusão |
| `token_vazio` | lacuna real explicitamente marcada | não preencher com suposição útil |
| `decision` | escolha operacional registrada | não mascarar como descoberta |

Regra operacional:

```text
TOKEN_VAZIO é preferível a uma certeza fabricada.
```

---

## 4. Conexão entre OmegaArtifact, OmegaNode e OmegaRelation

A camada mínima funciona em três níveis:

```text
OmegaArtifact
  ├── contém pergunta, contexto, método, evidências e limitações
  ├── referencia OmegaNodes por relações ou evidências
  └── registra próxima pergunta

OmegaNode
  ├── representa uma célula semântica versionada
  ├── carrega valor, confiança, pontuações e hash
  └── pode apontar para um parent semântico

OmegaRelation
  ├── conecta source_node e target_node
  ├── registra evidência, coerência e reprodutibilidade
  └── calcula ou documenta peso relacional
```

A fórmula documental do documento 12 permanece:

```text
Peso_relação = Evidência × Coerência × Reprodutibilidade
```

`temporal_stability` é registrado como métrica adicional de auditoria temporal, mas não substitui a fórmula canônica.

---

## 5. Preparação para Omega Kernel v4

O documento 12 descreve o salto do Ω Kernel v3 para v4 como uma passagem de eventos estruturais para significado semântico.

A camada atual prepara esse salto sem implementar o kernel:

| Kernel v3 | Camada de schemas | Kernel v4 futuro |
|---|---|---|
| evento | `OmegaArtifact` | evento com pergunta e contexto |
| estado | `OmegaNode` | estado semântico versionado |
| hash/auditoria | `OmegaRelation` + audit | relação com peso e evidência |
| commit | rollback/governance | decisão semântica reversível |

Esta etapa não altera runtime, pipelines científicos ou workflows. Ela apenas cria o contrato mínimo para que uma implementação futura possa ser testada sem ambiguidade.

---

## 6. Validação sem inflar o repositório

A validação local deve permanecer leve:

```bash
python3 scripts/validate_omega_schemas.py
```

O script usa apenas biblioteca padrão do Python e verifica:

1. se os arquivos JSON são parseáveis;
2. se os campos principais existem em `required`;
3. se os estados epistemológicos obrigatórios estão presentes;
4. se a fórmula de relação foi preservada documentalmente;
5. se a equação canônica Ω foi preservada documentalmente.

Limite declarado:

```text
Este validador não substitui uma biblioteca JSON Schema completa.
Ele valida disciplina estrutural mínima dos schemas, não instâncias científicas.
```

---

## 7. Lacunas remanescentes

| Lacuna | Estado | Próximo gate |
|---|---|---|
| Validação completa de instâncias JSON Schema | TOKEN_VAZIO | decidir se `jsonschema` externo é aceitável no futuro |
| Exemplos canônicos de `OmegaArtifact` | TOKEN_VAZIO | criar fixtures mínimos sem claims científicos |
| Fórmula operacional de `weight` | TOKEN_VAZIO | definir se será calculada pelo produtor ou por validador futuro |
| Política de promoção de `hypothesis` para `fact` | TOKEN_VAZIO | documento de governança semântica |
| Integração com Ω Kernel v4 | TOKEN_VAZIO | especificação técnica futura |

---

## 8. Próximo estado

A camada de schemas cria um contrato de forma, não uma conclusão científica.

O próximo passo natural é criar exemplos mínimos e fixtures de validação para demonstrar como `fact`, `hypothesis`, `metaphor`, `evidence`, `token_vazio` e `decision` aparecem em objetos reais sem promover metáfora a evidência.
