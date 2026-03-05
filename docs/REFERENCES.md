# Referências Canônicas — Relativity Living Light

Este arquivo define a organização fixa de referências do repositório em duas classes:

- `INT-*` → fontes internas do próprio repositório.
- `EXT-*` → literatura externa (papers, livros, notícias, preprints, bases e ferramentas externas).

## Fontes internas do repositório

- **INT-001** — `README_patch_unified_PT_EN_v4.md` (framework técnico do modelo).
- **INT-002** — `relativity_living_light_models.csv` e `unified_entropy_margin_10_12.csv` (resultados computacionais).
- **INT-003** — `NATURE_ARTICLE_ANALYSIS.md` (análise principal do artigo da Nature).
- **INT-004** — `ARTICLE_ANALYSIS_SUMMARY.md` (resumo da análise).
- **INT-005** — `CONCEPTUAL_FRAMEWORK.md` (diagramas/conceitos de apoio).

## Literatura externa

- **EXT-001** — Nonlocality-enabled photonic analogies of parallel spaces. *Nature Communications* (2025). DOI: 10.1038/s41467-025-63981-3.
- **EXT-002** — Bell (1964), EPR paradox and nonlocality.
- **EXT-003** — Aspect, Dalibard & Roger (1982), Bell inequalities (PRL).
- **EXT-004** — Gisin (2014), *Quantum Chance*.
- **EXT-005** — Mandel & Wolf (1995), *Optical Coherence and Quantum Optics*.
- **EXT-006** — Klaers et al. (2010), Bose-Einstein condensation of photons.
- **EXT-007** — Weinberg (1989), cosmological constant problem.
- **EXT-008** — Peebles & Ratra (2003), dark energy review.
- **EXT-009** — Bertone, Hooper & Silk (2005), dark matter review.
- **EXT-010** — Planck Collaboration (2020), cosmological parameters.
- **EXT-011** — DESI Collaboration (2024), BAO cosmological constraints (preprint).
- **EXT-012** — DES Collaboration (2022), Y3 cosmological constraints.
- **EXT-013** — Castelvecchi (2025), *Nature News* sobre dark energy.
- **EXT-014** — Milgrom (1983), MOND.
- **EXT-015** — De Felice & Tsujikawa (2010), f(R) theories.
- **EXT-016** — Caldwell, Dave & Steinhardt (1998), quintessence.
- **EXT-017** — Caldwell (2002), phantom energy.
- **EXT-018** — Wang et al. (2016), interactions in dark sector.
- **EXT-019** — Treu (2010), strong lensing by galaxies.
- **EXT-020** — Bartelmann & Schneider (2001), weak lensing.
- **EXT-021** — Kneib & Natarajan (2011), cluster lenses.
- **EXT-022** — Clowe et al. (2006), Bullet Cluster evidence.
- **EXT-023** — JWST follow-up observations of Bullet Cluster (2024–2025).
- **EXT-024** — Lelli, McGaugh & Schombert (2016), SPARC database.
- **EXT-025** — Zurek (2003), decoherence theory.
- **EXT-026** — Hartle & Hawking (1983), wave function of the Universe.
- **EXT-027** — Leggett (2002), limits of quantum mechanics.
- **EXT-028** — Widrow (2002), origin of cosmic magnetic fields.
- **EXT-029** — Carilli & Taylor (2002), cluster magnetic fields.
- **EXT-030** — Beck (2015), Faraday rotation and galactic fields.
- **EXT-031** — Peratt (1992), plasma universe.
- **EXT-032** — Sarazin (1988), intracluster medium physics.
- **EXT-033** — Lewis & Bridle (2002), MCMC in cosmology.
- **EXT-034** — Trotta (2008), Bayesian model selection.
- **EXT-035** — Casimir (1948), Casimir effect.
- **EXT-036** — Milonni (1994), quantum vacuum.
- **EXT-037** — Verlinde (2011), entropic gravity.
- **EXT-038** — Bousso (2002), holographic principle.
- **EXT-039** — Euclid mission (ESA, ongoing data).
- **EXT-040** — Vera Rubin Observatory / LSST.
- **EXT-041** — Roman Space Telescope (NASA).
- **EXT-042** — Quantum gravity developments (LQG/string theory).
- **EXT-043** — Machine learning in cosmology.
- **EXT-044** — NASA/IPAC Extragalactic Database (NED).
- **EXT-045** — SDSS SkyServer.
- **EXT-046** — Planck Legacy Archive.
- **EXT-047** — arXiv Astrophysics archive.
- **EXT-048** — CLASS (software).
- **EXT-049** — CAMB (software).
- **EXT-050** — CosmoMC (software).
- **EXT-051** — emcee (software).
- **EXT-052** — astropy (software).

## Regra editorial para novas adições

1. **Classificação obrigatória**: toda nova referência entra em apenas uma seção (`INT-*` ou `EXT-*`).
2. **Atribuição de ID**: usar o próximo número sequencial disponível na classe (ex.: próximo interno após `INT-005` é `INT-006`).
3. **Campos mínimos obrigatórios**:
   - **ID** (`INT-*`/`EXT-*`)
   - **Título/descrição curta**
   - **Origem** (caminho do arquivo no repo para `INT`, ou autoria/veículo para `EXT`)
   - **Ano** (quando aplicável)
   - **Link/DOI** (obrigatório para `EXT` quando existir)
4. **Links cruzados**: ao incluir item novo aqui, atualizar também `book/39_apendice_referencias_fontes.md` e `ANALISE_COMPLETA/Bibliografia_Completa.md`.
