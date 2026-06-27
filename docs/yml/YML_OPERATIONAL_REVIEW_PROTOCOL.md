# YML Operational Review Protocol

Status date: 2026-06-27

## Objetivo

Este protocolo define a revisão operacional dos arquivos `.yml` e `.yaml` do repositório.

A pergunta não é apenas:

```text
este YAML é válido?
```

A pergunta correta é:

```text
este YAML executa, configura, manifesta, roteia, registra, exemplifica ou apenas estrutura?
```

## Ciclo de conferência

```text
observar
  -> parsear
  -> classificar papel
  -> detectar scripts referenciados
  -> checar workflow executável
  -> checar claim_allowed
  -> checar baseline/falsificador
  -> registrar erro/aviso
  -> retroalimentar o inventário
```

## Classes operacionais

| Classe | Função | Executa sozinho? | Pode virar evidência? |
|---|---|---:|---:|
| workflow | GitHub Actions, tem `name/on/jobs` | sim | só com artefatos e gates |
| config | entrada consumida por script | não | só quando consumida e validada |
| manifest | inventário ou declaração de arquivos/fontes | não | não sozinho |
| route | mapa de rotas entre módulos/scripts | não | não sozinho |
| ledger | lista curada de fontes/candidatos | não | só com raw data + checksum |
| result | saída de execução anterior | não | depende de commit, script, checksum e métrica |
| example | exemplo/teste didático | não | nunca como dado real |
| schema | contrato estrutural | não | valida forma, não conteúdo empírico |
| iml | árvore estrutural/arquitetural | não | só se pipeline consumidor executar |

## Níveis de execução

| Nível | Sentido |
|---|---|
| E0 | texto, árvore, exemplo ou material estrutural |
| E1 | manifesto/config declarativo |
| E2 | YAML consumido por script |
| E3 | workflow executável |
| E4 | artefato de resultado |
| E5 | evidência científica reproduzível com baseline e falsificador |

## Gate novo

Arquivo:

```text
tools/check_yml_operational_contracts.py
```

Funções:

```text
1. varre todos os .yml/.yaml
2. valida parse YAML com PyYAML
3. classifica role e execution_level
4. detecta referências a .py/.sh
5. falha se workflow referencia script inexistente
6. falha se claim_allowed=true não tiver marcador de baseline e falsificador
7. avisa quando YAML declarativo pode ser confundido com execução
```

## Schema de metadado recomendado

Arquivo:

```text
schemas/yml_role.schema.json
```

Bloco recomendado para novos YAMLs:

```yaml
meta:
  yml_role: config
  execution_level: E2
  runs_by_itself: false
  consumed_by:
    - scripts/example_consumer.py
  produces:
    - results/example_output.json
  claim_allowed: false
  baseline_required: true
  falsifier_required: true
  negative_result_policy: preserve_negative_results
```

## Regra anti-falso-positivo

```text
YAML existente não é validação empírica.
YAML estruturado não é execução.
YAML com source não é dado bruto validado.
YAML com result não é claim sem script, commit, checksum, baseline e falsificador.
```

## Saídas esperadas

Quando executado com `--write`, o checker gera:

```text
data/results/yml_operational_contracts.json
docs/yml/YML_OPERATIONAL_CONTRACT_REVIEW.md
```

No CI, por padrão, ele roda sem escrever arquivos e bloqueia apenas erros reais.

## Política de retroalimentação

1. Erro de parse YAML: corrigir imediatamente.
2. Workflow sem `name/on/jobs`: corrigir imediatamente.
3. Workflow chamando script inexistente: corrigir imediatamente.
4. `claim_allowed=true` sem baseline/falsificador: bloquear.
5. YAML declarativo sem consumidor: registrar como aviso, não falha.
6. Example/mock/sample: nunca promover para evidência.
7. Result YAML: exigir contexto de execução antes de claim.

## Frase canônica

> O sistema YML do RLL deve verificar cada arquivo como peça operacional: workflow executa, config orienta, manifest preserva, IML estrutura, result documenta e claim boundary impede falso positivo.

## F_ok / F_gap / F_next

```text
F_ok:
  existe checker operacional e schema de papel YML.

F_gap:
  nem todos os YAMLs antigos declaram meta.yml_role ainda.

F_next:
  migrar gradualmente YAMLs críticos para o bloco meta e ativar relatórios escritos em PRs de inventário.
```
