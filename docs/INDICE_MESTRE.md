# ÍNDICE MESTRE — Documentação Oficial
## Relativity Living Light

**Atualizado em:** 2026-03-05
**Regra:** seção principal lista apenas caminhos canônicos oficiais.

---

## Escopo deste arquivo

Este arquivo é a **navegação canônica** da documentação do repositório.

- Lista os caminhos oficiais por trilha temática.
- Atua como referência de navegação para leitura e manutenção.
- Não substitui o README (porta de entrada) e não tenta reproduzir o inventário bruto.

Encaminhamentos complementares:
- Porta de entrada: [`README.md`](../README.md)
- Inventário bruto (`.md` e `.zip`): [`docs/DOCUMENTATION_FULL_INVENTORY.md`](DOCUMENTATION_FULL_INVENTORY.md)
- Procedimento de atualização: `python3 tools/docs_inventory.py` e validação `python3 tools/docs_inventory.py --check`.

---


## Procedimento de atualização do inventário documental

1. Regenerar inventário completo publicado:

   ```bash
   python3 tools/docs_inventory.py
   ```

2. Validar contagem publicada vs. varredura real:

   ```bash
   python3 tools/docs_inventory.py --check
   ```

3. Confirmar no cabeçalho do inventário: data/hora, commit de referência e total.

---

## 1) Núcleo científico oficial

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
- [`docs/FORMULAS_CANONICAS_INDEX.md`](FORMULAS_CANONICAS_INDEX.md) ← referência oficial de fórmulas

## 2) Governança, organização e auditoria

- [`docs/DOCUMENTATION_ORGANIZATION_MASTER.md`](DOCUMENTATION_ORGANIZATION_MASTER.md)
- [`docs/CANONICAL_SOURCES.md`](CANONICAL_SOURCES.md)
- [`docs/POLITICA_REPOSITORIO_TEXTO_E_ARTEFATOS.md`](POLITICA_REPOSITORIO_TEXTO_E_ARTEFATOS.md) **(fonte oficial para formatos no core e publicação de artefatos externos)**
- [`docs/RELEASE_NOTES_HISTORY.md`](RELEASE_NOTES_HISTORY.md)
- [`docs/DOCUMENTATION_FULL_INVENTORY.md`](DOCUMENTATION_FULL_INVENTORY.md)
- [`docs/ZIP_CONTENT_INDEX.md`](ZIP_CONTENT_INDEX.md) *(inventário histórico; não normativo para armazenamento no core)*
- [`docs/DATA_INTEGRITY_CHECKLIST.md`](DATA_INTEGRITY_CHECKLIST.md)
- [`docs/ADMIN.md`](ADMIN.md)
- [`docs/AUDITORIA_DOCUMENTAL_E_DIRETORIOS_2026-03-05.md`](AUDITORIA_DOCUMENTAL_E_DIRETORIOS_2026-03-05.md)

## 3) Série canônica consolidada (`docs/canonicos/`)

- [`docs/canonicos/00_COMO_LER.md`](canonicos/00_COMO_LER.md)
- [`docs/canonicos/06_COMPARACOES_DETALHADAS.md`](canonicos/06_COMPARACOES_DETALHADAS.md)
- [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- [`docs/canonicos/10_FAQ_COMPLETO.md`](canonicos/10_FAQ_COMPLETO.md)
- [`docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`](canonicos/11_DOCUMENTO_PRIORIDADE.md)
- [`docs/canonicos/12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md`](canonicos/12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md)

---


## 4) Validação observacional e matriz de dados reais

- [`docs/VALIDATION_DATA_MATRIX_RLL_MCRP.md`](VALIDATION_DATA_MATRIX_RLL_MCRP.md)
- [`docs/cases/AMAS_SOUTH_ATLANTIC_MAGNETIC_ANOMALY_RLL.md`](cases/AMAS_SOUTH_ATLANTIC_MAGNETIC_ANOMALY_RLL.md)
- [`docs/pipelines/GEOMAGNETIC_VALIDATION_PIPELINE.md`](pipelines/GEOMAGNETIC_VALIDATION_PIPELINE.md)
- [`docs/pipelines/RADIATION_TRANSMISSION_VALIDATION.md`](pipelines/RADIATION_TRANSMISSION_VALIDATION.md)
- [`docs/pipelines/COSMOLOGY_VALIDATION_STACK.md`](pipelines/COSMOLOGY_VALIDATION_STACK.md)

---

## Arquivo/Legacy

> Materiais abaixo são preservados por histórico/rastreabilidade e **não** são a fonte oficial.

### Duplicatas históricas da série canônica
- Duplicatas históricas mantidas para rastreabilidade (raiz, `RMR/` e `news/archive_legacy/`).
- Fonte oficial única para consulta e citação:
  - [`docs/canonicos/00_COMO_LER.md`](canonicos/00_COMO_LER.md)
  - [`docs/canonicos/06_COMPARACOES_DETALHADAS.md`](canonicos/06_COMPARACOES_DETALHADAS.md)
  - [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
  - [`docs/canonicos/10_FAQ_COMPLETO.md`](canonicos/10_FAQ_COMPLETO.md)
  - [`docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`](canonicos/11_DOCUMENTO_PRIORIDADE.md)
  - [`docs/canonicos/12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md`](canonicos/12_DOCUMENTO_CANONICO_RLL_PREPRINT_PTBR.md)
- 00_COMO_LER.md → [`docs/canonicos/00_COMO_LER.md`](canonicos/00_COMO_LER.md)
- 06_COMPARACOES_DETALHADAS.md → [`docs/canonicos/06_COMPARACOES_DETALHADAS.md`](canonicos/06_COMPARACOES_DETALHADAS.md)
- 09_GLOSSARIO_COMPLETO.md → [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- 09_GLOSSARIO_COMPLETO-1.md → [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- 10_FAQ_COMPLETO.md → [`docs/canonicos/10_FAQ_COMPLETO.md`](canonicos/10_FAQ_COMPLETO.md)
- 11_DOCUMENTO_PRIORIDADE.md → [`docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`](canonicos/11_DOCUMENTO_PRIORIDADE.md)
- RMR/00_COMO_LER.md → [`docs/canonicos/00_COMO_LER.md`](canonicos/00_COMO_LER.md)
- RMR/06_COMPARACOES_DETALHADAS.md → [`docs/canonicos/06_COMPARACOES_DETALHADAS.md`](canonicos/06_COMPARACOES_DETALHADAS.md)
- RMR/09_GLOSSARIO_COMPLETO.md → [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- RMR/09_GLOSSARIO_COMPLETO-1.md → [`docs/canonicos/09_GLOSSARIO_COMPLETO.md`](canonicos/09_GLOSSARIO_COMPLETO.md)
- RMR/10_FAQ_COMPLETO.md → [`docs/canonicos/10_FAQ_COMPLETO.md`](canonicos/10_FAQ_COMPLETO.md)
- RMR/11_DOCUMENTO_PRIORIDADE.md → [`docs/canonicos/11_DOCUMENTO_PRIORIDADE.md`](canonicos/11_DOCUMENTO_PRIORIDADE.md)

### Arquivos de arquivo estendido
- [`news/archive_legacy/`](../news/archive_legacy/)
- [`docs/README_ROOT_LEGACY_ARCHIVE.md`](README_ROOT_LEGACY_ARCHIVE.md)
- Referência canônica central desta navegação: seção principal deste arquivo.
- Inventário bruto e completo (inclui histórico/legado): [`docs/DOCUMENTATION_FULL_INVENTORY.md`](DOCUMENTATION_FULL_INVENTORY.md).
