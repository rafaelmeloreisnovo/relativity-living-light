# INDICE MESTRE - Documentacao Oficial
## Relativity Living Light

**Atualizado em:** 2026-05-27
**Regra:** secao principal lista apenas caminhos canonicos oficiais.

---

## Escopo deste arquivo

Este arquivo e a **navegacao canonica** da documentacao do repositorio.

- Lista os caminhos oficiais por trilha tematica.
- Atua como referencia de navegacao para leitura e manutencao.
- Nao substitui o README (porta de entrada) e nao tenta reproduzir o inventario bruto.

Encaminhamentos complementares:
- Porta de entrada: [`README.md`](../README.md)
- Inventario bruto (`.md` e `.zip`): [`docs/DOCUMENTATION_FULL_INVENTORY.md`](DOCUMENTATION_FULL_INVENTORY.md)
- Procedimento de atualizacao: `python3 tools/docs_inventory.py` e validacao `python3 tools/docs_inventory.py --check`.

---

## Procedimento de atualizacao do inventario documental

1. Regenerar inventario completo publicado:

   ```bash
   python3 tools/docs_inventory.py
   ```

2. Validar contagem publicada vs. varredura real:

   ```bash
   python3 tools/docs_inventory.py --check
   ```

3. Confirmar no cabecalho do inventario: data/hora, commit de referencia e total.

---

## 1) Nucleo cientifico oficial

- [`README.md`](../README.md)
- [`docs/Relativity_Living_Light.md`](Relativity_Living_Light.md)
- [`docs/BOOSTERS.md`](BOOSTERS.md)
- [`docs/Results.md`](Results.md)
- [`docs/RESULTADOS_CORRIGIDOS.md`](RESULTADOS_CORRIGIDOS.md)
- [`docs/COMPARACAO_DESI_2025.md`](COMPARACAO_DESI_2025.md)
- [`docs/ROADMAP_VALIDACAO.md`](ROADMAP_VALIDACAO.md)
- [`docs/PLANO_ABCD_JWST_AGN_SMBH.md`](PLANO_ABCD_JWST_AGN_SMBH.md)
- [`docs/ARQUITETURA_DUAS_RADIACOES_IMPLEMENTACAO.md`](ARQUITETURA_DUAS_RADIACOES_IMPLEMENTACAO.md)
- [`docs/MODELO_COSMOLOGICO_UNIFICADO_MAGNETISMO_RADIACAO_PLASMA.md`](MODELO_COSMOLOGICO_UNIFICADO_MAGNETISMO_RADIACAO_PLASMA.md)
- [`docs/REFERENCES.md`](REFERENCES.md)
- [`docs/FORMULAS_CANONICAS_INDEX.md`](FORMULAS_CANONICAS_INDEX.md) - referencia oficial de formulas
- [`docs/RLL_RESPONSE_MEDIUM_EQUATIONS.md`](RLL_RESPONSE_MEDIUM_EQUATIONS.md)
- [`docs/RLL_STATISTICAL_FINANCIAL_METRICS.md`](RLL_STATISTICAL_FINANCIAL_METRICS.md)
- [`docs/RLL_CLAIM_BOUNDARIES.md`](RLL_CLAIM_BOUNDARIES.md)
- [`rll_equation_registry.yml`](../rll_equation_registry.yml)

## 1.1) Casos observacionais

- [`docs/cases/AMAS_SOUTH_ATLANTIC_MAGNETIC_ANOMALY_RLL.md`](cases/AMAS_SOUTH_ATLANTIC_MAGNETIC_ANOMALY_RLL.md)
- [`docs/cases/SN2017egm_SUPERLUMINOUS_SUPERNOVA_MAGNETAR_ENGINE_RLL.md`](cases/SN2017egm_SUPERLUMINOUS_SUPERNOVA_MAGNETAR_ENGINE_RLL.md)

## 2) Governanca, organizacao e auditoria

- [`docs/DOCUMENTATION_ORGANIZATION_MASTER.md`](DOCUMENTATION_ORGANIZATION_MASTER.md)
- [`docs/CANONICAL_SOURCES.md`](CANONICAL_SOURCES.md)
- [`docs/POLITICA_REPOSITORIO_TEXTO_E_ARTEFATOS.md`](POLITICA_REPOSITORIO_TEXTO_E_ARTEFATOS.md) **(fonte oficial para formatos no core e publicacao de artefatos externos)**
- [`docs/RAFAELIA_REGIME_INDEX.md`](RAFAELIA_REGIME_INDEX.md) **(classificacao de regimes: formula, hipotese, dado, validacao, legado e simbolico)**
- [`docs/RELEASE_NOTES_HISTORY.md`](RELEASE_NOTES_HISTORY.md)
- [`docs/DOCUMENTATION_FULL_INVENTORY.md`](DOCUMENTATION_FULL_INVENTORY.md)
- [`docs/ZIP_CONTENT_INDEX.md`](ZIP_CONTENT_INDEX.md) *(inventario historico; nao normativo para armazenamento no core)*
- [`docs/DATA_INTEGRITY_CHECKLIST.md`](DATA_INTEGRITY_CHECKLIST.md)
- [`docs/ADMIN.md`](ADMIN.md)
- [`docs/AUDITORIA_DOCUMENTAL_E_DIRETORIOS_2026-03-05.md`](AUDITORIA_DOCUMENTAL_E_DIRETORIOS_2026-03-05.md)

## 3) Serie canonica consolidada (`docs/canonicos/`)

- [`docs/canonicos/00_COMO_LER.md`](canonicos/00_COMO_LER.md)
- [`docs/canonicos/06_COMPARACOES_DETALHADAS.md`](canonicos/06_COMPARACOES_DETALHADAS.md)
- [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- [`docs/canonicos/10_FAQ_COMPLETO.md`](canonicos/10_FAQ_COMPLETO.md)
- [`docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`](canonicos/11_DOCUMENTO_PRIORIDADE.md)
- [`docs/canonicos/12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md`](canonicos/12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md)

---

## 4) Validacao observacional e matriz de dados reais

- [`docs/VALIDATION_DATA_MATRIX_RLL_MCRP.md`](VALIDATION_DATA_MATRIX_RLL_MCRP.md)
- [`docs/cases/AMAS_SOUTH_ATLANTIC_MAGNETIC_ANOMALY_RLL.md`](cases/AMAS_SOUTH_ATLANTIC_MAGNETIC_ANOMALY_RLL.md)
- [`docs/cases/SN2017egm_SUPERLUMINOUS_SUPERNOVA_MAGNETAR_ENGINE_RLL.md`](cases/SN2017egm_SUPERLUMINOUS_SUPERNOVA_MAGNETAR_ENGINE_RLL.md)
- [`docs/pipelines/GEOMAGNETIC_VALIDATION_PIPELINE.md`](pipelines/GEOMAGNETIC_VALIDATION_PIPELINE.md)
- [`docs/pipelines/RADIATION_TRANSMISSION_VALIDATION.md`](pipelines/RADIATION_TRANSMISSION_VALIDATION.md)
- [`docs/pipelines/COSMOLOGY_VALIDATION_STACK.md`](pipelines/COSMOLOGY_VALIDATION_STACK.md)

---

## Arquivo/Legacy

> Materiais abaixo sao preservados por historico/rastreabilidade e **nao** sao a fonte oficial.

### Duplicatas historicas da serie canonica
- Duplicatas historicas mantidas para rastreabilidade (raiz, `RMR/` e `news/archive_legacy/`).
- Fonte oficial unica para consulta e citacao:
  - [`docs/canonicos/00_COMO_LER.md`](canonicos/00_COMO_LER.md)
  - [`docs/canonicos/06_COMPARACOES_DETALHADAS.md`](canonicos/06_COMPARACOES_DETALHADAS.md)
  - [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
  - [`docs/canonicos/10_FAQ_COMPLETO.md`](canonicos/10_FAQ_COMPLETO.md)
  - [`docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`](canonicos/11_DOCUMENTO_PRIORIDADE.md)
  - [`docs/canonicos/12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md`](canonicos/12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md)
- 00_COMO_LER.md -> [`docs/canonicos/00_COMO_LER.md`](canonicos/00_COMO_LER.md)
- 06_COMPARACOES_DETALHADAS.md -> [`docs/canonicos/06_COMPARACOES_DETALHADAS.md`](canonicos/06_COMPARACOES_DETALHADAS.md)
- 09_GLOSSARIO_COMPLETO.md -> [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- 09_GLOSSARIO_COMPLETO-1.md -> [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- 10_FAQ_COMPLETO.md -> [`docs/canonicos/10_FAQ_COMPLETO.md`](canonicos/10_FAQ_COMPLETO.md)
- 11_DOCUMENTO_PRIORIDADE.md -> [`docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`](canonicos/11_DOCUMENTO_PRIORIDADE.md)
- RMR/00_COMO_LER.md -> [`docs/canonicos/00_COMO_LER.md`](canonicos/00_COMO_LER.md)
- RMR/06_COMPARACOES_DETALHADAS.md -> [`docs/canonicos/06_COMPARACOES_DETALHADAS.md`](canonicos/06_COMPARACOES_DETALHADAS.md)
- RMR/09_GLOSSARIO_COMPLETO.md -> [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- RMR/09_GLOSSARIO_COMPLETO-1.md -> [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- RMR/10_FAQ_COMPLETO.md -> [`docs/canonicos/10_FAQ_COMPLETO.md`](canonicos/10_FAQ_COMPLETO.md)
- RMR/11_DOCUMENTO_PRIORIDADE.md -> [`docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`](canonicos/11_DOCUMENTO_PRIORIDADE.md)

### Arquivos de arquivo estendido
- [`news/archive_legacy/`](../news/archive_legacy/)
- [`docs/README_ROOT_LEGACY_ARCHIVE.md`](README_ROOT_LEGACY_ARCHIVE.md)
- Referencia canonica central desta navegacao: secao principal deste arquivo.
- Inventario bruto e completo (inclui historico/legado): [`docs/DOCUMENTATION_FULL_INVENTORY.md`](DOCUMENTATION_FULL_INVENTORY.md).
