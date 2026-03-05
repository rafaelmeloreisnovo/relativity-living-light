# 31. Roadmap — Curto Prazo

[⬅️ Capítulo anterior](./30_governanca_releases_reformas.md) | [📚 Sumário do livro](./README.md) | [Capítulo próximo ➡️](./32_roadmap_medio_longo_prazo.md)

Entregas imediatas para sair de Parcial real rumo a Real validado.

## Conteúdo incorporado (itens soltos/localizados)
Documentos e artefatos relacionados incorporados nesta etapa:

- docs/ROADMAP_VALIDACAO.md
- 11_DOCUMENTO_PRIORIDADE.md
- docs/11_DOCUMENTO_PRIORIDADE.md

## Notas de consolidação
- Este capítulo funciona como nó canônico para evitar dispersão de arquivos soltos.
- Atualize este capítulo quando novos materiais da mesma temática forem adicionados ao repositório.

## Task única priorizada

### [ ] Validação preditiva pós-publicação (DR2/Okada/CMB dipolo)

**Escopo estruturado (transcrição dos blocos já descritos):**

1. **Antecipação temporal (Fev/2025 vs Dez/2025 vs Jan/2026)**
   - **Fev/2025:** formulação registrada no repositório (hipótese de transição e base analítica do modelo).
   - **Dez/2025 (DESI DR2):** evidência observacional de `w(z)` dinâmico em combinação BAO+CMB+SNe.
   - **Jan/2026 (Okada/PRL):** cenário de matéria escura quente→fria convergente com o comportamento assintótico de `f(z)`.

2. **Evidências pós-modelo (DESI DR2, Okada PRL, não-localidade fotônica)**
   - **DESI DR2:** convergência qualitativa com `w_eff(z)` dinâmico e necessidade de conexão quantitativa direta.
   - **Okada PRL:** convergência física com a transição quente→fria já reproduzida analiticamente por `f(z)`.
   - **Nature Comms. (não-localidade fotônica):** base conceitual para microfísica de superposição; extrapolação cosmológica ainda exige derivação de escala rigorosa.

3. **Hipóteses falsificáveis pendentes**
   - Consolidar teste quantitativo RLL↔ΛCDM/CPL com dados reais (sem depender de validação apenas qualitativa).
   - Implementar e testar a extensão anisotrópica `f(z,θ,φ)` para o dipolo de `5.4σ` reportado em CMB/estrutura.

**Entregáveis objetivos (nesta task):**

- Rodar ajuste **MCMC** com **DESI DR2 + BAO** no pipeline canônico.
- Calcular **`ln B` vs ΛCDM** (Bayes factor em log) com protocolo reproduzível.
- Reportar constraints para:
  - `w_eff(z=0)`
  - `z_t`
  - parâmetro anisotrópico direcional da extensão `f(z,θ,φ)`.

**Critérios de aceite explícitos:**

- Tabela final com parâmetros inferidos + incertezas (intervalos credíveis definidos).
- Valor de **`ln B`** reproduzível a partir dos artefatos versionados.
- Decisão binária de avanço:
  - **“publicável”** se `ln B > 5`
  - **“revisar modelo”** caso contrário.

**Pontos de implementação já existentes (referências para execução):**

- Código: `src/rll/`
- Metodologia de pipeline de validação: `book/11_metodologia_pipeline_validacao.md`
- Metodologia de dados reais: `book/13_metodologia_dados_reais.md`
- Metodologia de notebooks e scripts: `book/14_metodologia_notebooks_scripts.md`

---
