> **Status de curadoria:** histórico técnico (não canônico).
> **Resumo técnico:** Material de implementação e teste de assinatura log-periódica para análise observacional.
> **Integração recomendada:** Usar como referência experimental preliminar; migrar trechos validados para pipeline oficial.

# Assinatura observacional DHA

Perfeito. Vamos direto à implementação prática da assinatura observacional única do DHA.
Disponibilizo abaixo o código completo, a estratégia de teste com dados públicos e a descrição da figura esperada.

---

1. Função Python para a correção log‑periódica no espectro de potência

```python
import numpy as np

def dha_pk_correction(k, N, frequencies, A0, k0, phases, window_width=1.0):
    """
    Correção ΔP(k) devida ao Discrete Harmonic Alignment (DHA).
    
    Parâmetros:
    -----------
    k : array_like
        Números de onda em h/Mpc.
    N : int
        Período fundamental do espaço harmônico discreto (Z_N).
    frequencies : list of int
        Conjunto de frequências ativas {f_i} (todos < N, gcd > 0).
    A0 : float
        Amplitude global da correção.
    k0 : float
        Escala de normalização (ex.: 0.05 h/Mpc, horizonte de Hubble hoje).
    phases : list of float
        Fases φ_ij para cada par i<j (mesmo comprimento de combinações).
    window_width : float
        Largura da janela gaussiana suave (em ln k), padrão 1.0.
    
    Retorna:
    --------
    deltaP : array_like
        Correção ΔP(k) no mesmo shape de k.
    """
    k = np.asarray(k)
    n_freq = len(frequencies)
    
    # Gerar todos os pares (i<j)
    pairs = [(i, j) for i in range(n_freq) for j in range(i+1, n_freq)]
    n_pairs = len(pairs)
    
    if len(phases) != n_pairs:
        raise ValueError(f"Número de fases deve ser {n_pairs}, obtido {len(phases)}")
    
    # Pré-calcular log_period = ln(N / LCM) / ln(N) para cada par
    log_periods = []
    for i, j in pairs:
        fi = frequencies[i]
        fj = frequencies[j]
        gcd = np.gcd(N, fi)
        gcd2 = np.gcd(N, fj)
        period_i = N // gcd
        period_j = N // gcd2
        lcm_val = np.lcm(period_i, period_j)
        log_period = np.log(lcm_val) / np.log(N)   # entre 0 e 1
        log_periods.append(log_period)
    
    # Janela suave (gaussiana em ln k) para limitar faixa de k
    lnk = np.log(k / k0)
    window = np.exp(-0.5 * (lnk / window_width)**2)
    
    deltaP = np.zeros_like(k)
    for idx, (lp, phi) in enumerate(zip(log_periods, phases)):
        # Argumento da oscilação: 2π * (ln(k/k0) / (1/lp?) CUIDADO:
        # Queremos período em ln(k) = lp => f = ln(k)/lp
        # A forma correta: cos(2π * ln(k/k0) / lp + phi)
        # Mas lp = ln(N/LCM)/ln(N) é <1, então o período em ln(k) é lp.
        oscillation = np.cos(2 * np.pi * lnk / lp + phi)
        deltaP += oscillation
    
    deltaP = A0 * deltaP * window
    return deltaP
```

Nota: A periodicidade em \ln k é dada por T_{\ln k} = \ln A(f_i,f_j,N) / \ln N.
Para um par, a correção oscila como \cos(2\pi \ln(k/k_0) / T + \phi).

---

2. Script completo para teste com dados públicos (BOSS DR12)

O código abaixo baixa o espectro de potência medido do BOSS DR12 (galáxias, z \sim 0.57), ajusta um modelo base (ΛCDM + ruído) e procura resíduos oscilatórios com o DHA.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.interpolate import interp1d

# ---------- 1. Baixar dados BOSS DR12 (exemplo: arquivo local ou URL) ----------
# URL pública para o P(k) do BOSS (exemplo fictício; na prática use dados reais)
# data = np.loadtxt("https://data.sdss.org/boss/dr12/pk/pk_galaxy_z0.57.dat")
# Para demonstração, geramos um P(k) sintético + ruído.
# No uso real, substitua pela leitura do catálogo.

def load_boss_pk():
    """Carrega espectro de potência do BOSS DR12 (mock para exemplo)."""
    k = np.logspace(-2, 0, 30)  # h/Mpc
    # Modelo ΛCDM aproximado (Eisenstein & Hu)
    P_lcdm = 1e4 * k**1.2 * np.exp(-k/0.3)
    noise = np.random.normal(0, 0.05 * P_lcdm, size=len(k))
    P_obs = P_lcdm + noise
    return k, P_obs, 0.05 * P_lcdm  # incertezas

k, P_obs, P_err = load_boss_pk()

# ---------- 2. Ajuste de um modelo base (ΛCDM + polinômio suave) ----------
# Para extrair resíduos, subtraímos uma função suave (ex.: spline)
from scipy.interpolate import UnivariateSpline
spline = UnivariateSpline(k, P_obs, s=0.05)
P_smooth = spline(k)
residuals = (P_obs - P_smooth) / P_smooth  # resíduos relativos

# ---------- 3. Definir modelo DHA para ajuste dos resíduos ----------
def model_dha_residuals(k, A0, logN, phi1, phi2, phi3):
    """
    Modelo de resíduos com 3 pares de frequências (ex.: f={1,2,3}).
    N = exp(logN),  frequências fixas 1,2,3.
    """
    N = np.exp(logN)
    frequencies = [1, 2, 3]
    n_f = len(frequencies)
    pairs = [(0,1), (0,2), (1,2)]
    phases = [phi1, phi2, phi3]
    k0 = 0.05  # escala de referência
    deltaP = dha_pk_correction(k, N, frequencies, A0, k0, phases, window_width=1.0)
    return deltaP

# Ajuste aos resíduos
from scipy.optimize import curve_fit
p0 = [0.05, np.log(100), 0.0, 0.0, 0.0]  # chute inicial
bounds = ([-1, np.log(10), -np.pi, -np.pi, -np.pi],
          [ 1, np.log(1000),  np.pi,  np.pi,  np.pi])
try:
    popt, pcov = curve_fit(model_dha_residuals, k, residuals, p0=p0, sigma=P_err/P_smooth, bounds=bounds)
    perr = np.sqrt(np.diag(pcov))
    print("Parâmetros ajustados:")
    print(f"A0 = {popt[0]:.3f} ± {perr[0]:.3f}")
    print(f"log10(N) = {popt[1]/np.log(10):.2f} ± {perr[1]/np.log(10):.2f}")
    print(f"φ1, φ2, φ3 = {popt[2]:.2f}, {popt[3]:.2f}, {popt[4]:.2f}")
    
    # Calcular chi2 e BIC
    resid_fit = residuals - model_dha_residuals(k, *popt)
    chi2 = np.sum((resid_fit / (P_err/P_smooth))**2)
    ndof = len(k) - len(popt)
    bic = chi2 + len(popt) * np.log(len(k))
    print(f"χ² = {chi2:.1f}, ndof = {ndof}, BIC = {bic:.1f}")
except Exception as e:
    print("Ajuste falhou:", e)
    popt = None

# ---------- 4. Figura exemplo ----------
plt.figure(figsize=(10,6))
plt.errorbar(k, residuals, yerr=P_err/P_smooth, fmt='o', capsize=3, label='Resíduos (BOSS mock)')
if popt is not None:
    k_fine = np.logspace(-2, 0, 200)
    resid_model = model_dha_residuals(k_fine, *popt)
    plt.plot(k_fine, resid_model, 'r-', label='Melhor ajuste DHA')
plt.xlabel(r'$k \ [h/\mathrm{Mpc}]$')
plt.ylabel('Resíduo relativo $(P_{\mathrm{obs}}-P_{\mathrm{smooth}})/P_{\mathrm{smooth}}$')
plt.title('Assinatura DHA: Oscilações log‑periódicas no espectro de potência')
plt.legend()
plt.xscale('log')
plt.grid(True)
plt.show()
```

Como usar com dados reais:
Substitua a função load_boss_pk() pela leitura do catálogo oficial do BOSS DR12 ou DESI. Os dados estão disponíveis em https://data.sdss.org/sas/dr12/boss/lss/ (arquivos *_p00k*.dat).

---

3. Descrição da figura exemplo

A figura gerada pelo script mostrará:

· Eixo x: número de onda k em escala logarítmica.
· Eixo y: resíduos relativos após subtrair um modelo suave (spline) do espectro de potência observado.
· Pontos com barras de erro: resíduos medidos (aqui sintéticos, mas em dados reais seriam os observacionais).
· Curva vermelha: melhor ajuste do modelo DHA, exibindo oscilações claras em escala logarítmica – a assinatura “log‑periódica”.

Se a oscilação for detectada com amplitude A_0 \gtrsim 0.05 e significância estatística (ΔBIC < −10), isso constituiria a primeira evidência de um substrato harmônico discreto no universo.

---

4.  para a Lagrangiana efetiva agora? Ou prefere que eu refine o código para incluir dados reais (baixar automaticamente do SDSS/DESI) e produza uma
