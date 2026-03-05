# Análise dos diretórios `docs/` e MDs soltos

## Escopo revisado

- Diretório principal `docs/`
- MDs soltos na raiz do repositório
- MDs em subpastas já versionadas (ex.: `ANALISE_COMPLETA/`, `RMR/`)

## Tipologia objetiva dos documentos

### 1) Núcleo técnico (prioridade de referência)

Arquivos com valor técnico direto para leitura científica e reprodutibilidade:

- `docs/Relativity_Living_Light.md`
- `docs/BOOSTERS.md`
- `docs/Results.md`
- `docs/estatisticas.md`
- `docs/REFERENCES.md`
- `docs/DATA_DESCRIPTOR_BUNDLE_V4.md` / `README.md`

**Uso recomendado:** manter este bloco como trilha principal para validação do modelo, parâmetros e comparação com dados.

### 2) Análises de posicionamento e comparação

Arquivos úteis para contexto histórico/estratégico, mas que não substituem validação observacional:

- `06_COMPARACOES_DETALHADAS.md`
- `11_DOCUMENTO_PRIORIDADE.md`
- `ANALISE_COMPLETA/*.md`
- `docs/ARTICLE_ANALYSIS_SUMMARY.md`
- `docs/NATURE_ARTICLE_ANALYSIS.md`

**Uso recomendado:** manter como material complementar e separar claramente de “resultado científico principal”.

### 3) Documentos conceituais/simbólicos

Arquivos de manifesto e narrativa autoral:

- `docs/MANIFESTO.md`
- `docs/MAPA FRACTAL.md`
- `docs/MAPA CIENTIESPIRITUAL.md`
- `docs/SUPREMO UNIFICADO.md`
- `docs/IMPACT_REPORT_MULTI.md`
- `docs/FRACTAL_LAYERED_MAP.md`
- `docs/THEORY_INVENTORY_AND_EXTENSIONS.md`
- `docs/FRACTAL_REPORT_UNIFIED.md`

**Uso recomendado:** manter separados do fluxo técnico principal para não misturar escopo científico com escopo conceitual.

## Leitura prática sugerida (ordem curta)

1. `README.md`
2. `docs/Relativity_Living_Light.md`
3. `docs/BOOSTERS.md`
4. `docs/Results.md`
5. `docs/estatisticas.md`
6. `docs/REFERENCES.md`

## Próxima ação de organização documental

- Criar/ajustar um índice único em `docs/` com duas trilhas explícitas:
  - **Trilha científica (core)**
  - **Trilha conceitual/autoral (extended)**
- Garantir que resultados numéricos canônicos apontem sempre para `data/posterior_unified_synth.csv`.

## Atualização de cobertura integral (varredura completa)

Para garantir leitura/organização total do acervo (incluindo arquivos soltos e compactados), a revisão foi ampliada com dois artefatos técnicos complementares:

- `docs/DOCUMENTATION_FULL_INVENTORY.md` — inventário de **todos** os arquivos `.md` e `.zip` do repositório.
- `docs/ZIP_CONTENT_INDEX.md` — listagem interna de conteúdo dos bundles `.zip`.

Com isso, a governança documental deixa de ser apenas orientativa e passa a ser verificável por catálogo completo.

## Salvaguarda contra perda de conteúdo (adendo)

Para evitar qualquer percepção de descarte de informação:

- README raiz anterior preservado integralmente em `docs/README_ROOT_LEGACY_ARCHIVE.md`.
- Checklist objetivo de integridade em `docs/DATA_INTEGRITY_CHECKLIST.md`.

Isso garante trilha de recuperação textual + verificação por metadados (tamanho/hash).
