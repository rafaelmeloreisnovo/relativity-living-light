#!/usr/bin/env python3
"""
rll_option_a_inverted_transition.py
Gerado: 2026-06-27 | ∆RafaelVerboΩ | RAFCODE-Φ

Testa Opção A: transição invertida g(z) = 1 - f(z)
Setor age como DE em z > zt e como matéria em z < zt.
Isso produz wa_eff < 0 — compatível com DESI DR2.

Uso: python3 rll_option_a_inverted_transition.py
"""
from __future__ import annotations
import math


def f_rll(z, zt, wt):
    try:
        return 1.0 / (1.0 + math.exp((z - zt) / wt))
    except OverflowError:
        return 0.0 if z > zt else 1.0


def g_rll(z, zt, wt):
    """g(z) = 1 - f(z): invertida. DE em alto z, matéria em baixo z."""
    return 1.0 - f_rll(z, zt, wt)


def rho_s_optionA(z, zt, wt):
    """ρ_s/ρ_s0 com transição invertida: g(z)·1 + (1-g(z))·a⁻³."""
    gz = g_rll(z, zt, wt)  # = 1 - f(z)
    fz = f_rll(z, zt, wt)   # = f(z)
    # gz·(DE-like, w=-1) + fz·(matter-like, a⁻³)
    return gz * 1.0 + fz * (1.0 + z) ** 3


def drho_optionA(z, zt, wt, h=1e-6):
    a = 1.0 / (1.0 + z)
    ln_a = math.log(a)

    def rho_a(aa):
        zz = 1.0 / aa - 1.0
        gz = g_rll(zz, zt, wt)
        fz = f_rll(zz, zt, wt)
        return gz * 1.0 + fz * (1.0 / aa) ** 3

    return (rho_a(math.exp(ln_a + h)) - rho_a(math.exp(ln_a - h))) / (2.0 * h)


def w_eff_optionA(z, zt, wt):
    rf = rho_s_optionA(z, zt, wt)
    if rf <= 1e-10:
        return -1.0
    dr = drho_optionA(z, zt, wt)
    return -1.0 - dr / (3.0 * rf)


def w_cpl(z, w0, wa):
    return w0 + wa * (1.0 - 1.0 / (1.0 + z))


# ── Comparação com DESI DR2 CPL best-fit ────────────────────────────────────

DESI_W0, DESI_WA = -0.838, -0.620
SIGMA_W = 0.08

Z_TRACERS = [0.295, 0.510, 0.706, 0.934, 1.321, 1.484, 2.330]
W_DESI = [w_cpl(z, DESI_W0, DESI_WA) for z in Z_TRACERS]


def chi2_optA(zt, wt):
    return sum(
        (w_eff_optionA(z, zt, wt) - wd) ** 2 / SIGMA_W ** 2
        for z, wd in zip(Z_TRACERS, W_DESI)
    )


def scan():
    best = {"chi2": 1e9}
    zt_range = [round(0.3 + i * 0.1, 1) for i in range(18)]
    wt_range = [round(0.1 + i * 0.05, 2) for i in range(14)]

    print("SCAN Opção A (transição invertida)")
    print(f"{'zt':>5} {'wt':>5} {'chi2':>10} {'w0_eff':>8} {'wa_eff':>8} {'diag':>14}")
    print("-" * 60)

    compatible = []
    for zt in zt_range:
        for wt in wt_range:
            chi2 = chi2_optA(zt, wt)
            w0e = w_eff_optionA(0.0, zt, wt)
            # wa_eff via finite diff
            h = 1e-4
            z_h = h / (1.0 - h)
            dw_da = (w_eff_optionA(0.0, zt, wt) - w_eff_optionA(z_h, zt, wt)) / h
            wae = -dw_da
            diag = "COMPAT" if chi2 < 15 else ("MARGINAL" if chi2 < 40 else "INCOMPAT")
            if chi2 < 40:
                print(f"{zt:>5.1f} {wt:>5.2f} {chi2:>10.2f} {w0e:>8.4f} {wae:>8.4f} {diag:>14}")
            if chi2 < best["chi2"]:
                best = {"chi2": chi2, "zt": zt, "wt": wt, "w0e": w0e, "wae": wae}
            if chi2 < 15:
                compatible.append((zt, wt, chi2, w0e, wae))

    print(f"\n=== MELHOR Opção A ===")
    print(f"  zt={best['zt']}  wt={best['wt']}")
    print(f"  chi2={best['chi2']:.2f}")
    print(f"  w0_eff={best['w0e']:.4f}  wa_eff={best['wae']:.4f}")
    print(f"  DESI: w0={DESI_W0}  wa={DESI_WA}")
    print(f"  Δw0={best['w0e']-DESI_W0:.4f}  Δwa={best['wae']-DESI_WA:.4f}")
    print(f"\n  Regiões compatíveis (chi2<15): {len(compatible)}")
    if compatible:
        print("  TOP 5:")
        for zt, wt, chi2, w0e, wae in sorted(compatible, key=lambda x: x[2])[:5]:
            print(f"    zt={zt}  wt={wt}  chi2={chi2:.2f}  w0={w0e:.4f}  wa={wae:.4f}")

    print("\n=== COMPARAÇÃO BASELINE vs OPÇÃO A ===")
    print(f"  RLL original (zt=1.0,wt=0.3): chi2=2162.57  wa_eff=+0.32")
    print(f"  RLL Opção A  (zt={best['zt']},wt={best['wt']}):  chi2={best['chi2']:.2f}  wa_eff={best['wae']:.4f}")
    improv = 2162.57 / best["chi2"]
    print(f"  Melhoria de chi2: {improv:.1f}×")

    print("\n=== DIAGNÓSTICO EPISTEMOLÓGICO ===")
    if best["chi2"] < 15:
        print("  [H] HIPÓTESE SUPORTADA: Opção A é compatível com DESI")
        print("  Próximo passo: implementar em rll_vs_lcdm.py e rodar AIC/BIC real")
    elif best["chi2"] < 100:
        print("  [H] HIPÓTESE PARCIALMENTE SUPORTADA: melhoria significativa")
        print("  Mas ainda fora do contorno 1σ DESI — mais parâmetros ou reformulação")
    else:
        print("  [VAZIO] Opção A também incompatível com DESI nesta parametrização")
        print("  TOKEN_VAZIO preservado — reformulação mais profunda necessária")


if __name__ == "__main__":
    scan()
