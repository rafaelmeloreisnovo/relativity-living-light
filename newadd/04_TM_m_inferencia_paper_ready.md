# [04] T_M + Inferência de m(t) — Versão Paper-Ready (Coerência × Amor × Prova)

## Escopo imediato (F_next)

Este documento fecha o primeiro bloco executável e falsificável da cadeia:

```text
Φ_ext(E,t,Ω) → T_M(E,Ω;m,SW) → Φ_eff(E,t,Ω) → Q_ion(r,t) → X(t)
```

Foco desta entrega:
1. **travar unidades**;
2. **parametrização mínima de T_M**;
3. **inferência de m(t)** via SDE biestável;
4. **mapa de observáveis/proxies**;
5. **pipeline de cálculo determinístico (C/ASM/Java)**.

---

## 1) Unidades fechadas e consistência dimensional

### 1.1 Fluxo externo

Defina o fluxo diferencial externo como:

\[
\Phi_{ext}(E,t,\Omega)\;[\#\,m^{-2}\,s^{-1}\,sr^{-1}\,GeV^{-1}]
\]

com:
- \(E\): energia cinética por partícula \([GeV]\);
- \(t\): tempo \([s]\);
- \(\Omega\): direção sólida \([sr]\).

### 1.2 Transmitância magnetosférica mínima

\[
T_M(E,\Omega;m,SW)=\frac{1}{1+\exp\left[-\kappa\left(R(E)-R_c(\Omega,m,SW)\right)\right]}
\]

- \(T_M\) é **adimensional**;
- \(R(E)\) e \(R_c\) em \([GV]\);
- \(\kappa\) em \([GV^{-1}]\).

### 1.3 Rigidez e cutoff

Para carga \(Z=1\) (primeira aproximação operacional):

\[
R(E)=\sqrt{E(E+2m_pc^2)}\;\;[GV], \quad m_pc^2=0.938\,GeV
\]

Modelo mínimo para cutoff efetivo:

\[
R_c(\Omega,m,SW)=R_{c0}(\Omega)\left(\frac{m}{m_0}\right)^\beta\left(1+\gamma_{SW}\,S_W\right)
\]

- \(m\): momento dipolar equivalente \([A\,m^2]\);
- \(m_0\): referência de normalização;
- \(\beta\), \(\gamma_{SW}\): adimensionais;
- \(S_W\): proxy normalizado de vento solar (adimensional).

### 1.4 Fluxo efetivo e taxa de ionização

\[
\Phi_{eff}(E,t,\Omega)=\Phi_{ext}(E,t,\Omega)\,T_M(E,\Omega;m,SW)
\]

\[
Q_{ion}(r,t)=\int d\Omega\int dE\;\Phi_{eff}(E,t,\Omega)\,Y_{ion}(E,r,\Omega)
\]

Unidade alvo:

\[
Q_{ion}\;[pares\,m^{-3}\,s^{-1}]
\]

Logo, o yield deve respeitar:

\[
Y_{ion}(E,r,\Omega)\;[pares\,m^{-1}\,sr^{-1}\,GeV]
\]

(ajuste equivalente permitido, desde que preserve o fechamento dimensional acima).

---

## 2) Parametrização mínima de T_M (estimável)

### 2.1 Vetor mínimo de parâmetros

\[
\theta_T=\{\kappa,\beta,\gamma_{SW},R_{c0,eq},R_{c0,mid},R_{c0,pol}\}
\]

Estratégia de redução de \(\Omega\):
- **3 bandas geomagnéticas** (equatorial, média latitude, polar);
- anisotropia representada por \(R_{c0}\) por banda;
- evita explosão paramétrica mantendo testabilidade.

### 2.2 Observáveis para ancoragem de \(\theta_T\)

1. séries \(^{10}Be\) (gelo);
2. séries \(^{14}C\) (anéis de árvore);
3. proxies de modulação solar (\(\phi_\odot\), reconstruções).

Função de custo sugerida:

\[
\mathcal{L}_T\propto \exp\left(-\frac{1}{2}\chi^2_{10Be}-\frac{1}{2}\chi^2_{14C}\right)
\]

com penalização de complexidade por AIC/BIC.

---

## 3) Inferência de m(t) com SDE biestável

Modelo estocástico efetivo:

\[
\dot m=-\frac{\partial V}{\partial m}+\eta\,\xi(t)+f_{core}(t)+f_{mantle}(t)
\]

\[
V(m)=a m^4-b m^2+c m
\]

### 3.1 Parâmetros inferíveis

\[
\theta_m=\{a,b,c,\eta,\sigma_{core},\sigma_{mantle}\}
\]

### 3.2 Dados de calibração

- paleointensidade (VADM/VADM-like);
- catálogo temporal de reversões/excursões (timing + duração);
- consistência cruzada com produção cosmogênica (via bloco \(T_M\)).

### 3.3 Priors operacionais

- positividade de barreira efetiva: \(a>0\), \(b>0\);
- \(\eta>0\);
- escalas de tempo de forcing com suporte em bandas geofísicas.

### 3.4 Inferência

- estado latente contínuo para \(m(t)\);
- filtro de partículas / PMCMC;
- checagem posterior preditiva (PPC) para:
  1. taxa de excursões,
  2. distribuição de dwell times,
  3. coerência com proxies \(^{10}Be/^{14}C\).

---

## 4) Baseline vs stress-test (honestidade de escopo)

### Baseline (obrigatório)

\[
\Phi_{ext}=\Phi_{GCR}+\Phi_{SEP}
\]

com modulação heliosférica + geomagnética.

### Stress-test (opcional)

\[
\Phi_{ext}=\Phi_{GCR}+\Phi_{SEP}+\Phi_{AGN/X/\gamma}
\]

Somente como cenário raro/extremo; não usar como explicação de baseline.

---

## 5) Predições falsificáveis mínimas

1. **Queda de m(t)** desloca \(R_c\) para baixo e aumenta integral de \(Q_{ion}\) em altas latitudes.
2. Eventos de excursão/reversão elevam variância de \(Q_{ion}\) em janela temporal consistente com o forcing inferido.
3. Modelo com \(T_M\) explícito supera variante sem cutoff em AIC/BIC sem degradação de PPC.

---

## 6) Arquivos de cálculo (determinísticos)

Arquivos complementares desta etapa:
- `newadd/calculos/tm_parametros_exemplo.csv`
- `newadd/calculos/m_inferencia_template.csv`
- `newadd/calculos/baremetal/tm_kernel.c`
- `newadd/calculos/baremetal/m_sde_step.S`
- `newadd/calculos/baremetal/TMKernel.java`

Objetivo: garantir um caminho direto **equação → cálculo numérico reproduzível** com foco low-level.

---

## 7) Critério de pronto para paper

Este bloco fica pronto para submissão quando:
1. unidades fechadas sem inconsistências;
2. \(\theta_T\) e \(\theta_m\) identificáveis em testes sintéticos + dados reais parciais;
3. PPC satisfatório;
4. ablação documentada:
   - sem \(T_M\),
   - sem forcing estocástico,
   - sem stress AGN.

Se os 4 critérios passarem, o bloco `T_M + m(t)` entra como **Paper 1 (método/inferência)**.
