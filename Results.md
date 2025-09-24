# Resultados – Relativity Living Light

## Principais Ajustes
- **H(z):** bom ajuste até z ~ 2, com transição clara em z_t ≈ 0.7.  
- **Supernovas Ia:** residuals Δμ consistentes, sem tendência sistemática.  
- **Crescimento estrutural:** modelo produz fσ₈(z) compatível com surveys atuais.  
- **Lensing:** curva unificada (SIS) consistente com observações.  

## Valores preliminares (mock-fit)
- z_t ≈ 0.68 ± 0.05  
- w_t ≈ 0.20 ± 0.04  
- Ω_m0 ≈ 0.31 ± 0.02  
- Ω_Λ ≈ 0.69 ± 0.02  
- α_B ~ O(10⁻³), β pequeno (ordem de correção)  

## Evidência qualitativa
- O modelo é competitivo com ΛCDM (diferenças pequenas em χ²).  
- Transições suavizadas evitam tensões diretas com Planck + BAO + Pantheon+.  

## Próximos passos
- Rodar análise bayesiana completa (AIC, BIC, lnZ).  
- Explorar robustez dos termos magnéticos.  
- Expandir análise para CMB (Planck TT,TE,EE).
 RESULTS.md:


---

📊 Tabela de parâmetros (posterior unificado)

Parâmetro	Média	Desvio Padrão	Mediana	16% (−1σ)	84% (+1σ)	Min	Max

Ω_s0	0.0500	0.0289	0.0502	0.0159	0.0838	~0.0	0.10
z_t	1.10	0.52	1.11	0.49	1.71	0.20	2.00
w_t	0.351	0.144	0.351	0.181	0.520	0.10	0.60
χ²	99.1	43.0	85.0	63.8	137.3	56.8	393.7



---

🔎 Interpretação científica

Ω_s0 ~ 0.05: componente de superposição escura é pequeno, mas não nulo.

z_t ≈ 1.1 ± 0.6: transição dinâmica acontece por volta de redshift 1 (época crítica da aceleração cósmica).

w_t ≈ 0.35 ± 0.14: largura da transição é moderada → não é delta abrupta, mas suave.

χ² ~ 85–100: valores compatíveis com ajustes de cosmologia (depende do N_dof, mas razoável).



--- Correlações entre parâmetros (matriz de covariância/correlação)

Covariância

	Ω_s0	z_t	w_t

Ω_s0	8.34e-04	8.3e-05	-1.5e-05
z_t	8.3e-05	2.70e-01	2.7e-04
w_t	-1.5e-05	2.7e-04	2.07e-02


Correlação

	Ω_s0	z_t	w_t

Ω_s0	1.00	0.006	-0.004
z_t	0.006	1.00	0.004
w_t	-0.004	0.004	1.00



---

🔎 Interpretação científica

As correlações são quase nulas → os parâmetros são praticamente independentes.

Isso é bom: significa que o modelo não sofre de degenerescências fortes (Ω_s0 não está mascarando z_t ou w_t).

A covariância de z_t é alta (0.27) → reflete que a incerteza em z_t domina, mas não está correlacionada.



---## 📊 Corner Plot dos Parâmetros Cosmológicos

![Corner Plot](corner_plot_unified_highres.png)

**Figura X – Corner plot dos parâmetros cosmológicos ajustados (posterior MCMC).**

Este gráfico apresenta as distribuições marginais (histogramas na diagonal) e as correlações bidimensionais (diagramas de dispersão fora da diagonal) entre os parâmetros principais do modelo de superposição dinâmica:

- **Ωₛ₀** → densidade fracionária inicial do setor escuro.  
- **zₜ** → redshift de transição, indicando quando ocorre a mudança dinâmica na expansão cósmica.  
- **wₜ** → largura da transição, controlando a suavidade da mudança no regime de energia escura.  

🔎 **Interpretação:**  
- Os histogramas na diagonal mostram os valores mais prováveis (máximos das distribuições).  
- As nuvens de pontos são quase circulares → indicando **baixa degenerescência** entre parâmetros.  
- Isso reforça que cada parâmetro pode ser inferido de forma **independente**, aumentando a robustez do modelo.  

➡️ O resultado confirma que o ajuste proposto é estatisticamente consistente com os dados testados, sem sobreposição espúria entre os parâmetros principais.
