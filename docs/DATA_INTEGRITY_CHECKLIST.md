# Checklist de Integridade de Dados e Documentação

Objetivo: confirmar que arquivos críticos permanecem presentes, com tamanho e hash para auditoria rápida.

| Arquivo | Existe | Tamanho (bytes) | SHA-256 (12) |
|---|---|---:|---|
| `data/posterior_unified_synth.csv` | sim | 2479312 | `1ff8978bfb7e` |
| `data/relativity_living_light_models.csv` | sim | 148820 | `88f44ff22de8` |
| `data/unified_entropy_margin_10_12.csv` | sim | 82965 | `08c7f1e333ee` |
| `data/RelativityLivingLight_v4_bundle.zip` | sim | 4096271 | `957575ff422f` |
| `data/relativity_bundle_results.zip` | sim | 4095297 | `5c0cca457927` |
| `docs/rll_revisado_v2.zip` | sim | 40801 | `aa61125ad94d` |
| `docs/README_ROOT_LEGACY_ARCHIVE.md` | sim | 74707 | `9cd827af2bb9` |
| `docs/DOCUMENTATION_FULL_INVENTORY.md` | sim | 12907 | `6142fa0cd7d3` |
| `docs/ZIP_CONTENT_INDEX.md` | sim | 4557 | `23aac857b9db` |

## Decisão canônica de posterior sintético

- Arquivo canônico definido: `data/posterior_unified_synth.csv`.
- Arquivos removidos por duplicidade nominal: `data/posterior_unified_synth (1).csv` e `data/posterior_unified_synth (2).csv`.
- Todas as referências documentais devem apontar exclusivamente para o caminho canônico.

## Comandos rápidos de auditoria

```bash
git status --short
git log --oneline -n 10
wc -l README.md docs/README_ROOT_LEGACY_ARCHIVE.md
```

## Nota

- Este checklist não substitui backup externo; é uma verificação técnica local de integridade.

## Validação de links

Executar validação editorial dos capítulos alterados em `book/` antes de abrir/atualizar PR de documentação:

```bash
python3 scripts/validate_book_links.py
```

Opcionalmente, validar um subconjunto explícito de capítulos alterados:

```bash
python3 scripts/validate_book_links.py book/12_metodologia_dados_mock.md book/13_metodologia_dados_reais.md
```

**Regra de aceite:** zero links relativos quebrados nos capítulos alterados, incluindo a sequência mínima de navegação editorial (`capítulo anterior`, `sumário`, `capítulo próximo`).

## Rastreabilidade científica crítica

Checklist operacional (marcar todos os itens antes de concluir revisão técnica/editorial):

- [ ] Toda *claim* crítica (resultado observacional, valor de parâmetro, significância estatística, comparação de modelo) possui chave bibliográfica explícita.
- [ ] Cada chave usada resolve para uma entrada válida na bibliografia unificada.
- [ ] *Claims* com dados internos citam também artefato interno rastreável (arquivo + caminho + versão/commit).
- [ ] *Claims* com números (ex.: sigma, χ², AIC/BIC, redshift) possuem fonte primária indicada.
- [ ] Revisão final: zero *claims* críticas sem referência.
Checklist operacional (marcar cada item após conferência):

- [ ] Toda claim crítica (resultado observacional, valor de parâmetro, significância estatística, comparação de modelo) possui chave bibliográfica explícita.
- [ ] Cada chave usada resolve para uma entrada válida na bibliografia unificada.
- [ ] Claims com dados internos citam também artefato interno rastreável (arquivo + caminho + versão/commit).
- [ ] Claims com números (ex.: sigma, χ², AIC/BIC, redshift) possuem fonte primária indicada.
- [ ] Revisão final: zero claims críticas sem referência.

### Bloco de auditoria manual

| claim | tipo (INT/EXT) | chave | local no documento | status |
|---|---|---|---|---|
|  |  |  |  |  |
|  |  |  |  |  |
|  |  |  |  |  |
| _preencher_ | _INT/EXT_ | _ex.: Smith2024_ | _arquivo + seção/página_ | _pendente/aprovado_ |
