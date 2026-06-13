# REAL / SYNTHETIC / MOCK BOUNDARY AUDIT

Classificação de cada ocorrência de termos de fronteira em arquivos YAML.
Varredura: `grep -RInE "mock|synthetic|placeholder|fake|demo|real_validated|embedded_fallback"`
restrita a `*.yml`/`*.yaml`. Sem inferência.

## Princípio verificado

Nenhum workflow promove `mock`/`synthetic`/`example`/`placeholder`/`demo` para
`real_validated`. Confirmado por leitura direta dos 13 workflows e dos
manifests.

## Tabela de ocorrências

| Arquivo:linha | Termo | Classificação |
|---|---|---|
| `validacao_real/sources.yml:12,21` | `embedded_fallback` | placeholder honesto — aponta para dado real versionado usado se a rede cair |
| `validacao_real/data/desi_dr2_bao.yml:7` | `status: real_embedded_fallback` | uso legítimo — dado real DESI DR2 embutido |
| `validacao_real/data/hz_cosmic_chronometers.yml:6` | `status: real_embedded_fallback` | uso legítimo — compilação CC de Moresco |
| `validacao_real/fetched/desi_dr2_bao.yml:7` | `status: real_embedded_fallback` | artefato materializado (execução) |
| `validacao_real/fetched/hz_cosmic_chronometers.yml:7` | `status: real_embedded_fallback` | artefato materializado (execução) |
| `rll_equation_registry.yml:58` | `claim_boundary: "placeholder metric…"` | placeholder honesto declarado |
| `dha-fisher-ci.yml:29,38,42` | `mock_catalog.csv` | **mock rotulado**, CI-only; alimenta teste de extrator; NÃO promovido |
| `repo-real-inventory.yml:87,88,128` | `synthetic`/`mock` | código de detecção de risco (flag), não dado |
| `START_MANUAL_HERE.yml:37` | "dados reais não sintéticos" | descrição de input (intenção correta) |
| `real-data-complete-execution.yml:101,132,216` | `mock/synthetic` | política anti-promoção (failsafe) |
| `data/observational_sources.yml:31,52` | `evidence_level: real_validated` | refere-se ao **dataset DESI DR2 real publicado**, não a claim do modelo RLL |
| `data/real_sources/rll_real_orchestrator_inventory.iml.yml:110` | `no_fake_fill: TOKEN_VAZIO/lacuna` | TOKEN_VAZIO protegido |
| `data/real_sources/rll_pantheon_real_validation.iml.yml:79` | "no superiority claim from synthetic…" | claim boundary explícito |
| `data/real/rll_real_sources_manifest_2026.yml:13` | "sem fake-fill" | princípio anti-fabricação |
| `tools/inventory_config.yml:4` | `claim_boundary: No synthetic claim…` | claim boundary explícito |
| `data/rll_latentes/examples/valid_minimal.yml` | "Fixture only; no discovery claim." | fixture de exemplo honesta |
| `data/rll_latentes/examples/invalid_missing_falsifier.yml` | "Fixture only…" | fixture negativa (schema test) |

## Conclusão (FATO_VERIFICADO)

- Toda ocorrência cai em: uso legítimo, placeholder honesto, TOKEN_VAZIO
  protegido, ou código de detecção. **Nenhum ERRO de contaminação.**
- `real_validated` aparece **somente** sobre datasets externos reais (DESI
  DR2), nunca sobre superioridade do modelo RLL.
- **RISCO residual (baixo)**: `dha-fisher-ci.yml` constrói um catálogo `mock`
  para exercitar o extrator ln(1+z). É honesto e isolado, mas recomenda-se
  renomear o artefato para `ci_smoke_catalog.csv` para reduzir ambiguidade
  semântica (registrado em `YML_NEXT_ACTIONS.md`).
