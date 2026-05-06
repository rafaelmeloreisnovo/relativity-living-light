# VALIDATION DATA MATRIX — RLL/MCRP

Status geral: **Parcial real em preparação**.

Este documento organiza a matriz de validação observacional em camadas para a equação:

\[
\Phi_{\mathrm{eff}}(E,t,\Omega)=\Phi_{\mathrm{ext}}(E,t,\Omega)\cdot T_M(E,\Omega;M(t),m(t),SW)
\]

e para a camada cosmológica RLL \(E^2(a), f(z), w(z)\).

## Regras metodológicas transversais
- Não tratar AMAS/SAA como prova do RLL.
- Não declarar validação real completa sem download/processamento reproduzível.
- Separar explicitamente: **Hipótese**, **Dado**, **Modelo**, **Métrica**.
- Manter cadeia de custódia (fonte, versão, acesso, hash, script).
- Até execução dos pipelines: status operacional = **Parcial real em preparação**.

---

## A) Campo magnético terrestre

### Fontes primárias
- IGRF14 (IAGA/NOAA/BGS).
- WMM2025 (NOAA/NGA/BGS).
- ESA Swarm (nível de campo e derivados).

### Variáveis-alvo
- Intensidade total: \(B\) / \(F\).
- Componentes: \(X, Y, Z\).
- Horizontal: \(H\).
- Inclinação e declinação.
- Variação secular (SV).
- Coeficientes de Gauss \(g_n^m, h_n^m\).

### Relação com RLL/MCRP
- \(M(t)\): componente de grande escala (momento dipolar/estrutura global).
- \(m(t)\): modulação regional/local (assimetria e patches).
- \(T_M\): função de transmissão magnetoespacial dependente de energia, direção e estado geomagnético.

### Estrutura H-D-M-M
- Hipótese: a transmissão regional responde à evolução conjunta \(M(t),m(t)\).
- Dado: séries IGRF/WMM + observações Swarm.
- Modelo: reconstrução espaço-temporal do campo e derivação de \(T_M\).
- Métrica: RMS, tendência nT/ano, deslocamento espacial, IC.

---

## B) AMAS / South Atlantic Anomaly (SAA)

### Fontes primárias
- ESA Swarm (2014–2025).
- NASA South Atlantic Anomaly resources.
- PEPI 2025: *Core field changes from eleven years of Swarm satellite observations*.
- PEPI 2017: *Relating the South Atlantic Anomaly and geomagnetic flux patches*.

### Variáveis-alvo
- Mínimo de intensidade do campo.
- Área abaixo de limiar (nT).
- Drift longitudinal/latitudinal do núcleo anômalo.
- Estrutura de reverse flux patches no CMB.

### Relação com RLL/MCRP
- Vínculo físico entre flux patches no limite núcleo-manto e geometria da anomalia.
- Tradução para risco orbital (exposição de satélites) como observável de \(\Phi_{\mathrm{eff}}\), não como prova isolada da teoria completa.

### Estrutura H-D-M-M
- Hipótese: mudanças de topologia no campo interno alteram \(T_M\) regional da AMAS.
- Dado: Swarm + referências NASA/PEPI.
- Modelo: mapas temporais e rastreamento de mínimos/anéis de baixa intensidade.
- Métrica: drift km/ano, variação nT/ano, área sob limiar e IC.

---

## C) Forçamento heliosférico

### Fontes primárias
- NASA OMNI / SPDF.

### Variáveis-alvo
- IMF total e componentes (incl. \(B_z\)).
- Velocidade do vento solar.
- Densidade de plasma e pressão dinâmica.
- Índices geomagnéticos: Kp, Dst, AE.
- F10.7.
- Fluxo de prótons energéticos.

### Relação com RLL/MCRP
- Entrada exógena **SW** na função \(T_M\).
- Forçante temporal principal de \(\Phi_{\mathrm{ext}}\).

### Estrutura H-D-M-M
- Hipótese: variações de SW modulam transmissão regional e carga radiativa incidente.
- Dado: OMNI multi-resolução.
- Modelo: acoplamento SW→\(\Phi_{\mathrm{ext}}\) com janela temporal sincronizada.
- Métrica: correlação defasada, erro preditivo de fluxo efetivo, sensibilidade por regime solar.

---

## D) Raios cósmicos

### Fontes primárias
- NMDB (neutron monitor database).

### Variáveis-alvo
- Contagens por estação.
- Eventos GLE.
- Quedas Forbush.
- Histórico e stream quase em tempo real.

### Relação com RLL/MCRP
- Proxy observacional da modulação heliosférica e de \(\Phi_{\mathrm{ext}}\).

### Estrutura H-D-M-M
- Hipótese: oscilações de raios cósmicos rastreiam modulação externa relevante para \(\Phi_{\mathrm{eff}}\).
- Dado: séries NMDB multi-estação.
- Modelo: normalização por estação, composição robusta e remoção de offsets.
- Métrica: coerência inter-estação, resposta a eventos extremos, erro de reconstrução temporal.

---

## E) Radiação orbital

### Fontes primárias
- NASA SAA.
- SPENVIS AE9/AP9.
- GOES energetic particles.

### Variáveis-alvo
- Fluxos de prótons e elétrons.
- Dose acumulada e taxa de dose.
- Espectros por energia.
- Eventos SEU (quando públicos).

### Relação com RLL/MCRP
- \(T_M\) como transmissividade geomagnética regional por energia e direção orbital.
- \(\Phi_{\mathrm{eff}}\) comparável a medições de ambiente de radiação em LEO.

### Estrutura H-D-M-M
- Hipótese: variação de transmissividade explica parte da variabilidade de dose/partículas em órbita.
- Dado: GOES + modelos AE9/AP9 + referências SAA.
- Modelo: projeção orbital e integração espectral para fluxo efetivo.
- Métrica: RMS espectral, skill score de eventos, consistência por inclinação orbital.

---

## F) Ionização e química atmosférica

### Fontes primárias
- IntCal20 (\(^{14}C\)).
- Proxies \(^{10}Be\).
- Reanálises atmosféricas (quando disponíveis para janela compatível).

### Variáveis-alvo
- Séries de proxy cosmogênico.
- Indicadores de ionização integrada.
- Campos auxiliares de composição/química (quando acoplados).

### Relação com RLL/MCRP
- Conversão de variações de fluxo em termos de \(Q_{ion}\) e \(X_{chem}\).

### Estrutura H-D-M-M
- Hipótese: mudanças de fluxo externo efetivo deixam assinatura em proxies cosmogênicos.
- Dado: séries paleoclimáticas e reanálises.
- Modelo: mapeamento fluxo→ionização→proxy observável.
- Métrica: ajuste temporal, robustez a incertezas de datação, IC.

---

## G) Cosmologia RLL

### Fontes primárias
- DESI DR2 BAO.
- Pantheon+ SNe Ia.
- Planck 2018 chains.
- H(z) cosmic chronometers.
- fσ8 (crescimento de estrutura).

### Variáveis-alvo
- \(E^2(a)\), \(H(z)\), \(\mu(z)\), \(f\sigma_8(z)\), \(w(z)\).

### Relação com camada cosmológica RLL
- Testar consistência de expansão e crescimento para RLL versus \(\Lambda\)CDM e \(w_0w_a\)CDM.

### Estrutura H-D-M-M
- Hipótese: parametrização RLL oferece ajuste competitivo e fisicamente consistente.
- Dado: BAO + SNe + CMB + H(z) + crescimento.
- Modelo: inferência conjunta com likelihoods consistentes e covariâncias.
- Métrica: \(\chi^2\), AIC, BIC, posterior MCMC, testes de robustez.

---

## Governança de validação observacional
- Estado atual: **Parcial real em preparação**.
- Condição para upgrade de status: execução integral dos pipelines, artefatos versionados e auditoria cruzada.
- Cadeia de custódia obrigatória em `data/real/*/README.md`.
