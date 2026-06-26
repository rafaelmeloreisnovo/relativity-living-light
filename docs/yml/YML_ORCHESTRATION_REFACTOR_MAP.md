# YML orchestration refactor map

Status date: 2026-06-26

## Propósito

Este documento transforma o inventário de YAML/YML do repositório em um mapa simples de arquitetura.

A pergunta central é:

```text
quando uma ação chega, qual YAML recebe, quem ele chama, o que roda, que artefato sai e qual claim pode ou não pode nascer disso?
```

Regra principal:

```text
YAML não é automaticamente execução.
YAML pode ser workflow, contrato, árvore estrutural, fonte, manifesto, seed ou artefato.
```

Portanto, cada arquivo `.yml/.yaml` precisa ter uma função explícita.

---

## Leitura para leigo

Pense nos YAMLs como placas de sinalização dentro de uma fábrica científica:

| Tipo | Explicação simples | Roda sozinho? |
|---|---|---|
| Workflow | Botão ou esteira do GitHub Actions | sim |
| Manifesto | Lista do que existe ou deve existir | não |
| Configuração | Contrato que um script lê | não sozinho |
| IML | Árvore estrutural / mapa de arquitetura | não, salvo quando um pipeline lê |
| Fonte observacional | Lista de fontes e entradas reais | não |
| Resultado | Artefato produzido por execução anterior | não |
| Exemplo/mock | Material didático ou teste negativo | não deve virar evidência |

Frase curta:

> Workflow executa. Config orienta. Manifesto registra. IML estrutura. Resultado comprova execução. Exemplo ensina, mas não prova.

---

## Classificação operacional proposta

| Nível | Classe | Função | Pode gerar claim? |
|---|---|---|---|
| E0 | texto/árvore estrutural | organiza ideias, rotas e relações | não |
| E1 | manifesto/config declarativo | declara fontes, caminhos, critérios | não sozinho |
| E2 | config consumida por script | alimenta validador ou pipeline | só após script + artefato |
| E3 | workflow executável | dispara jobs, scripts e artifacts | só se outputs e gates passarem |
| E4 | artefato de resultado | registra saída de execução | depende de métrica e boundary |
| E5 | evidência científica | resultado reproduzível + baseline + falsificador | sim, com claim boundary |

---

## Famílias existentes no repositório

### 1. Workflows executáveis

Pasta:

```text
.github/workflows/*.yml
```

Função:

```text
evento GitHub -> job -> steps -> scripts -> artefatos -> status CI
```

Exemplos principais:

| Workflow | Papel |
|---|---|
| `START_MANUAL_HERE.yml` | porta de entrada manual, escolhe perfil, escopo, modo e grupo de dados |
| `rll-real-data-orchestrator.yml` | orquestrador de dados reais: fetch, compute, plots, book, IML e fórmulas |
| `real-data-contract-ci.yml` | contrato de dados reais e testes de pipeline |
| `claim-boundary-quality-gates.yml` | bloqueia promoção indevida de claim |
| `yml-syntax-validation.yml` | valida sintaxe/higiene YAML |
| `repo-real-inventory.yml` | gera inventários e índices |
| `validacao_real.yml` | pacote executável legado/real-validation |

Leitura correta:

```text
estes YAMLs são execução real, porque possuem name/on/jobs e rodam no GitHub Actions.
```

---

### 2. Orquestrador manual

Arquivo:

```text
.github/workflows/START_MANUAL_HERE.yml
```

Função:

```text
menu humano -> plano de seleção -> valida YAML -> valida interoperabilidade -> sonda pipeline -> artefato de auditoria
```

Entrada humana:

```text
run_profile
pipeline_scope
dataset_group
book_scope
mode
real_data_source
validate_workflows
validate_data_yml
run_data_preparation_probe
strict_mode
```

Saída:

```text
artifacts/manual-start/SELECTION_PLAN.md
artifacts/manual-start/METHODOLOGY_SUMMARY.md
artifacts/manual-start/probe/
```

Uso ideal:

```text
porta de entrada para leigo/técnico escolher o que quer validar sem conhecer todos os scripts.
```

---

### 3. Orquestrador de dados reais

Arquivo:

```text
.github/workflows/rll-real-data-orchestrator.yml
```

Função:

```text
validar inventário -> buscar fontes reais -> computar -> gerar plots -> rodar book/RLL -> rodar IML -> gerar fórmulas -> publicar artifact
```

Cadeia resumida:

```text
workflow_dispatch
  -> tools/docs_inventory.py --check
  -> scripts/fetch_real_sources.py
  -> scripts/compute_rll_real_pipeline.py
  -> scripts/generate_rll_plots.py
  -> scripts/rll_pipeline.py
  -> tools/iml/iml_pipeline.py
  -> tools/formula_artifact_builder.py
  -> CHECKSUMS.sha256 + MANIFEST.json + artifact
```

Uso ideal:

```text
pipeline central de execução empírica com artifacts e checksum.
```

Risco:

```text
se modo/escopo não forem claros, o usuário pode achar que metadata_only é validação científica.
```

Correção sugerida:

```text
cada modo deve declarar claim_state: metadata_only, fetched, computed, plotted, reported, validated.
```

---

### 4. YAMLs IML / árvores estruturais

Exemplos:

```text
data/real_sources/rll_real_orchestrator_inventory.iml.yml
data/real_sources/rll_pantheon_real_validation.iml.yml
```

Função:

```text
mapear rotas, engines, inputs, outputs, status e política de interpretação.
```

Leitura correta:

```text
parece execução, mas é principalmente contrato/árvore de arquitetura.
```

Só vira execução quando um consumidor lê:

```text
tools/iml/iml_pipeline.py
scripts/run_real_pantheon_validation.py
tools/real_data_materialization_audit.py
tools/verify_real_source_signatures.py
```

Uso ideal:

```text
blueprint do sistema: diz quais rotas existem e qual script deve ser chamado.
```

---

### 5. YAMLs de sementes e ledgers observacionais

Exemplos:

```text
data/real/bootstrap/real_seed_pipeline_orchestration.yml
data/real/high_z_smbh/high_z_seed_sources.yml
data/real/lensing/dark_lens_sources.yml
data/real/compact_objects/remnant_boundary_sources.yml
data/real/structure/residual_gravity_sources.yml
data/real/kinematics/hypervelocity_sources.yml
data/real/orbital_dynamics/angular_momentum_shape_sources.yml
```

Função:

```text
semente observacional -> rota -> ledger -> script de validação -> output esperado -> baseline exigido
```

Leitura correta:

```text
não são validação final; são mapas para buscar dados brutos, rodar métricas e testar falsificadores.
```

Uso ideal:

```text
fila de experimentos científicos com claim_allowed=false até raw data + baseline + métrica.
```

---

### 6. YAMLs cosmológicos e de validação real

Exemplos:

```text
data/real/cosmology/RLL_COSMO_VALIDATION_MATRIX.yml
data/real/cosmology/DESI_BAO_MATH_ARTIFACTS.yml
validacao_real/sources.yml
validacao_real/data/desi_dr2_bao.yml
validacao_real/data/hz_cosmic_chronometers.yml
validacao_real/fetched/desi_dr2_bao.yml
validacao_real/fetched/hz_cosmic_chronometers.yml
```

Função:

```text
dados reais / medições / matrizes / fontes -> pipeline cosmológico -> comparação de modelo
```

Uso ideal:

```text
comparar RLL contra ΛCDM, wCDM e w0waCDM/CPL com χ², AIC, AICc, BIC e covariâncias.
```

Claim boundary:

```text
sem baseline e penalização estatística, não há claim de superioridade.
```

---

### 7. YAMLs de resultados

Exemplos:

```text
data/results/desi_dr2_bao_zml.yml
```

Função:

```text
artefato de execução anterior ou materialização de resultado.
```

Leitura correta:

```text
resultado é evidência de execução, mas ainda precisa contexto: script, commit, input, checksum e métrica.
```

Uso ideal:

```text
ser sempre acompanhado por MANIFEST, CHECKSUMS, commit SHA e relatório de interpretação.
```

---

### 8. YAMLs de exemplos/testes negativos

Exemplos:

```text
data/rll_latentes/examples/valid_minimal.yml
data/rll_latentes/examples/invalid_missing_falsifier.yml
```

Função:

```text
testar schema, falsificador e claim boundary.
```

Leitura correta:

```text
exemplo não é dado real.
```

Uso ideal:

```text
educar o pipeline: um exemplo válido deve passar; um exemplo sem falsificador deve falhar.
```

---

## O mapa de chamada real

### Forma simples

```text
Pessoa escolhe ação
  -> workflow GitHub recebe inputs
  -> workflow chama scripts
  -> scripts leem YAMLs declarativos
  -> scripts geram outputs
  -> outputs viram artifacts
  -> artifacts passam por claim boundary
  -> só então pode haver interpretação científica
```

### Forma técnica

```text
workflow_dispatch
  -> workflow.yml
  -> job.steps[].run
  -> script.py / script.sh
  -> config.yml / manifest.yml / iml.yml
  -> results/*.json|*.csv|*.yml
  -> docs/*.md
  -> artifacts/*
  -> CHECKSUMS.sha256
  -> claim_state
```

---

## Problema atual

O repositório tem muitos YAMLs úteis, mas a função de cada um ainda está misturada no nome.

Exemplo de confusão:

```text
arquivo parece pipeline, mas é manifesto
arquivo parece execução, mas é árvore IML
arquivo parece dado real, mas é seed
arquivo parece resultado, mas é exemplo
```

Isso cria risco de falso positivo:

```text
YAML existe -> parece estruturado -> usuário acha que já validou
```

Mas a leitura científica correta é:

```text
YAML existe -> contrato existe -> ainda falta execução + métrica + baseline + falsificador
```

---

## Refatoração profissional proposta

### Regra 1 — prefixo por função

Padronizar gradualmente novos YAMLs com prefixo de função:

| Prefixo | Uso |
|---|---|
| `workflow_` | só para GitHub Actions ou wrappers de execução |
| `manifest_` | inventário/lista de fontes/arquivos |
| `config_` | entrada consumida por script |
| `route_` | mapa de rotas entre módulos |
| `ledger_` | lista curada de fontes/candidatos |
| `result_` | artefato de execução |
| `example_` | exemplo didático/teste |
| `schema_` | contrato estrutural |

Não precisa renomear tudo agora. Primeiro criar metadado `role_type`.

### Regra 2 — todo YAML deve declarar papel

Bloco mínimo recomendado:

```yaml
meta:
  yml_role: config | workflow | manifest | route | ledger | result | example | schema | iml
  execution_level: E0 | E1 | E2 | E3 | E4 | E5
  consumed_by: []
  produces: []
  claim_allowed: false
  falsifier_required: true
  baseline_required: true
```

### Regra 3 — separar árvore de execução

Quando um YAML for só estrutura:

```yaml
meta:
  yml_role: iml
  execution_level: E0
  runs_by_itself: false
```

Quando for consumido por script:

```yaml
meta:
  yml_role: config
  execution_level: E2
  consumed_by:
    - scripts/validation/validate_x.py
```

Quando for workflow:

```yaml
meta:
  yml_role: workflow
  execution_level: E3
  trigger: workflow_dispatch
```

### Regra 4 — artefato científico exige falsificador

Nenhuma rota pode promover claim sem:

```yaml
validation_contract:
  metric:
  baseline:
  falsifier:
  uncertainty:
  negative_result_policy:
  claim_state:
```

### Regra 5 — output precisa ser legível para humano

Todo pipeline importante deve gerar:

```text
MANIFEST.json
CHECKSUMS.sha256
COMPUTE_REPORT.md
CLAIM_REFERENCE_AUDIT.md
NEGATIVE_RESULTS.md
```

---

## Orquestrador ideal

Um orquestrador profissional deve ter uma tabela central:

```yaml
routes:
  - id: null_limit_test
    trigger: manual_or_ci
    workflow: .github/workflows/rll-real-data-orchestrator.yml
    config:
      - data/real/cosmology/RLL_COSMO_VALIDATION_MATRIX.yml
    scripts:
      - scripts/compute_rll_real_pipeline.py
    outputs:
      - results/null_limit_diagnostic.json
      - docs/RLL_NULL_LIMIT_DIAGNOSTIC.md
    baselines:
      - LCDM
      - w0waCDM
    falsifier:
      - Omega_s0_free_collapses_to_zero
      - AIC_BIC_worse_than_baseline
    claim_state: candidate_only
```

---

## Aplicações práticas

### Para leigo

```text
Aperta START_MANUAL_HERE.
Escolhe escopo e modo.
Baixa artifact.
Lê METHODOLOGY_SUMMARY.
Vê se saiu OK, TOKEN_VAZIO ou CONTRADICTION.
```

### Para pesquisador

```text
abre route map
confere fonte
confere baseline
confere script
confere métrica
confere artifact
confere claim boundary
```

### Para CI/CD

```text
PR muda YAML
CI valida sintaxe
CI valida consumed_by
CI valida artifacts esperados
CI bloqueia claim sem falsificador
```

### Para paper

```text
usar somente rotas E5:
resultado reproduzível + dados reais + baseline + falsificador + commit + checksum
```

---

## F_gap

1. Nem todo YAML declara `yml_role` e `execution_level`.
2. Alguns YAMLs parecem execução, mas são árvores/manifestos.
3. Alguns workflows geram artifact, mas nem sempre geram relatório de resultado negativo.
4. A diferença entre seed, fonte real, fetched data e result precisa ficar explícita em todos os arquivos.
5. O uso acadêmico precisa sempre passar por baseline e falsificador.
6. YAMLs com `TOKEN_VAZIO`, `sample`, `example`, `mock` ou `placeholder` devem ficar travados contra promoção científica.

---

## F_next

1. Criar schema leve para metadado comum de YAML:

```text
schemas/yml_role.schema.json
```

2. Atualizar o gerador:

```text
tools/generate_yml_audit_docs.py
```

para emitir também:

```text
docs/yml/YML_ORCHESTRATION_MAP.md
```

3. Adicionar coluna ao ledger:

```text
execution_level
role_type
claim_allowed
falsifier_required
baseline_required
```

4. Criar gate CI:

```text
se YAML novo não declara papel -> warning
se YAML com claim_allowed=true não tem falsifier/baseline -> fail
se result YAML não aponta script/commit/checksum -> warning/fail conforme pasta
```

5. Criar rota acadêmica principal:

```text
RLL_NULL_LIMIT_DIAGNOSTIC
RLL_VS_W0WACDM_DIAGNOSTIC
NEGATIVE_RESULTS_LEDGER
```

---

## Frase canônica

> O sistema YAML do RLL deve ser lido como uma orquestra científica: workflows executam, configs orientam, manifestos preservam, IML estrutura, resultados documentam e claim boundaries impedem falso positivo.

## Estado recomendado

```text
F_ok:
  inventário YML, readiness e workflows já existem.

F_gap:
  falta metadado comum para distinguir execução, árvore, manifesto, seed e resultado.

F_next:
  padronizar role_type/execution_level e gerar um orchestration map automático.
```
