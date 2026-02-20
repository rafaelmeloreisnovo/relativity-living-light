# Organização Integral de Documentação e Artefatos
## Relativity Living Light — estrutura técnica, canônica e auditável

**Versão:** 1.0 (reorganização documental integral)  
**Data:** 2026-02-20

---

## 1) Objetivo formal

Este documento estabelece um **mapa único de organização** para:
- documentos técnicos centrais;
- documentos autorais/conceituais;
- documentos soltos na raiz;
- artefatos compactados (`.zip`) e sua rastreabilidade.

A finalidade é eliminar ambiguidade, elevar governança do acervo e sustentar manutenção de longo prazo em padrão técnico-profissional avançado.

---

## 2) Arquitetura documental canônica

## 2.1 Trilhas oficiais

### A. Trilha científica (core)
**Uso:** validação, replicação, comparação observacional, leitura técnica primária.

Documentos de referência:
- `README.md`
- `docs/Relativity_Living_Light.md`
- `docs/BOOSTERS.md`
- `docs/Results.md`
- `docs/REFERENCES.md`
- `docs/ROADMAP_VALIDACAO.md`
- `docs/COMPARACAO_DESI_2025.md`

### B. Trilha de governança e organização
**Uso:** política de repositório, escopo, auditoria e evolução estrutural.

Documentos de referência:
- `docs/ADMIN.md`
- `GOVERNANCE_REORG_DRAFT.md`
- `SECURITY_SUMMARY.md`
- `REFORM_LOG.md`
- `docs/ANALISE_DIRETORIOS_E_MDS_SOLTOS.md`
- `docs/RELEASE_NOTES_HISTORY.md`

### C. Trilha autoral/conceitual expandida
**Uso:** contexto filosófico, manifesto, material simbólico e estrutura narrativa ampliada.

Documentos de referência:
- `docs/MANIFESTO.md`
- `docs/MAPA FRACTAL.md`
- `docs/MAPA CIENTIESPIRITUAL.md`
- `docs/SUPREMO UNIFICADO.md`
- `docs/IMPACT_REPORT_MULTI.md`
- `docs/numeros_rafaelianos/*.md`

---

## 3) Tratamento de documentos soltos na raiz

## 3.1 Diagnóstico
A raiz contém documentos válidos, porém heterogêneos em função (científica, resumo executivo, duplicatas históricas e ponteiros canônicos).

## 3.2 Diretriz de organização
- **Manter na raiz somente**: arquivos estruturantes do repositório e ponteiros de alto nível.
- **Centralizar evolução documental** em `docs/`.
- **Evitar duplicações ativas** entre raiz e `docs/`; preferir ponteiros para origem canônica.

## 3.3 Mapeamento recomendado (raiz → função)
- `README.md` → entrada principal do projeto.
- `README_MASTER.md` → visão consolidada de navegação.
- `REFORM_LOG.md` / `RESUMO_REFORMA.md` → histórico de reorganização.
- `COMPREHENSIVE_REPOSITORY_ANALYSIS.md` → análise sistêmica ampla.
- `00_COMO_LER.md`, `06_COMPARACOES_DETALHADAS.md`, `09_GLOSSARIO_COMPLETO.md`, `10_FAQ_COMPLETO.md`, `11_DOCUMENTO_PRIORIDADE.md` → ponteiros canônicos de leitura rápida.

---

## 4) Inventário técnico de artefatos compactados (.zip)

## 4.1 Arquivos localizados
1. `data/RelativityLivingLight_v4_bundle.zip`
2. `data/relativity_bundle_results.zip`
3. `docs/rll_revisado_v2.zip`

## 4.2 Observações de conteúdo e uso

### `data/RelativityLivingLight_v4_bundle.zip`
- Contém pacote de resultados (CSV, figuras principais, resumo sintético).
- Serve como snapshot operacional de geração de resultados.

### `data/relativity_bundle_results.zip`
- Conteúdo essencialmente equivalente ao bundle v4, com timestamps distintos.
- Recomendação: declarar explicitamente no changelog quando for substituto ou espelho.

### `docs/rll_revisado_v2.zip`
- Contém pacote revisado de documentação científica (`README_CIENTIFICO`, `ROADMAP_VALIDACAO`, `PAPER_CORRIGIDO`, etc.).
- Recomendação: manter checksum e data de geração em futuras revisões para cadeia de custódia documental.

---

## 5) Padrão de atualização contínua

1. Sempre que houver PR de documentação:
   - atualizar `docs/RELEASE_NOTES_HISTORY.md`;
   - registrar impacto e arquivos canônicos alterados.
2. Sempre que houver novo bundle zip:
   - atualizar seção de inventário;
   - registrar finalidade e diferença para bundles anteriores.
3. Para novos documentos técnicos:
   - inserir link no índice mestre (`docs/INDICE_MESTRE.md`);
   - classificar imediatamente em uma trilha (core, governança, autoral).

---

## 6) Sequência de leitura profissional recomendada

1. `README.md`
2. `docs/INDICE_MESTRE.md`
3. `docs/RELEASE_NOTES_HISTORY.md`
4. `docs/Results.md`
5. `docs/COMPARACAO_DESI_2025.md`
6. `docs/ROADMAP_VALIDACAO.md`
7. `docs/REFERENCES.md`

---

## 7) Resultado desta refatoração documental

- Histórico de updates/release notes com links e datas estabelecido.
- Mapa organizacional único para documentação e zips estabelecido.
- Critérios formais de continuidade e manutenção documental definidos.

---

## 8) Artefatos de varredura integral (controle total do acervo)

- Inventário total de documentação e bundles: [`docs/DOCUMENTATION_FULL_INVENTORY.md`](DOCUMENTATION_FULL_INVENTORY.md)
- Índice interno de conteúdo dos arquivos compactados: [`docs/ZIP_CONTENT_INDEX.md`](ZIP_CONTENT_INDEX.md)

Esses dois arquivos são a base objetiva para revisão integral, pois listam **todos** os `.md` e `.zip` detectados no repositório, com metadados de rastreabilidade.


## 9) Pendências identificadas na varredura completa

Arquivos Markdown vazios (ou praticamente vazios) detectados:

- `docs/1.md`
- `docs/Easy..md`
- `RMR/1.md`

Recomendação: converter em ponteiros canônicos (com link e contexto) ou remover em revisão futura para reduzir ruído estrutural.


## 10) Salvaguarda explícita de conteúdo legado

- Arquivo de preservação integral do README raiz anterior: [`docs/README_ROOT_LEGACY_ARCHIVE.md`](README_ROOT_LEGACY_ARCHIVE.md)
- Checklist técnico de integridade: [`docs/DATA_INTEGRITY_CHECKLIST.md`](DATA_INTEGRITY_CHECKLIST.md)

Esses artefatos reduzem risco de perda percebida, mantendo recuperação textual e auditoria objetiva por hash/tamanho.

## 11) Convenção de figuras (`figs/`)

### 11.1 Estrutura oficial
- `figs/paper/` → figuras ativas de artigos, preprints, LaTeX principal (`main.tex`) e documentação científica em uso.
- `figs/archive/` → screenshots, snapshots históricos, variações duplicadas (`(1)`, `(2)`, etc.) e material legado para rastreabilidade.

### 11.2 Convenção de nomenclatura
- Use nomes descritivos, minúsculos e estáveis para material de paper, por exemplo:
  - `unified_H_ratio.png`
  - `cluster_lensing_SIS_unified.png`
  - `fig_pipeline.png`
- Evitar novos nomes com sufixos automáticos de cópia (`(1)`, `(2)`, ...). Quando existirem, manter em `figs/archive/`.

### 11.3 Regra de destino
1. Figura nova para manuscrito, paper ou doc científico ativo: salvar em `figs/paper/`.
2. Screenshot de execução, imagem provisória, backup visual ou versão antiga: salvar em `figs/archive/`.
3. Ao substituir figura de paper, mover versão anterior para `figs/archive/` para preservar histórico.

