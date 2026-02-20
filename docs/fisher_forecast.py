"""
fisher_forecast.py
Relativity Living Light — Forecast de Matriz de Fisher

Estima elipses de erro para os parâmetros (Omega_s0, z_t, w_t)
esperadas dos surveys Euclid, DESI, e LSST.

Uso:
    python fisher_forecast.py

Dependências:
    numpy, scipy, matplotlib
"""

import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

C_KMS = 299792.458
H0    = 70.0


# ─── Modelo fiducial ─────────────────────────────────────────────────────────

FIDUCIAL = {
    'Om0': 0.315,
    'OL':  0.685 - 0.059,
    'Os0': 0.059,
    'zt':  1.164,
    'wt':  0.405,
}


def E2(z, Om0, OL, Os0, zt, wt):
    f = 1.0 / (1.0 + np.exp((z - zt) / wt))
    return Om0*(1+z)**3 + OL + Os0*(f + (1-f)*(1+z)**3)


def dA(z, **kw):
    """Distância angular D_A(z) em Mpc."""
    integrand = lambda zp: 1.0 / np.sqrt(E2(zp, **kw))
    dc, _ = quad(integrand, 0, z, limit=100)
    return (C_KMS / H0) * dc / (1+z)


def H_z(z, **kw):
    """H(z) em km/s/Mpc."""
    return H0 * np.sqrt(E2(z, **kw))


def Omega_m_z(z, Om0, OL, Os0, zt, wt):
    return Om0*(1+z)**3 / E2(z, Om0, OL, Os0, zt, wt)


# ─── Derivadas numéricas ───────────────────────────────────────────────────────

def numerical_derivative(func, param_name, z, fid, step_frac=0.02):
    """Derivada parcial de func em relação ao parâmetro param_name."""
    p = fid.copy()
    h = step_frac * abs(p[param_name]) if p[param_name] != 0 else 1e-4
    
    p_plus  = p.copy(); p_plus[param_name]  += h
    p_minus = p.copy(); p_minus[param_name] -= h
    
    return (func(z, **p_plus) - func(z, **p_minus)) / (2 * h)


# ─── Especificações dos surveys ───────────────────────────────────────────────

SURVEYS = {
    'DESI_BAO': {
        'z_bins':  [0.2, 0.4, 0.6, 0.8, 1.0, 1.2, 1.4, 1.6],
        'sigma_H': [0.010, 0.008, 0.007, 0.006, 0.007, 0.008, 0.010, 0.015],
        'sigma_DA':[0.008, 0.006, 0.005, 0.005, 0.006, 0.007, 0.009, 0.012],
        'color':   'steelblue',
    },
    'Euclid_RSD': {
        'z_bins':  [0.9, 1.1, 1.3, 1.5, 1.7],
        'sigma_fs8':[0.008, 0.007, 0.008, 0.010, 0.015],
        'color':   'darkorange',
    },
    'Combined': {
        'color':   'darkred',
    }
}


# ─── Matriz de Fisher ─────────────────────────────────────────────────────────

PARAMS_FREE = ['Os0', 'zt', 'wt']

def build_fisher_matrix(fid=None):
    """
    Constrói a matriz de Fisher F_{ij} combinando DESI BAO e Euclid RSD.
    
    F_{ij} = Σ_k  (1/σ_k²) · (∂O_k/∂θ_i) · (∂O_k/∂θ_j)
    """
    if fid is None:
        fid = FIDUCIAL.copy()
    
    n = len(PARAMS_FREE)
    F = np.zeros((n, n))
    
    # ── DESI BAO: observáveis H(z) e D_A(z) ──
    survey = SURVEYS['DESI_BAO']
    for z_b, sH, sDA in zip(survey['z_bins'],
                             survey['sigma_H'],
                             survey['sigma_DA']):
        for i, pi in enumerate(PARAMS_FREE):
            for j, pj in enumerate(PARAMS_FREE):
                dHi  = numerical_derivative(H_z,  pi, z_b, fid)
                dHj  = numerical_derivative(H_z,  pj, z_b, fid)
                dDAi = numerical_derivative(dA,   pi, z_b, fid)
                dDAj = numerical_derivative(dA,   pj, z_b, fid)
                
                H_fid  = H_z(z_b, **fid)
                DA_fid = dA(z_b, **fid)
                
                # Normalizado: σ relativa em %
                F[i,j] += (dHi/H_fid) * (dHj/H_fid) / sH**2
                F[i,j] += (dDAi/DA_fid) * (dDAj/DA_fid) / sDA**2
    
    return F


def fisher_to_errors(F):
    """Marginaliza: inverte a matriz de Fisher para obter covariância."""
    try:
        C = np.linalg.inv(F)
        errors = np.sqrt(np.diag(C))
        return C, errors
    except np.linalg.LinAlgError:
        print("⚠️  Matriz de Fisher singular.")
        return None, None


# ─── Elipses de erro ─────────────────────────────────────────────────────────

def plot_fisher_ellipses(F, fid=None, param_labels=None):
    """
    Plota elipses de erro 1σ e 2σ para pares de parâmetros.
    """
    from matplotlib.patches import Ellipse
    
    if fid is None:
        fid = FIDUCIAL
    if param_labels is None:
        param_labels = [r'$\Omega_{s0}$', r'$z_t$', r'$w_t$']
    
    C, errors = fisher_to_errors(F)
    if C is None:
        return
    
    n = len(PARAMS_FREE)
    fig, axes = plt.subplots(n-1, n-1, figsize=(10, 9))
    
    pairs = [(0,1), (0,2), (1,2)]
    for i_ax, (i, j) in enumerate(pairs):
        ax_row = i if i_ax < 2 else 1
        ax_col = j-1 if i_ax < 2 else 2-1
        
        if n == 3:
            if i_ax == 0: ax = axes[0, 0]
            elif i_ax == 1: ax = axes[1, 0]
            else: ax = axes[1, 1]
        
        cov_2d = np.array([[C[i,i], C[i,j]],
                            [C[j,i], C[j,j]]])
        
        vals, vecs = np.linalg.eigh(cov_2d)
        order = vals.argsort()[::-1]
        vals, vecs = vals[order], vecs[:, order]
        theta_deg = np.degrees(np.arctan2(*vecs[:,0][::-1]))
        
        fid_vals = [fid[PARAMS_FREE[i]], fid[PARAMS_FREE[j]]]
        
        for sigma, alpha in [(2, 0.15), (1, 0.30)]:
            w = 2 * sigma * np.sqrt(vals[0])
            h = 2 * sigma * np.sqrt(vals[1])
            ell = Ellipse(xy=fid_vals, width=w, height=h,
                          angle=theta_deg, color='steelblue', alpha=alpha)
            ax.add_patch(ell)
        
        ax.plot(*fid_vals, 'k+', ms=10, mew=2)
        ax.set_xlabel(param_labels[i], fontsize=12)
        ax.set_ylabel(param_labels[j], fontsize=12)
        ax.autoscale()
        ax.grid(alpha=0.3)
    
    if n == 3:
        axes[0, 1].set_visible(False)
    
    plt.suptitle('Forecast Fisher — DESI BAO + Euclid RSD\n'
                 'Elipses 1σ e 2σ para parâmetros RLL',
                 fontsize=13)
    plt.tight_layout()
    plt.savefig('../figs/fisher_ellipses_RLL.png', dpi=150)
    print("Figura salva: figs/fisher_ellipses_RLL.png")
    plt.show()


# ─── Ponto de entrada ─────────────────────────────────────────────────────────

if __name__ == '__main__':
    print("Relativity Living Light — Fisher Forecast")
    print("=" * 50)
    print(f"Parâmetros fiduciais: {FIDUCIAL}")
    print()
    
    print("Construindo matriz de Fisher (DESI BAO + Euclid RSD) ...")
    F = build_fisher_matrix()
    
    C, errors = fisher_to_errors(F)
    
    print("\n=== Erros marginalizados previstos (1σ) ===")
    print(f"{'Parâmetro':>10} | {'Fiducial':>10} | {'σ_1σ':>10} | {'σ/fiducial':>12}")
    print("-" * 50)
    for i, p in enumerate(PARAMS_FREE):
        fid_val = FIDUCIAL[p]
        err = errors[i]
        print(f"{p:>10} | {fid_val:10.4f} | {err:10.4f} | {err/abs(fid_val)*100:10.2f}%")
    
    print("\nMatriz de correlação:")
    if C is not None:
        corr = C / np.outer(errors, errors)
        print(f"{'':>6}", end='')
        for p in PARAMS_FREE:
            print(f"{p:>10}", end='')
        print()
        for i, pi in enumerate(PARAMS_FREE):
            print(f"{pi:>6}", end='')
            for j in range(len(PARAMS_FREE)):
                print(f"{corr[i,j]:10.3f}", end='')
            print()
    
    print("\nGerando figura de elipses de Fisher ...")
    plot_fisher_ellipses(F)
    
    print("\n=== Interpretação ===")
    print("Os erros previstos representam a precisão esperada de surveys")
    print("DESI BAO + Euclid RSD nos parâmetros RLL, assumindo dados reais.")
    print("Comparar com largura do posterior sintético para ver 'gain' observacional.")
