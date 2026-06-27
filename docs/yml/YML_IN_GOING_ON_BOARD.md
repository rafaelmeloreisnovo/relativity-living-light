# YML In Going On Board

Status date: 2026-06-27

## Objetivo

Este quadro mostra o trabalho YML em andamento por unidades pequenas.

A pergunta e:

```text
qual arquivo/familia esta sendo revisado, qual a funcao, qual o status e qual o proximo passo?
```

## Legenda simples

| Status | Significado |
|---|---|
| TODO | ainda nao revisado |
| DOING | em revisao |
| CHECK | precisa conferir chamada/output |
| FIX | precisa correcao pequena |
| OK | papel claro e seguro |
| BLOCKED | risco de falso positivo ou rota quebrada |
| TOKEN_VAZIO | lacuna conhecida e protegida |

## Quadro principal

| Ordem | Familia | Tipo | Pergunta principal | Status inicial | Proximo passo |
|---:|---|---|---|---|---|
| 1 | `.github/workflows/*.yml` | workflow | roda no GitHub Actions? | DOING | checar job, timeout, scripts, artifacts |
| 2 | `START_MANUAL_HERE.yml` | workflow/menu | ajuda leigo a escolher rota? | CHECK | transformar em porta de entrada com cards |
| 3 | `real-data-complete-execution.yml` | workflow real-data | gera artifacts completos? | DOING | acompanhar Pantheon/Structure-D ate final |
| 4 | `yml-operational-review.yml` | workflow checker | revisa papeis YML? | NEW | aguardar CI do PR #452 |
| 5 | `docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml` | route/ledger | C01..C10 sao portas de teste? | CHECK | gerar tabela C01..C10 com status |
| 6 | `data/real/**/*.yml` | source/ledger | fonte real tem local/checksum? | TODO | separar real, fetched, seed, result |
| 7 | `data/results/**/*.yml` | result | resultado tem script/commit/checksum? | TODO | bloquear claim sem manifest |
| 8 | `*.iml.yml` | IML/arvore | e arquitetura ou execucao? | TODO | marcar runs_by_itself=false |
| 9 | `examples/*.yml` | example/teste | exemplo nao vira evidencia? | TODO | garantir claim_allowed=false |
| 10 | schemas | schema | contratos existem? | DOING | evoluir `schemas/yml_role.schema.json` |

## Roteiro modular por unidade

### Unidade 1 — Workflow que roda

Checklist:

```text
[ ] tem name
[ ] tem on
[ ] tem jobs
[ ] tem timeout-minutes
[ ] instala dependencias necessarias
[ ] scripts chamados existem
[ ] artifact final e enviado
[ ] erro mostra diagnostico util
```

### Unidade 2 — Route/ledger cientifico

Checklist:

```text
[ ] tem id unico
[ ] tem dataset/fonte
[ ] tem confirma_se
[ ] tem refuta_se
[ ] tem claim_boundary
[ ] tem consumidor declarado
[ ] nao diz que ja validou se nao rodou
```

### Unidade 3 — Dados reais

Checklist:

```text
[ ] fonte publica declarada
[ ] caminho local declarado
[ ] checksum quando materializado
[ ] diferenciar seed/fetched/result
[ ] fallback nao fabrica dado
[ ] strict mode preservado
```

### Unidade 4 — Resultado/artifact

Checklist:

```text
[ ] aponta script produtor
[ ] aponta commit/run id
[ ] tem checksum
[ ] tem input usado
[ ] tem metrica
[ ] tem baseline
[ ] preserva negativo
```

### Unidade 5 — IML/arvore estrutural

Checklist:

```text
[ ] dizer que nao roda sozinho
[ ] dizer quem consome
[ ] dizer quais rotas descreve
[ ] evitar nome que pareca action se nao for action
```

## Como qualquer pessoa usa

```text
1. abrir este board
2. escolher uma familia
3. abrir o cartao do arquivo
4. responder checklist
5. marcar F_ok/F_gap/F_next
6. corrigir um ponto por PR
```

## Primeiro caso em andamento

```text
Arquivo: docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml
Tipo: route/ledger cientifico
Status: CHECK
Problema de usabilidade: pode parecer workflow/action, mas nao roda sozinho
F_next: gerar cards C01..C10 e ligar cada caminho a script/dataset/artifact quando existir
```

## Politica de conforto operacional

```text
um PR = uma familia ou um erro claro
um card = um arquivo ou uma rota pequena
um status = uma decisao simples
um claim = so depois de artifact + baseline + falsificador
```

## Fechamento

```text
F_ok:
  o trabalho YML agora tem quadro visual e roteiro modular.

F_gap:
  falta preencher status real arquivo por arquivo apos o checker rodar.

F_next:
  usar a saida do checker para transformar TODO/CHECK/FIX em PRs pequenos.
```
