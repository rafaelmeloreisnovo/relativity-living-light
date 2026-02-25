# Relativity Living Light

**Resumo de validação observacional:** validação ainda em estágio **Sintético**, com integração **Parcial real** em preparação e sem etapa **Real validado** concluída.

[![DOI](https://zenodo.org/badge/1046495816.svg)](https://doi.org/10.5281/zenodo.17188137)

Repositório principal do modelo **Relativity Living Light (RLL)**, com foco em cosmologia de superposição dinâmica, documentação técnico-científica, trilhas de validação observacional e acervo autoral RAFAELIA (∆RafaelVerboΩ).

---


## Status dos Dados

- **Sintético:** simulações internas, mocks e diagnósticos computacionais sem inferência observacional final.
- **Parcial real:** uso de dados observacionais reais em parte do pipeline, ainda sem validação cruzada completa.
- **Real validado:** resultados reproduzíveis com dados reais, checagens estatísticas e documentação de validação concluídas.

**Nível atual deste README:** `Sintético` (com trilha `Parcial real` em andamento).

---

## 0) Preservação integral de conteúdo (sem perda)

Para eliminar risco de perda textual, o conteúdo histórico completo do `README.md` anterior foi preservado em:

- [docs/README_ROOT_LEGACY_ARCHIVE.md](docs/README_ROOT_LEGACY_ARCHIVE.md)

Validação de integridade (histórico Git):

```bash
git show 64a12a3:README.md
```

Este `README.md` atual é uma camada de organização técnica; o acervo narrativo/autoral foi mantido e rastreável.

---

## 1) Visão geral técnica

O RLL propõe uma extensão efetiva da dinâmica cosmológica via componente de superposição fotônica com transição controlada por função logística, acoplada a termos magnéticos e plasmáticos:

```math
E^2(a)=\Omega_r a^{-4}+\Omega_m a^{-3}+\Omega_\Lambda
+\Omega_{s0}[f(a)+(1-f)a^{-3}]
+\Omega_{B0}a^{-4}+\Omega_{P0}a^{-4}
```

com:

```math
f(z)=\frac{1}{1+\exp((z-z_t)/w_t)}
```

### Objetivo operacional

- comparar RLL vs ΛCDM em observáveis de expansão e crescimento;
- manter rastreabilidade de dados, figuras e versões documentais;
- separar trilha científica (core) da trilha conceitual/autoral.

---

## 2) Navegação principal (canônica)

### Núcleo científico

- [docs/Relativity_Living_Light.md](docs/Relativity_Living_Light.md)
- [docs/Results.md](docs/Results.md)
- [docs/BOOSTERS.md](docs/BOOSTERS.md)
- [docs/COMPARACAO_DESI_2025.md](docs/COMPARACAO_DESI_2025.md)
- [docs/ROADMAP_VALIDACAO.md](docs/ROADMAP_VALIDACAO.md)
- [docs/REFERENCES.md](docs/REFERENCES.md)
- [docs/PLANO_ABCD_JWST_AGN_SMBH.md](docs/PLANO_ABCD_JWST_AGN_SMBH.md)

### Governança e organização documental

- [docs/INDICE_MESTRE.md](docs/INDICE_MESTRE.md)
- [docs/RELEASE_NOTES_HISTORY.md](docs/RELEASE_NOTES_HISTORY.md)
- [docs/DOCUMENTATION_ORGANIZATION_MASTER.md](docs/DOCUMENTATION_ORGANIZATION_MASTER.md)
- [docs/DOCUMENTATION_FULL_INVENTORY.md](docs/DOCUMENTATION_FULL_INVENTORY.md)
- [docs/ZIP_CONTENT_INDEX.md](docs/ZIP_CONTENT_INDEX.md)

### Trilha autoral e conceitual (integridade de selo)

- [docs/MANIFESTO.md](docs/MANIFESTO.md)
- [docs/MAPA_RAFAELIA_TOTAL.md](docs/MAPA_RAFAELIA_TOTAL.md)
- [docs/SUPREMO UNIFICADO.md](docs/SUPREMO%20UNIFICADO.md)
- [docs/numeros_rafaelianos/Readme.md](docs/numeros_rafaelianos/Readme.md)

---

## 3) Gráficos, infográficos e imagens

### 3.1 Figura de referência solicitada (`híbrido`)

![Crescimento Estrutural: RLL vs ΛCDM vs Dados BOSS](https://github.com/instituto-Rafael/relativity-living-light/file_00000000bf0c71f59bb294eeaca6995f.png)

### 3.2 Painel de resultados principais

| Tema | Selo de origem | Figura |
|---|---|---|
| Expansão cósmica H(z) | `mock` | ![H ratio](figs/unified_H_ratio.png) |
| Distância de luminosidade (Δμ) | `mock` | ![mu residuals](figs/unified_mu_residuals.png) |
| Frações de energia | `mock` | ![fractions](figs/unified_fractions.png) |
| Dinâmica f(z) e w_eff | `mock` | ![f and weff](figs/unified_f_and_weff.png) |

### 3.3 Painel observacional complementar

| Tema | Selo de origem | Figura |
|---|---|---|
| Crescimento de estrutura fσ₈(z) | `híbrido` | ![growth](figs/unified_growth_fs8.png) |
| Lente em aglomerados | `híbrido` | ![cluster lensing](figs/cluster_lensing_SIS_unified.png) |
| Curva de rotação (SPARC) | `híbrido` | ![rotation](figs/rotcurve_NGC_2403.png) |
| Ajuste H mock | `mock` | ![mock H](figs/mock_H_fit.png) |

---

## 4) Dados e reprodutibilidade

### Dados centrais

- `data/posterior_unified_synth.csv`
- `data/relativity_living_light_models.csv`
- `data/unified_entropy_margin_10_12.csv`

### Notebooks

- `data/Hz_superposicao.ipynb`
- `data/density_decomp.ipynb`
- `data/rotation_model.ipynb`

### Bundles compactados

- `data/RelativityLivingLight_v4_bundle.zip`
- `data/relativity_bundle_results.zip`
- `docs/rll_revisado_v2.zip`

Inventário interno dos bundles: [docs/ZIP_CONTENT_INDEX.md](docs/ZIP_CONTENT_INDEX.md)

---

## 5) Bibliografia expandida (seleção essencial)

> Referência bibliográfica completa e ampliada: [docs/REFERENCES.md](docs/REFERENCES.md)

### Cosmologia observacional e modelo padrão

1. Planck Collaboration (2018), *Planck 2018 results. VI. Cosmological parameters*.  
   DOI: <https://doi.org/10.1051/0004-6361/201833910>
2. Riess et al. (1998), *Observational Evidence from Supernovae for an Accelerating Universe*.  
   DOI: <https://doi.org/10.1086/300499>
3. Perlmutter et al. (1999), *Measurements of Ω and Λ from 42 High-Redshift Supernovae*.  
   DOI: <https://doi.org/10.1086/307221>
4. Alam et al. (2017), *The clustering of galaxies in SDSS-III BOSS*.  
   DOI: <https://doi.org/10.1093/mnras/stx721>

### Crescimento, estrutura e tensões cosmológicas

5. DES Collaboration (2022), *Dark Energy Survey Year 3 Results*.  
   DOI: <https://doi.org/10.1103/PhysRevD.105.023520>
6. Euclid Collaboration (programa científico e forecasts).  
   URL: <https://www.euclid-ec.org/science/>
7. DESI Collaboration (BAO / growth program).  
   URL: <https://www.desi.lbl.gov/>

### Não-localidade fotônica e conexão conceitual

8. Nature Communications (2025), artigo relacionado à não-localidade fotônica e espaços paralelos.  
   DOI/ID: `s41467-025-63981-3`
9. Base analítica no repositório:
   - [docs/NATURE_ARTICLE_ANALYSIS.md](docs/NATURE_ARTICLE_ANALYSIS.md)
   - [docs/ARTICLE_ANALYSIS_SUMMARY.md](docs/ARTICLE_ANALYSIS_SUMMARY.md)
   - [docs/ANALISE_ARTIGO_NATURE_PT.md](docs/ANALISE_ARTIGO_NATURE_PT.md)

### Formalismo e extensão do modelo RLL

10. [docs/LAGRANGIANO_EFT.md](docs/LAGRANGIANO_EFT.md)
11. [docs/PERTURBACOES_CRESCIMENTO.md](docs/PERTURBACOES_CRESCIMENTO.md)
12. [docs/ESTABILIDADE_GHOST_CHECK.md](docs/ESTABILIDADE_GHOST_CHECK.md)
13. [docs/VELOCIDADE_SOM.md](docs/VELOCIDADE_SOM.md)
14. [docs/COMPARACAO_DESI_2025.md](docs/COMPARACAO_DESI_2025.md)

---

## 6) Como usar este repositório (fluxo curto)

1. Ler [docs/INDICE_MESTRE.md](docs/INDICE_MESTRE.md)
2. Validar resultados em [docs/Results.md](docs/Results.md)
3. Checar formulação em [docs/BOOSTERS.md](docs/BOOSTERS.md)
4. Verificar releases em [docs/RELEASE_NOTES_HISTORY.md](docs/RELEASE_NOTES_HISTORY.md)
5. Auditar inventário em [docs/DOCUMENTATION_FULL_INVENTORY.md](docs/DOCUMENTATION_FULL_INVENTORY.md)

---

## 7) Licença, autoria e integridade

- Licença: [LICENSE.md](LICENSE.md)
- Governança: [docs/ADMIN.md](docs/ADMIN.md)
- Autoria original: ∆RafaelVerboΩ
- Princípio de integridade textual RAFAELIA: preservar literais simbólicos (⊕ ⊗ ∮ ∫ √ π φ Δ Ω Σ ψ χ ρ ∧) e trilhas canônicas.

---

## 8) Nota de organização documental

Este `README.md` passa a atuar como **entrada principal organizada** do repositório. Conteúdo narrativo/autoral expandido permanece nos documentos dedicados da trilha conceitual para evitar mistura de escopos em leitura técnica.



O DIRETORIO news/ tem documento soltos e devem ser integrados e movidos
