# Histórico de Updates e Release Notes
## Relativity Living Light — trilha cronológica com data, escopo e evidência

**Objetivo:** consolidar, em formato auditável, os principais ciclos de evolução do repositório com links diretos para commits e pull requests.

**Repositório de referência:** <https://github.com/instituto-Rafael/relativity-living-light>

---

## 1) Linha do tempo executiva (macro releases)

| Data | Marco | Evidência | O que mudou (síntese técnica) |
|---|---|---|---|
| 2026-02-20 (hotfix) | **Salvaguarda de conteúdo legado + checklist de integridade** | [docs/README_ROOT_LEGACY_ARCHIVE.md](README_ROOT_LEGACY_ARCHIVE.md) · [docs/DATA_INTEGRITY_CHECKLIST.md](DATA_INTEGRITY_CHECKLIST.md) | Arquivamento do README anterior completo e criação de checklist de integridade para reduzir risco de perda de dados. |
| 2026-02-20 (atual) | **Varredura integral de documentação e bundles** | [docs/RELEASE_NOTES_HISTORY.md](RELEASE_NOTES_HISTORY.md) · [docs/DOCUMENTATION_FULL_INVENTORY.md](DOCUMENTATION_FULL_INVENTORY.md) · [docs/ZIP_CONTENT_INDEX.md](ZIP_CONTENT_INDEX.md) | Inventário completo de `.md` e `.zip`, índice interno de bundles e reforço de governança com rastreabilidade total. |
| 2026-02-20 (data-integrity) | **Canonização do posterior sintético e limpeza de duplicatas** | [docs/DATA_INTEGRITY_CHECKLIST.md](DATA_INTEGRITY_CHECKLIST.md) · [docs/RELEASE_NOTES_HISTORY.md](RELEASE_NOTES_HISTORY.md) | `data/posterior_unified_synth.csv` definido como arquivo canônico; remoção de `posterior_unified_synth (1|2).csv` e atualização de referências em docs. |
| 2025-09-02 → 2025-09-25 | Fundação documental e primeira consolidação de conteúdo | [Commits iniciais](https://github.com/instituto-Rafael/relativity-living-light/commits/main/?since=2025-09-01&until=2025-09-26) | Estrutura base, README iterativo, criação de documentos temáticos e primeiros artefatos científicos. |
| 2025-10-19 | **Reorganização estrutural RAFAELIA** | [PR #1](https://github.com/instituto-Rafael/relativity-living-light/pull/1) · [8d49cba](https://github.com/instituto-Rafael/relativity-living-light/commit/8d49cba) | Migração para organização por domínios (`docs/`, `data/`, `figs/paper/`), com inventário e documentação de reforma. |
| 2025-11-04 | **Pacote de análise Nature + integração conceitual** | [PR #2](https://github.com/instituto-Rafael/relativity-living-light/pull/2) · [5c9e74f](https://github.com/instituto-Rafael/relativity-living-light/commit/5c9e74f) | Inclusão de análise aprofundada do artigo Nature, novos índices de leitura e trilha técnico-conceitual multilíngue. |
| 2025-12-18 | **Governança e arquitetura documental** | [PR #3](https://github.com/instituto-Rafael/relativity-living-light/pull/3) · [9447f5d](https://github.com/instituto-Rafael/relativity-living-light/commit/9447f5d) | Auditoria de governança, draft de reorganização e critérios para evolução disciplinada do acervo. |
| 2026-01-04 | **Análise integral do repositório (nível enciclopédico)** | [PR #4](https://github.com/instituto-Rafael/relativity-living-light/pull/4) · [1d72696](https://github.com/instituto-Rafael/relativity-living-light/commit/1d72696) | Catálogo ampliado, hierarquia em níveis, métricas e revisão de consistência de links/citações. |
| 2026-01-09 | **Reforço técnico dos boosters e correções de fórmula** | [PR #5](https://github.com/instituto-Rafael/relativity-living-light/pull/5) · [07bc36e](https://github.com/instituto-Rafael/relativity-living-light/commit/07bc36e) | Documentação formal de boosters, ajustes de notação e correção da equação de estado. |
| 2026-02-20 | **Ciclo de saneamento científico e canonização documental** | [PR #6](https://github.com/instituto-Rafael/relativity-living-light/pull/6) · [PR #7](https://github.com/instituto-Rafael/relativity-living-light/pull/7) · [PR #8](https://github.com/instituto-Rafael/relativity-living-light/pull/8) · [PR #9](https://github.com/instituto-Rafael/relativity-living-light/pull/9) · [PR #10](https://github.com/instituto-Rafael/relativity-living-light/pull/10) | Refino de `Results`, padronização de equações, separação de escopos (scientific-core vs simbólico-jurídico) e definição de documentos canônicos com ponteiros. |

---

## 2) Release notes detalhadas por ciclo

### Release 2025.10 — Reestruturação sistêmica
- **Data de referência:** 2025-10-19
- **Commits-chave:**
  - [8d49cba](https://github.com/instituto-Rafael/relativity-living-light/commit/8d49cba) — Restructure repository following RAFAELIA principles
  - [d0ba960](https://github.com/instituto-Rafael/relativity-living-light/commit/d0ba960) — Add comprehensive reform summary
  - [88166c6](https://github.com/instituto-Rafael/relativity-living-light/commit/88166c6) — Add security summary and complete restructuring
- **Impacto:** padronização de layout, redução de ambiguidade de localização de arquivos e fortalecimento da rastreabilidade.

### Release 2025.11 — Análise científica ampliada
- **Data de referência:** 2025-11-04
- **Commits-chave:**
  - [5c9e74f](https://github.com/instituto-Rafael/relativity-living-light/commit/5c9e74f) — Add comprehensive Nature article analysis and documentation
  - [60ac578](https://github.com/instituto-Rafael/relativity-living-light/commit/60ac578) — Add Portuguese analysis and comprehensive documentation index
  - [3a1121f](https://github.com/instituto-Rafael/relativity-living-light/commit/3a1121f) — Complete Nature article analysis
- **Impacto:** elevação da profundidade analítica e estruturação de trilha de leitura especializada.

### Release 2025.12 — Governança e controle de qualidade documental
- **Data de referência:** 2025-12-18
- **Commits-chave:**
  - [9447f5d](https://github.com/instituto-Rafael/relativity-living-light/commit/9447f5d) — docs: add governance audit draft
  - [8d4abdf](https://github.com/instituto-Rafael/relativity-living-light/commit/8d4abdf) — docs: refine governance audit draft
- **Impacto:** critérios de revisão e governança explícita para evolução sustentável do repositório.

### Release 2026.01 — Consolidação enciclopédica e precisão de referências
- **Data de referência:** 2026-01-04
- **Commits-chave:**
  - [1d72696](https://github.com/instituto-Rafael/relativity-living-light/commit/1d72696) — Add comprehensive analysis directory
  - [7f50acd](https://github.com/instituto-Rafael/relativity-living-light/commit/7f50acd) — Complete comprehensive analysis with 14 thematic areas
  - [1922a9f](https://github.com/instituto-Rafael/relativity-living-light/commit/1922a9f) — Add comprehensive file-by-file catalog
  - [8b66ef8](https://github.com/instituto-Rafael/relativity-living-light/commit/8b66ef8) — Final consistency fix
- **Impacto:** maturidade de documentação para leitura técnica extensiva, auditoria e manutenção.

### Release 2026.01b — Boosters e formalismo da equação de estado
- **Data de referência:** 2026-01-09
- **Commits-chave:**
  - [bade667](https://github.com/instituto-Rafael/relativity-living-light/commit/bade667) — Add comprehensive boosters documentation
  - [e4aa77e](https://github.com/instituto-Rafael/relativity-living-light/commit/e4aa77e) — Update boosters links/references
  - [07bc36e](https://github.com/instituto-Rafael/relativity-living-light/commit/07bc36e) — Fix equation of state formula
- **Impacto:** clareza matemática e robustez da documentação de performance/boosters.

### Release 2026.02 — Saneamento, canonização e separação de escopos
- **Data de referência:** 2026-02-20
- **Commits-chave:**
  - [6ec0f3d](https://github.com/instituto-Rafael/relativity-living-light/commit/6ec0f3d) — Results com destaque ao posterior_unified_synth
  - [74e1f75](https://github.com/instituto-Rafael/relativity-living-light/commit/74e1f75) — refino estatístico e inventário de MDs
  - [c7dbee0](https://github.com/instituto-Rafael/relativity-living-light/commit/c7dbee0) — padronização de equação de estado
  - [335dbb4](https://github.com/instituto-Rafael/relativity-living-light/commit/335dbb4) — scientific-core scope + split simbólico-jurídico
  - [39d5693](https://github.com/instituto-Rafael/relativity-living-light/commit/39d5693) — consolidação de documentos canônicos
- **Impacto:** redução de duplicidade, governança de escopo e melhoria de integridade documental.


### Release 2026.02b — Varredura integral de documentação e artefatos
- **Data de referência:** 2026-02-20
- **Entregas-chave:**
  - `docs/DOCUMENTATION_FULL_INVENTORY.md` — catálogo de todos os `.md` e `.zip`
  - `docs/ZIP_CONTENT_INDEX.md` — listagem interna de cada bundle
  - Integração aos índices mestres e governança documental
- **Impacto:** cobertura integral do acervo, redução de lacunas de leitura e base objetiva para manutenção contínua.



### Release 2026.02d — Canonização de dataset e remoção de duplicatas nominais
- **Data de referência:** 2026-02-20
- **Entregas-chave:**
  - `data/posterior_unified_synth.csv` mantido como fonte canônica de posterior sintético.
  - Remoção de `data/posterior_unified_synth (1).csv` e `data/posterior_unified_synth (2).csv`.
  - Atualização de referências documentais para uso exclusivo do caminho canônico.
- **Impacto:** eliminação de ambiguidade de origem de dados, menor risco de deriva documental e rastreabilidade mais forte do pipeline analítico.

### Release 2026.02c — Salvaguarda de conteúdo legado e integridade
- **Data de referência:** 2026-02-20
- **Entregas-chave:**
  - `docs/README_ROOT_LEGACY_ARCHIVE.md` — preservação integral do README anterior
  - `docs/DATA_INTEGRITY_CHECKLIST.md` — auditoria por presença/tamanho/hash
- **Impacto:** proteção explícita contra perda de conteúdo e validação rápida do acervo crítico.

---

## 3) Política recomendada de versionamento documental (a partir desta revisão)

1. **Cada PR relevante** deve atualizar este histórico com:
   - data;
   - links para PR/commit;
   - escopo e impacto verificável.
2. **Cada release semântica documental** deve ter rótulo `YYYY.MM` (ex.: `2026.02`).
3. **Mudanças canônicas** devem sempre apontar para documentos-fonte (evitar cópias divergentes).
4. **Bundles `.zip`** devem manter nota de conteúdo e data de geração em índice documental único, com checklist de aceitação concluído para promoção ao tronco principal (seção 5).

---

## 4) Relação com documentação complementar

- Índice de organização integral: [`docs/DOCUMENTATION_ORGANIZATION_MASTER.md`](DOCUMENTATION_ORGANIZATION_MASTER.md)
- Índice mestre científico: [`docs/INDICE_MESTRE.md`](INDICE_MESTRE.md)
- Log de reforma estrutural prévio: [`REFORM_LOG.md`](../REFORM_LOG.md)

## 5) Checklist de aceitação para promoção de bundle ao tronco principal

**Objetivo:** bloquear integração de bundles incompletos no fluxo de release documental/técnico.

- [ ] **Links válidos:** README e documentos do bundle apontam apenas para caminhos existentes no repositório de destino.
- [ ] **Sem duplicação de pipeline:** não introduz versões paralelas de scripts/datasets já canonizados sem justificativa e sem plano de migração.
- [ ] **Caminhos canônicos definidos:** cada artefato crítico promovido possui caminho final único documentado em `docs/ZIP_CONTENT_INDEX.md`.
- [ ] **Hash registrado:** SHA-256 do bundle registrado no índice técnico de conteúdo antes da promoção.
- [ ] **Status de integração atualizado:** estado do bundle marcado como `não iniciado`, `em progresso` ou `concluído` no índice.

### Vinculação com fluxo de releases

Este checklist passa a ser **gate obrigatório** das releases que envolvem ingestão de bundles. Antes de fechar a release, a validação deve ser registrada em:

1. `docs/ZIP_CONTENT_INDEX.md` (registro técnico do bundle e status de integração).
2. `docs/RELEASE_NOTES_HISTORY.md` (entrada da release com escopo/impacto e referência ao bundle promovido).


## 6) Checklist editorial obrigatório (mudança de equação base)

Quando houver alteração em equação base, convenção de sinais, definição de `f(z)`, `w_sup` ou `w_total`, executar obrigatoriamente:

- [ ] Revisar `docs/canonicos/CONVENCOES_GLOBAIS_RLL.md`.
- [ ] Revisar glossário canônico (`docs/canonicos/09_GLOSSARIO_COMPLETO.md`).
- [ ] Revisar FAQ canônico (`docs/canonicos/10_FAQ_COMPLETO.md`).
- [ ] Revisar README raiz (`README.md`).
- [ ] Revisar trilha PhD (`newadd/*`, com prioridade para `00_INDICE_ANALISE_PHD.md`, `01_RLL_DESI_CrossAnalysis_PhD.md`, `03_Descricao_Academica_PhD_Completa.md`).
- [ ] Revisar comparativos (`docs/canonicos/06_COMPARACOES_DETALHADAS.md`, `docs/COMPARACAO_DESI_2025.md`).

### Gate automático simples (CI/documentação)

Rodar o detector de padrões contraditórios antes de fechar release/PR:

```bash
scripts/check_convention_conflicts.sh
```

Critério de reprovação: presença de strings de risco (ex.: `1→DE, 0→DM`) no mesmo arquivo em que aparece a forma logística canônica, sem contextualização de legado/hipótese.
