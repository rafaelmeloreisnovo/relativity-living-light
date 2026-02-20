"""
crescimento_estrutural.py
Relativity Living Light — Solver de Crescimento Estrutural

Calcula f*sigma8(z) para o modelo RLL e compara com ΛCDM e dados BOSS DR12.

Uso:
    python crescimento_estrutural.py

Dependências:
    numpy, scipy, matplotlib
"""

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt


# ─── Modelo RLL ───────────────────────────────────────────────────────────────

def H2_over_H02(z, Om0, OL, Os0, zt, wt):
    """
    H²(z)/H₀² para o modelo Relativity Living Light.
    
    Parâmetros
    ----------
    Om0 : Ω_m hoje
    OL  : Ω_Λ (constante cosmológica residual)
    Os0 : Ω_s0 (superposição)
    zt  : z_t (redshift de transição)
    wt  : w_t (largura da transição)
    """
    f = 1.0 / (1.0 + np.exp((z - zt) / wt))
    return (Om0 * (1+z)**3
            + OL
            + Os0 * (f + (1.0 - f) * (1+z)**3))


def H2_lcdm(z, Om0, OL):
    """H²(z)/H₀² para ΛCDM padrão."""
    return Om0 * (1+z)**3 + OL


def growth_rhs(lna, y, Om0, OL, Os0, zt, wt):
    """
    Lado direito da equação de crescimento em variável lna = ln(a).
    y = [D, D'] onde D' = dD/d(lna)
    """
    D, Dp = y
    z = np.exp(-lna) - 1.0

    H2 = H2_over_H02(z, Om0, OL, Os0, zt, wt)

    # d(lnH²)/d(lna) via diferença finita
    dz = 1e-4
    dH2dz = (H2_over_H02(z + dz, Om0, OL, Os0, zt, wt)
           - H2_over_H02(z - dz, Om0, OL, Os0, zt, wt)) / (2 * dz)
    # dz/d(lna) = −(1+z)
    dlnH2_dlna = dH2dz * (-(1.0 + z)) / H2

    # Ω_m(a)
    Omz = Om0 * (1+z)**3 / H2

    # D'' + [2 + d(lnH)/d(lna)] D' - (3/2) Ω_m(a) D = 0
    D_pp = -(2.0 + 0.5 * dlnH2_dlna) * Dp + 1.5 * Omz * D
    return [Dp, D_pp]


def compute_growth(z_eval, Om0, OL, Os0, zt, wt, z_ini=100.0):
    """
    Integra a equação de crescimento de z_ini até z_eval.
    Retorna D(z)/D(0) e f(z) = d(lnD)/d(lna).
    """
    lna_ini = np.log(1.0 / (1.0 + z_ini))
    lna_0   = 0.0

    # Condição inicial: growing mode em matter domination
    D_ini = 1.0 / (1.0 + z_ini)
    y0 = [D_ini, D_ini]   # D_ini, D'_ini = D_ini

    lna_eval = np.sort(np.log(1.0 / (1.0 + np.array(z_eval))))

    sol = solve_ivp(
        growth_rhs,
        [lna_ini, lna_0],
        y0,
        args=(Om0, OL, Os0, zt, wt),
        t_eval=lna_eval,
        method='DOP853',
        rtol=1e-8,
        atol=1e-10,
        dense_output=False,
    )

    D_arr  = sol.y[0]
    Dp_arr = sol.y[1]
    D_0    = D_arr[-1]   # D(z=0), normalization

    D_norm = D_arr / D_0
    f_rate = Dp_arr / D_arr  # f = d(lnD)/d(lna)

    return D_norm, f_rate


def compute_fs8(z_eval, Om0, OL, Os0, zt, wt, sigma8_0=0.811):
    """Calcula fσ₈(z) para os parâmetros fornecidos."""
    D_norm, f_rate = compute_growth(z_eval, Om0, OL, Os0, zt, wt)
    sigma8_z = sigma8_0 * D_norm
    fs8      = f_rate * sigma8_z
    return fs8


# ─── Dados observacionais ─────────────────────────────────────────────────────

BOSS_DATA = {
    'z':    np.array([0.15,  0.38,  0.51,  0.61,  0.978, 1.40 ]),
    'fs8':  np.array([0.490, 0.497, 0.458, 0.436, 0.379, 0.482]),
    'err':  np.array([0.145, 0.045, 0.038, 0.034, 0.176, 0.116]),
    'label':['6dFGS', 'BOSS', 'BOSS', 'BOSS', 'VIPERS', 'FastSound'],
}


# ─── Script principal ─────────────────────────────────────────────────────────

if __name__ == '__main__':

    # Parâmetros RLL (mediana do posterior)
    params_rll = dict(
        Om0=0.315, OL=0.685 - 0.059,
        Os0=0.059, zt=1.164, wt=0.405,
    )
    # ΛCDM equivalente
    params_lcdm = dict(
        Om0=0.315, OL=0.685,
        Os0=0.0,   zt=1.0,   wt=0.3,
    )

    sigma8_0 = 0.811

    z_plot = np.linspace(0.05, 1.8, 200)

    print("Calculando fσ₈(z) para RLL ...")
    fs8_rll  = compute_fs8(z_plot, **params_rll,  sigma8_0=sigma8_0)
    print("Calculando fσ₈(z) para ΛCDM ...")
    fs8_lcdm = compute_fs8(z_plot, **params_lcdm, sigma8_0=sigma8_0)

    # ── Figura ──────────────────────────────────────────────────────────────
    fig, axes = plt.subplots(2, 1, figsize=(8, 8),
                             gridspec_kw={'height_ratios': [3, 1]})

    ax = axes[0]
    ax.errorbar(BOSS_DATA['z'], BOSS_DATA['fs8'], yerr=BOSS_DATA['err'],
                fmt='ko', ms=6, zorder=5, label='Dados observacionais')
    ax.plot(z_plot, fs8_lcdm, 'b--', lw=2, label=r'$\Lambda$CDM')
    ax.plot(z_plot, fs8_rll,  'r-',  lw=2, label='RLL (parâmetros sintéticos)')
    ax.set_ylabel(r'$f\sigma_8(z)$', fontsize=13)
    ax.set_title('Crescimento Estrutural: RLL vs ΛCDM', fontsize=13)
    ax.legend(fontsize=11)
    ax.grid(alpha=0.3)
    ax.set_xlim(0, 1.8)

    ax2 = axes[1]
    delta_pct = 100.0 * (fs8_rll - fs8_lcdm) / fs8_lcdm
    ax2.plot(z_plot, delta_pct, 'r-', lw=2)
    ax2.axhline(0, color='b', lw=1, ls='--')
    ax2.set_xlabel('Redshift z', fontsize=13)
    ax2.set_ylabel(r'$\Delta(f\sigma_8)$ [%]', fontsize=12)
    ax2.set_xlim(0, 1.8)
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    plt.savefig('../figs/paper/fs8_comparison_RLL_vs_LCDM.png', dpi=150)
    print("Figura salva: figs/paper/fs8_comparison_RLL_vs_LCDM.png")
    plt.show()

    # ── Desvios nos pontos de dados ─────────────────────────────────────────
    fs8_rll_pts  = compute_fs8(BOSS_DATA['z'].tolist(), **params_rll,  sigma8_0=sigma8_0)
    fs8_lcdm_pts = compute_fs8(BOSS_DATA['z'].tolist(), **params_lcdm, sigma8_0=sigma8_0)

    print("\nDesvio RLL vs ΛCDM nos pontos BOSS:")
    print(f"{'z':>6}  {'Δ(fσ₈) [%]':>12}  {'Observado':>10}  {'RLL':>8}  {'ΛCDM':>8}")
    print("-" * 55)
    for i, z in enumerate(BOSS_DATA['z']):
        d = 100.0 * (fs8_rll_pts[i] - fs8_lcdm_pts[i]) / fs8_lcdm_pts[i]
        print(f"{z:6.3f}  {d:+12.2f}%  "
              f"{BOSS_DATA['fs8'][i]:10.3f}  "
              f"{fs8_rll_pts[i]:8.3f}  "
              f"{fs8_lcdm_pts[i]:8.3f}")

    # χ² parcial
    chi2_rll  = np.sum(((BOSS_DATA['fs8'] - fs8_rll_pts)  / BOSS_DATA['err'])**2)
    chi2_lcdm = np.sum(((BOSS_DATA['fs8'] - fs8_lcdm_pts) / BOSS_DATA['err'])**2)
    print(f"\nχ²(RLL)  = {chi2_rll:.3f}  (6 pontos, 3 parâmetros livres → dof = 3)")
    print(f"χ²(ΛCDM) = {chi2_lcdm:.3f}  (6 pontos, 2 parâmetros livres → dof = 4)")
    print(f"Δχ²      = {chi2_rll - chi2_lcdm:+.3f}")

    # NOTA: estes χ² usam apenas 6 pontos e parâmetros do posterior sintético.
    # Com Pantheon+ + DESI BAO os parâmetros serão re-estimados.
    print("\n⚠️  NOTA: parâmetros derivados de dados sintéticos.")
    print("   Substituir params_rll por resultado de Pantheon+ MCMC.")
