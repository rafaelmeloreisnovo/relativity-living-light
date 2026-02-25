# ÍNDICE MESTRE — Pacote de Revisão Científica
## Relativity Living Light v2.0

**Gerado em:** Fevereiro 2026  
**Propósito:** Versão revisada e consistente do repositório, pronta para validação com dados reais e submissão ao arXiv

---

## Governança de atualização e organização (novo)

- Histórico cronológico de updates/releases (com links, datas e mudanças):
  - [`docs/RELEASE_NOTES_HISTORY.md`](RELEASE_NOTES_HISTORY.md)
- Organização integral de documentos, arquivos soltos e bundles `.zip`:
  - [`docs/DOCUMENTATION_ORGANIZATION_MASTER.md`](DOCUMENTATION_ORGANIZATION_MASTER.md)
- Inventário completo (todos os `.md` e `.zip` catalogados):
  - [`docs/DOCUMENTATION_FULL_INVENTORY.md`](DOCUMENTATION_FULL_INVENTORY.md)
- Índice interno dos bundles compactados:
  - [`docs/ZIP_CONTENT_INDEX.md`](ZIP_CONTENT_INDEX.md)
- Preservação integral do README histórico (arquivo legado completo):
  - [`docs/README_ROOT_LEGACY_ARCHIVE.md`](README_ROOT_LEGACY_ARCHIVE.md)
- Auditoria rápida de integridade de dados/documentos:
  - [`docs/DATA_INTEGRITY_CHECKLIST.md`](DATA_INTEGRITY_CHECKLIST.md)
- Referência operacional:
  - Pipeline oficial de prova observacional (Pantheon+ RLL vs ΛCDM, validações e formato canônico de saídas):
    - [`docs/ROADMAP_VALIDACAO.md`](ROADMAP_VALIDACAO.md)
- Diagnóstico de lacunas para padrão pós-PhD formal/profissional:
  - [`docs/POST_PHD_FORMAL_GAP_ANALYSIS.md`](POST_PHD_FORMAL_GAP_ANALYSIS.md)
- Plano estratégico A→B→C→D (JWST/AGN/SMBH) com checklist operacional:
  - [`docs/PLANO_ABCD_JWST_AGN_SMBH.md`](PLANO_ABCD_JWST_AGN_SMBH.md)
  - [Subseção “Teste discriminante primário” (âncora interna)](PLANO_ABCD_JWST_AGN_SMBH.md#teste-discriminante-primario)

---

## Estrutura do Pacote

```
rll_revisado_v2/
│
├── README_CIENTIFICO.md          ← Ponto de entrada principal (substitui README.md)
├── ROADMAP_VALIDACAO.md          ← 7 prioridades ordenadas por impacto
├── requirements.txt              ← Dependências Python
│
├── docs/
│   ├── RESULTADOS_CORRIGIDOS.md  ← Parâmetros reais do CSV (Ω_s0=0.059, z_t=1.164)
│   ├── PAPER_CORRIGIDO.tex       ← Preprint LaTeX com valores consistentes
│   └── COMPARACAO_DESI_2025.md   ← Cruzamento honesto com literatura 2025-26
│
├── teoria/
│   ├── EXTENSAO_ANISOTROPICA.md  ← f(z,θ,φ) para dipolo Böhme — maior potencial
│   ├── PERTURBACOES_CRESCIMENTO.md ← Equação D''(a), fσ₈(z), dados BOSS
│   ├── VELOCIDADE_SOM.md         ← cs²(z), escala de Jeans
│   ├── LAGRANGIANO_EFT.md        ← Formalismo de campo escalar
│   └── ESTABILIDADE_GHOST_CHECK.md ← Critérios anti-ghost e anti-taquião
│
├── codigo/
│   ├── crescimento_estrutural.py ← Solver D''(a) + figura fσ₈ vs BOSS
│   ├── panteon_likelihood.py     ← Template MCMC para Pantheon+ real
│   └── fisher_forecast.py        ← Previsão de erros DESI/Euclid
│
└── data/
    └── CITATION.cff              ← Metadados de citação corrigidos
```

---

## Correções Aplicadas em Relação à Versão Anterior

**Valores de parâmetros:** Os valores MAP reportados anteriormente (Ω_s0=0.72, z_t=0.65, w_t=−0.97) foram substituídos pelos valores reais extraídos do CSV:

```
Ω_s0 = 0.059  [0.048 – 0.071]  (mediana, 68% CR)
z_t  = 1.164  [0.882 – 1.430]
w_t  = 0.405  [0.271 – 0.534]
```

**Transparência sobre dados:** Todos os documentos agora identificam explicitamente que os resultados atuais derivam de dados sintéticos. Esta transparência é necessária para credibilidade acadêmica.

**Equação de estado corrigida:** O `BOOSTERS.md` original identificou corretamente a inconsistência em w_eff. A formulação correta `w_eff,sup = −f(z)` é usada consistentemente neste pacote.

---

## Arquivos do Repositório Original que Permanecem Válidos

Os seguintes arquivos do repositório original não necessitam de revisão e devem ser mantidos:

- `data/posterior_unified_synth.csv` — dados brutos corretos
- `data/relativity_living_light_models.csv` — grid de modelos
- `figs/paper/*.png` — figuras geradas dos dados sintéticos
- `data/Hz_superposicao.ipynb` — notebook de análise H(z)
- `docs/BOOSTERS.md` — documentação técnica dos boosters (contém autocorrição valiosa)

---

## O Que Este Pacote Não Contém

**Conteúdo simbólico e espiritual:** Os documentos `SUPREMO UNIFICADO.md`, `MAPA CIENTIESPIRITUAL.md`, `numeros_rafaelianos/`, `MANIFESTO.md` e similares não foram incluídos neste pacote técnico. Esses documentos têm valor como obra autoral e manifesto pessoal, mas prejudicam a credibilidade científica quando misturados ao canal técnico do repositório.

**Afirmações de prioridade:** As comparações estilo "Rafael fez primeiro" foram substituídas por análise factual de convergência de ideias com distinção explícita entre precedência de commit e prioridade acadêmica formal.

**Projeções de mercado sem base:** As tabelas com valores USD 5B–10B foram removidas por não possuírem metodologia de avaliação.

---

## Próximo Passo Recomendado

Executar `codigo/crescimento_estrutural.py` com os parâmetros centrais do posterior. Isso gera o primeiro resultado com dados reais parciais (BOSS DR12 fσ₈) e é o caminho mais rápido para sair do estado "dados sintéticos" e obter uma comparação observacional genuína.

```bash
cd codigo/
python crescimento_estrutural.py
```

A figura gerada (`figs/paper/fs8_comparison_RLL_vs_LCDM.png`) pode ser incluída imediatamente no preprint revisado.
