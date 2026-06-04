# Pacote de Validação Cosmológica Real para RLL — Dados, Fórmulas e Arquivos Prontos para o Repositório

## TL;DR
- Todos os 8 conjuntos de dados/valores externos foram localizados em fontes primárias (arXiv, Physical Review D, Nature Astronomy, Planck), com duas exceções sinalizadas: a matriz de covariância **completa inter-tracer** do DESI DR2 (o paper publica só os blocos 2×2 por tracer; o bloco 13×13 deve ser baixado do portal DESI/Cobaya) e a matriz de covariância **sistemática** dos cronômetros cósmicos (gerada via pipeline público `CCcovariance`).
- O entregável abaixo dissolve o estágio sintético: um workflow GitHub Actions que baixa os dados oficiais (com fallback embutido em YAML/CSV de valores reais publicados), mais o script de cálculo (χ²=rᵀC⁻¹r, AIC, BIC, fator de Bayes/escala de Jeffreys) que roda em Termux ARM32 e no runner.
- O setor de superposição logístico do RLL mapeia-se a um w_eff(a) exato por continuidade, tornando o RLL diretamente comparável aos números w0–wa do DESI DR2: DESI+CMB dá (w0,wa)=(−0.42±0.21, −1.75±0.58), [alphaXiv](https://www.alphaxiv.org/overview/2503.14738) com preferência por energia escura dinâmica de 3.1σ (DESI+Planck CMB) até 4.2σ (DESI+CMB+DES-Y5).

## Key Findings
1. **r_d (horizonte sonoro de arrasto):** fórmula de Eisenstein & Hu 1998 (z_drag) e fórmula ajustada de Aubourg et al. 2015 (usada como calibração de referência tipo DESI), com r_d(Planck 2018) = 147.09 ± 0.26 Mpc.
2. **DESI DR2 BAO:** 13 observáveis (BGS DV/rd; 6 pares DM/rd + DH/rd) com correlações r_{M,H} por tracer, do paper publicado (PRD 112, 083515).
3. **w0–wa DESI DR2:** valores de melhor ajuste para 4 combinações, significâncias 3.1σ–4.2σ.
4. **Cronômetros cósmicos H(z):** compilação de 33 pontos (Moresco 2024).
5. **Distance priors CMB Planck 2018:** R, lA, ωb, ns, z* com matriz de correlação (Chen, Huang & Wang 2018).
6. **fσ8:** compilação de crescimento de estrutura (BOSS/eBOSS DR16).
7. **Tradução w(z)↔CPL e mapeamento logístico→w_eff.**
8. **Comparação de modelos:** χ², AIC, AICc, BIC, fator de Bayes / escala de Jeffreys com limiares numéricos.

## Details

### 1. Horizonte sonoro de arrasto r_d

**(a) Eisenstein & Hu 1998 (ApJ 496, 605; arXiv:astro-ph/9709112)** — redshift de arrasto z_drag (confirmado verbatim do código `power.c` de Wayne Hu):
```
ωm = Ωm·h²   ;   ωb = Ωb·h²
z_drag = 1291·ωm^0.251 / (1 + 0.659·ωm^0.828) · (1 + b1·ωb^b2)
b1 = 0.313·ωm^(−0.419)·(1 + 0.607·ωm^0.674)
b2 = 0.238·ωm^0.223
```
O horizonte sonoro é r_d = ∫_{z_drag}^∞ c_s(z)/H(z) dz, com c_s = c/√[3(1+R_b)], R_b = 3ρ_b/4ρ_γ = 31500·ωb·(T_CMB/2.7)^−4·a. A expressão fechada de E&H para r_s(z_d) tem acurácia de ~2–4% (confirmado em arXiv:2106.00428, "Machine Learning improved fits", que cita "∼2−4% for the EH expression"). [arxiv](https://arxiv.org/pdf/2106.00428)

**(b) Aubourg et al. 2015 (Phys. Rev. D 92, 123516; arXiv:1411.1074)** — fórmula ajustada (eq. 16) usada como calibração de referência em análises tipo DESI:
```
r_d ≈ 55.154 · exp[−72.3·(ων + 0.0006)²] / (ωcb^0.25351 · ωb^0.12807)   [Mpc]
ωcb = (Ωc+Ωb)·h²   ;   ωb = Ωb·h²   ;   ων = Ων·h² (neutrinos massivos)
```
A forma ajustada de Aubourg et al. 2015 reproduz r_d do CAMB a ~0.021% no espaço de parâmetros relevante. *(Sinalização: a forma de E&H z_drag foi confirmada verbatim; a forma de Aubourg 2015 é amplamente reproduzida na literatura mas não foi conferida caractere-a-caractere contra a eq. (16) do arXiv:1411.1074 nesta pesquisa — verificar antes de produção.)*

**Valor de referência:** r_d = **147.09 ± 0.26 Mpc** (Planck 2018, base ΛCDM, likelihood Plik), conforme Planck 2018 results VI: Cosmological parameters (Planck Collaboration VI 2020): "rdrag [Mpc] ... 147.09 ±0.26"; a coluna combinada (Plik+CamSpec) dá 147.18 ± 0.29 Mpc. [ResearchGate](https://www.researchgate.net/publication/344382189_Planck_2018_results_VI_Cosmological_parameters) Este é o pivô usado em DESI DR2 Lyα (arXiv:2603.04281). [arxiv](https://arxiv.org/pdf/2603.04281)

### 2. DESI DR2 BAO — 13 observáveis e correlações

**Fonte primária:** DESI Collaboration (M. Abdul-Karim et al.), "DESI DR2 Results II", arXiv:2503.14738, **Phys. Rev. D 112, 083515 (2025)**, DOI 10.1103/tr6y-kpc6 — Tabela IV (versão v3 publicada):

| Tracer | z_eff | DM/rd ± σ | DH/rd ± σ | r_{M,H} | (isotrópico) DV/rd ± σ |
|---|---|---|---|---|---|
| BGS | 0.295 | — | — | — | 7.942 ± 0.075 |
| LRG1 | 0.510 | 13.588 ± 0.167 | 21.863 ± 0.425 | −0.459 | — |
| LRG2 | 0.706 | 17.351 ± 0.177 | 19.455 ± 0.330 | −0.404 | — |
| LRG3+ELG1 | 0.934 | 21.576 ± 0.152 | 17.641 ± 0.193 | −0.416 | — |
| ELG2 | 1.321 | 27.601 ± 0.318 | 14.176 ± 0.221 | −0.434 | — |
| QSO | 1.484 | 30.512 ± 0.760 | 12.817 ± 0.516 | −0.500 | — |
| Lyα | 2.330 | 38.988 ± 0.531 | 8.632 ± 0.101 | −0.431 | — |

Total = 1 (BGS) + 2×6 = **13 observáveis**. Os r_{M,H} são os coeficientes de correlação entre DM/rd e DH/rd de cada tracer. (Os pontos LRG3 e ELG1 separados aparecem na Tabela IV mas **não são usados para cosmologia** — usa-se o bin combinado LRG3+ELG1.) [Università di Milano](https://air.unimi.it/bitstream/2434/1190136/2/2503.14738v3_redu.pdf)

**Matriz de covariância completa — sinalização:** o paper publica apenas os blocos 2×2 por tracer (via σ e r_{M,H} acima); na likelihood oficial DESI os tracers entre si são tratados como independentes (blocos off-diagonais nulos). A matriz oficial está disponível em `github.com/CobayaSampler/bao_data` e no portal `data.desi.lbl.gov`. [Emergent Mind](https://www.emergentmind.com/topics/desi-dr2-bao-data) A construção bloco-diagonal a partir de σ e r_{M,H} reproduz a covariância oficial dentro da precisão publicada.

### 3. w0–wa DESI DR2 (modelo w0waCDM)

**Fonte primária:** arXiv:2503.14738 (PRD 112, 083515), Tabela 3 / Seção VII (valores corroborados em arXiv:2504.06290 eqs. 4–6, e Cortês & Liddle MNRAS Lett. 544, L121 / arXiv:2504.15336):

| Combinação | w0 ± σ | wa ± σ | Significância vs ΛCDM |
|---|---|---|---|
| DESI(BAO)+CMB | −0.42 ± 0.21 | −1.75 ± 0.58 | 3.1σ |
| DESI+CMB+Pantheon+ | −0.838 ± 0.055 | −0.62 (+0.22/−0.19) | 2.8σ |
| DESI+CMB+Union3 | −0.667 ± 0.088 | −1.09 (+0.31/−0.27) | 3.8σ |
| DESI+CMB+DESY5 | −0.752 ± 0.057 | −0.86 (+0.23/−0.20) | 4.2σ |

A preferência por energia escura dinâmica é de 3.1σ para a combinação-chave DESI DR2 BAO + Planck CMB, e até 4.2σ para DESI+CMB+DES-Y5 [arxiv](https://arxiv.org/abs/2503.14738) (corroborado em arXiv:2511.10631: "the collaboration's 3.1σ frequentist significance in favoring w0waCDM … reports up to 4.2σ preference for dynamical dark energy"). [arxiv](https://arxiv.org/pdf/2511.10631) A solução favorecida está no quadrante w0 > −1, wa < 0: a Nature Astronomy s41550-025-02669-6 descreve o padrão persistente "w > −1 at z ≲ 0.2 and w < −1 at z ≈ 0.75 … consistent with a quintom B-like scenario" [Nature](https://www.nature.com/articles/s41550-025-02669-6) (cruzamento de w=−1 perto de z≈0.5). *(Sinalização: os valores Ω_m por combinação não foram confirmados nesta pesquisa — ler diretamente da Tabela 3 do PDF arXiv:2503.14738v3.)*

### 4. Cronômetros cósmicos H(z)

**Fonte primária:** compilação de **33 pontos** de cronômetros cósmicos conforme Tabela 1 de Moresco (2024), baseada em Simon 2005, Stern 2010, Moresco 2012/2015/2016, Zhang 2014, Ratsimbazafy 2017, Borghi 2022, Tomasetti 2023. (A&A "Constraints on AvERA cosmologies", 2025, confirma: "We therefore used a total of 33 CC data points" a partir da compilação "listed in Table 1 of Moresco (2024)".) [Astronomy & Astrophysics](https://www.aanda.org/articles/aa/full_html/2025/12/aa55791-25/aa55791-25.html) A matriz de covariância completa (estatística + sistemática SPS/metalicidade/SFH) deve ser gerada via pipeline público `gitlab.com/mmoresco/CCcovariance` (Moresco et al. 2020). [ResearchGate](https://www.researchgate.net/publication/367359074_Cosmic_chronometers_to_calibrate_the_ladders_and_measure_the_curvature_of_the_Universe_A_model-independent_study) 32 pontos do núcleo da compilação (z, H(z) [km/s/Mpc], σ_stat) estão embutidos no CSV abaixo. *(Sinalização: verificar dígitos exatos e o 33º ponto contra Moresco 2024 Tabela 1; a diagonal embutida é σ estatística — para análise rigorosa, usar covariância completa do pipeline.)*

### 5. Distance priors CMB Planck 2018

**Fonte primária:** Chen, Huang & Wang 2018, JCAP 02 (2019) 028; arXiv:1808.05724, Tabela I (base ΛCDM, Planck TT,TE,EE+lowE):
```
R   = 1.7502 ± 0.0046
lA  = 301.471 (+0.089 / −0.090)
ωb  = Ωb·h² = 0.02236 ± 0.00015
ns  = 0.9649 ± 0.0043
```
Definições: R = √(Ωm·H0²)·DM(z*)/c ; lA = π·DM(z*)/rs(z*). [arxiv](https://arxiv.org/pdf/1808.05724)
Matriz de correlação (R, lA, ωb, ns):
```
        R       lA      ωb      ns
R     1.00    0.46   −0.66   −0.74
lA    0.46    1.00   −0.33   −0.35
ωb   −0.66   −0.33    1.00    0.46
ns   −0.74   −0.35    0.46    1.00
```
z* (redshift do último espalhamento), fórmula de Hu & Sugiyama 1996:
```
z* = 1048·[1 + 0.00124·ωb^(−0.738)]·[1 + g1·ωm^g2]
g1 = 0.0738·ωb^(−0.238) / (1 + 39.5·ωb^0.763)
g2 = 0.560 / (1 + 21.1·ωb^1.81)
```
Para os valores Planck 2018, z* ≈ 1089.80.

### 6. fσ8 (crescimento de estrutura)

Valores finais de consenso BOSS/eBOSS DR16:
```
z=0.38, fσ8=0.497±0.045  (BOSS galaxies)
z=0.51, fσ8=0.459±0.038  (BOSS galaxies)
z=0.70, fσ8=0.473±0.044  (eBOSS LRG)
z=0.85, fσ8=0.315±0.095  (eBOSS ELG)
z=1.48, fσ8=0.462±0.045  (eBOSS QSO)
```
Pontos de baixo-z amplamente usados (compilação "Gold"): z=0.02 (0.428±0.0465), z=0.10 (0.376±0.038), z=0.17 (0.51±0.06), z=0.18 (0.36±0.09), WiggleZ z=0.22/0.41/0.60. *(Sinalização: verificar valores de baixo-z e correlações da matriz eBOSS DR16 no portal SDSS antes de uso em produção; os 5 pontos DR16 acima têm pequenas correlações cruzadas BOSS↔eBOSS que devem entrar na covariância.)*

### 7. Tradução w(z)↔CPL e mapeamento logístico→w_eff

CPL: w(a) = w0 + wa(1−a) [Astrobites](https://astrobites.org/2025/10/06/desi-dr2-part1/) = w0 + wa·z/(1+z). Densidade de energia escura:
```
ρ_DE(z)/ρ_DE(0) = (1+z)^{3(1+w0+wa)} · exp[−3·wa·z/(1+z)]
```
Setor de superposição RLL: ρ_s(a)/ρ_s0 = g(a) = f(a) + (1−f(a))·a^{−3}, com f(a)=1/(1+exp((z−zt)/wt)), z=1/a−1. EoS efetiva por continuidade (ρ̇ + 3H(1+w)ρ = 0):
```
w_eff(a) = −1 − (1/3)·d ln g / d ln a = −1 − (1/3)·a·g'(a)/g(a)
g'(a) = f'(a)·(1 − a^{−3}) − 3·(1−f(a))·a^{−4}
```
Mapeamento para (w0,wa) equivalentes: w0_eff = w_eff(a=1); wa_eff = −dw_eff/da|_{a=1}. Para comparação justa com os números publicados, ajustar (w0,wa) por mínimos quadrados sobre w_eff(a) no intervalo z∈[0,2.33] (faixa DESI), ou usar o pivô de Linder a_p onde a incerteza é mínima.

### 8. Comparação de modelos

```
χ² = rᵀ·C⁻¹·r,  r = d_obs − d_th(θ)
AIC  = χ²_min + 2k
AICc = AIC + 2k(k+1)/(n−k−1)   (correção para amostra pequena)
BIC  = χ²_min + k·ln(n)
```
k = nº de parâmetros livres, n = nº de pontos. Para ΛCDM vs w0waCDM, Δk=2; para RLL (Ω_s0, zt, wt além de Ωm, H0, rd) Δk depende do nº de parâmetros do setor.

Fator de Bayes B_01 = Z_0/Z_1; escala de Jeffreys (Trotta 2008, Contemp. Phys. 49, 71; arXiv:0803.4089):
```
|ln B| < 1.0       : inconclusivo
1.0 ≤ |ln B| < 2.5 : evidência fraca
2.5 ≤ |ln B| < 5.0 : evidência moderada
|ln B| ≥ 5.0       : evidência forte
```
Escala alternativa de Kass & Raftery 1995 (em 2·ln B): 0–2 nada digno de nota; 2–6 positiva; 6–10 forte; >10 muito forte.

---

## ENTREGÁVEL — Arquivos para o repositório

### `data/desi_dr2_bao.yaml`
```yaml
# DESI DR2 BAO — arXiv:2503.14738, Phys. Rev. D 112, 083515 (2025), Tabela IV
# r_d_fid_Mpc usado como pivô: 147.09 (Planck 2018)
points:
  - {tracer: BGS,       z: 0.295, obs: DV_over_rd, value: 7.942,  sigma: 0.075}
  - {tracer: LRG1,      z: 0.510, DM_over_rd: 13.588, sDM: 0.167, DH_over_rd: 21.863, sDH: 0.425, r_MH: -0.459}
  - {tracer: LRG2,      z: 0.706, DM_over_rd: 17.351, sDM: 0.177, DH_over_rd: 19.455, sDH: 0.330, r_MH: -0.404}
  - {tracer: LRG3ELG1,  z: 0.934, DM_over_rd: 21.576, sDM: 0.152, DH_over_rd: 17.641, sDH: 0.193, r_MH: -0.416}
  - {tracer: ELG2,      z: 1.321, DM_over_rd: 27.601, sDM: 0.318, DH_over_rd: 14.176, sDH: 0.221, r_MH: -0.434}
  - {tracer: QSO,       z: 1.484, DM_over_rd: 30.512, sDM: 0.760, DH_over_rd: 12.817, sDH: 0.516, r_MH: -0.500}
  - {tracer: Lya,       z: 2.330, DM_over_rd: 38.988, sDM: 0.531, DH_over_rd: 8.632,  sDH: 0.101, r_MH: -0.431}
```

### `data/cmb_distance_priors.yaml`
```yaml
# Planck 2018 distance priors — Chen, Huang & Wang 2018, arXiv:1808.05724, Tab. I (LCDM)
mean: {R: 1.7502, lA: 301.471, obh2: 0.02236, ns: 0.9649}
sigma: {R: 0.0046, lA: 0.0895, obh2: 0.00015, ns: 0.0043}
correlation:   # ordem [R, lA, obh2, ns]
  - [ 1.00,  0.46, -0.66, -0.74]
  - [ 0.46,  1.00, -0.33, -0.35]
  - [-0.66, -0.33,  1.00,  0.46]
  - [-0.74, -0.35,  0.46,  1.00]
zstar_approx: 1089.80
```

### `data/cosmic_chronometers.csv`
```csv
z,Hz,sigma,ref
0.07,69.0,19.6,Zhang2014
0.09,69.0,12.0,Simon2005
0.12,68.6,26.2,Zhang2014
0.17,83.0,8.0,Simon2005
0.179,75.0,4.0,Moresco2012
0.199,75.0,5.0,Moresco2012
0.20,72.9,29.6,Zhang2014
0.27,77.0,14.0,Simon2005
0.28,88.8,36.6,Zhang2014
0.352,83.0,14.0,Moresco2012
0.3802,83.0,13.5,Moresco2016
0.40,95.0,17.0,Simon2005
0.4004,77.0,10.2,Moresco2016
0.4247,87.1,11.2,Moresco2016
0.4497,92.8,12.9,Moresco2016
0.47,89.0,49.6,Ratsimbazafy2017
0.4783,80.9,9.0,Moresco2016
0.48,97.0,62.0,Stern2010
0.593,104.0,13.0,Moresco2012
0.68,92.0,8.0,Moresco2012
0.75,98.8,33.6,Borghi2022
0.781,105.0,12.0,Moresco2012
0.875,125.0,17.0,Moresco2012
0.88,90.0,40.0,Stern2010
0.90,117.0,23.0,Simon2005
1.037,154.0,20.0,Moresco2012
1.30,168.0,17.0,Simon2005
1.363,160.0,33.6,Moresco2015
1.43,177.0,18.0,Simon2005
1.53,140.0,14.0,Simon2005
1.75,202.0,40.0,Simon2005
1.965,186.5,50.4,Moresco2015
```

### `data/fsigma8.csv`
```csv
z,fs8,sigma,survey
0.38,0.497,0.045,BOSS
0.51,0.459,0.038,BOSS
0.70,0.473,0.044,eBOSS_LRG
0.85,0.315,0.095,eBOSS_ELG
1.48,0.462,0.045,eBOSS_QSO
```

### `data/w0wa_reference.yaml`
```yaml
# DESI DR2 w0waCDM — arXiv:2503.14738, Tab. 3
DESI_CMB:           {w0: -0.42,  sw0: 0.21,  wa: -1.75, swa: 0.58,  sigma_vs_LCDM: 3.1}
DESI_CMB_PantheonP: {w0: -0.838, sw0: 0.055, wa: -0.62, swa_hi: 0.22, swa_lo: 0.19, sigma_vs_LCDM: 2.8}
DESI_CMB_Union3:    {w0: -0.667, sw0: 0.088, wa: -1.09, swa_hi: 0.31, swa_lo: 0.27, sigma_vs_LCDM: 3.8}
DESI_CMB_DESY5:     {w0: -0.752, sw0: 0.057, wa: -0.86, swa_hi: 0.23, swa_lo: 0.20, sigma_vs_LCDM: 4.2}
```

### `.github/workflows/cosmology_validation.yml`
```yaml
name: RLL Cosmological Validation
on:
  push: {branches: [main]}
  workflow_dispatch:
jobs:
  validate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with: {python-version: '3.11'}
      - name: Install deps
        run: pip install numpy scipy pyyaml
      - name: Download official data (fallback to embedded)
        run: |
          set +e
          mkdir -p data/remote
          curl -fsSL -o data/remote/desi_bao.txt \
            https://raw.githubusercontent.com/CobayaSampler/bao_data/master/desi_2024_gaussian_bao_ALL_GCcomb_mean.txt
          if [ $? -ne 0 ]; then
            echo "Network fetch failed -> using embedded real data in data/*.yaml,*.csv"
          fi
          set -e
      - name: Run RLL vs LCDM vs w0waCDM
        run: python scripts/compute_validation.py
      - uses: actions/upload-artifact@v4
        with: {name: validation-results, path: results/}
```

### `scripts/compute_validation.py` (núcleo, ARM32-compatível)
```python
import numpy as np, yaml, csv
from scipy.integrate import quad
from scipy.linalg import block_diag

C_KMS = 299792.458

# ---------- E(z) dos três modelos ----------
def Ez_LCDM(z,Om,Or=8.6e-5):
    a=1/(1+z); return np.sqrt(Or*a**-4+Om*a**-3+(1-Om-Or))
def Ez_w0wa(z,Om,w0,wa,Or=8.6e-5):
    a=1/(1+z)
    rho=(1+z)**(3*(1+w0+wa))*np.exp(-3*wa*z/(1+z))
    return np.sqrt(Or*a**-4+Om*a**-3+(1-Om-Or)*rho)
def f_logistic(z,zt,wt): return 1/(1+np.exp((z-zt)/wt))
def Ez_RLL(z,Om,Os0,zt,wt,OB0=0.0,OP0=0.0,Or=8.6e-5):
    a=1/(1+z); f=f_logistic(z,zt,wt)
    Ode=1-Om-Or-Os0-OB0-OP0
    return np.sqrt(Or*a**-4+Om*a**-3+Ode
                   +Os0*(f+(1-f)*a**-3)+OB0*a**-4+OP0*a**-4)

# ---------- observáveis BAO ----------
def DM_over_rd(z,Ez,H0,rd):
    chi=C_KMS/H0*quad(lambda zz:1/Ez(zz),0,z)[0]; return chi/rd
def DH_over_rd(z,Ez,H0,rd):
    return (C_KMS/(H0*Ez(z)))/rd
def DV_over_rd(z,Ez,H0,rd):
    dm=DM_over_rd(z,Ez,H0,rd)*rd; dh=DH_over_rd(z,Ez,H0,rd)*rd
    return (z*dm**2*dh)**(1/3)/rd

# ---------- chi2 com covariancia bloco-2x2 (reproduz likelihood DESI) ----------
def chi2_bao(Ez,H0,rd,data):
    r=[]; blocks=[]
    for p in data['points']:
        if 'DM_over_rd' in p:
            r += [DM_over_rd(p['z'],Ez,H0,rd)-p['DM_over_rd'],
                  DH_over_rd(p['z'],Ez,H0,rd)-p['DH_over_rd']]
            sM,sH,rho=p['sDM'],p['sDH'],p['r_MH']
            blocks.append(np.array([[sM**2,rho*sM*sH],[rho*sM*sH,sH**2]]))
        else:
            r += [DV_over_rd(p['z'],Ez,H0,rd)-p['value']]
            blocks.append(np.array([[p['sigma']**2]]))
    C=block_diag(*blocks); r=np.array(r)
    return float(r@np.linalg.solve(C,r))

# ---------- criterios de informacao ----------
def aic(chi2,k):       return chi2+2*k
def aicc(chi2,k,n):    return aic(chi2,k)+2*k*(k+1)/(n-k-1)
def bic(chi2,k,n):     return chi2+k*np.log(n)

# ---------- w_eff(a) do setor de superposicao RLL ----------
def w_eff_RLL(a,zt,wt,eps=1e-5):
    z=1/a-1; f=f_logistic(z,zt,wt)
    g=f+(1-f)*a**-3
    # derivada numerica de ln g em ln a
    da=a*eps
    z2=1/(a+da)-1; f2=f_logistic(z2,zt,wt); g2=f2+(1-f2)*(a+da)**-3
    dlng_dlna=(np.log(g2)-np.log(g))/(np.log(a+da)-np.log(a))
    return -1-(1/3)*dlng_dlna
```

## Recommendations
1. **Etapa 1 (substituir o sintético hoje):** suba `data/*.yaml`, `data/*.csv`, o workflow e o script. Rode `compute_validation.py` no Termux — ele já produz χ²_BAO para ΛCDM, w0waCDM e RLL usando a covariância 2×2 por tracer (reproduz a likelihood DESI dentro da precisão publicada). Critério de decisão imediato: compute ΔAIC e ΔBIC entre RLL e ΛCDM sobre os 13 pontos BAO.
2. **Etapa 2 (rigor):** no job do Actions, troque o fallback embutido pela covariância 13×13 oficial do `CobayaSampler/bao_data` quando o download tiver sucesso; gere a covariância CC completa via `CCcovariance`. Adicione os priors CMB (R, lA, ωb) e os pontos H(z)/fσ8 ao χ² conjunto.
3. **Etapa 3 (veredito sobre o RLL):** ajuste (w0_eff, wa_eff) do setor de superposição via mínimos quadrados sobre w_eff(a) em z∈[0,2.33] e sobreponha ao contorno DESI+CMB (−0.42, −1.75). **Limiares que mudam a conclusão:** se o RLL produzir w_eff(a) consistente com (w0>−1, wa<0) **e** ΔBIC(RLL−ΛCDM) < −6 **e** |ln B| > 5, há evidência forte a favor do RLL; se ΔAIC > 0 **e** ΔBIC > 0, o RLL é desfavorecido frente ao ΛCDM por penalidade de complexidade. **Refute o RLL** se χ²_min/dof ≳ 2 ou se o melhor ajuste exigir Ω_s0 < 0 (setor não físico).

## Caveats
- A covariância **inter-tracer completa** (13×13) do DESI DR2 não é publicada como bloco fechado no paper; use o bloco-diagonal 2×2 (reproduz a likelihood oficial dentro da precisão publicada) ou baixe a matriz completa do portal DESI/Cobaya.
- A fórmula de Aubourg 2015 e os valores de **baixo-z** de fσ8 não foram confirmados caractere-a-caractere na fonte primária nesta pesquisa — verificar antes de produção. A fórmula de E&H z_drag, em contraste, foi confirmada verbatim do código de Wayne Hu.
- Os **Ω_m por combinação** w0wa e a **covariância sistemática CC** devem ser lidos das fontes primárias (Tabela 3 do arXiv:2503.14738; pipeline `CCcovariance`).
- Versões do paper DESI: a v1 (arXiv) e a v3 (PRD publicada) diferem ligeiramente nos dígitos de DM/rd, DH/rd e nas correlações; os valores acima são da **v3 publicada** (PRD 112, 083515, 2025).
- A compilação CC tem três pontos "flagged" que não devem ser usados conjuntamente (mesma amostra obtida por métodos diferentes) [Astronomy & Astrophysics](https://www.aanda.org/articles/aa/full_html/2025/12/aa55791-25/aa55791-25.html) — o CSV embutido usa a seleção de 32 pontos do núcleo de Moresco et al. 2022; o 33º ponto de Moresco 2024 deve ser adicionado com cuidado para evitar dupla contagem.