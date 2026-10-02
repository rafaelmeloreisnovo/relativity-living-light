# Rota de fragmentos de pesquisa RLL, bibliografia e Pages — v1

Status: implementação inicial claim-gated em branch de revisão. O intake aceita um identificador arXiv por execução manual; não há polling agendado.

## 1. Objetivo

Conectar metadados bibliográficos, relações candidatas, artefatos canônicos, receipts e uma visualização Jekyll. A trilha preserva a distinção:

```text
SOURCE ≠ ARTIFACT ≠ EXECUTION ≠ EVIDENCE ≠ CLAIM
```

Um título, nome de autor, citação, semelhança de termos ou aresta do grafo não valida uma hipótese RLL. Cada aresta candidata precisa apontar para a fonte e digest que a originou, indicar o método e continuar revisável.

## 2. Ponto de partida no repositório

O repositório já contém ACADEMIC_CORR_001, um ledger de validação relacional, os schemas de pacote/grafo, um validador estrutural e o workflow validate-academic-correlation-package.yml. O pacote atual é RELATIONAL_PENDING e claim_allowed=false.

Esta rota estende esse trilho com:

1. um registro bibliográfico curado de dois anchors já citados no mapa acadêmico;
2. intake manual de um registro público do arXiv, com resposta Atom bruta e SHA-256;
3. arestas opcionais apenas quando quem dispara fornece IDs de destino e uma justificativa;
4. dados de página gerados com hashes do grafo, pacote e registro bibliográfico;
5. uma build Jekyll isolada que vira artifact de preview, sem deploy em Pages.

A validação de formato e o hash de metadados verificam custódia/estrutura. Eles não verificam a interpretação científica do paper nem a relação declarada.

## 3. Modelo de dados e identidade

| Entidade | Chave canônica | Regra de consolidação |
|---|---|---|
| Artigo/trabalho | `arxiv:<id>v<n>` ou `doi:<doi>` | Versão de preprint e DOI publicado são identificadores relacionados, não uma substituição destrutiva. |
| Pessoa | `orcid:<id>` quando confirmado | Nome isolado nunca funde duas pessoas. Sem ORCID, manter person_candidate e registrar a fonte do nome. |
| Instituição | `ror:<id>` quando confirmado | Afiliação textual não prova identidade institucional. |
| Dataset | DOI ou accession do provedor | Guardar provedor, versão, licença, checksum e locator. |
| Artefato de repositório | `gh:<owner>/<repo>@<commit>:<path>#sha256=<digest>` | Commit, path e bytes formam uma referência reprodutível. |
| Claim | ID estável do registro RLL | Texto e estado epistemológico permanecem na fonte canônica correspondente. |
| Execução/receipt | `ghrun:<repo>/<run_id>` | Guardar ref, commit, workflow, resultado, inputs efetivos e digests dos outputs. |

Para o grafo, arestas existentes usam from, edge_type e to. Novas arestas de intake recebem também source_locator, source_sha256, relation_note, review_state e claim_allowed:false. O campo relation_note é fornecido por uma pessoa; o intake não infere relações a partir de nome, título ou resumo.

## 4. Pipeline de fragmentos

```text
arXiv ID manual
→ resposta Atom bruta + SHA-256 + retrieved_at
→ metadados normalizados + autores como strings públicas
→ edge candidata opcional, somente com alvo e nota fornecidos
→ testes de schema, endpoints, digest e claim boundary
→ receipt de intake + pacote Jekyll
→ preview baixável para revisão
```

Cada intake consulta um único identificador e termina. A rota não varre categorias do arXiv nem agenda monitoramento. A API oficial documenta id_list para consultar IDs e entrega registros Atom; o manual pede intervalo de três segundos entre chamadas sucessivas. O workflow faz no máximo uma consulta por execução. Fonte: https://info.arxiv.org/help/api/user-manual.html

Campos preservados no receipt:

- identificador pedido e ID/version retornados;
- título, nomes de autores, datas published/updated, categorias, DOI e referência de periódico quando o endpoint os fornece;
- URL da fonte, URL do endpoint, instante de coleta, ator e GITHUB_RUN_ID;
- bytes originais da resposta Atom e SHA-256;
- alvos/nota de relação declarada, se houver;
- claim_allowed=false e review_state=RELATIONAL_PENDING.

Instituições e ORCIDs ainda não são extraídos ou inferidos por este intake. Esses nós só entram depois de resolver um identificador oficial e guardar a fonte correspondente.

## 5. Perfis de pipeline e capacidade

O session catalog removeu o glob amplo de workflows da raiz e carrega somente manifestos explícitos. O perfil é um recorte por finalidade; o gate continua single-flight dentro da sessão.

| Perfil | Workflows escolhidos | Soma máxima dos timeouts dos manifestos |
|---|---|---:|
| quick_session | sintaxe YAML | 20 min |
| real_data_session | preflight + real-data controlado + orquestrador de metadados | 165 min |
| science_session | fórmulas + IML + pacote relacional/Jekyll | 75 min |
| literature_session | intake opcional + validação + preview | 15 min |
| pages_preview_session | preview Jekyll do grafo curado | 15 min |
| frontier_session | fronteira isolada | 190 min |
| full_session | sete manifestos allowlisted; exclui frontier | 260 min |

O job pai usa 320 minutos, deixando 60 minutos de margem sobre o orçamento máximo atual. A documentação oficial do GitHub define máximo de 360 minutos por job: https://docs.github.com/en/actions/reference/workflows-and-actions/workflow-syntax

Uso direcionado: no workflow acadêmico, preencha arxiv_id. Para criar uma relação candidata, inclua related_node_ids existentes e uma relation_note; no orchestrator, os mesmos valores podem ser passados em overrides para academic_correlation_package. Sem alvos, a intake cria apenas um registro bibliográfico sem conexão.

## 6. Jekyll e GitHub Pages

A origem do preview fica isolada em pages/rll-research/. O build gera _data/research_graph.json durante a execução, consome o ledger/grafo, o registro bibliográfico e, quando houver, o receipt arXiv. O HTML mostra a fronteira de claim, hashes de inputs, fontes e arestas pendentes.

Este corte usa actions/jekyll-build-pages para construir o site e actions/upload-artifact para guardar o resultado. O workflow não solicita pages:write nem id-token:write, não usa actions/deploy-pages e não altera a publicação existente. A ação oficial de build pode produzir um artifact compatível com Pages, mas este pipeline mantém o artifact como preview: https://github.com/actions/jekyll-build-pages

Não encontrei _config.yml, Gemfile ou workflow Jekyll/Pages no conteúdo do repositório, e o endpoint de configuração Pages não ficou disponível para leitura pela conexão GitHub nesta auditoria. Isso não demonstra que Pages esteja desativado. A configuração de publicação está TOKEN_VAZIO; confirme a origem/branch antes de conectar um deploy.

## 7. PATs, permissões e comunicação entre fragmentos

O código visível não contém referências a PAT_AGENTS, PAT_ACTIONS ou PAT_ENV. A conexão atual não expõe valores nem escopos dos secrets do GitHub; eles permanecem não verificados. O orquestrador de sessão usa o GITHUB_TOKEN fornecido pelo runner com contents: read e actions: write para despachar Actions. A intake bibliográfica usa contents: read e não precisa de PAT.

A comunicação entre fragmentos começa como relação navegável: o preview mostra quais IDs foram apontados e que fonte/note gerou a ligação. Não envia email, Slack, convites ou mensagem a pesquisadores. A associação automática entre pessoas e artefatos fica bloqueada até resolver ORCID, confirmar autoria e definir um canal interno de revisão.

## 8. Gates seguintes

1. Revisar os dois anchors curados contra registros oficiais e capturar snapshots/digests diretamente da API em futura atualização.
2. Adicionar uma relação ao grafo canônico só depois de registrar uma passagem do texto, contexto da fonte, argumento, baseline, incerteza e teste de contradição.
3. Implementar resolver ORCID/ROR após definir qual API oficial será fonte e como guardar a resposta/digest.
4. Verificar a configuração GitHub Pages e a branch/source escolhidas; só então preparar um PR separado que inclua deploy e permissões mínimas.
5. Criar notifications internas somente a partir de mapping explícito fragmento→responsável/inscrição, sem inferir dono a partir de nomes.
6. Para ingestão contínua, resolver primeiro a governança de monitoramento. Esta implementação requer uma execução manual por paper e não cria tarefa agendada.

## 9. Referências bibliográficas iniciais

- DESI Collaboration, DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints, arXiv:2503.14738v3, Phys. Rev. D 112, 083515 (2025), DOI 10.1103/tr6y-kpc6. Fonte: https://arxiv.org/abs/2503.14738v3
- Planck Collaboration, Planck 2018 results. VI. Cosmological parameters, arXiv:1807.06209v4, A&A 641, A6 (2020), DOI 10.1051/0004-6361/201833910. Fonte: https://arxiv.org/abs/1807.06209v4

Esses trabalhos são anchors de contexto/adversarial e baseline. A citação não implica endosso nem valida RLL.

## R3

```text
F_ok   = perfis explícitos, intake arXiv manual com hash, relações pendentes e preview Jekyll em artifact.
F_gap  = deploy Pages, resolver ORCID/ROR, snapshots da bibliografia curada e canal de notificação ainda não configurados.
F_next = executar uma intake por arXiv ID e revisar o receipt antes de promover qualquer relação.
```
