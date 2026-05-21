# RLL Falseability Matrix (RLL × GR/ΛCDM)

> Status: **programa de teste falsificável**, não reivindicação de prova.

## 1) Núcleo científico mínimo (operacional)

\[
\Phi_{\gamma}^{obs}=\mathcal{L}_{multi}\!\left[\Phi_{\gamma}^{fonte}\right]+\epsilon_{RLL}
\]

\[
\epsilon_{RLL}(\mathcal{O},z,t)=\mathcal{O}_{obs}(z,t)-\mathcal{O}_{GR+\Lambda CDM}(z,t)
\]

com \(\mathcal{O}\in\{H(z), D_L(z), \mu(z), w(z), f\sigma_8(z), C_\ell^{lens}, h(f)\}\).

Interpretação:
- se \(\epsilon_{RLL}\approx 0\) dentro dos erros, GR/ΛCDM explicam;
- se \(\epsilon_{RLL}\neq 0\), RLL precisa prever **sinal, amplitude, escala, erro e condição observacional**.

## 2) Vetores principais e critérios de refutação

| Vetor | Observáveis | Base pública | Exigência RLL | Como falsifica |
|---|---|---|---|---|
| A. Cosmologia de precisão | \(H(z), D_L(z),\mu(z), f\sigma_8(z)\) | DESI BAO, Planck 2018, Pantheon+ | Curvas e \(\chi^2\) com penalidade justa | Pior que ΛCDM em AIC/BIC |
| B. Energia escura dinâmica | \(w_{RLL}(z)\), mapeamento CPL \(w_0,w_a\) | DESI+Planck+SNe | Curva efetiva consistente | Intervalos credíveis excluem modelo |
| C. \(\sum m_\nu\), \(H_0\), \(\Omega_m\), \(\sigma_8\) | parâmetros acoplados | análises DESI DR2 | não “resolver” DE quebrando neutrinos/H0 | melhora parcial com quebra de pilar |
| D. Lenteamento dinâmico / BH errante | \(\theta_{obs}(t)\), \(\epsilon^{lens}_{RLL}(t)\) | HST/Gaia/JWST/Roman | assinatura temporal prevista | GR móvel explica tudo |
| E. Rede cósmica + lenteamento fraco | \(P(k), C_\ell^{lens},\gamma(\theta),\kappa(\theta)\) | COSMOS-Web, DES, HSC, Euclid, KiDS | mapas e resíduos coerentes | padrão não reproduzido |
| F. Ondas gravitacionais | \(h_{obs}(f)=h_{GR}(f)+\epsilon^{GW}_{RLL}(f)\) | LIGO/Virgo/KAGRA | fase/amplitude/eco/dispersão | assinatura ausente |
| G. QGEM / laboratório | testemunha de emaranhamento \(E_N\) | literatura QGEM | direção do efeito (aumenta/reduz/neutro) | resultado contradiz previsão |

## 3) Camadas de escrita científica (antiplágio)

1. **Base bibliográfica** (DESI, Planck, Pantheon+, JWST, LIGO, QGEM).
2. **Formulação própria** (equações residuais e multi-lenteamento).
3. **Regra de refutação** (AIC/BIC + intervalos + resíduos observacionais).

## 4) Ponte com as fórmulas autorais (T7 / coerência informacional)

As fórmulas enviadas (1..50) podem ser tratadas como **camada de estado latente** de um modelo de geração de hipóteses:
- espaço toroidal \(\mathbb{T}^7\) e estado \(\mathbf{s}\in[0,1)^7\);
- dinâmica de coerência/entropia \((C_t,H_t,\alpha)\);
- termos espectrais \(S(\omega), R_L\);
- camada de hashing/integridade (CRC/Merkle);
- operador informacional \(\mathcal{I}=\Phi(\mathbf{s},S,H,C,G)\).

Para manter falsificabilidade física, essa camada deve projetar previsões em observáveis cosmológicos mensuráveis (seção 2), evitando inferências não observáveis.

## 5) Implementação mínima no repositório

- Script: `rll_vs_lcdm.py`
- Entradas atuais: `data/real/Hz_data_real.csv`, `data/real/BAO_data_real.csv`
- Saídas: `results/rll_vs_lcdm_predictions.csv`, `results/rll_vs_lcdm_summary.json`
- Métricas: \(\chi^2\), AIC, BIC (ΛCDM vs RLL-CPL efetivo)

## 6) Referências-base iniciais (cabeçalho bibliográfico)

1. Planck Collaboration (2018 results VI; publ. 2020).
2. Pantheon+ SN Ia dataset (2022/2023).
3. DESI BAO / DR2-era analyses (2025).
4. DESI dynamic dark energy / neutrino-mass tension analyses (2025).
5. Astrometric microlensing PBH/BH studies (Gaia/HST).
6. JWST COSMOS-Web structure/lensing products.
7. LIGO/Virgo/KAGRA GW catalogs and DM-environment tests.
8. QGEM protocol literature.

## 7) Critério final (síntese)

\[
\text{observação} - \text{GR/}\Lambda\text{CDM} = \text{resíduo}
\]

Se o resíduo é ruído, hipótese descartada. Se é coerente e **predito antes** com erro quantificado, hipótese ganha conteúdo científico.
