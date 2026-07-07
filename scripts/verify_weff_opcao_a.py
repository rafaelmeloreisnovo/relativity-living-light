#!/usr/bin/env python3
"""Verify TOKEN_VAZIO FASE 10: w_eff comparison — RLL standard vs Opção A (inverted transition).

Standard sector:  Ωs0·[f(z) + (1−f(z))·(1+z)³]
  - f→1 at z=0 (DE-like); f→0 at z→∞ (matter-like)
  - w_eff transitions from −1 to 0, going POSITIVE in z~0.5–2

Opção A sector:  Ωs0·[(1−f(z)) + f(z)·(1+z)³]
  - (1−f)→0 at z=0 (matter-like initially); f→1 at z→∞ (DE-like at high z)
  - w_eff starts near 0 at low z, goes phantom at high z

Output: results/weff_opcao_a_comparison.json
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO / "results"

# RLL parameters (TOKEN_VAZIO P1: no first-principles derivation)
Z_T = 1.0
W_T = 0.3

# DESI DR2 CPL target from compute_weff_cpl_mapping.py
DESI_Z = (0.295, 0.510, 0.706, 0.934, 1.321, 1.484)
DESI_W = (-0.671, -0.558, -0.459, -0.354, -0.210, -0.156)

# Evaluation grid
Z_GRID = (0.0, 0.1, 0.295, 0.5, 0.706, 0.934, 1.0, 1.321, 1.484, 1.5, 2.0, 3.0)


def f_rll(z: float, z_t: float = Z_T, w_t: float = W_T) -> float:
    arg = max(-700.0, min(700.0, (z - z_t) / w_t))
    return 1.0 / (1.0 + math.exp(arg))


def rho_standard(z: float) -> float:
    """Standard sector density: f(z) + (1−f(z))·(1+z)³ (normalized at z=0)."""
    a = 1.0 / (1.0 + z)
    f = f_rll(z)
    return f + (1.0 - f) * a**-3


def rho_opcao_a(z: float) -> float:
    """Opção A sector density: (1−f(z)) + f(z)·(1+z)³."""
    a = 1.0 / (1.0 + z)
    f = f_rll(z)
    return (1.0 - f) + f * a**-3


def _d_rho_d_lna(rho_fn, z: float, h: float = 1e-5) -> float:
    """Numerical derivative of ρ w.r.t. ln(a) at redshift z."""
    a = 1.0 / (1.0 + z)
    x = math.log(a)

    def at_lna(lna: float) -> float:
        aa = math.exp(lna)
        zz = 1.0 / aa - 1.0
        return rho_fn(zz)

    return (at_lna(x + h) - at_lna(x - h)) / (2.0 * h)


def weff_standard(z: float) -> float:
    rho = rho_standard(z)
    drho = _d_rho_d_lna(rho_standard, z)
    return -1.0 - drho / (3.0 * rho)


def weff_opcao_a(z: float) -> float:
    rho = rho_opcao_a(z)
    drho = _d_rho_d_lna(rho_opcao_a, z)
    return -1.0 - drho / (3.0 * rho)


def chi2_vs_desi(weff_fn) -> float:
    """χ² of w_eff values at DESI BAO redshifts vs CPL target."""
    sigma = 0.05  # assumed uncertainty
    return sum(((weff_fn(z) - w_target) / sigma) ** 2 for z, w_target in zip(DESI_Z, DESI_W))


def classify_regime(w: float) -> str:
    if w > 0.1:
        return "matter-like (w>0)"
    if w > -0.5:
        return "transitional (-0.5<w<0)"
    if w > -1.0:
        return "quintessence (-1<w<-0.5)"
    if abs(w - (-1.0)) < 0.05:
        return "cosmological constant (w≈-1)"
    return "phantom (w<-1)"


def run_comparison() -> dict:
    rows = []
    for z in Z_GRID:
        f = f_rll(z)
        w_std = weff_standard(z)
        w_a = weff_opcao_a(z)
        # CPL target (interpolated linearly near DESI points or extrapolated)
        w_cpl = None
        if DESI_Z[0] <= z <= DESI_Z[-1]:
            for i in range(len(DESI_Z) - 1):
                if DESI_Z[i] <= z <= DESI_Z[i + 1]:
                    frac = (z - DESI_Z[i]) / (DESI_Z[i + 1] - DESI_Z[i])
                    w_cpl = DESI_W[i] + frac * (DESI_W[i + 1] - DESI_W[i])
                    break

        rows.append({
            "z": round(z, 4),
            "f_z": round(f, 6),
            "w_eff_standard": round(w_std, 6),
            "w_eff_opcao_a": round(w_a, 6),
            "w_cpl_desi_target": round(w_cpl, 6) if w_cpl is not None else None,
            "regime_standard": classify_regime(w_std),
            "regime_opcao_a": classify_regime(w_a),
        })

    chi2_std = chi2_vs_desi(weff_standard)
    chi2_a = chi2_vs_desi(weff_opcao_a)

    # Find z where w_eff_standard crosses zero
    zero_cross_std = None
    for i in range(len(Z_GRID) - 1):
        ws_i = weff_standard(Z_GRID[i])
        ws_j = weff_standard(Z_GRID[i + 1])
        if ws_i < 0 <= ws_j or ws_i >= 0 > ws_j:
            zero_cross_std = round(Z_GRID[i], 3)
            break

    return {
        "meta": {
            "script": "verify_weff_opcao_a.py",
            "date": "2026-07-07",
            "phase": "FASE 10",
            "description": "Comparação numérica w_eff setor RLL: padrão vs Opção A (transição invertida)",
        },
        "parameters": {"z_t": Z_T, "w_t": W_T},
        "grid_comparison": rows,
        "chi2_vs_desi_cpl": {
            "standard": round(chi2_std, 3),
            "opcao_a": round(chi2_a, 3),
            "threshold_pass": 10.0,
            "standard_passes": chi2_std < 10.0,
            "opcao_a_passes": chi2_a < 10.0,
        },
        "structural_diagnosis": {
            "standard_zero_crossing_z": zero_cross_std,
            "standard_regime_z07": classify_regime(weff_standard(0.706)),
            "opcao_a_regime_z07": classify_regime(weff_opcao_a(0.706)),
            "standard_regime_z15": classify_regime(weff_standard(1.5)),
            "opcao_a_regime_z15": classify_regime(weff_opcao_a(1.5)),
        },
        "falsifiers": {
            "F_WEFF_STANDARD_01": chi2_std < 10.0,
            "F_WEFF_OPCA0_A_01": chi2_a < 10.0,
            "neither_passes": chi2_std >= 10.0 and chi2_a >= 10.0,
        },
        "epistemic_status": (
            "[E] análise numérica executada — nenhuma variante replica CPL DESI. "
            "Incompatibilidade é estrutural (arquitetura DE↔matéria vs DE suave). "
            "Resolução requer revisão do setor ou reinterpretação da assinatura."
        ),
        "next_steps": [
            "[H] Opção B: setor com EOS evolutiva pura sem cruzamento de fase",
            "[H] Opção C: setor duplo α·f + (1-α)·(1-f) + matéria separada",
            "[VAZIO P0] Predição datada: se dados Euclid/DESI DR3 mostrarem w>0 em z~0.7, favorece RLL",
        ],
    }


def main() -> int:
    result = run_comparison()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "weff_opcao_a_comparison.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    chi2 = result["chi2_vs_desi_cpl"]
    diag = result["structural_diagnosis"]
    print("=== w_eff Setor RLL: Padrão vs Opção A ===")
    print(f"{'z':>6}  {'w_std':>9}  {'w_A':>9}  {'w_CPL':>9}  regime_std")
    for row in result["grid_comparison"]:
        cpl = f"{row['w_cpl_desi_target']:>9.4f}" if row["w_cpl_desi_target"] is not None else "      N/A"
        print(f"{row['z']:>6.3f}  {row['w_eff_standard']:>9.4f}  {row['w_eff_opcao_a']:>9.4f}  {cpl}  {row['regime_standard']}")
    print()
    print(f"χ² vs CPL DESI — Padrão: {chi2['standard']:.1f}  Opção A: {chi2['opcao_a']:.1f}  (threshold < 10)")
    print(f"Padrão PASS: {chi2['standard_passes']}  |  Opção A PASS: {chi2['opcao_a_passes']}")
    print(f"Cruzamento w=0 (padrão): z ≈ {diag['standard_zero_crossing_z']}")
    print(f"\nStatus: {result['epistemic_status'][:80]}...")
    print(f"\nOutput: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
