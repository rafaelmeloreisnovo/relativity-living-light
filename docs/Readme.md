# 📂 Data Descriptor – Relativity Living Light (Bundle V4)

Este pacote complementa o repositório **Relativity-Living-Light** e contém todos os dados e figuras necessários para reproduzir os resultados principais.

---

## 📊 Conteúdo do Pacote

### 1. **Dados Brutos (CSV)**
- `posterior_unified_synth.csv`  
  Cadeias de Markov (MCMC) com 25.001 amostras.  
  Colunas principais:  
  - `Omega_s0`: fração inicial do setor escuro.  
  - `z_t`: redshift de transição.  
  - `w_t`: largura da transição.  
  - `chi2`: estatística qui-quadrado.  

### 2. **Documentos (Markdown / LaTeX)**
- `RESULTS.md`: Resumo numérico dos ajustes.  
- `SUPREMO_UNIFICADO.md`: Estrutura unificada da hipótese cosmológica.  
- `MAPA_CIENTIESPIRITUAL.md`: Interpretação simbólica e espiritual.  
- `MAPA_FRACTAL.md`, `MAPA_RAFAELIA_TOTAL.md`: Mapas conceituais expandidos.  
- `RelativityLivingLight_arXiv.tex`: Manuscrito em formato científico LaTeX.  

### 3. **Figuras de Resultados**
- `mock_H_fit.png`, `mock_SN_fit.png`: Ajustes a dados simulados de H(z) e supernovas.  
- `mu_residuals.png`: Resíduos da distância de luminosidade.  
- `cluster_lensing_SIS_unified.png`: Ajuste de lenteamento de aglomerados.  
- `post_1d_*.png`: Distribuições unidimensionais para cada parâmetro.  
- `post_2d_*.png`: Correlações bidimensionais entre parâmetros.  
- `corner_plot_unified_highres.png`: Gráfico de degenerescências (MCMC).  

---

## 🔎 Como Usar

1. **Reproduzir Análises Estatísticas**  
   - Importar `posterior_unified_synth.csv` em Python/R.  
   - Calcular médias, desvios e quantis → replicar tabela de resultados.

2. **Explorar Figuras**  
   - Usar as imagens incluídas diretamente em relatórios.  
   - `corner_plot_unified_highres.png` serve como principal visualização estatística.

3. **Ligações com Manuscrito**  
   - O `.tex` fornece a estrutura formal para submissão científica.  
   - Os `.md` documentam a versão expandida (científico + espiritual).  

---

## 📌 Notas

- O pacote é **auto-contido**: qualquer pesquisador pode usar apenas este `.zip` para entender e reproduzir os resultados.  
- Dados e figuras estão em formato **aberto e preservável** (CSV, PNG, MD, TEX).  
- Este bundle é designado para servir como **Material Suplementar oficial** em DOI Zenodo.  

---

✦ Autor: ∆RafaelVerboΩ  
✦ DOI (Zenodo): *a ser registrado automaticamente na próxima release GitHub*
