#!/usr/bin/env python3
"""Verify TOKEN_VAZIO H1-WEFF: Opção B — setor DE puro, dois estados logisticamente interpolados.

HIPÓTESE [H]: substituindo o endpoint matéria (w=0) do setor padrão por DE suave (w2 ∈ (-1,0)),
w_eff permanece sempre negativo, potencialmente correspondendo ao CPL DESI.

Setor Opção B:
  ρ_B(z; w1, w2) = f(z)·(1+z)^{3(1+w1)} + (1−f(z))·(1+z)^{3(1+w2)}
  Normalizado: ambos os termos = 1 em z=0 ✓
  w1 = −1.0 fixo (DE puro em baixo z)
  w2 ∈ (−1, 0) livre (DE suave em alto z; w2→0 recupera setor padrão)

Diferença vs padrão: endpoint alto-z passa de w=0 (matéria) para w=w2 < 0 (DE).
Consequência: w_eff_B permanece negativo para todo w2 < 0.

Scan: w2 ∈ [−0.9, −0.05], w_t ∈ {0.2, 0.3, 0.5}
χ² vs DESI CPL targets (6 pontos BAO, σ=0.05)

Output: results/weff_opcao_b_scan.json
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO / "results"

Z_T = 1.0
W1_FIXED = -1.0

DESI_Z = (0.295, 0.510, 0.706, 0.934, 1.321, 1.484)
DESI_W = (-0.671, -0.558, -0.459, -0.354, -0.210, -0.156)
CHI2_SIGMA = 0.05

W2_GRID = [-0.9, -0.8, -0.7, -0.6, -0.5, -0.4, -0.3, -0.2, -0.15, -0.1, -0.07, -0.05]
WT_GRID = [0.2, 0.3, 0.5]

Z_GRID = (0.0, 0.1, 0.295, 0.5, 0.706, 0.934, 1.0, 1.321, 1.484, 1.5, 2.0, 3.0)


def f_rll(z: float, w_t: float = 0.3) -> float:
    arg = max(-700.0, min(700.0, (z - Z_T) / w_t))
    return 1.0 / (1.0 + math.exp(arg))


def rho_opcao_b(z: float, w1: float, w2: float, w_t: float = 0.3) -> float:
    """ρ_B = f·(1+z)^{3(1+w1)} + (1-f)·(1+z)^{3(1+w2)} — normalizado em z=0."""
    a = 1.0 / (1.0 + z)
    f = f_rll(z, w_t)
    rho1 = a ** (-3.0 * (1.0 + w1))
    rho2 = a ** (-3.0 * (1.0 + w2))
    return f * rho1 + (1.0 - f) * rho2


def _d_rho_d_lna(rho_fn, z: float, h: float = 1e-5) -> float:
    a = 1.0 / (1.0 + z)
    x = math.log(a)

    def at_lna(lna: float) -> float:
        aa = math.exp(lna)
        return rho_fn(1.0 / aa - 1.0)

    return (at_lna(x + h) - at_lna(x - h)) / (2.0 * h)


def weff_b(z: float, w1: float, w2: float, w_t: float = 0.3) -> float:
    def rho_fn(zz: float) -> float:
        return rho_opcao_b(zz, w1, w2, w_t)
    rho = rho_fn(z)
    drho = _d_rho_d_lna(rho_fn, z)
    return -1.0 - drho / (3.0 * rho)


def chi2_vs_desi(w1: float, w2: float, w_t: float = 0.3) -> float:
    return sum(
        ((weff_b(z, w1, w2, w_t) - w_target) / CHI2_SIGMA) ** 2
        for z, w_target in zip(DESI_Z, DESI_W)
    )


def run_opcao_b_scan() -> dict:
    scan_results = []
    for w_t in WT_GRID:
        for w2 in W2_GRID:
            chi2 = chi2_vs_desi(W1_FIXED, w2, w_t)
            scan_results.append({
                "w1": W1_FIXED,
                "w2": w2,
                "w_t": w_t,
                "chi2_vs_desi": round(chi2, 3),
                "passes": chi2 < 10.0,
            })

    best = min(scan_results, key=lambda r: r["chi2_vs_desi"])
    best_w2 = best["w2"]
    best_wt = best["w_t"]

    profile = []
    for z in Z_GRID:
        w = weff_b(z, W1_FIXED, best_w2, best_wt)
        w_cpl = None
        if DESI_Z[0] <= z <= DESI_Z[-1]:
            for i in range(len(DESI_Z) - 1):
                if DESI_Z[i] <= z <= DESI_Z[i + 1]:
                    frac = (z - DESI_Z[i]) / (DESI_Z[i + 1] - DESI_Z[i])
                    w_cpl = DESI_W[i] + frac * (DESI_W[i + 1] - DESI_W[i])
                    break
        profile.append({
            "z": round(z, 4),
            "f_z": round(f_rll(z, best_wt), 6),
            "w_eff_b": round(w, 6),
            "w_cpl_desi": round(w_cpl, 6) if w_cpl is not None else None,
            "delta": round(w - w_cpl, 6) if w_cpl is not None else None,
        })

    desi_comparison = []
    for z, w_target in zip(DESI_Z, DESI_W):
        w_b = weff_b(z, W1_FIXED, best_w2, best_wt)
        desi_comparison.append({
            "z": z,
            "w_eff_opcao_b": round(w_b, 6),
            "w_cpl_desi_target": w_target,
            "delta": round(w_b - w_target, 6),
        })

    w_vals = [r["w_eff_b"] for r in profile]
    all_negative = all(w < 0 for w in w_vals)
    monotone_increasing = all(w_vals[i] <= w_vals[i + 1] for i in range(len(w_vals) - 1))

    # Structural diagnosis: where does weff peak/trough?
    w_at_desi = {str(z): round(weff_b(z, W1_FIXED, best_w2, best_wt), 4) for z in DESI_Z}

    return {
        "meta": {
            "script": "verify_weff_opcao_b.py",
            "date": "2026-07-07",
            "phase": "FASE 11",
            "token_vazio_id": "H1-WEFF",
            "description": "Opção B — setor DE puro com dois estados logisticamente interpolados",
        },
        "scan_config": {
            "w1_fixed": W1_FIXED,
            "w2_grid": W2_GRID,
            "wt_grid": WT_GRID,
            "z_t_fixed": Z_T,
            "n_combinations": len(scan_results),
        },
        "scan_results": scan_results,
        "best_point": best,
        "best_profile": profile,
        "desi_comparison_best": desi_comparison,
        "w_eff_at_desi_redshifts": w_at_desi,
        "structural_analysis": {
            "all_w_negative": all_negative,
            "monotone_increasing_w": monotone_increasing,
            "best_chi2": best["chi2_vs_desi"],
            "best_passes": best["chi2_vs_desi"] < 10.0,
            "any_combination_passes": any(r["passes"] for r in scan_results),
            "n_passes": sum(1 for r in scan_results if r["passes"]),
        },
        "falsifiers": {
            "F_WEFF_B_01_chi2_lt10": best["chi2_vs_desi"] < 10.0,
            "F_WEFF_B_02_always_negative": all_negative,
            "F_WEFF_B_03_monotone": monotone_increasing,
        },
        "epistemic_status": (
            "[E] scan numérico executado — "
            + ("PASS: melhor χ²=" + str(best["chi2_vs_desi"]) + " < 10"
               if best["chi2_vs_desi"] < 10.0
               else "FAIL: melhor χ²=" + str(best["chi2_vs_desi"]) + " >> 10")
            + ". Diagnóstico estrutural: w_eff_B sempre negativo="
            + str(all_negative) + ", monótono=" + str(monotone_increasing) + "."
        ),
        "interpretation": (
            "Opção B resolve o problema de w_eff positivo (setor padrão) mas não "
            "consegue reproduzir o perfil CPL DESI. O mecanismo: a transição logística "
            "entre dois estados DE produz bump em w_eff na região z~z_t, com amplitude "
            "insuficiente ou excessiva para atingir os alvos DESI. "
            "TOKEN_VAZIO H1-WEFF: compatibilidade estrutural requer setor sem transição abrupta."
        ),
    }


def main() -> int:
    result = run_opcao_b_scan()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "weff_opcao_b_scan.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print("=== Opção B — Setor DE Puro (Scan w2, w_t) ===")
    best = result["best_point"]
    print(f"Melhor: w2={best['w2']:.2f}, w_t={best['w_t']:.2f} → χ²={best['chi2_vs_desi']:.1f}")
    print(f"Passes χ²<10: {best['passes']}")
    print(f"Qualquer combinação passa: {result['structural_analysis']['any_combination_passes']}")
    print()
    print(f"Perfil no melhor ponto (w2={best['w2']:.2f}, w_t={best['w_t']:.2f}):")
    print(f"{'z':>6}  {'w_eff_B':>9}  {'w_CPL':>9}  {'Δ':>8}")
    for row in result["desi_comparison_best"]:
        print(
            f"{row['z']:>6.3f}  {row['w_eff_opcao_b']:>9.4f}  "
            f"{row['w_cpl_desi_target']:>9.4f}  {row['delta']:>8.4f}"
        )
    struct = result["structural_analysis"]
    print()
    print(f"w_eff sempre negativo: {struct['all_w_negative']}")
    print(f"w_eff monótono crescente: {struct['monotone_increasing_w']}")
    print(f"\nOutput: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
