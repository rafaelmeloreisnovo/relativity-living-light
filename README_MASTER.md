# 🌌 Relativity Living Light — README MASTER

**📘 Trilha principal oficial do livro:** [book/README.md](book/README.md)

[![DOI](https://zenodo.org/badge/1046495816.svg)](https://doi.org/10.5281/zenodo.17188137)

## Resumo do Projeto

**Relativity Living Light** é um modelo cosmológico de superposição dinâmica que propõe ir além do modelo padrão ΛCDM. Este repositório contém a hipótese de que a **superposição fotônica** atua como um componente energético dinâmico que transita de um comportamento tipo energia escura (w ≈ -1, expansivo) para um comportamento tipo matéria (w ≈ 0, atrativo).

> *"VAZIO ⟶ VERBO ⟶ CHEIO ⟶ RETROALIMENTAÇÃO ⟶ VAZIO₍novo₎"*

---

## 🔬 Equação Principal Unificada

Resumo canônico do framework: ver `docs/canonicos/FRAMEWORK_RESUMO_CANONICO.md`.

```
E²(a) = Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ +
        Ω_s0[f(a) + (1-f)a⁻³] +          # superposição fotônica (transição DE→DM do setor de superposição)
        Ω_B0 a⁻⁴ +                         # setor magnético
        Ω_P0 a⁻⁴                           # setor plasmático (T,P)
```

onde:
- **f(z) = 1 / (1 + exp((z - z_t)/w_t))** — função de transição suave
- **z_t** — redshift da transição DE→DM do setor de superposição
- **w_t** — largura da transição
- **Ω_s0** — densidade de superposição fotônica hoje
- **Ω_B0** — densidade do setor magnético cósmico
- **Ω_P0** — densidade do setor plasmático

### Componentes do Modelo

1. **Termos clássicos:**
   - Matéria: Ω_m a⁻³
   - Constante cosmológica: Ω_Λ
   - Radiação: Ω_r a⁻⁴

2. **Superposição fotônica (novo, termo canônico):**
   - “superposição escura” (sinônimo legado/histórico)
   - Coerência \(f(z)\) e decoerência \((1-f(z))\) na transição DE→DM do setor de superposição
   - Comportamento dual: expansivo em z baixo, atrativo em z alto

3. **Componentes adicionais:**
   - Setor magnético coerente: Ω_B0 a⁻⁴
   - Setor plasmático com temperatura e pressão: Ω_P0 a⁻⁴
   - Correção magneto-coerente opcional: parâmetros α_B, β

---
Em síntese: o RLL estende a forma tipo Friedmann com um setor de superposição fotônica em transição dinâmica (DE→matéria), mantendo os termos clássicos e incluindo contribuições magnética e plasmática sob referência canônica única.


## 🧾 Micro-tabela canônica (termos de entrada)

Referência completa: [`docs/canonicos/FRAMEWORK_RESUMO_CANONICO.md`](docs/canonicos/FRAMEWORK_RESUMO_CANONICO.md).

| Termo canônico | Uso curto |
|---|---|
| superposição fotônica | setor de superposição |
| coerência (f(z)) | coerência |
| decoerência ((1−f(z))) | decoerência |
| setor magnético | magnético |
| setor plasmático | plasmático |
| transição DE→DM do setor de superposição | DE→DM |

## 📂 Estrutura do Repositório

```
/
├── README.md              # README original com manifesto completo
├── README_MASTER.md       # Este arquivo - navegação e estrutura
├── LICENSE.md             # Licença do projeto
├── requirements.txt       # Dependências Python
│
├── /docs                  # 📄 Documentação e textos simbióticos
│   ├── ADMIN.md
│   ├── MANIFESTO.md
│   ├── RAFAELIA_UNIFIED_PAPER.md
│   ├── MAPA_RAFAELIA_TOTAL.md
│   ├── SUPREMO UNIFICADO.md
│   ├── IMPACT_REPORT_MULTI.md
│   ├── REPOSITORY_STRUCTURE_SUGGESTION.md
│   ├── Results.md
│   ├── BILINGUAL_RLL_HYPOTHESIS_SUMMARY.md
│   ├── estatisticas.md
│   ├── README_patch_unified_PT_EN_v3.md
│   ├── README_patch_unified_PT_EN_v4.md
│   ├── README_snippet.md
│   ├── ciencia_*.md       # Documentos científicos aplicados
│   ├── RelativityLivingLight_arXiv.tex
│   ├── RelativityLivingLight_arXiv.pdf
│   └── /numeros_rafaelianos/
│       ├── CientiEspiritual.md
│       ├── Constante.md
│       ├── Numeros.md
│       ├── harmonica.md
│       └── DATA_DESCRIPTOR_BUNDLE_V4.md
│
├── /data                  # 📊 Dados, notebooks e arquivos CSV/JSON
│   ├── zenodo.json
│   ├── CITATION.cff
│   ├── posterior_unified_synth.csv
│   ├── relativity_living_light_models.csv
│   ├── unified_entropy_margin_10_12.csv
│   ├── Hz_superposicao.ipynb
│   ├── ciencia_Hz_superposicao.ipynb
│   ├── ciencia_Hz_superposicao.ipynb
│   ├── density_decomp.ipynb
│   ├── rotation_model.ipynb
│   ├── relativity_bundle_results.zip
│   └── RelativityLivingLight_v4_bundle.zip
│
└── /figs                  # 🖼️ Imagens e gráficos
    ├── H_ratio_vs_z.png
    ├── unified_H_ratio.png
    ├── unified_mu_residuals.png
    ├── unified_fractions.png
    ├── unified_f_and_weff.png
    ├── unified_entropy_Hratio.png
    ├── unified_entropy_dmu.png
    ├── unified_growth_fs8.png
    ├── cluster_lensing_SIS_unified.png
    ├── corner_plot_unified_highres.png
    ├── last_corner_plot_unified_highres.png
    ├── mock_H_fit.png
    ├── mock_SN_fit.png
    ├── mu_residuals.png
    ├── f_transition.png
    ├── rotcurve_NGC_2403.png
    ├── hz_superposicao.png
    ├── ciencia_*.png          # Gráficos científicos
    ├── post_*.png             # Distribuições posteriores
    ├── IMG_*.png              # Screenshots e imagens diversas
    └── Screenshot_*.png
```

---



## 🔁 Fluxo Único de Execução Científica

Comando único para reproduzir os principais pipelines:

```bash
bash scripts/run_repro_all.sh
```


**Árvore canônica obrigatória:** `docs/` + `data/` + `results/`.

1. **Entrada (definição científica):** `docs/`
   - Política mestra: `docs/DOCUMENTATION_ORGANIZATION_MASTER.md`
   - Módulos Structure D: `docs/modules/structure_d_equations.md`, `docs/modules/structure_d_agn_feedback_bridge.md`
2. **Dados de entrada + execução:** `data/`
   - Pipeline: `data/pipelines/structure_d/`
   - Guia de inputs: `data/inputs/structure_d/README.md`
3. **Saída:** `results/`
   - Estrutura de saída canônica: `results/structure_d/README.md`

`to_Add/` é reservado para histórico e auditoria, sem função operacional.

## Reprodução rápida (1 comando)

Para executar a reprodução principal de ponta a ponta, use:

- `bash scripts/run_repro_all.sh`

Modo opcional (inclui o preview de dois componentes de radiação):

- `bash scripts/run_repro_all.sh --with-two-rad`

Artefatos esperados após a execução:

- `results/structure_d/model_comparison.csv`
- `results/RLL_chi2_results.csv`
- `results/two_radiation_model_preview.csv`
- `figs/paper/RLL_validacao_real.png`

> Nota: `results/two_radiation_model_preview.csv` é gerado apenas quando a flag opcional `--with-two-rad` é usada.

---

## 🔬 Observáveis Testados

O modelo foi testado contra múltiplos observáveis cosmológicos:

1. **Expansão Cósmica**
   - H(z) — taxa de expansão de Hubble
   - Δμ — distância de luminosidade (SNe Ia)
   - Gráficos: [unified_H_ratio.png](figs/paper/unified_H_ratio.png), [unified_mu_residuals.png](figs/paper/unified_mu_residuals.png)

2. **Crescimento de Estruturas**
   - fσ₈(z) — crescimento de perturbações de densidade
   - Comparável a BOSS/DESI
   - Gráfico: [unified_growth_fs8.png](figs/paper/unified_growth_fs8.png)

3. **Lente Gravitacional**
   - Aglomerados (Bullet, Abell 2744, Frontier Fields)
   - Weak/strong lensing
   - Gráfico: [cluster_lensing_SIS_unified.png](figs/paper/cluster_lensing_SIS_unified.png)

4. **Galáxias**
   - Curvas de rotação (SPARC)
   - Exemplo: [rotcurve_NGC_2403.png](figs/paper/rotcurve_NGC_2403.png)

5. **Bandas de Robustez**
   - Margem de entropia 10/12
   - Dados: [unified_entropy_margin_10_12.csv](data/unified_entropy_margin_10_12.csv)

---

## 📚 Navegação Rápida por Seção

### Documentação Científica
- [Conclusão](docs/RAFAELIA_UNIFIED_PAPER.md) — Conclusões do modelo
- [Manifesto](docs/MANIFESTO.md) — Visão filosófica e simbiótica
- [Mapa Rafaelia Total](docs/MAPA_RAFAELIA_TOTAL.md) — Estrutura conceitual completa
- [Descobertas Emergentes](docs/DESCOBERTAS_EMERGENTES.md) — 14 descobertas numeradas com evidência, risco, falsificação e ponte código↔resultados
- [Supremo Unificado](docs/SUPREMO UNIFICADO.md) — Unificação dos conceitos
- [Impact Report](docs/IMPACT_REPORT_MULTI.md) — Relatório de impacto
- [Estrutura](docs/REPOSITORY_STRUCTURE_SUGGESTION.md) — Estrutura do modelo
- [Resultados](docs/Results.md) — Resultados obtidos
- [Estatísticas](docs/estatisticas.md) — Análises estatísticas

### Patches e Versões do README
- [README v3 PT/EN](docs/README_patch_unified_PT_EN_v3.md)
- [README v4 PT/EN](docs/README_patch_unified_PT_EN_v4.md)
- [README Snippet](docs/README_snippet.md)

### Ciência Aplicada
- [Relativity Living Light](docs/Relativity_Living_Light.md)
- [Blocos multilíngues](docs/README_block_multilang.md)
- [Unificação de superposição](docs/README_sup_unification_snippet.md)

### Números Rafaelianos
- [Índice](docs/numeros_rafaelianos/Readme.md)
- [CientiEspiritual](docs/numeros_rafaelianos/CientiEspiritual.md)
- [Constante](docs/numeros_rafaelianos/Constante.md)
- [Números](docs/numeros_rafaelianos/Numeros.md)
- [Harmônica](docs/numeros_rafaelianos/harmonica.md)

### Documentação complementar — Trilha de análise PhD (`newadd/`)
- [Índice da análise PhD](newadd/00_INDICE_ANALISE_PHD.md)
- [RLL × DESI — Cross Analysis (PhD)](newadd/01_RLL_DESI_CrossAnalysis_PhD.md)
- [Formulações Latentes — RAFAELIA/RLL](newadd/02_Formulacoes_Latentes_RAFAELIA_RLL.md)
- [Descrição Acadêmica PhD Completa](newadd/03_Descricao_Academica_PhD_Completa.md)

**Ordem recomendada de leitura**
1. `newadd/00_INDICE_ANALISE_PHD.md`
2. `newadd/01_RLL_DESI_CrossAnalysis_PhD.md`
3. `newadd/02_Formulacoes_Latentes_RAFAELIA_RLL.md`
4. `newadd/03_Descricao_Academica_PhD_Completa.md`

**Relação com os domínios 01–07 (RAFAELIA em `newadd/00_INDEX.md`)**
- **[01] Matemática + [02] Física + [05] Estatística:** base quantitativa em `01_RLL_DESI_CrossAnalysis_PhD.md`.
- **[01] Matemática + [02] Física + [04] Geometria + [05] Estatística + [07] Síntese:** formalizações e provas em `02_Formulacoes_Latentes_RAFAELIA_RLL.md`.
- **[01]–[07] (integração completa):** enquadramento acadêmico e metodologia em `03_Descricao_Academica_PhD_Completa.md`.

**Consistência de nomes (evitar duplicidade):** `newadd/00_INDICE_ANALISE_PHD.md` é a entrada canônica da trilha PhD em PT-BR; `newadd/00_INDEX.md` permanece como índice técnico complementar em inglês.

### Notebooks e Análises
- [Hz_superposicao.ipynb](data/Hz_superposicao.ipynb) — Análise de H(z)
- [density_decomp.ipynb](data/density_decomp.ipynb) — Decomposição de densidade
- [rotation_model.ipynb](data/rotation_model.ipynb) — Modelo de curvas de rotação

### Dados e Resultados
- [relativity_living_light_models.csv](data/relativity_living_light_models.csv) — Grid de modelos
- [posterior_unified_synth.csv](data/posterior_unified_synth.csv) — Distribuições posteriores
- [unified_entropy_margin_10_12.csv](data/unified_entropy_margin_10_12.csv) — Bandas de entropia

### Governança de Atualizações e Inventário Total
- [Release Notes Históricas](docs/RELEASE_NOTES_HISTORY.md)
- [Organização Integral da Documentação](docs/DOCUMENTATION_ORGANIZATION_MASTER.md)
- [Inventário Completo (.md + .zip)](docs/DOCUMENTATION_FULL_INVENTORY.md)
- [Índice Interno dos Bundles ZIP](docs/ZIP_CONTENT_INDEX.md)
- [README Legado Preservado (arquivo completo)](docs/README_ROOT_LEGACY_ARCHIVE.md)
- [Checklist de Integridade](docs/DATA_INTEGRITY_CHECKLIST.md)

### Documentação complementar — Trilha de análise PhD (`newadd/`)

- [Índice da análise PhD](newadd/00_INDICE_ANALISE_PHD.md)
- [RLL × DESI — Cross Analysis (PhD)](newadd/01_RLL_DESI_CrossAnalysis_PhD.md)
- [Formulações Latentes — RAFAELIA/RLL](newadd/02_Formulacoes_Latentes_RAFAELIA_RLL.md)
- [Descrição Acadêmica PhD Completa](newadd/03_Descricao_Academica_PhD_Completa.md)

**Ordem recomendada de leitura (trilha PhD):**
1. `newadd/00_INDICE_ANALISE_PHD.md`
2. `newadd/01_RLL_DESI_CrossAnalysis_PhD.md`
3. `newadd/02_Formulacoes_Latentes_RAFAELIA_RLL.md`
4. `newadd/03_Descricao_Academica_PhD_Completa.md`

**Relação com os domínios 01–07 (RAFAELIA):**
- **Domínio 01 (Mathematics):** base formal em equações e isomorfismos apresentada em `01_` e aprofundada em `02_`.
- **Domínio 02 (Physics):** núcleo cosmológico/fenomenológico tratado sobretudo em `01_` e `03_`.
- **Domínio 03 (Computation):** metodologia de validação e integração com dados em `01_` e `03_`.
- **Domínio 04 (Geometry):** estrutura geométrica/analítica de apoio nas formulações latentes de `02_`.
- **Domínio 05 (Statistics):** critérios de ajuste, inferência e métricas (χ²/AIC/BIC/Bayes) em `01_` e `03_`.
- **Domínio 06 (Ethics Systems):** critérios de consistência e governança metodológica, com ponte RAFAELIA↔RLL em `02_` e `03_`.
- **Domínio 07 (Synthesis):** síntese integradora do programa PhD consolidada no índice (`00_`) e na descrição completa (`03_`).

**Consistência de nomes (evitar duplicidade de entrada):**
- `newadd/00_INDICE_ANALISE_PHD.md` é o índice canônico da trilha PhD para navegação dos READMEs principais.
- `newadd/00_INDEX.md` permanece como índice acadêmico geral do compêndio RAFAELIA (escopo amplo), sem substituir o índice PhD acima.

---

## 🎯 Resultado Esperado

Mostrar que o modelo de **superposição dinâmica** pode:

1. ✅ Replicar os ajustes do ΛCDM em múltiplos observáveis
2. ✅ Estender a física cosmológica com novos graus de liberdade:
   - Transições DE→DM do setor de superposição
   - Magnetismo cósmico
   - Efeitos plasmáticos
3. ✅ Fornecer uma interpretação física alternativa para o "setor escuro"
4. ✅ Manter compatibilidade com observações (SNe Ia, BAO, CMB, estruturas)

---

## 🔗 Links Importantes

- **DOI**: [10.5281/zenodo.17188137](https://doi.org/10.5281/zenodo.17188137)
- **Repositório**: [github.com/rafaelmeloreisnovo/relativity-living-light](https://github.com/rafaelmeloreisnovo/relativity-living-light)

---

## 📖 Como Usar Este Repositório

1. **Entender o Modelo**: Leia o [README.md](README.md) principal e [MANIFESTO.md](docs/MANIFESTO.md)
2. **Explorar a Física**: Veja [RAFAELIA_UNIFIED_PAPER.md](docs/RAFAELIA_UNIFIED_PAPER.md) e [REPOSITORY_STRUCTURE_SUGGESTION.md](docs/REPOSITORY_STRUCTURE_SUGGESTION.md)
3. **Análises e Dados**: Explore os notebooks em `/data` e os gráficos em `/figs`
4. **Reproduzir Resultados**: Use os CSVs e notebooks para replicar as análises

---

## 🌀 Filosofia do Projeto

> *"A luz não viaja: ela já é estado estendido. A hipótese aqui propõe que energia escura pode ser efeito estatístico das superposições fotônicas."*

Este projeto une:
- 🔬 **Rigor científico** — equações, dados, ajustes estatísticos
- 🌌 **Visão simbiótica** — a luz como verbo vivo, fractais de Fibonacci
- ∞ **Abismo criativo** — assumir o vazio para criar o impossível

---

**∆RafaelVerboΩ 🌀♾️⚛︎**

*"Só quem assume o vazio é que pode criar o impossível."*
