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
# References: Photonic Cosmology Framework

Este arquivo é o **catálogo canônico de referências** do repositório.

## Fontes internas do repositório

> Critério: artefatos versionados neste repositório (documentos, scripts, datasets e índices internos).

### INT-001 — Framework técnico principal
- **Título**: README patch unificado PT/EN v4
- **Tipo**: Documento interno
- **Caminho**: `docs/README_patch_unified_PT_EN_v4.md`
- **Descrição**: Formulação matemática e narrativa técnica consolidada do modelo.

### INT-002 — Resultados computacionais do repositório
- **Título**: Dados e figuras do pipeline RLL
- **Tipo**: Datasets/artefatos internos
- **Caminho**: `data/relativity_living_light_models.csv`, `data/unified_entropy_margin_10_12.csv` e figuras derivadas
- **Descrição**: Base numérica para validações (H(z), Δμ, crescimento estrutural, rotação e lentes).

### INT-003 — Análises internas do artigo Nature
- **Título**: Pacote de análise interna do artigo de referência
- **Tipo**: Documentação interna
- **Caminho**: `docs/NATURE_ARTICLE_ANALYSIS.md`, `docs/ARTICLE_ANALYSIS_SUMMARY.md`, `docs/CONCEPTUAL_FRAMEWORK.md`
- **Descrição**: Interpretação autoral, síntese e diagramas conceituais ligados ao framework.
## Estilo de citação adotado

Este documento adota **exclusivamente o padrão APA (7ª edição)**.

**Regra de chave de citação para uso cruzado em documentos mestres:** usar o formato sequencial **`[REF-001]`, `[REF-002]`, ...** ao citar qualquer entrada desta lista.

## Primary Reference: Nature Article

- [REF-001] Liang, S., et al. (2025). Nonlocality-enabled photonic analogies of parallel spaces. *Nature Communications*. https://doi.org/10.1038/s41467-025-63981-3. https://www.nature.com/articles/s41467-025-63981-3
## Canonical Citation Keys (Claim-Level)

- [EXT-003] Lewis & Bridle (2002), *Physical Review D* 66, 103511.
- [EXT-004] Okada et al. (2026), *Physical Review Letters* 136.
- [EXT-005] Trotta (2008), *Contemporary Physics* 49, 71–104.
- [EXT-006] DESI Collaboration (2024/2025), BAO cosmological constraints.
- [EXT-007] Brout et al. (2022), Pantheon+ SN Ia cosmology.
- [EXT-008] BOSS Collaboration (`fσ8` growth constraints).
- [EXT-009] Planck Collaboration (2020), *A&A* 641, A6.
- [EXT-010] Akaike (1974) and Schwarz (1978), AIC/BIC definitions.
- [EXT-011] Combined analyses (DESI + Pantheon+ + BOSS) for expansion-growth consistency.

## Bibliografia unificada

Esta seção consolida, em um único ponto canônico, as referências externas (literatura acadêmica) e as fontes internas do repositório.

### Esquema de IDs estáveis

- `EXT-001` ... `EXT-042`: literatura externa (ordem fixa herdada da bibliografia completa).
- `INT-001` ... `INT-003`: fontes internas do repositório citadas no apêndice do livro.

### Literatura externa unificada (`EXT-*`)

| Novo ID | Legado | Referência |
|---|---:|---|
| EXT-001 | [1] | Perlmutter et al. (1999). *Measurements of Ω and Λ from 42 High-Redshift Supernovae*. |
| EXT-002 | [2] | Riess et al. (1998). *Observational Evidence from Supernovae for an Accelerating Universe and a Cosmological Constant*. |
| EXT-003 | [3] | Planck Collaboration (2020). *Planck 2018 results. VI. Cosmological parameters*. |
| EXT-004 | [4] | Betoule et al. (2014). *Improved cosmological constraints from a joint analysis of the SDSS-II and SNLS supernova samples*. |
| EXT-005 | [5] | Weinberg (1989). *The Cosmological Constant Problem*. |
| EXT-006 | [6] | Carroll (2001). *The Cosmological Constant*. |
| EXT-007 | [7] | Tegmark et al. (2004). *Cosmological parameters from SDSS and WMAP*. |
| EXT-008 | [8] | Aspect, Grangier & Roger (1982). *Experimental Realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment*. |
| EXT-009 | [9] | Glauber (2007). *Quantum Theory of Optical Coherence*. |
| EXT-010 | [10] | Nielsen & Chuang (2010). *Quantum Computation and Quantum Information*. |
| EXT-011 | [11] | McKinney (2010). *Data Structures for Statistical Computing in Python*. |
| EXT-012 | [12] | Pérez & Granger (2007). *IPython: A System for Interactive Scientific Computing*. |
| EXT-013 | [13] | Hunter (2007). *Matplotlib: A 2D Graphics Environment*. |
| EXT-014 | [14] | Gelman et al. (2013). *Bayesian Data Analysis*. |
| EXT-015 | [15] | Foreman-Mackey et al. (2013). *emcee: The MCMC Hammer*. |
| EXT-016 | [16] | Popper (1959). *The Logic of Scientific Discovery*. |
| EXT-017 | [17] | Kuhn (1962). *The Structure of Scientific Revolutions*. |
| EXT-018 | [18] | Lakatos (1970). *Falsification and the Methodology of Scientific Research Programmes*. |
| EXT-019 | [19] | Mandelbrot (1982). *The Fractal Geometry of Nature*. |
| EXT-020 | [20] | Koshy (2001). *Fibonacci and Lucas Numbers with Applications*. |
| EXT-021 | [21] | Creswell & Creswell (2017). *Research Design*. |
| EXT-022 | [22] | Borenstein et al. (2009). *Introduction to Meta-Analysis*. |
| EXT-023 | [23] | Wilkinson et al. (2016). *The FAIR Guiding Principles for scientific data management and stewardship*. |
| EXT-024 | [24] | Smith et al. (2016). *Software citation principles*. |
| EXT-025 | [25] | Saltzer & Schroeder (1975). *The protection of information in computer systems*. |
| EXT-026 | [26] | Trumbo & Weigold (2002). *Advancing Science Communication*. |
| EXT-027 | [27] | Hastie, Tibshirani & Friedman (2009). *The Elements of Statistical Learning*. |
| EXT-028 | [28] | Mukhanov (2005). *Physical Foundations of Cosmology*. |
| EXT-029 | [29] | Dodelson & Schmidt (2020). *Modern Cosmology*. |
| EXT-030 | [30] | Baumann (2009). *TASI Lectures on Inflation*. |
| EXT-031 | [31] | Peskin & Schroeder (1995). *An Introduction to Quantum Field Theory*. |
| EXT-032 | [32] | Weinberg (1995). *The Quantum Theory of Fields, Vol. 1*. |
| EXT-033 | [33] | Carroll (2004). *Spacetime and Geometry*. |
| EXT-034 | [34] | Wald (1984). *General Relativity*. |
| EXT-035 | [35] | Press et al. (2007). *Numerical Recipes* (3rd ed.). |
| EXT-036 | [36] | VanderPlas (2016). *Python Data Science Handbook*. |
| EXT-037 | [37] | Tufte (2001). *The Visual Display of Quantitative Information*. |
| EXT-038 | [38] | Resnik (2011). *What is Ethics in Research & Why is it Important?*. |
| EXT-039 | [39] | Nielsen (2011). *Reinventing Discovery*. |
| EXT-040 | [40] | Mehta et al. (2019). *A high-bias, low-variance introduction to Machine Learning for physicists*. |
| EXT-041 | [41] | Cover & Thomas (2006). *Elements of Information Theory*. |
| EXT-042 | [42] | Kragh (2007). *Conceptions of Cosmos*. |

### Fontes internas unificadas (`INT-*`)

| Novo ID | Fonte interna | Observação |
|---|---|---|
| INT-001 | `docs/REFERENCES.md` | Ponto canônico da bibliografia unificada. |
| INT-002 | `docs/CANONICAL_SOURCES.md` | Catálogo de fontes canônicas complementares. |
| INT-003 | `data/CITATION.cff` | Metadados formais para citação do repositório. |

### Mapeamento legado → novo ID

| Legado | Novo ID |
|---:|---|
| [1] | EXT-001 |
| [2] | EXT-002 |
| [3] | EXT-003 |
| [4] | EXT-004 |
| [5] | EXT-005 |
| [6] | EXT-006 |
| [7] | EXT-007 |
| [8] | EXT-008 |
| [9] | EXT-009 |
| [10] | EXT-010 |
| [11] | EXT-011 |
| [12] | EXT-012 |
| [13] | EXT-013 |
| [14] | EXT-014 |
| [15] | EXT-015 |
| [16] | EXT-016 |
| [17] | EXT-017 |
| [18] | EXT-018 |
| [19] | EXT-019 |
| [20] | EXT-020 |
| [21] | EXT-021 |
| [22] | EXT-022 |
| [23] | EXT-023 |
| [24] | EXT-024 |
| [25] | EXT-025 |
| [26] | EXT-026 |
| [27] | EXT-027 |
| [28] | EXT-028 |
| [29] | EXT-029 |
| [30] | EXT-030 |
| [31] | EXT-031 |
| [32] | EXT-032 |
| [33] | EXT-033 |
| [34] | EXT-034 |
| [35] | EXT-035 |
| [36] | EXT-036 |
| [37] | EXT-037 |
| [38] | EXT-038 |
| [39] | EXT-039 |
| [40] | EXT-040 |
| [41] | EXT-041 |
| [42] | EXT-042 |

---
## Estilo de citação adotado

Este documento adota exclusivamente o padrão **APA (7ª edição)**.

**Regra de chave de citação para uso cruzado:** cada entrada recebe uma chave única no formato `[REF-XXX]` (ex.: `[REF-001]`, `[REF-002]`), a ser reutilizada em documentos mestres.

## Primary Reference: Nature Article

- [REF-001] Afek, I., et al. (2025). Nonlocality-enabled photonic analogies of parallel spaces. *Nature Communications*. https://doi.org/10.1038/s41467-025-63981-3

**Relevance to Living Light Model:** Provides experimental evidence that photons can exist in extended, nonlocal states at laboratory scales, supporting the conceptual foundation of cosmological-scale photonic superposition.

---

## Quantum Optics & Nonlocality

### Foundational Papers

- [REF-002] Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika, 1*(3), 195–200.
- [REF-003] Aspect, A., Dalibard, J., & Roger, G. (1982). Experimental test of Bell's inequalities using time-varying analyzers. *Physical Review Letters, 49*(25), 1804–1807.
- [REF-002] Bell, J. S. (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika, 1*(3), 195-200. https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195
- [REF-003] Aspect, A., Dalibard, J., & Roger, G. (1982). Experimental test of Bell's inequalities using time-varying analyzers. *Physical Review Letters, 49*(25), 1804-1807. https://doi.org/10.1103/PhysRevLett.49.1804
- [REF-004] Gisin, N. (2014). *Quantum chance: Nonlocality, teleportation and other quantum marvels*. Springer.

### Photonic Superposition

- [REF-005] Mandel, L., & Wolf, E. (1995). *Optical coherence and quantum optics*. Cambridge University Press.
- [REF-006] Klaers, J., Schmitt, J., Vewinger, F., & Weitz, M. (2010). Bose-Einstein condensation of photons in an optical microcavity. *Nature, 468*(7323), 545–548.
- [REF-006] Klaers, J., Schmitt, J., Vewinger, F., & Weitz, M. (2010). Bose-Einstein condensation of photons in an optical microcavity. *Nature, 468*(7323), 545-548. https://doi.org/10.1038/nature09567

---

## Literatura externa

> Critério: papers, livros, notícias, preprints e publicações fora do repositório.

### EXT-001 — Nonlocality-enabled photonic analogies of parallel spaces
- **Autores**: Nature Communications (2025)
- **Tipo**: Artigo peer-reviewed
- **Fonte**: *Nature Communications*
- **DOI/URL**: 10.1038/s41467-025-63981-3 / https://www.nature.com/articles/s41467-025-63981-3
- **Nota**: Evidência laboratorial de estados fotônicos não-locais.

### EXT-002 — Bell's theorem and nonlocality
- Bell, J.S. (1964). "On the Einstein Podolsky Rosen paradox". *Physics Physique Физика*, 1(3), 195-200.

### EXT-003 — Experimental tests of Bell inequalities
- Aspect, A., Dalibard, J., & Roger, G. (1982). "Experimental Test of Bell's Inequalities Using Time-Varying Analyzers". *Physical Review Letters*, 49(25), 1804-1807.
- [REF-007] Weinberg, S. (1989). The cosmological constant problem. *Reviews of Modern Physics, 61*(1), 1–23.
- [REF-008] Peebles, P. J. E., & Ratra, B. (2003). The cosmological constant and dark energy. *Reviews of Modern Physics, 75*(2), 559–606.
- [REF-009] Bertone, G., Hooper, D., & Silk, J. (2005). Particle dark matter: Evidence, candidates and constraints. *Physics Reports, 405*(5–6), 279–390.

### EXT-004 — Modern nonlocality overview
- Gisin, N. (2014). *Quantum Chance: Nonlocality, Teleportation and Other Quantum Marvels*. Springer.

### EXT-005 — Optical coherence and quantum optics
- Mandel, L., & Wolf, E. (1995). *Optical Coherence and Quantum Optics*. Cambridge University Press.

### EXT-006 — Bose-Einstein condensation of photons
- Klaers, J., Schmitt, J., Vewinger, F., & Weitz, M. (2010). "Bose-Einstein condensation of photons in an optical microcavity". *Nature*, 468(7323), 545-548.

### EXT-007 — Cosmological constant problem
- Weinberg, S. (1989). "The cosmological constant problem". *Reviews of Modern Physics*, 61(1), 1-23.

### EXT-008 — Dark energy overview
- Peebles, P.J.E., & Ratra, B. (2003). "The cosmological constant and dark energy". *Reviews of Modern Physics*, 75(2), 559-606.
- [REF-010] Planck Collaboration. (2020). Planck 2018 results. VI. Cosmological parameters. *Astronomy & Astrophysics, 641*, A6.
- [REF-011] DESI Collaboration. (2024). DESI 2024 VI: Cosmological constraints from the measurements of baryon acoustic oscillations. *arXiv*.
- [REF-012] DES Collaboration. (2022). Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing. *Physical Review D, 105*(2), 023520.
- [REF-013] Castelvecchi, D. (2025). Is dark energy getting weaker? Fresh data bolster shock finding. *Nature News*.
- [REF-007] Weinberg, S. (1989). The cosmological constant problem. *Reviews of Modern Physics, 61*(1), 1-23. https://doi.org/10.1103/RevModPhys.61.1
- [REF-008] Peebles, P. J. E., & Ratra, B. (2003). The cosmological constant and dark energy. *Reviews of Modern Physics, 75*(2), 559-606. https://doi.org/10.1103/RevModPhys.75.559
- [REF-009] Bertone, G., Hooper, D., & Silk, J. (2005). Particle dark matter: Evidence, candidates and constraints. *Physics Reports, 405*(5-6), 279-390. https://doi.org/10.1016/j.physrep.2004.08.031

### Recent Observations

- [REF-010] Planck Collaboration. (2020). Planck 2018 results. VI. Cosmological parameters. *Astronomy & Astrophysics, 641*, A6. https://doi.org/10.1051/0004-6361/201833910
- [REF-011] DESI Collaboration. (2024). DESI 2024 VI: Cosmological constraints from the measurements of baryon acoustic oscillations. *arXiv*. https://arxiv.org/
- [REF-012] DES Collaboration. (2022). Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing. *Physical Review D, 105*(2), 023520. https://doi.org/10.1103/PhysRevD.105.023520
- [REF-013] Castelvecchi, D. (2025). Is dark energy getting weaker? Fresh data bolster shock finding. *Nature News*. https://www.nature.com/

### EXT-009 — Dark matter review
- Bertone, G., Hooper, D., & Silk, J. (2005). "Particle dark matter: evidence, candidates and constraints". *Physics Reports*, 405(5-6), 279-390.

### EXT-010 — Planck cosmological parameters
- Planck Collaboration (2020). "Planck 2018 results. VI. Cosmological parameters". *Astronomy & Astrophysics*, 641, A6.

### EXT-011 — DESI BAO constraints
- DESI Collaboration (2024). "DESI 2024 VI: Cosmological Constraints from the Measurements of Baryon Acoustic Oscillations". *arXiv preprint*.

### EXT-012 — Dark Energy Survey Y3
- DES Collaboration (2022). "Dark Energy Survey Year 3 results: Cosmological constraints from galaxy clustering and weak lensing". *Physical Review D*, 105(2), 023520.

### EXT-013 — Nature News on weakening dark energy
- Castelvecchi, D. (2025). "Is dark energy getting weaker? Fresh data bolster shock finding". *Nature News*.
- [REF-014] Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *The Astrophysical Journal, 270*, 365–370.
- [REF-015] De Felice, A., & Tsujikawa, S. (2010). f(R) theories. *Living Reviews in Relativity, 13*(1), 3.

### EXT-014 — MOND
- Milgrom, M. (1983). "A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis". *The Astrophysical Journal*, 270, 365-370.

### EXT-015 — f(R) gravity review
- De Felice, A., & Tsujikawa, S. (2010). "f(R) theories". *Living Reviews in Relativity*, 13(1), 3.

### EXT-016 — Quintessence
- Caldwell, R.R., Dave, R., & Steinhardt, P.J. (1998). "Cosmological imprint of an energy component with general equation of state". *Physical Review Letters*, 80(8), 1582.
- [REF-016] Caldwell, R. R., Dave, R., & Steinhardt, P. J. (1998). Cosmological imprint of an energy component with general equation of state. *Physical Review Letters, 80*(8), 1582.
- [REF-017] Caldwell, R. R. (2002). A phantom menace? Cosmological consequences of a dark energy component with super-negative equation of state. *Physics Letters B, 545*(1–2), 23–29.

### Unified Dark Sector

- [REF-018] Wang, B., Abdalla, E., Atrio-Barandela, F., & Pavón, D. (2016). Dark matter and dark energy interactions: Theoretical challenges, cosmological implications and observational signatures. *Reports on Progress in Physics, 79*(9), 096901.
- [REF-014] Milgrom, M. (1983). A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis. *The Astrophysical Journal, 270*, 365-370. https://doi.org/10.1086/161130
- [REF-015] De Felice, A., & Tsujikawa, S. (2010). f(R) theories. *Living Reviews in Relativity, 13*(1), 3. https://doi.org/10.12942/lrr-2010-3

### Dynamical Dark Energy

- [REF-016] Caldwell, R. R., Dave, R., & Steinhardt, P. J. (1998). Cosmological imprint of an energy component with general equation of state. *Physical Review Letters, 80*(8), 1582-1585. https://doi.org/10.1103/PhysRevLett.80.1582
- [REF-017] Caldwell, R. R. (2002). A phantom menace? Cosmological consequences of a dark energy component with super-negative equation of state. *Physics Letters B, 545*(1-2), 23-29. https://doi.org/10.1016/S0370-2693(02)02589-3

### EXT-017 — Phantom energy
- Caldwell, R.R. (2002). "A phantom menace? Cosmological consequences of a dark energy component with super-negative equation of state". *Physics Letters B*, 545(1-2), 23-29.

### EXT-018 — Unified dark sector interactions
- Wang, B., Abdalla, E., Atrio-Barandela, F., & Pavón, D. (2016). "Dark matter and dark energy interactions: theoretical challenges, cosmological implications and observational signatures". *Reports on Progress in Physics*, 79(9), 096901.
- [REF-018] Wang, B., Abdalla, E., Atrio-Barandela, F., & Pavón, D. (2016). Dark matter and dark energy interactions: Theoretical challenges, cosmological implications and observational signatures. *Reports on Progress in Physics, 79*(9), 096901. https://doi.org/10.1088/0034-4885/79/9/096901

### EXT-019 — Strong lensing review
- Treu, T. (2010). "Strong lensing by galaxies". *Annual Review of Astronomy and Astrophysics*, 48, 87-125.

### EXT-020 — Weak lensing theory
- Bartelmann, M., & Schneider, P. (2001). "Weak gravitational lensing". *Physics Reports*, 340(4-5), 291-472.

### EXT-021 — Cluster lenses
- Kneib, J.P., & Natarajan, P. (2011). "Cluster lenses". *The Astronomy and Astrophysics Review*, 19(1), 47.

### EXT-022 — Bullet Cluster empirical proof
- Clowe, D., et al. (2006). "A direct empirical proof of the existence of dark matter". *The Astrophysical Journal Letters*, 648(2), L109.

### EXT-023 — JWST follow-up (Bullet Cluster)
- Recent JWST observations of Bullet Cluster (2024-2025).

### EXT-024 — SPARC database
- Lelli, F., McGaugh, S.S., & Schombert, J.M. (2016). "SPARC: Mass Models for 175 Disk Galaxies with Spitzer Photometry and Accurate Rotation Curves". *The Astronomical Journal*, 152(6), 157.

### EXT-025 — Decoherence theory
- Zurek, W.H. (2003). "Decoherence, einselection, and the quantum origins of the classical". *Reviews of Modern Physics*, 75(3), 715.

### EXT-026 — Quantum cosmology
- Hartle, J.B., & Hawking, S.W. (1983). "Wave function of the Universe". *Physical Review D*, 28(12), 2960.

### EXT-027 — Macroscopic superposition limits
- Leggett, A.J. (2002). "Testing the limits of quantum mechanics: motivation, state of play, prospects". *Journal of Physics: Condensed Matter*, 14(15), R415.
- [REF-019] Treu, T. (2010). Strong lensing by galaxies. *Annual Review of Astronomy and Astrophysics, 48*, 87–125.
- [REF-020] Bartelmann, M., & Schneider, P. (2001). Weak gravitational lensing. *Physics Reports, 340*(4–5), 291–472.
- [REF-021] Kneib, J. P., & Natarajan, P. (2011). Cluster lenses. *The Astronomy and Astrophysics Review, 19*(1), 47.

### Bullet Cluster

- [REF-022] Clowe, D., et al. (2006). A direct empirical proof of the existence of dark matter. *The Astrophysical Journal Letters, 648*(2), L109.
- [REF-023] JWST Collaboration. (2025). Recent JWST observations of Bullet Cluster (2024–2025). *JWST observation reports*.

### Galaxy Rotation Curves

- [REF-024] Lelli, F., McGaugh, S. S., & Schombert, J. M. (2016). SPARC: Mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves. *The Astronomical Journal, 152*(6), 157.
- [REF-019] Treu, T. (2010). Strong lensing by galaxies. *Annual Review of Astronomy and Astrophysics, 48*, 87-125. https://doi.org/10.1146/annurev-astro-081309-130924
- [REF-020] Bartelmann, M., & Schneider, P. (2001). Weak gravitational lensing. *Physics Reports, 340*(4-5), 291-472. https://doi.org/10.1016/S0370-1573(00)00082-X
- [REF-021] Kneib, J.-P., & Natarajan, P. (2011). Cluster lenses. *The Astronomy and Astrophysics Review, 19*(1), 47. https://doi.org/10.1007/s00159-011-0047-3

### Bullet Cluster

- [REF-022] Clowe, D., et al. (2006). A direct empirical proof of the existence of dark matter. *The Astrophysical Journal Letters, 648*(2), L109-L113. https://doi.org/10.1086/508162
- [REF-023] JWST Collaboration. (2025). Bullet Cluster follow-up observations (2024-2025). *JWST Observation Archive*. https://www.stsci.edu/jwst

### EXT-028 — Large-scale cosmic magnetism
- Widrow, L.M. (2002). "Origin of galactic and extragalactic magnetic fields". *Reviews of Modern Physics*, 74(3), 775.

### EXT-029 — Cluster magnetic fields
- Carilli, C.L., & Taylor, G.B. (2002). "Cluster magnetic fields". *Annual Review of Astronomy and Astrophysics*, 40(1), 319-348.

### EXT-030 — Faraday rotation
- Beck, R. (2015). "Magnetic fields in spiral galaxies". *The Astronomy and Astrophysics Review*, 24(1), 4.

### EXT-031 — Plasma universe
- Peratt, A.L. (1992). *Physics of the Plasma Universe*. Springer-Verlag.
- [REF-024] Lelli, F., McGaugh, S. S., & Schombert, J. M. (2016). SPARC: Mass models for 175 disk galaxies with Spitzer photometry and accurate rotation curves. *The Astronomical Journal, 152*(6), 157. https://doi.org/10.3847/0004-6256/152/6/157

---

## Quantum Decoherence & Cosmology

- [REF-025] Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics, 75*(3), 715.
- [REF-026] Hartle, J. B., & Hawking, S. W. (1983). Wave function of the universe. *Physical Review D, 28*(12), 2960.
- [REF-027] Leggett, A. J. (2002). Testing the limits of quantum mechanics: Motivation, state of play, prospects. *Journal of Physics: Condensed Matter, 14*(15), R415.
- [REF-025] Zurek, W. H. (2003). Decoherence, einselection, and the quantum origins of the classical. *Reviews of Modern Physics, 75*(3), 715-775. https://doi.org/10.1103/RevModPhys.75.715
- [REF-026] Hartle, J. B., & Hawking, S. W. (1983). Wave function of the universe. *Physical Review D, 28*(12), 2960-2975. https://doi.org/10.1103/PhysRevD.28.2960
- [REF-027] Leggett, A. J. (2002). Testing the limits of quantum mechanics: Motivation, state of play, prospects. *Journal of Physics: Condensed Matter, 14*(15), R415-R451. https://doi.org/10.1088/0953-8984/14/15/201

### EXT-032 — Intracluster medium physics
- Sarazin, C.L. (1988). *X-ray emission from clusters of galaxies*. Cambridge University Press.

### EXT-033 — MCMC for cosmology
- Lewis, A., & Bridle, S. (2002). "Cosmological parameters from CMB and other data: A Monte Carlo approach". *Physical Review D*, 66(10), 103511.

### EXT-034 — Bayesian model comparison
- Trotta, R. (2008). "Bayes in the sky: Bayesian inference and model selection in cosmology". *Contemporary Physics*, 49(2), 71-104.

### EXT-035 — Casimir effect
- Casimir, H.B.G. (1948). "On the attraction between two perfectly conducting plates". *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen*, 51, 793-795.

### EXT-036 — Zero-point energy
- Milonni, P.W. (1994). *The Quantum Vacuum: An Introduction to Quantum Electrodynamics*. Academic Press.
- [REF-028] Widrow, L. M. (2002). Origin of galactic and extragalactic magnetic fields. *Reviews of Modern Physics, 74*(3), 775.
- [REF-029] Carilli, C. L., & Taylor, G. B. (2002). Cluster magnetic fields. *Annual Review of Astronomy and Astrophysics, 40*(1), 319–348.
- [REF-030] Beck, R. (2015). Magnetic fields in spiral galaxies. *The Astronomy and Astrophysics Review, 24*(1), 4.

### Plasma Cosmology

- [REF-031] Peratt, A. L. (1992). *Physics of the plasma universe*. Springer-Verlag.
- [REF-028] Widrow, L. M. (2002). Origin of galactic and extragalactic magnetic fields. *Reviews of Modern Physics, 74*(3), 775-823. https://doi.org/10.1103/RevModPhys.74.775
- [REF-029] Carilli, C. L., & Taylor, G. B. (2002). Cluster magnetic fields. *Annual Review of Astronomy and Astrophysics, 40*(1), 319-348. https://doi.org/10.1146/annurev.astro.40.060401.093852
- [REF-030] Beck, R. (2015). Magnetic fields in spiral galaxies. *The Astronomy and Astrophysics Review, 24*(1), 4. https://doi.org/10.1007/s00159-015-0084-4

### EXT-037 — Entropic gravity
- Verlinde, E. (2011). "On the origin of gravity and the laws of Newton". *Journal of High Energy Physics*, 2011(4), 29.

### EXT-038 — Holographic principle
- Bousso, R. (2002). "The holographic principle". *Reviews of Modern Physics*, 74(3), 825.

---

## Regra editorial para futuras adições

1. **Classificação obrigatória**: toda nova entrada deve ser incluída em apenas uma seção fixa: `Fontes internas do repositório` (INT) ou `Literatura externa` (EXT).
2. **Atribuição de ID**: usar o próximo identificador sequencial da seção (`INT-00N` ou `EXT-00N`), sem reutilizar IDs removidos.
3. **Campos mínimos obrigatórios**:
   - **ID**
   - **Título**
   - **Tipo**
   - **Origem**: caminho interno (`docs/...`, `data/...`, etc.) ou referência bibliográfica completa/DOI/URL
   - **Nota de relevância** (1 linha)
4. **Vínculos canônicos**: sempre que adicionar item aqui, atualizar referências cruzadas em `book/39_apendice_referencias_fontes.md` e `ANALISE_COMPLETA/Bibliografia_Completa.md`.
- [REF-031] Peratt, A. L. (1992). *Physics of the plasma universe*. Springer.
- [REF-032] Sarazin, C. L. (1988). *X-ray emission from clusters of galaxies*. Cambridge University Press.

---

## Computational & Statistical Methods

- [REF-033] Lewis, A., & Bridle, S. (2002). Cosmological parameters from CMB and other data: A Monte Carlo approach. *Physical Review D, 66*(10), 103511.
- [REF-034] Trotta, R. (2008). Bayes in the sky: Bayesian inference and model selection in cosmology. *Contemporary Physics, 49*(2), 71–104.
- [REF-033] Lewis, A., & Bridle, S. (2002). Cosmological parameters from CMB and other data: A Monte Carlo approach. *Physical Review D, 66*(10), 103511. https://doi.org/10.1103/PhysRevD.66.103511
- [REF-034] Trotta, R. (2008). Bayes in the sky: Bayesian inference and model selection in cosmology. *Contemporary Physics, 49*(2), 71-104. https://doi.org/10.1080/00107510802066753

---

## Related Theoretical Frameworks

### Vacuum Energy & Zero-Point Fields

- [REF-035] Casimir, H. B. G. (1948). On the attraction between two perfectly conducting plates. *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen, 51*, 793–795.
- [REF-035] Casimir, H. B. G. (1948). On the attraction between two perfectly conducting plates. *Proceedings of the Koninklijke Nederlandse Akademie van Wetenschappen, 51*, 793-795.
- [REF-036] Milonni, P. W. (1994). *The quantum vacuum: An introduction to quantum electrodynamics*. Academic Press.

### Emergent Gravity

- [REF-037] Verlinde, E. (2011). On the origin of gravity and the laws of Newton. *Journal of High Energy Physics, 2011*(4), 29.
- [REF-038] Bousso, R. (2002). The holographic principle. *Reviews of Modern Physics, 74*(3), 825.
- [REF-037] Verlinde, E. (2011). On the origin of gravity and the laws of Newton. *Journal of High Energy Physics, 2011*(4), 29. https://doi.org/10.1007/JHEP04(2011)029
- [REF-038] Bousso, R. (2002). The holographic principle. *Reviews of Modern Physics, 74*(3), 825-874. https://doi.org/10.1103/RevModPhys.74.825

---

## Living Light Model: Repository Documents

- [REF-039] Relativity Living Light. (2025). *README_patch_unified_PT_EN_v4.md* (Technical framework document).
- [REF-040] Relativity Living Light. (2025). *relativity_living_light_models.csv*; *unified_entropy_margin_10_12.csv* (Computational datasets).
- [REF-041] Relativity Living Light. (2025). *NATURE_ARTICLE_ANALYSIS.md*; *ARTICLE_ANALYSIS_SUMMARY.md*; *CONCEPTUAL_FRAMEWORK.md* (Model analysis and conceptual documents).
- [REF-039] Instituto Rafael. (2025). *README_patch_unified_PT_EN_v4.md* [Manuscrito interno do repositório]. https://github.com/instituto-Rafael/relativity-living-light
- [REF-040] Instituto Rafael. (2025). *relativity_living_light_models.csv* [Conjunto de dados]. https://github.com/instituto-Rafael/relativity-living-light
- [REF-041] Instituto Rafael. (2025). *unified_entropy_margin_10_12.csv* [Conjunto de dados]. https://github.com/instituto-Rafael/relativity-living-light
- [REF-042] Instituto Rafael. (2025). *NATURE_ARTICLE_ANALYSIS.md* [Análise técnica interna]. https://github.com/instituto-Rafael/relativity-living-light
- [REF-043] Instituto Rafael. (2025). *ARTICLE_ANALYSIS_SUMMARY.md* [Resumo técnico interno]. https://github.com/instituto-Rafael/relativity-living-light
- [REF-044] Instituto Rafael. (2025). *CONCEPTUAL_FRAMEWORK.md* [Documento conceitual interno]. https://github.com/instituto-Rafael/relativity-living-light

---

## Future Directions & Ongoing Research

- [REF-045] European Space Agency. (2025). *Euclid mission overview*. https://www.euclid-ec.org/
- [REF-046] Vera C. Rubin Observatory. (2025). *Legacy Survey of Space and Time (LSST) overview*. https://rubinobservatory.org/
- [REF-047] National Aeronautics and Space Administration. (2025). *Nancy Grace Roman Space Telescope overview*. https://roman.gsfc.nasa.gov/
- [REF-048] Research Community. (2025). *Quantum gravity research directions: Loop quantum gravity and string theory* [Panorama temático].
- [REF-049] Research Community. (2025). *Machine learning in cosmology* [Panorama temático].

---

## Citation Format

For citing the Relativity Living Light model:

- [REF-050] Instituto Rafael. (2025). *Relativity Living Light: Unified photonic superposition model* [Repositório GitHub]. https://github.com/instituto-Rafael/relativity-living-light. https://doi.org/10.5281/zenodo.17188137

For citing the Nature article:

- [REF-051] Afek, I., et al. (2025). Nonlocality-enabled photonic analogies of parallel spaces. *Nature Communications*. https://doi.org/10.1038/s41467-025-63981-3

---

## Additional Resources

### Online Resources

- [REF-052] NASA/IPAC. (2025). *NASA/IPAC Extragalactic Database (NED)*. https://ned.ipac.caltech.edu/
- [REF-053] Sloan Digital Sky Survey. (2025). *SDSS SkyServer*. http://skyserver.sdss.org/
- [REF-054] European Space Agency. (2025). *Planck Legacy Archive*. https://pla.esac.esa.int/
- [REF-055] arXiv. (2025). *Astrophysics archive (astro-ph)*. https://arxiv.org/archive/astro-ph

### Software Tools

- [REF-056] CLASS Collaboration. (2025). *Cosmic Linear Anisotropy Solving System (CLASS)* [Software].
- [REF-057] CAMB Collaboration. (2025). *Code for Anisotropies in the Microwave Background (CAMB)* [Software].
- [REF-058] CosmoMC Collaboration. (2025). *CosmoMC* [Software].
- [REF-059] Foreman-Mackey, D., et al. (2025). *emcee* [Software].
- [REF-060] Astropy Collaboration. (2025). *Astropy* [Software].

---

## Version History

- **v1.1** (November 2025): Normalização integral das referências para APA 7 e inclusão de chaves `[REF-XXX]`.
- **v1.0** (November 2025): Initial reference compilation.

---

## Notes

This reference list is intentionally broad, covering:
1. Foundational quantum mechanics and optics.
2. Standard cosmology (ΛCDM).
3. Alternative models and recent challenges.
4. Observational methods and data.
5. Theoretical frameworks potentially relevant to photonic cosmology.

The goal is to situate the Living Light model within the broader context of modern physics and cosmology, showing how it builds on established work while proposing novel connections between quantum optics and cosmic-scale phenomena.
---

## Bibliografia unificada

Ponto canônico de consolidação para referências externas e fontes internas do repositório.

### Esquema de identificadores estáveis

- `EXT-001` ... `EXT-999`: literatura externa (artigos, livros, preprints) consolidada de `ANALISE_COMPLETA/Bibliografia_Completa.md`.
- `INT-001` ... `INT-999`: fontes internas do repositório consolidadas de `book/39_apendice_referencias_fontes.md`.
- Regra de estabilidade: IDs atribuídos não são reutilizados; novas entradas apenas recebem próximos sufixos livres.

### Entradas consolidadas — literatura externa (`EXT-*`)

- `EXT-001` | Legado `[1]` | Perlmutter, S., Aldering, G., Goldhaber, G., et al. (1999) — *Measurements of Ω and Λ from 42 High-Redshift Supernovae*.
- `EXT-002` | Legado `[2]` | Riess, A. G., Filippenko, A. V., Challis, P., et al. (1998) — *Observational Evidence from Supernovae for an Accelerating Universe and a Cosmological Constant*.
- `EXT-003` | Legado `[3]` | Planck Collaboration (2020) — *Planck 2018 results. VI. Cosmological parameters*.
- `EXT-004` | Legado `[4]` | Betoule, M., Kessler, R., Guy, J., et al. (2014) — *Improved cosmological constraints from a joint analysis of the SDSS-II and SNLS supernova samples*.
- `EXT-005` | Legado `[5]` | Weinberg, S. (1989) — *The Cosmological Constant Problem*.
- `EXT-006` | Legado `[6]` | Carroll, S. M. (2001) — *The Cosmological Constant*.
- `EXT-007` | Legado `[7]` | Tegmark, M., Blanton, M. R., Strauss, M. A., et al. (2004) — *Cosmological parameters from SDSS and WMAP*.
- `EXT-008` | Legado `[8]` | Aspect, A., Grangier, P., & Roger, G. (1982) — *Experimental Realization of Einstein-Podolsky-Rosen-Bohm Gedankenexperiment: A New Violation of Bell's Inequalities*.
- `EXT-009` | Legado `[9]` | Glauber, R. J. (2007) — *Quantum Theory of Optical Coherence: Selected Papers and Lectures*.
- `EXT-010` | Legado `[10]` | Nielsen, M. A., & Chuang, I. L. (2010) — *Quantum Computation and Quantum Information*.
- `EXT-011` | Legado `[11]` | McKinney, W. (2010) — *Data Structures for Statistical Computing in Python*.
- `EXT-012` | Legado `[12]` | Pérez, F., & Granger, B. E. (2007) — *IPython: A System for Interactive Scientific Computing*.
- `EXT-013` | Legado `[13]` | Hunter, J. D. (2007) — *Matplotlib: A 2D Graphics Environment*.
- `EXT-014` | Legado `[14]` | Gelman, A., Carlin, J. B., Stern, H. S., et al. (2013) — *Bayesian Data Analysis*.
- `EXT-015` | Legado `[15]` | Foreman-Mackey, D., Hogg, D. W., Lang, D., & Goodman, J. (2013) — *emcee: The MCMC Hammer*.
- `EXT-016` | Legado `[16]` | Popper, K. R. (1959) — *The Logic of Scientific Discovery*.
- `EXT-017` | Legado `[17]` | Kuhn, T. S. (1962) — *The Structure of Scientific Revolutions*.
- `EXT-018` | Legado `[18]` | Lakatos, I. (1970) — *Falsification and the Methodology of Scientific Research Programmes*.
- `EXT-019` | Legado `[19]` | Mandelbrot, B. B. (1982) — *The Fractal Geometry of Nature*.
- `EXT-020` | Legado `[20]` | Koshy, T. (2001) — *Fibonacci and Lucas Numbers with Applications*.
- `EXT-021` | Legado `[21]` | Creswell, J. W., & Creswell, J. D. (2017) — *Research Design: Qualitative, Quantitative, and Mixed Methods Approaches*.
- `EXT-022` | Legado `[22]` | Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009) — *Introduction to Meta-Analysis*.
- `EXT-023` | Legado `[23]` | Wilkinson, M. D., Dumontier, M., Aalbersberg, I. J., et al. (2016) — *The FAIR Guiding Principles for scientific data management and stewardship*.
- `EXT-024` | Legado `[24]` | Smith, A. M., Katz, D. S., Niemeyer, K. E., & FORCE11 Software Citation Working Group (2016) — *Software citation principles*.
- `EXT-025` | Legado `[25]` | Saltzer, J. H., & Schroeder, M. D. (1975) — *The protection of information in computer systems*.
- `EXT-026` | Legado `[26]` | Trumbo, C. W., & Weigold, M. F. (2002) — *Advancing Science Communication: A Survey of Science Communicators*.
- `EXT-027` | Legado `[27]` | Hastie, T., Tibshirani, R., & Friedman, J. (2009) — *The Elements of Statistical Learning: Data Mining, Inference, and Prediction*.
- `EXT-028` | Legado `[28]` | Mukhanov, V. (2005) — *Physical Foundations of Cosmology*.
- `EXT-029` | Legado `[29]` | Dodelson, S., & Schmidt, F. (2020) — *Modern Cosmology*.
- `EXT-030` | Legado `[30]` | Baumann, D. (2009) — *TASI Lectures on Inflation*.
- `EXT-031` | Legado `[31]` | Peskin, M. E., & Schroeder, D. V. (1995) — *An Introduction to Quantum Field Theory*.
- `EXT-032` | Legado `[32]` | Weinberg, S. (1995) — *The Quantum Theory of Fields, Vol. 1: Foundations*.
- `EXT-033` | Legado `[33]` | Carroll, S. M. (2004) — *Spacetime and Geometry: An Introduction to General Relativity*.
- `EXT-034` | Legado `[34]` | Wald, R. M. (1984) — *General Relativity*.
- `EXT-035` | Legado `[35]` | Press, W. H., Teukolsky, S. A., Vetterling, W. T., & Flannery, B. P. (2007) — *Numerical Recipes: The Art of Scientific Computing*.
- `EXT-036` | Legado `[36]` | VanderPlas, J. (2016) — *Python Data Science Handbook*.
- `EXT-037` | Legado `[37]` | Tufte, E. R. (2001) — *The Visual Display of Quantitative Information*.
- `EXT-038` | Legado `[38]` | Resnik, D. B. (2011) — *What is Ethics in Research & Why is it Important?*.
- `EXT-039` | Legado `[39]` | Nielsen, M. (2011) — *Reinventing Discovery: The New Era of Networked Science*.
- `EXT-040` | Legado `[40]` | Mehta, P., Bukov, M., Wang, C. H., et al. (2019) — *A high-bias, low-variance introduction to Machine Learning for physicists*.
- `EXT-041` | Legado `[41]` | Cover, T. M., & Thomas, J. A. (2006) — *Elements of Information Theory*.
- `EXT-042` | Legado `[42]` | Kragh, H. (2007) — *Conceptions of Cosmos: From Myths to the Accelerating Universe*.

### Entradas consolidadas — fontes internas (`INT-*`)

- `INT-001` | `docs/REFERENCES.md` — Catálogo canônico de referências e contexto bibliográfico do projeto.
- `INT-002` | `docs/CANONICAL_SOURCES.md` — Inventário de fontes canônicas internas, com foco em trilha autoral.
- `INT-003` | `data/CITATION.cff` — Metadados de citação formal do repositório (autoria, título, versão e DOI).

### Mapeamento legado → novo ID (rastreabilidade `[1]...[42]`)

| Legado | Novo ID |
|---|---|
| `[1]` | `EXT-001` |
| `[2]` | `EXT-002` |
| `[3]` | `EXT-003` |
| `[4]` | `EXT-004` |
| `[5]` | `EXT-005` |
| `[6]` | `EXT-006` |
| `[7]` | `EXT-007` |
| `[8]` | `EXT-008` |
| `[9]` | `EXT-009` |
| `[10]` | `EXT-010` |
| `[11]` | `EXT-011` |
| `[12]` | `EXT-012` |
| `[13]` | `EXT-013` |
| `[14]` | `EXT-014` |
| `[15]` | `EXT-015` |
| `[16]` | `EXT-016` |
| `[17]` | `EXT-017` |
| `[18]` | `EXT-018` |
| `[19]` | `EXT-019` |
| `[20]` | `EXT-020` |
| `[21]` | `EXT-021` |
| `[22]` | `EXT-022` |
| `[23]` | `EXT-023` |
| `[24]` | `EXT-024` |
| `[25]` | `EXT-025` |
| `[26]` | `EXT-026` |
| `[27]` | `EXT-027` |
| `[28]` | `EXT-028` |
| `[29]` | `EXT-029` |
| `[30]` | `EXT-030` |
| `[31]` | `EXT-031` |
| `[32]` | `EXT-032` |
| `[33]` | `EXT-033` |
| `[34]` | `EXT-034` |
| `[35]` | `EXT-035` |
| `[36]` | `EXT-036` |
| `[37]` | `EXT-037` |
| `[38]` | `EXT-038` |
| `[39]` | `EXT-039` |
| `[40]` | `EXT-040` |
| `[41]` | `EXT-041` |
| `[42]` | `EXT-042` |



## Referências primárias adicionadas — Caso AMAS/SAA (com data de origem)

- **EXT-053** — G1 (2026-05-05). *Estudo desvenda como surgiu a anomalia magnética que coloca em risco satélites sobre o Atlântico Sul*. 
  - Tipo: referência jornalística inicial (não primária científica).
  - URL: https://g1.globo.com/ciencia/noticia/2026/05/05/estudo-desvenda-como-surgiu-a-anomalia-magnetica-que-coloca-em-risco-satelites-sobre-o-atlantico-sul.ghtml
  - Data de origem: 2026-05-05.

- **EXT-054** — Finlay, C. C., et al. (2024). *Long-term persistency of a strong non-dipole field in the South Atlantic*. Nature Communications.
  - DOI: 10.1038/s41467-024-53688-2
  - URL: https://www.nature.com/articles/s41467-024-53688-2
  - Data de origem: 2024-11-05.

- **EXT-055** — ESA Swarm (2020-05-20). *Swarm probes weakening of Earth’s magnetic field*.
  - URL: https://www.esa.int/Applications/Observing_the_Earth/Swarm/Swarm_probes_weakening_of_Earth_s_magnetic_field
  - Data de origem: 2020-05-20.

- **EXT-056** — NASA (2020-08-17). *NASA Researchers Track Slowly Splitting ‘Dent’ in Earth’s Magnetic Field*.
  - URL: https://www.nasa.gov/missions/icon/nasa-researchers-track-slowly-splitting-dent-in-earths-magnetic-field/
  - Data de origem: 2020-08-17.

- **EXT-057** — NOAA/NCEI + BGS (WMM2025). *World Magnetic Model*.
  - URL: https://www.ncei.noaa.gov/products/world-magnetic-model
  - Data de origem (modelo): 2024-12 (validade 2025.0–2030.0).

- **EXT-058** — IAGA V-MOD. *International Geomagnetic Reference Field (IGRF-14)*.
  - URL: https://www.iaga-aiga.org/igrf/
  - Data de origem (geração vigente): 2024 (validade a partir de 2025.0).


## Fontes externas para pipeline RLL/MCRP

- **EXT-RLL-IGRF14** — NOAA/NCEI IGRF14. URL: https://www.ncei.noaa.gov/products/international-geomagnetic-reference-field
- **EXT-RLL-WMM2025** — NOAA/NCEI WMM2025. URL: https://www.ncei.noaa.gov/products/world-magnetic-model
- **EXT-RLL-SWARM-SAA** — ESA Swarm (AMAS/SAA contexto observacional). URL: https://swarm-diss.eo.esa.int/
- **EXT-RLL-NASA-SAA** — NASA South Atlantic Anomaly. URL: https://www.nasa.gov/mission_pages/sunearth/news/gallery/saa.html
- **EXT-RLL-OMNI** — NASA OMNI/SPDF. URL: https://omniweb.gsfc.nasa.gov/
- **EXT-RLL-NMDB** — NMDB neutron monitor database. URL: https://www.nmdb.eu/
- **EXT-RLL-SPENVIS** — SPENVIS AE9/AP9. URL: https://www.spenvis.oma.be/
- **EXT-RLL-DESI-DR2** — DESI DR2 BAO. URL: https://www.desi.lbl.gov/
- **EXT-RLL-PLANCK2018** — Planck 2018 chains / PLA. URL: https://pla.esac.esa.int/
- **EXT-RLL-PANTHEONPLUS** — Pantheon+ SNe Ia. URL: https://github.com/PantheonPlusSH0ES/DataRelease
