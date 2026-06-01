# RLL-LATENTES — sete passos futuros integrados

**Pré-etapa obrigatória:** aplicar [`RAW_TEXT_FIRST.md`](RAW_TEXT_FIRST.md) antes de qualquer score, vetor, métrica ou inferência. Claims sem âncora literal devem permanecer em `raw_preserved`, `insufficient_metadata` ou `rejected`, sem promoção estatística.

**Finalidade:** consolidar as sugestões futuras em uma rota única, verificável e executável para transformar o formalismo RLL-LATENTES em um módulo de pesquisa mais automatizado, auditável e preparado para revisão externa.

**Regra de segurança científica:** cada passo abaixo deve preservar a distinção entre `candidate`, `validated_control`, `rejected_noise` e `evidence_claim`. Nenhum artefato gerado por pipeline deve elevar uma semente latente para reivindicação científica sem hipótese nula, incerteza, controle negativo e replicação independente.

## Visão geral dos 7 passos

| Passo | Entrega | Critério de aceite | Failsafe / rollback |
| --- | --- | --- | --- |
| 1 | Contrato de dados endurecido | YAML, schema e exemplos mínimos validam em CI | bloquear ingestão quando campo crítico faltar |
| 2 | Coletor reprodutível | fontes baixam para `artifacts/rll_latentes/raw/` com checksum | manter manifesto de falha sem sobrescrever dados prévios |
| 3 | Núcleo determinístico de score | `S_L` e métricas auxiliares produzem saída estável | retornar `score_status: invalid` quando entradas violarem domínio |
| 4 | Modelos nulos e controles negativos | permutação, bootstrap e controles por domínio são executáveis | invalidar score que sobreviva apenas sem controle negativo |
| 5 | Proveniência criptográfica | hashes, Merkle root e trilha de versão são emitidos | restaurar último manifesto íntegro |
| 6 | Orquestração fullstack | CLI, CI, relatórios e artefatos navegáveis ficam conectados | degradar para relatório textual quando dashboard/API falhar |
| 7 | Pacote acadêmico de validação | relatório, checklist FAIR, limitações e release citável | publicar resultado negativo quando validação não confirmar hipótese |

## Passo 1 — contrato de dados endurecido

- Expandir `schemas/rll_latentes_observations.schema.json` para cobrir `future_steps`, checksums opcionais, tamanho esperado, licença, versão de acesso e política de retenção.
- Criar exemplos mínimos positivos e negativos em `data/rll_latentes/examples/`.
- Adicionar teste unitário para impedir catálogos sem falsificador.

**Aceite:** `python3 scripts/validate_rll_latentes_catalog.py` valida o catálogo principal e rejeita pelo menos um exemplo inválido.

## Passo 2 — coletor reprodutível

- Implementar um coletor por fonte, preferencialmente idempotente, que nunca apague artefatos anteriores sem manifesto de rollback.
- Registrar `downloaded_at_utc`, `source_url`, `etag`/`last_modified` quando disponível, `sha256`, bytes e comando usado.
- Separar dados grandes de metadados pequenos para evitar poluição do repositório.

**Aceite:** cada fonte gera um `manifest.json` local com checksum ou um `failure.json` auditável.

## Passo 3 — núcleo determinístico de score

- Implementar o cálculo de `S_L` com validação de domínio: `C,I,P,E,R_c,A_m,V_b ∈ [0,1]` e `R_u >= 0`.
- Adicionar funções puras para suavização `C_{t+1}`, `H_{t+1}` com `alpha = 0.25`, entropia discreta, coerência de fase e projeção toroidal normalizada.
- Preparar caminho de otimização futura para kernels sem heap quando houver necessidade real de baixo nível; no Python, manter implementação pura e previsível antes de otimização prematura.

**Aceite:** entradas fixas geram CSV/JSON determinístico e testes de borda passam para zero, um, NaN rejeitado e ruído alto.

## Passo 4 — modelos nulos e controles negativos

- Definir controles negativos por domínio: sideband em partículas, time-slide em ondas gravitacionais, embaralhamento de redshift em cosmologia, batch shuffle em biologia e motion-control em neurociência.
- Publicar os parâmetros do modelo nulo antes do ajuste exploratório.
- Exigir que todo score venha acompanhado de pelo menos um teste adversarial.

**Aceite:** relatório marca `provisional` quando controle negativo estiver ausente e `rejected_noise` quando a assinatura não sobreviver ao controle.

## Passo 5 — proveniência criptográfica e integridade

- Construir um manifesto Merkle para `raw`, `normalized`, `null_models`, `scores` e `reports`.
- Registrar hash do catálogo YAML, hash do schema, hash do código executor e commit Git.
- Criar política de rollback: nunca editar artefato antigo; criar nova versão e preservar diferença.

**Aceite:** `results/rll_latentes/provenance/merkle_manifest.json` permite verificar integridade de todos os artefatos publicados.

## Passo 6 — orquestração fullstack e observabilidade

- Expor uma CLI `rll-latentes` ou subcomando `rll latentes` com `validate`, `fetch`, `normalize`, `score`, `report` e `verify`.
- Integrar CI para schema, unidade, inventário, links e regressão de scores.
- Gerar relatório Markdown e, futuramente, uma visualização estática de scores por domínio, estado e fonte.

**Aceite:** uma execução local em modo seco (`--dry-run`) produz plano completo sem baixar dados grandes.

## Passo 7 — validação acadêmica, release e revisão externa

- Consolidar relatório de validação com resumo, métodos, hipóteses nulas, limitações, resultados negativos e próximos experimentos.
- Preparar pacote citável com `CITATION.cff`, Zenodo/GitHub release, DOI quando aplicável e licença por artefato.
- Submeter a revisão interna/externa antes de qualquer linguagem de descoberta.

**Aceite:** pacote de release inclui checklist FAIR, matriz de falsificabilidade, versão de dados, versão de código e declaração explícita do que foi refutado, inconclusivo ou suportado.

## Sugestões integradas de engenharia

- Priorizar invariantes e contratos antes de otimização: branchless, SIMD, freestanding ou bare-metal só devem entrar após perfilamento demonstrar gargalo real.
- Evitar loops e condicionais redundantes por desenho de schema, vetorização e tabelas de dispatch, não por obscurecimento de código.
- Tratar failover como rota explícita de dados: fonte primária, fonte espelho, cache local, relatório negativo.
- Tratar rollback como versionamento imutável: nunca apagar o erro sem deixar manifesto.
- Tratar token vazio como estado legítimo: `VOID`, `unknown`, `not_applicable` e `insufficient_metadata` devem ser diferentes de falso positivo.


## Estado de materialização v0.2

Esta revisão implementa uma versão mínima, testada e não destrutiva dos sete passos:

- `scripts/validate_rll_latentes_catalog.py` valida o catálogo principal e confirma que o exemplo inválido é rejeitado.
- `scripts/rll_latentes_pipeline.py` expõe a mesma CLI de `python -m rll.latentes`.
- `src/rll/latentes.py` implementa validação, plano, fetch seco, score, controle negativo, Merkle, relatório e verificação.
- `tests/test_rll_latentes.py` cobre contrato, exemplo inválido, cálculo `S_L`, domínio inválido, mapa toroidal, pipeline seco e CLI.

A implementação permanece conservadora: coleta real de dados, API, dashboard e kernels de baixo nível continuam bloqueados até haver perfilamento, contrato de dados endurecido e política explícita de armazenamento de artefatos grandes.
