"""
panteon_likelihood.py
Relativity Living Light — Template de Likelihood para Pantheon+

Template para rodar MCMC com dados reais Pantheon+ (1701 SNe Ia).
Os dados reais devem ser baixados de:
    https://github.com/PantheonPlusSH0ES/DataRelease

Uso:
    1. Baixar lcparam_full_long_zhel.txt e sys_full_long.txt de Pantheon+
    2. Colocar em data/pantheon/
    3. python panteon_likelihood.py
"""

import numpy as np
from scipy.integrate import quad
from scipy.linalg import solve
import os


# ─── Constantes ───────────────────────────────────────────────────────────────
C_KMS = 299792.458   # velocidade da luz km/s
H0    = 70.0         # H₀ fiducial km/s/Mpc


# ─── Modelo RLL ───────────────────────────────────────────────────────────────

def E2_RLL(z, Om0, OL, Os0, zt, wt):
    """H²(z)/H₀² normalizado."""
    f = 1.0 / (1.0 + np.exp((z - zt) / wt))
    return (Om0 * (1+z)**3
            + OL
            + Os0 * (f + (1.0 - f) * (1+z)**3))


def comoving_distance(z, Om0, OL, Os0, zt, wt):
    """Distância comóvel D_C(z) em Mpc (com H₀ = 70 km/s/Mpc fiducial)."""
    integrand = lambda zp: 1.0 / np.sqrt(E2_RLL(zp, Om0, OL, Os0, zt, wt))
    dc, _ = quad(integrand, 0, z, limit=100)
    return (C_KMS / H0) * dc


def luminosity_distance(z, Om0, OL, Os0, zt, wt):
    """Distância de luminosidade D_L(z) em Mpc."""
    dc = comoving_distance(z, Om0, OL, Os0, zt, wt)
    return (1.0 + z) * dc


def mu_model(z_vals, Om0, OL, Os0, zt, wt, M_abs=-19.3):
    """
    Módulo de distância μ(z) = 5 log10(D_L / 10pc) + M_abs.
    M_abs: magnitude absoluta da SN Ia (marginalizado ou fixado).
    """
    mu = np.array([
        5.0 * np.log10(luminosity_distance(z, Om0, OL, Os0, zt, wt) * 1e6 / 10.0)
        for z in z_vals
    ])
    return mu + M_abs


# ─── Carregamento de dados Pantheon+ ─────────────────────────────────────────

def load_pantheon(data_dir='data/pantheon'):
    """
    Carrega dados Pantheon+.
    
    Retorna
    -------
    z_hel : array de redshifts heliocêntricos
    mu_obs : array de módulos de distância observados
    C_inv  : matriz de covariância inversa
    """
    lc_file  = os.path.join(data_dir, 'lcparam_full_long_zhel.txt')
    sys_file = os.path.join(data_dir, 'sys_full_long.txt')
    
    if not os.path.exists(lc_file):
        raise FileNotFoundError(
            f"Arquivo não encontrado: {lc_file}\n"
            "Baixe os dados Pantheon+ de:\n"
            "https://github.com/PantheonPlusSH0ES/DataRelease"
        )
    
    # Carregar parâmetros das supernovas
    data = np.genfromtxt(lc_file, names=True, skip_header=0)
    z_hel  = data['zcmb']    # ou 'zhel' dependendo da versão
    mu_obs = data['mb']      # módulo de distância observado
    mu_err = data['dmb']     # erro estatístico
    
    N = len(z_hel)
    
    # Matriz de covariância estatística
    C_stat = np.diag(mu_err**2)
    
    # Matriz sistemática (se disponível)
    if os.path.exists(sys_file):
        C_sys = np.loadtxt(sys_file).reshape(N, N)
        C_total = C_stat + C_sys
    else:
        C_total = C_stat
        print("⚠️  Matriz sistemática não encontrada, usando apenas covariância estatística.")
    
    C_inv = np.linalg.inv(C_total)
    
    return z_hel, mu_obs, C_inv


# ─── Likelihood ───────────────────────────────────────────────────────────────

def chi2_pantheon(theta, z_hel, mu_obs, C_inv):
    """
    χ² para Pantheon+ dado vetor de parâmetros theta.
    theta = [Om0, log10(1-OL_extra), Os0, zt, wt, M_abs]
    """
    Om0, Os0, zt, wt, M_abs = theta
    OL = 1.0 - Om0 - Os0  # flat Universe
    
    # Sanity checks
    if Om0 <= 0 or OL < 0 or Os0 < 0 or wt <= 0:
        return 1e10
    if zt < 0.1 or zt > 3.0:
        return 1e10
    
    try:
        mu_th = mu_model(z_hel, Om0, OL, Os0, zt, wt, M_abs=M_abs)
    except Exception:
        return 1e10
    
    delta = mu_obs - mu_th
    chi2  = float(delta @ C_inv @ delta)
    return chi2


def log_likelihood(theta, z_hel, mu_obs, C_inv):
    """Log-likelihood = −χ²/2."""
    return -0.5 * chi2_pantheon(theta, z_hel, mu_obs, C_inv)


# ─── Priors ───────────────────────────────────────────────────────────────────

def log_prior(theta):
    """
    Prior flat nos parâmetros.
    theta = [Om0, Os0, zt, wt, M_abs]
    """
    Om0, Os0, zt, wt, M_abs = theta
    
    if (0.1 < Om0 < 0.6  and
        0.0 < Os0 < 0.20 and
        0.2 < zt  < 2.5  and
        0.05 < wt < 1.0  and
        -20.0 < M_abs < -18.0):
        return 0.0
    return -np.inf


def log_posterior(theta, z_hel, mu_obs, C_inv):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, z_hel, mu_obs, C_inv)


# ─── MCMC com emcee ───────────────────────────────────────────────────────────

def run_mcmc(z_hel, mu_obs, C_inv,
             n_walkers=64, n_steps=3000, n_burn=500):
    """
    Roda MCMC com emcee.
    Requer: pip install emcee
    """
    try:
        import emcee
    except ImportError:
        raise ImportError("Instale emcee: pip install emcee")
    
    # Ponto inicial (próximo ao posterior sintético)
    theta_init = np.array([0.315, 0.059, 1.16, 0.40, -19.3])
    ndim = len(theta_init)
    
    # Dispersão inicial dos walkers
    spreads = np.array([0.02, 0.01, 0.1, 0.05, 0.05])
    pos = theta_init + spreads * np.random.randn(n_walkers, ndim)
    
    print(f"Iniciando MCMC: {n_walkers} walkers × {n_steps} steps")
    print(f"Parâmetros: Om0, Os0, zt, wt, M_abs")
    
    sampler = emcee.EnsembleSampler(
        n_walkers, ndim, log_posterior,
        args=(z_hel, mu_obs, C_inv)
    )
    
    sampler.run_mcmc(pos, n_steps, progress=True)
    
    # Remover burn-in
    samples = sampler.get_chain(discard=n_burn, flat=True)
    log_prob = sampler.get_log_prob(discard=n_burn, flat=True)
    
    return samples, log_prob, sampler


# ─── Sumário dos resultados ───────────────────────────────────────────────────

def summarize_posterior(samples, param_names=None):
    """Imprime mediana e intervalos 68% do posterior."""
    if param_names is None:
        param_names = ['Om0', 'Os0', 'zt', 'wt', 'M_abs']
    
    print("\n=== Posterior (dados reais Pantheon+) ===")
    print(f"{'Parâmetro':>10} | {'Mediana':>10} | {'16%':>10} | {'84%':>10}")
    print("-" * 48)
    
    for i, name in enumerate(param_names):
        q16, q50, q84 = np.percentile(samples[:, i], [16, 50, 84])
        print(f"{name:>10} | {q50:10.4f} | {q16:10.4f} | {q84:10.4f}")


# ─── Ponto de entrada ─────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Relativity Living Light — Template Pantheon+ MCMC")
    print("=" * 55)
    
    try:
        z_hel, mu_obs, C_inv = load_pantheon()
        print(f"Dados carregados: {len(z_hel)} supernovas")
        
        samples, log_prob, sampler = run_mcmc(z_hel, mu_obs, C_inv)
        summarize_posterior(samples)
        
        # Salvar resultados
        np.savetxt('data/posterior_real_pantheon.csv',
                   np.column_stack([samples, log_prob]),
                   delimiter=',',
                   header='Om0,Os0,zt,wt,M_abs,log_prob',
                   comments='')
        print("\nPosterior salvo em: data/posterior_real_pantheon.csv")
        
    except FileNotFoundError as e:
        print(f"\n{e}")
        print("\nPara testar a estrutura do código, execute com dados mock:")
        print("  python -c \"from panteon_likelihood import *; print('OK')\"")
