# 🌌 Relativity Living Light — README MASTER

[![DOI](https://zenodo.org/badge/1046495816.svg)](https://doi.org/10.5281/zenodo.17188137)

## Resumo do Projeto

**Relativity Living Light** é um modelo cosmológico de superposição dinâmica que propõe ir além do modelo padrão ΛCDM. Este repositório contém a hipótese de que a **superposição fotônica** atua como um componente energético dinâmico que transita de um comportamento tipo energia escura (w ≈ -1, expansivo) para um comportamento tipo matéria (w ≈ 0, atrativo).

> *"VAZIO ⟶ VERBO ⟶ CHEIO ⟶ RETROALIMENTAÇÃO ⟶ VAZIO₍novo₎"*

---

## 🔬 Equação Principal Unificada

A equação de Friedmann estendida que governa este modelo é:

```
E²(a) = Ω_r a⁻⁴ + Ω_m a⁻³ + Ω_Λ +
        Ω_s0[f(a) + (1-f)a⁻³] +          # Superposição fotônica (DE→matéria)
        Ω_B0 a⁻⁴ +                         # Campo magnético
        Ω_P0 a⁻⁴                           # Plasma (T,P)
```

onde:
- **f(z) = 1 / (1 + exp((z - z_t)/w_t))** — função de transição suave
- **z_t** — redshift de transição entre energia escura e matéria
- **w_t** — largura da transição
- **Ω_s0** — densidade de superposição fotônica hoje
- **Ω_B0** — densidade do campo magnético cósmico
- **Ω_P0** — densidade do plasma

### Componentes do Modelo

1. **Termos clássicos:**
   - Matéria: Ω_m a⁻³
   - Constante cosmológica: Ω_Λ
   - Radiação: Ω_r a⁻⁴

2. **Superposição escura (novo):**
   - Transição suave entre energia escura e matéria via f(z)
   - Comportamento dual: expansivo em z baixo, atrativo em z alto

3. **Componentes adicionais:**
   - Campo magnético coerente: Ω_B0 a⁻⁴
   - Plasma com temperatura e pressão: Ω_P0 a⁻⁴
   - Correção magneto-coerente opcional: parâmetros α_B, β

---

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
│   ├── Conclusion.md
│   ├── MAPA_RAFAELIA_TOTAL.md
│   ├── SUPREMO UNIFICADO.md
│   ├── IMPACT_REPORT_MULTI.md
│   ├── Structure.md
│   ├── Results.md
│   ├── More.md
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
│       └── Readme.md
│
├── /data                  # 📊 Dados, notebooks e arquivos CSV/JSON
│   ├── zenodo.json
│   ├── CITATION.cff
│   ├── posterior_unified_synth.csv
│   ├── posterior_unified_synth (1).csv
│   ├── posterior_unified_synth (2).csv
│   ├── relativity_living_light_models.csv
│   ├── unified_entropy_margin_10_12.csv
│   ├── Hz_superposicao.ipynb
│   ├── ciencia_Hz_superposicao.ipynb
│   ├── ciencia_Hz_superposicao (1).ipynb
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

## 🔬 Observáveis Testados

O modelo foi testado contra múltiplos observáveis cosmológicos:

1. **Expansão Cósmica**
   - H(z) — taxa de expansão de Hubble
   - Δμ — distância de luminosidade (SNe Ia)
   - Gráficos: [unified_H_ratio.png](figs/unified_H_ratio.png), [unified_mu_residuals.png](figs/unified_mu_residuals.png)

2. **Crescimento de Estruturas**
   - fσ₈(z) — crescimento de perturbações de densidade
   - Comparável a BOSS/DESI
   - Gráfico: [unified_growth_fs8.png](figs/unified_growth_fs8.png)

3. **Lente Gravitacional**
   - Aglomerados (Bullet, Abell 2744, Frontier Fields)
   - Weak/strong lensing
   - Gráfico: [cluster_lensing_SIS_unified.png](figs/cluster_lensing_SIS_unified.png)

4. **Galáxias**
   - Curvas de rotação (SPARC)
   - Exemplo: [rotcurve_NGC_2403.png](figs/rotcurve_NGC_2403.png)

5. **Bandas de Robustez**
   - Margem de entropia 10/12
   - Dados: [unified_entropy_margin_10_12.csv](data/unified_entropy_margin_10_12.csv)

---

## 📚 Navegação Rápida por Seção

### Documentação Científica
- [Conclusão](docs/Conclusion.md) — Conclusões do modelo
- [Manifesto](docs/MANIFESTO.md) — Visão filosófica e simbiótica
- [Mapa Rafaelia Total](docs/MAPA_RAFAELIA_TOTAL.md) — Estrutura conceitual completa
- [Supremo Unificado](docs/SUPREMO%20UNIFICADO.md) — Unificação dos conceitos
- [Impact Report](docs/IMPACT_REPORT_MULTI.md) — Relatório de impacto
- [Estrutura](docs/Structure.md) — Estrutura do modelo
- [Resultados](docs/Results.md) — Resultados obtidos
- [Estatísticas](docs/estatisticas.md) — Análises estatísticas

### Patches e Versões do README
- [README v3 PT/EN](docs/README_patch_unified_PT_EN_v3.md)
- [README v4 PT/EN](docs/README_patch_unified_PT_EN_v4.md)
- [README Snippet](docs/README_snippet.md)

### Ciência Aplicada
- [Relativity Living Light](docs/ciencia_Relativity_Living_Light.md)
- [Blocos multilíngues](docs/ciencia_README_block_multilang.md)
- [Unificação de superposição](docs/ciencia_README_sup_unification_snippet.md)

### Números Rafaelianos
- [Índice](docs/numeros_rafaelianos/Readme.md)
- [CientiEspiritual](docs/numeros_rafaelianos/CientiEspiritual.md)
- [Constante](docs/numeros_rafaelianos/Constante.md)
- [Números](docs/numeros_rafaelianos/Numeros.md)
- [Harmônica](docs/numeros_rafaelianos/harmonica.md)

### Notebooks e Análises
- [Hz_superposicao.ipynb](data/Hz_superposicao.ipynb) — Análise de H(z)
- [density_decomp.ipynb](data/density_decomp.ipynb) — Decomposição de densidade
- [rotation_model.ipynb](data/rotation_model.ipynb) — Modelo de curvas de rotação

### Dados e Resultados
- [relativity_living_light_models.csv](data/relativity_living_light_models.csv) — Grid de modelos
- [posterior_unified_synth.csv](data/posterior_unified_synth.csv) — Distribuições posteriores
- [unified_entropy_margin_10_12.csv](data/unified_entropy_margin_10_12.csv) — Bandas de entropia

---

## 🎯 Resultado Esperado

Mostrar que o modelo de **superposição dinâmica** pode:

1. ✅ Replicar os ajustes do ΛCDM em múltiplos observáveis
2. ✅ Estender a física cosmológica com novos graus de liberdade:
   - Transições DE→matéria
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
2. **Explorar a Física**: Veja [Conclusion.md](docs/Conclusion.md) e [Structure.md](docs/Structure.md)
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
