# YML Friendly Orchestration Playbook

Status date: 2026-06-27

## Para que serve

Este guia transforma os arquivos `.yml/.yaml` do RLL em um roteiro amigavel.

A ideia e simples:

```text
qualquer pessoa deve conseguir olhar um YML e saber:
1. ele roda ou so descreve?
2. quem chama?
3. o que ele usa?
4. o que ele gera?
5. qual erro comum pode acontecer?
6. qual proximo passo seguro?
```

## Regra de ouro

```text
YML nao e prova.
YML e placa, contrato, mapa, botao ou resultado.
A prova so nasce quando ha execucao + artifact + baseline + falsificador.
```

## Mapa visual pequeno

```text
[Pessoa / PR / Action]
        |
        v
[Workflow .github/workflows]
        |
        v
[Script .py/.sh]
        |
        v
[Config / route / manifest / IML .yml]
        |
        v
[Resultado / artifact]
        |
        v
[Claim boundary]
        |
        v
[OK / TOKEN_VAZIO / CONTRADICTION / F_NEXT]
```

## Tipos de YML

| Tipo | Como explicar para leigo | Exemplo de uso |
|---|---|---|
| workflow | botao/esteira que roda no GitHub Actions | CI, testes, validacao |
| route | mapa de caminhos possiveis | C01, C02, C03... |
| ledger | lista curada de fontes/candidatos | fontes reais, objetos, datasets |
| manifest | inventario do que existe/deve existir | raw data, checksums, arquivos |
| config | entrada que um script le | parametros, opcoes, datasets |
| iml | arvore estrutural de arquitetura | roteiro/blueprint |
| result | saida de execucao anterior | summary.json, status.yml |
| example | exemplo didatico/teste | valid_minimal, invalid_missing_falsifier |

## Cartao padrao de cada YML

Use este modelo para revisar um por um:

```text
Arquivo:
Tipo:
Nivel: E0/E1/E2/E3/E4/E5
Roda sozinho? sim/nao
Quem chama:
Scripts usados:
Inputs:
Outputs:
Artifact esperado:
Claim permitido? sim/nao
Falsificador:
Baseline/adversario:
Erro comum:
Checklist:
  [ ] parse YAML
  [ ] papel declarado
  [ ] scripts existem
  [ ] outputs esperados existem ou sao TOKEN_VAZIO
  [ ] claim boundary preservado
  [ ] resultado negativo preservado
F_next:
```

## Niveis E0..E5

| Nivel | Sentido pratico | Exemplo |
|---|---|---|
| E0 | texto, arvore, exemplo | IML sem consumidor, exemplo didatico |
| E1 | declaracao/inventario | manifest, ledger, lista de fontes |
| E2 | config consumida por script | YAML lido por ferramenta |
| E3 | workflow executavel | `.github/workflows/*.yml` |
| E4 | resultado produzido | `data/results/*.yml` |
| E5 | evidencia reproduzivel | artifact + commit + baseline + falsificador |

## Roteiro de revisao um a um

### Passo 1 — separar o que roda do que nao roda

```text
.github/workflows/*.yml      -> workflow executavel
outros caminhos              -> provavelmente declarativo, rota, config, ledger, IML ou result
```

### Passo 2 — abrir o cartao do arquivo

Responder:

```text
Esse arquivo e botao, mapa, lista, contrato, arvore, resultado ou exemplo?
```

### Passo 3 — conferir chamadas

Procurar referencias a:

```text
.py
.sh
results/
data/
docs/
artifacts/
```

### Passo 4 — conferir claim boundary

Se tiver:

```yaml
claim_allowed: true
```

entao precisa existir tambem:

```text
baseline/adversario
falsificador
politica de resultado negativo
```

### Passo 5 — decidir status

| Status | Uso |
|---|---|
| OK_EXECUTABLE | workflow ou script comprovadamente roda |
| OK_DECLARATIVE | mapa/manifest correto, nao executa sozinho |
| NEEDS_CONSUMER | YAML existe, mas falta quem leia |
| NEEDS_ARTIFACT | execucao esperada, mas falta output |
| TOKEN_VAZIO | lacuna conhecida e protegida |
| BLOCK_CLAIM | risco de falso positivo |
| BROKEN_LINK | script/output citado nao existe |

## Caso guiado — CAMINHOS_VALIDACAO_NOVOS.yml

Arquivo real:

```text
docs/pipelines/validation_paths/CAMINHOS_VALIDACAO_NOVOS.yml
```

Tipo:

```text
route + ledger cientifico
```

Nivel:

```text
E1 agora; E2 quando consumido por gerador/checker
```

Roda sozinho?

```text
nao
```

Quem consome:

```text
tools/generate_yml_audit_docs.py
tools/docs_inventory.py
docs/yml/YML_PIPELINE_EXECUTION_READINESS.md
```

Funcao:

```text
mapear C01..C10 como portas de teste ainda nao plenamente presentes no repositorio.
```

Claim boundary:

```text
nenhum caminho afirma descoberta; cada um e porta de teste com criterio de refutacao.
```

Erro de usabilidade atual:

```text
pode parecer workflow de GitHub Actions por causa do nome e da URL de Actions, mas nao e arquivo .github/workflows.
```

Melhor representacao:

```text
CAMINHOS_VALIDACAO_NOVOS.yml = mapa de rotas cientificas futuras, nao botao de execucao.
```

Checklist:

```text
[ ] manter claim_boundary
[ ] manter C01..C10 com confirma_se/refuta_se
[ ] ligar cada caminho a pelo menos um script ou issue futura
[ ] marcar caminhos sem script como NEEDS_CONSUMER
[ ] nao tratar como validacao ja executada
```

F_next:

```text
Criar uma tabela C01..C10 com status: planned, has_script, has_dataset, has_artifact, claim_allowed.
```

## Checklist diario de trabalho YML

```text
[ ] olhar workflows que falharam
[ ] identificar se erro e ambiente, rota, input ou artifact
[ ] corrigir o menor arquivo possivel
[ ] preservar strict mode
[ ] nao criar artifact falso
[ ] rerodar ou aguardar CI
[ ] documentar F_ok/F_gap/F_next
```

## Ordem recomendada de organizacao

1. Workflows `.github/workflows`.
2. YAMLs que workflows chamam diretamente.
3. YAMLs de dados reais.
4. YAMLs de rotas cientificas.
5. IML/arquitetura.
6. Results/artifacts.
7. Examples/tests negativos.

## Frase curta para README/uso humano

> No RLL, cada YML tem papel: alguns rodam, alguns orientam, alguns registram, alguns estruturam. O roteiro seguro e olhar papel, chamada, entrada, saida, artifact, baseline e falsificador antes de interpretar qualquer resultado.

## F_ok / F_gap / F_next

```text
F_ok:
  existe roteiro amigavel para revisar YML um por um.

F_gap:
  ainda falta preencher cartoes individuais para todos os arquivos.

F_next:
  gerar automaticamente uma tabela de cartoes por arquivo a partir do checker operacional.
```
