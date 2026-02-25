# 33. Apêndice — Glossário Consolidado

[⬅️ Capítulo anterior](./32_roadmap_medio_longo_prazo.md) | [📚 Sumário do livro](./README.md) | [Capítulo próximo ➡️](./34_apendice_faq.md)

Referência editorial única para símbolos, definições e convenções usadas no livro.

## Índice rápido
- [Cosmologia padrão](#cosmologia-padrão)
- [Superposição](#superposição)
- [Magnetismo](#magnetismo)
- [Plasma](#plasma)
- [Observáveis](#observáveis)
- [Conversões](#conversões)

## Cosmologia padrão

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **a** | Fator de escala | Razão entre escala em *t* e a escala atual: \(a(t)=R(t)/R_0\) | adimensional | \(a=1\) hoje; \(a \to 0\) no passado remoto |
| **z** | Redshift | \(z=1/a-1\) | adimensional | \(z=0\) hoje; \(z>0\) para o passado |
| **H(z)** | Parâmetro de Hubble | Taxa de expansão em função de *z* | km/s/Mpc | Em ΛCDM, tipicamente cresce com *z* |
| **H₀** | Hubble atual | Valor de \(H(z)\) em \(z=0\) | km/s/Mpc | Faixa observacional ~67–74 |
| **Ω_m** | Fração de matéria | Densidade de matéria relativa à crítica | adimensional | Ordem de grandeza atual ~0,3 |
| **Ω_Λ** | Fração de energia escura | Componente de vácuo em ΛCDM | adimensional | Ordem de grandeza atual ~0,7 |
| **w** | Equação de estado | Relação pressão-densidade: \(p=w\rho c^2\) | adimensional | Matéria: 0; radiação: 1/3; Λ: -1 |

## Superposição

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **Ω_s0** | Amplitude de superposição hoje | Fração atual da componente de superposição | adimensional | Parâmetro livre do modelo |
| **f(a)** | Fração de coerência (em *a*) | Fração logística de estado coerente da componente | adimensional | Varia entre 0 e 1 |
| **f(z)** | Fração de coerência (em *z*) | \(f(z)=\frac{1}{1+\exp((z-z_t)/w_t)}\) | adimensional | Controlada por \(z_t\) e \(w_t\) |
| **z_t** | Redshift de transição | Redshift no qual \(f(z_t)=0{,}5\) | adimensional | Define a época central da transição |
| **w_t** | Largura da transição | Escala de suavização da logística de \(f(z)\) | adimensional | Menor valor ⇒ transição mais abrupta |
| **w_eff(z)** | EoS efetiva da superposição | \(w_{eff}(z)=-\frac{f(z)}{f(z)+(1-f)a^{-3}}\) | adimensional | Interpola entre comportamento tipo DE e DM |

### Exemplo de uso — `f(z)`
> Em ajuste de dados de expansão, `f(z)` controla **quando** e **quão suave** é a transição entre regimes efetivos no termo de superposição. Um cenário com `z_t` maior desloca a transição para épocas mais antigas.

### Exemplo de uso — `w_eff`
> Ao comparar modelos no diagrama `w(z)`, `w_eff` resume a dinâmica da componente unificada: próximo de `-1` em regime tipo energia escura e próximo de `0` em regime tipo matéria.

## Magnetismo

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **B** | Campo magnético cósmico | Intensidade do campo magnético médio efetivo | T (ou G) | Escalas cosmológicas costumam ser tratadas em nG |
| **ρ_B** | Densidade magnética | \(\rho_B = B^2/(2\mu_0 c^2)\) | kg/m³ | Contribuição energética associada ao campo |
| **Ω_B0** | Fração magnética hoje | \(\rho_B(z=0)/\rho_c\) | adimensional | Tipicamente pequena em relação a Ω_m |
| **α_B** | Acoplamento magneto-coerente | Coeficiente de modulação magnética da superposição | adimensional | Parâmetro fenomenológico |
| **β** | Expoente de não linearidade | Expoente do termo de modulação magnética | adimensional | Ajusta curvatura da resposta |

## Plasma

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **ρ_P** | Densidade plasmática | Soma de contribuição térmica e magnética do plasma | kg/m³ | \(\rho_P\sim\frac{3}{2}nk_BT/c^2 + B^2/(2\mu_0c^2)\) |
| **Ω_P0** | Fração plasmática hoje | \(\rho_P(z=0)/\rho_c\) | adimensional | Parâmetro adicional do modelo |
| **n** | Densidade numérica | Número de partículas por volume | m⁻³ | Depende do meio (intergaláctico, intracluster etc.) |
| **T** | Temperatura do plasma | Escala térmica média das partículas | K | Frequentemente expressa também em eV/keV/MeV |
| **k_B** | Constante de Boltzmann | Conversão entre energia e temperatura | J/K | Valor SI: \(1{,}380649\times10^{-23}\) |

## Observáveis

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **E(z)** | Hubble normalizado | \(E(z)=H(z)/H_0\) | adimensional | Facilita comparação entre modelos |
| **D_L(z)** | Distância de luminosidade | Distância inferida via fluxo-luminosidade | Mpc | Base para análise de supernovas |
| **μ(z)** | Módulo de distância | \(\mu = 5\log_{10}(D_L/\mathrm{Mpc})+25\) | mag | Observável direto em SNe Ia |
| **Δμ(z)** | Resíduo de distância | \(\Delta\mu=\mu_{modelo}-\mu_{\Lambda CDM}\) | mag | Quantifica desvio em relação ao modelo de referência |
| **f** | Taxa de crescimento | \(f=d\ln\delta/d\ln a\) | adimensional | Mede crescimento de estrutura |
| **σ₈** | Amplitude de flutuação | RMS em 8 \(h^{-1}\) Mpc | adimensional | Normalização de estrutura em larga escala |
| **fσ₈** | Observável de crescimento | Produto \(f(z)\sigma_8(z)\) | adimensional | Principal alvo de medidas RSD |

### Exemplo de uso — `fσ8`
> Em comparação com dados de redshift-space distortions, curvas de `fσ8(z)` permitem distinguir cenários com mesma expansão de fundo (`H(z)`) mas crescimento estrutural diferente.

### Exemplo de uso — `Δμ`
> Em análises de supernovas, `Δμ(z)` é usado para visualizar sistematicamente onde o modelo fica acima/abaixo de ΛCDM ao longo do redshift.

## Conversões

| Símbolo | Nome | Definição | Unidade | Faixa/Observação |
|---|---|---|---|---|
| **z \leftrightarrow a** | Redshift ↔ fator de escala | \(z=1/a-1\), \(a=1/(1+z)\) | adimensional | Conversão fundamental para todas as equações de evolução |
| **ρ_c(z)** | Densidade crítica | \(\rho_c(z)=3H^2(z)/(8\pi G)\) | kg/m³ | Referência para definir todos os Ω |
| **ρ_X \leftrightarrow Ω_X** | Densidade física ↔ relativa | \(\rho_X=\Omega_X\rho_c\), \(\Omega_X=\rho_X/\rho_c\) | kg/m³ e adimensional | Relação usada em tabelas e códigos |
| **k_B T** | Temperatura ↔ energia | Conversão térmica (eV, keV, MeV) | J ou eV | Regra útil: 1 eV ≈ 11.604 K |

---

Nota editorial: este capítulo consolida a notação para consulta rápida e pode ser atualizado quando novos símbolos entrarem no corpo principal do livro.
