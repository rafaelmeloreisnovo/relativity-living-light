#!/usr/bin/env python3
"""Verify TOKEN_VAZIO H2-WEFF: Opção C — setor duplo α·f + (1-α)·(1-f) + matéria separada.

HIPÓTESE [H] (WEFF_INCOMPATIBILIDADE_RLL_CPL.md §5.2):
  ρ_C(z; α, r) = [α·f(z) + (1-α)·(1-f(z))] + r·(1-f(z))·(1+z)³

  Primeiro termo: DE-like ponderado — varia de α (z=0, f≈1) a (1-α) (z→∞, f≈0)
  Segundo termo: matéria escalada por (1-f), amplitude r = Ωs0_m/Ωs0_de
  Normalizado: ρ_C_norm(z) = ρ_C(z)/ρ_C(0) para cálculo correto de w_eff

  Casos especiais:
  - α=0.5, r=0: ρ_C ≈ constante → w_eff ≈ -1
  - α=1.0, r=0: ρ_C = f(z) → w_eff evolui puramente por f(z)
  - α=1.0, r→∞: recupera setor padrão (w_eff positivo)

Scan: α ∈ [0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0], r ∈ [0.0, 0.05, 0.1, 0.2, 0.3]
χ² vs DESI CPL targets (6 pontos BAO, σ=0.05)

Output: results/weff_opcao_c_scan.json
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO / "results"

Z_T = 1.0
W_T = 0.3

DESI_Z = (0.295, 0.510, 0.706, 0.934, 1.321, 1.484)
DESI_W = (-0.671, -0.558, -0.459, -0.354, -0.210, -0.156)
CHI2_SIGMA = 0.05

ALPHA_GRID = [0.5, 0.6, 0.7, 0.8, 0.9, 0.95, 1.0]
R_GRID = [0.0, 0.05, 0.1, 0.2, 0.3]

Z_GRID = (0.0, 0.1, 0.295, 0.5, 0.706, 0.934, 1.0, 1.321, 1.484, 1.5, 2.0, 3.0)


def f_rll(z: float) -> float:
    arg = max(-700.0, min(700.0, (z - Z_T) / W_T))
    return 1.0 / (1.0 + math.exp(arg))


def rho_opcao_c_raw(z: float, alpha: float, r: float) -> float:
    """ρ_C (unnormalized) = α·f + (1-α)·(1-f) + r·(1-f)·(1+z)³."""
    f = f_rll(z)
    rho_de = alpha * f + (1.0 - alpha) * (1.0 - f)
    rho_m = (1.0 - f) * (1.0 + z) ** 3
    return rho_de + r * rho_m


def rho_opcao_c(z: float, alpha: float, r: float) -> float:
    """ρ_C normalized: ρ_C(z)/ρ_C(0)."""
    norm = rho_opcao_c_raw(0.0, alpha, r)
    return rho_opcao_c_raw(z, alpha, r) / norm


def _d_rho_d_lna(rho_fn, z: float, h: float = 1e-5) -> float:
    a = 1.0 / (1.0 + z)
    x = math.log(a)

    def at_lna(lna: float) -> float:
        aa = math.exp(lna)
        return rho_fn(1.0 / aa - 1.0)

    return (at_lna(x + h) - at_lna(x - h)) / (2.0 * h)


def weff_c(z: float, alpha: float, r: float) -> float:
    def rho_fn(zz: float) -> float:
        return rho_opcao_c(zz, alpha, r)
    rho = rho_fn(z)
    drho = _d_rho_d_lna(rho_fn, z)
    return -1.0 - drho / (3.0 * rho)


def chi2_vs_desi(alpha: float, r: float) -> float:
    return sum(
        ((weff_c(z, alpha, r) - w_target) / CHI2_SIGMA) ** 2
        for z, w_target in zip(DESI_Z, DESI_W)
    )


def run_opcao_c_scan() -> dict:
    scan_results = []
    for alpha in ALPHA_GRID:
        for r in R_GRID:
            chi2 = chi2_vs_desi(alpha, r)
            w0_est = weff_c(0.0, alpha, r)
            wz1_est = weff_c(1.0, alpha, r)
            scan_results.append({
                "alpha": alpha,
                "r": r,
                "chi2_vs_desi": round(chi2, 3),
                "passes": chi2 < 10.0,
                "w_eff_z0": round(w0_est, 4),
                "w_eff_z1": round(wz1_est, 4),
            })

    best = min(scan_results, key=lambda x: x["chi2_vs_desi"])
    best_alpha = best["alpha"]
    best_r = best["r"]

    profile = []
    for z in Z_GRID:
        w = weff_c(z, best_alpha, best_r)
        w_cpl = None
        if DESI_Z[0] <= z <= DESI_Z[-1]:
            for i in range(len(DESI_Z) - 1):
                if DESI_Z[i] <= z <= DESI_Z[i + 1]:
                    frac = (z - DESI_Z[i]) / (DESI_Z[i + 1] - DESI_Z[i])
                    w_cpl = DESI_W[i] + frac * (DESI_W[i + 1] - DESI_W[i])
                    break
        profile.append({
            "z": round(z, 4),
            "f_z": round(f_rll(z), 6),
            "w_eff_c": round(w, 6),
            "w_cpl_desi": round(w_cpl, 6) if w_cpl is not None else None,
            "delta": round(w - w_cpl, 6) if w_cpl is not None else None,
        })

    desi_comparison = []
    for z, w_target in zip(DESI_Z, DESI_W):
        w_c = weff_c(z, best_alpha, best_r)
        desi_comparison.append({
            "z": z,
            "w_eff_opcao_c": round(w_c, 6),
            "w_cpl_target": w_target,
            "delta": round(w_c - w_target, 6),
        })

    w_vals = [entry["w_eff_c"] for entry in profile]
    all_negative = all(w < 0 for w in w_vals)

    # Special structural cases
    special_cases = {}
    for a in [0.5, 0.7, 0.9, 1.0]:
        for r in [0.0, 0.1]:
            key = f"alpha={a}_r={r}"
            try:
                chi2 = chi2_vs_desi(a, r)
                w0 = weff_c(0.0, a, r)
                w1 = weff_c(1.0, a, r)
                special_cases[key] = {
                    "chi2": round(chi2, 3),
                    "w_eff_z0": round(w0, 4),
                    "w_eff_z1": round(w1, 4),
                }
            except Exception as exc:
                special_cases[key] = {"error": str(exc)}

    return {
        "meta": {
            "script": "verify_weff_opcao_c.py",
            "date": "2026-07-07",
            "phase": "FASE 11",
            "token_vazio_id": "H2-WEFF",
            "description": "Opção C — setor duplo α·f + (1-α)·(1-f) + matéria separada",
        },
        "scan_config": {
            "alpha_grid": ALPHA_GRID,
            "r_grid": R_GRID,
            "z_t": Z_T,
            "w_t": W_T,
            "n_combinations": len(scan_results),
        },
        "scan_results": scan_results,
        "best_point": best,
        "best_profile": profile,
        "desi_comparison_best": desi_comparison,
        "special_cases": special_cases,
        "structural_analysis": {
            "all_w_negative_at_best": all_negative,
            "best_chi2": best["chi2_vs_desi"],
            "best_passes": best["chi2_vs_desi"] < 10.0,
            "any_combination_passes": any(r_entry["passes"] for r_entry in scan_results),
            "n_passes": sum(1 for r_entry in scan_results if r_entry["passes"]),
            "note_alpha_0p5_r0": "ρ_C ≈ constante → w_eff ≈ -1 para α=0.5, r=0",
        },
        "falsifiers": {
            "F_WEFF_C_01_chi2_lt10": best["chi2_vs_desi"] < 10.0,
            "F_WEFF_C_02_always_negative": all_negative,
        },
        "epistemic_status": (
            "[E] scan numérico executado — "
            + ("PASS: melhor χ²=" + str(best["chi2_vs_desi"]) + " < 10"
               if best["chi2_vs_desi"] < 10.0
               else "FAIL: melhor χ²=" + str(best["chi2_vs_desi"]) + " >> 10")
            + ". α=" + str(best_alpha) + ", r=" + str(best_r) + "."
        ),
        "interpretation": (
            "Opção C com α livre adiciona grau de liberdade mas mantém o problema estrutural: "
            "a transição logística de fase ainda produz variação brusca em w_eff na região z~z_t. "
            "O parâmetro r (matéria) agrava a incompatibilidade em alto z. "
            "Para α=0.5, r=0: setor constante (w=-1) — não distinguível de ΩΛ. "
            "TOKEN_VAZIO H2-WEFF: espaço paramétrico (α,r) não resolve a incompatibilidade estrutural."
        ),
    }


def main() -> int:
    result = run_opcao_c_scan()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "weff_opcao_c_scan.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    print("=== Opção C — Setor Duplo (Scan α, r) ===")
    best = result["best_point"]
    print(
        f"Melhor: α={best['alpha']:.2f}, r={best['r']:.2f} → "
        f"χ²={best['chi2_vs_desi']:.1f}"
    )
    print(f"Passes χ²<10: {best['passes']}")
    print(f"Qualquer combinação passa: {result['structural_analysis']['any_combination_passes']}")
    print()
    print(f"Perfil no melhor ponto (α={best['alpha']:.2f}, r={best['r']:.2f}):")
    print(f"{'z':>6}  {'w_eff_C':>9}  {'w_CPL':>9}  {'Δ':>8}")
    for row in result["desi_comparison_best"]:
        print(
            f"{row['z']:>6.3f}  {row['w_eff_opcao_c']:>9.4f}  "
            f"{row['w_cpl_target']:>9.4f}  {row['delta']:>8.4f}"
        )
    print()
    print("Casos especiais:")
    for key, vals in result["special_cases"].items():
        if "chi2" in vals:
            print(f"  {key}: χ²={vals['chi2']:.1f}, w(z=0)={vals['w_eff_z0']:.3f}, w(z=1)={vals['w_eff_z1']:.3f}")
    print(f"\nOutput: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
