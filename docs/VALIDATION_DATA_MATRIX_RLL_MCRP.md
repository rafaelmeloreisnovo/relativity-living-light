# VALIDATION DATA MATRIX — RLL/MCRP

**Status global:** Sintético com trilha **Parcial real em preparação**.

Este documento organiza a matriz de validação para as duas camadas:

\[
\Phi_{eff}(E,t,\Omega)=\Phi_{ext}(E,t,\Omega)\cdot T_M(E,\Omega;M(t),m(t),SW)
\]

\[
E^2(a)= \Omega_r a^{-4} + \Omega_m a^{-3} + \Omega_\Lambda
+ \Omega_{s0}[f(a)+(1-f)a^{-3}]
+ \Omega_{B0} a^{-4} + \Omega_{P0} a^{-4}
\]

\[
f(z)=\frac{1}{1+\exp((z-z_t)/w_t)}
\]

## Regras transversais
- Não afirmar que AMAS/SAA prova o RLL.
- Não afirmar “Real validado” sem dados reais processados, métricas e reprodutibilidade.
- Cada camada separa **Hipótese / Dado / Modelo / Métrica**.
- Cada fonte exige cadeia de custódia (origem, versão, licença, data de acesso, hash, script).

---

## A) Campo magnético terrestre

**Fontes**
- NOAA/NCEI IGRF14.
- WMM2025.
- ESA Swarm.

**Variáveis**
- B total.
- X, Y, Z.
- F, H.
- Inclinação.
- Declinação.
- Variação secular.
- Coeficientes de Gauss.

**Relação com o modelo**
- `M(t)`: estrutura de larga escala do campo.
- `m(t)`: estrutura regional/multipolar.
- `T_M`: transmissividade magnética dependente de energia, direção e estado geomagnético.

**H/D/M/M**
- Hipótese: a evolução de `M(t)` e `m(t)` modula `T_M`.
- Dado: IGRF14, WMM2025, Swarm.
- Modelo: reconstrução espaço-temporal do campo.
- Métrica: RMS, nT/ano, drift espacial, IC.

## B) Anomalia Magnética do Atlântico Sul (AMAS/SAA)

**Fontes**
- ESA Swarm 2014–2025.
- NASA South Atlantic Anomaly.
- Artigo científico primário citado pela matéria do G1.
- Estudos sobre reverse flux patches e core-mantle boundary.

**Relação com o modelo**
- Enfraquecimento regional de `M(t)`.
- Aumento regional de `T_M` para faixas de energia/rigidez.
- Risco para satélites.
- Partículas energéticas em LEO.

**H/D/M/M**
- Hipótese: mudanças regionais do campo interno alteram a transmissão local.
- Dado: Swarm + NASA + literatura primária.
- Modelo: evolução de mínimo, área e deslocamento da AMAS.
- Métrica: drift km/ano, variação nT/ano, área sob limiar, IC.

## C) Forçamento heliosférico

**Fontes**
- NASA OMNI/SPDF.

**Variáveis**
- IMF.
- Bz.
- Velocidade do vento solar.
- Densidade.
- Pressão dinâmica.
- Kp.
- Dst.
- AE.
- F10.7.
- Fluxo de prótons.

**Relação com o modelo**
- `SW` como entrada de `T_M`.
- Modulação de `\Phi_ext`.

**H/D/M/M**
- Hipótese: SW modula `\Phi_ext` e parte de `T_M`.
- Dado: OMNI/SPDF.
- Modelo: acoplamento temporal SW→fluxo incidente.
- Métrica: correlação defasada, erro de predição, sensibilidade por regime solar.

## D) Raios cósmicos

**Fontes**
- NMDB neutron monitor database.
- Dados de variação Forbush.
- Eventos GLE.

**Relação com o modelo**
- Proxy observacional de `\Phi_ext`.
- Modulação heliosférica.

**H/D/M/M**
- Hipótese: contagens NMDB rastreiam modulação externa relevante.
- Dado: séries multiesação, Forbush, GLE.
- Modelo: normalização por estação e composição robusta.
- Métrica: coerência inter-estação, resposta a eventos, erro temporal.

## E) Radiação orbital

**Fontes**
- NASA SAA.
- SPENVIS AE9/AP9.
- GOES energetic particles.
- Relatórios públicos de eventos em satélites (quando disponíveis).

**Relação com o modelo**
- `T_M`.
- `\Phi_eff`.
- Dose orbital.
- Single event upsets.

**H/D/M/M**
- Hipótese: variabilidade de transmissão explica parte da variabilidade de dose/eventos.
- Dado: GOES + AE9/AP9 + eventos públicos.
- Modelo: projeção por órbita/energia.
- Métrica: RMS espectral, skill score de eventos, taxa de acerto por janela temporal.

## F) Ionização e química atmosférica

**Fontes**
- IntCal20 para 14C.
- Proxies 10Be.
- Reanálises atmosféricas.
- Modelos de ionização.

**Relação com o modelo**
- `Q_ion`.
- Química reativa.
- NOx.
- HOx.
- O3.

**H/D/M/M**
- Hipótese: variações de fluxo efetivo deixam assinatura em ionização e proxies.
- Dado: 14C/10Be + reanálises.
- Modelo: fluxo→ionização→química/proxy.
- Métrica: ajuste temporal, robustez a incerteza de datação e IC.

## G) Cosmologia RLL

**Fontes**
- DESI DR2 BAO.
- Pantheon+ SNe Ia.
- Planck 2018.
- H(z) cosmic chronometers.
- fσ8/crescimento de estrutura.

**Relação com o modelo**
- `E²(a)`.
- `f(z)`.
- `w(z)`.
- Comparação RLL vs ΛCDM.

**H/D/M/M**
- Hipótese: RLL compete com ΛCDM/w0waCDM em expansão + crescimento.
- Dado: BAO+SNe+CMB+H(z)+fσ8.
- Modelo: likelihood conjunta com covariâncias.
- Métrica: χ², AIC, BIC, MCMC e robustez por subamostra.
