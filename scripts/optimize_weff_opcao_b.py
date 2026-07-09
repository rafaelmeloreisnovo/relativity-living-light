#!/usr/bin/env python3
"""Optimize Opção B w_eff vs DESI CPL — test Predição P-RLL-05.

PREDIÇÃO P-RLL-05 (PREDICAO_DATADA_RLL.md, 2026-07-07):
  "A Opção B com otimização contínua de (z_t, w2, w_t) atingirá χ²_DESI < 10,
   demonstrando compatibilidade estrutural com CPL DESI."

OPÇÃO B:
  ρ_B(z; w2, z_t, w_t) = f(z)·(1+z)^{3(1+w1)} + (1-f(z))·(1+z)^{3(1+w2)}
  w1 = -1.0 fixo (regime DE puro em z→0)
  f(z) = 1/(1+exp((z−z_t)/w_t))

Método: scipy.optimize.minimize (Nelder-Mead) com múltiplos pontos de partida.
  - Ponto de partida 1: melhor do scan discreto (FASE 11) — z_t=1.0, w2=−0.50, w_t=0.50
  - Ponto de partida 2: grade ampla de inicializações para evitar mínimos locais
  - Bounds: z_t ∈ (0.1, 3.0), w2 ∈ (−1.5, 0.0), w_t ∈ (0.05, 1.0)

Output: results/optimize_weff_opcao_b.json
  Falsificador P-RLL-05: "passes": chi2_opt < 10
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Callable

try:
    from scipy.optimize import minimize as scipy_minimize
    SCIPY_AVAILABLE = True
except ImportError:
    SCIPY_AVAILABLE = False

REPO = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO / "results"

W1_FIXED = -1.0

DESI_Z = (0.295, 0.510, 0.706, 0.934, 1.321, 1.484)
DESI_W = (-0.671, -0.558, -0.459, -0.354, -0.210, -0.156)
CHI2_SIGMA = 0.05


def f_rll(z: float, z_t: float, w_t: float) -> float:
    arg = max(-700.0, min(700.0, (z - z_t) / w_t))
    return 1.0 / (1.0 + math.exp(arg))


def rho_opcao_b(z: float, w2: float, z_t: float, w_t: float) -> float:
    f = f_rll(z, z_t, w_t)
    return f * (1.0 + z) ** (3.0 * (1.0 + W1_FIXED)) + (1.0 - f) * (1.0 + z) ** (3.0 * (1.0 + w2))


def _d_rho_d_lna(rho_fn: Callable[[float], float], z: float, h: float = 1e-5) -> float:
    a = 1.0 / (1.0 + z)
    x = math.log(a)

    def at_lna(lna: float) -> float:
        aa = math.exp(lna)
        return rho_fn(1.0 / aa - 1.0)

    return (at_lna(x + h) - at_lna(x - h)) / (2.0 * h)


def weff_b(z: float, w2: float, z_t: float, w_t: float) -> float:
    rho_fn = lambda zz: rho_opcao_b(zz, w2, z_t, w_t)
    rho = rho_fn(z)
    drho = _d_rho_d_lna(rho_fn, z)
    return -1.0 - drho / (3.0 * rho)


def chi2_vs_desi(params: tuple | list) -> float:
    w2, z_t, w_t = params
    if w_t <= 0:
        return 1e10
    return sum(
        ((weff_b(z, w2, z_t, w_t) - w_target) / CHI2_SIGMA) ** 2
        for z, w_target in zip(DESI_Z, DESI_W)
    )


def nelder_mead_fallback(chi2_fn: Callable, x0: list, bounds: list) -> dict:
    """Pure-Python Nelder-Mead for when scipy is unavailable (simplified, 3D)."""
    n = len(x0)
    alpha, gamma, rho_nm, sigma = 1.0, 2.0, 0.5, 0.5
    simplex = [list(x0)]
    for i in range(n):
        point = list(x0)
        point[i] *= 1.05 if x0[i] != 0 else 0.05
        simplex.append(point)

    def clamp(x: list) -> list:
        return [max(lo, min(hi, xi)) for xi, (lo, hi) in zip(x, bounds)]

    def f(x: list) -> float:
        return chi2_fn(clamp(x))

    scores = [(f(s), s) for s in simplex]
    for _ in range(2000):
        scores.sort(key=lambda t: t[0])
        best_score, worst_score = scores[0][0], scores[-1][0]
        centroid = [sum(scores[j][1][i] for j in range(n)) / n for i in range(n)]
        reflected = clamp([centroid[i] + alpha * (centroid[i] - scores[-1][1][i]) for i in range(n)])
        fr = f(reflected)
        if scores[0][0] <= fr < scores[-2][0]:
            scores[-1] = (fr, reflected)
        elif fr < scores[0][0]:
            expanded = clamp([centroid[i] + gamma * (reflected[i] - centroid[i]) for i in range(n)])
            scores[-1] = (f(expanded), expanded) if f(expanded) < fr else (fr, reflected)
        else:
            contracted = clamp([centroid[i] + rho_nm * (scores[-1][1][i] - centroid[i]) for i in range(n)])
            fc = f(contracted)
            if fc < scores[-1][0]:
                scores[-1] = (fc, contracted)
            else:
                best = scores[0][1]
                scores = [(f(clamp([best[i] + sigma * (s[i] - best[i]) for i in range(n)])),
                           clamp([best[i] + sigma * (s[i] - best[i]) for i in range(n)])) for _, s in scores]
        if worst_score - best_score < 1e-8:
            break
    scores.sort(key=lambda t: t[0])
    best_x = clamp(scores[0][1])
    return {"x": best_x, "fun": scores[0][0], "success": True}


START_POINTS = [
    [-0.50, 1.0, 0.50],
    [-0.50, 1.0, 0.30],
    [-0.60, 1.2, 0.50],
    [-0.40, 0.8, 0.60],
    [-0.30, 1.5, 0.40],
    [-0.70, 0.7, 0.70],
    [-0.50, 0.5, 0.80],
    [-0.20, 2.0, 0.30],
    [-0.80, 1.0, 0.20],
    [-0.50, 1.0, 1.00],
]

BOUNDS = [(-1.5, 0.0), (0.1, 3.0), (0.05, 1.5)]


def run_optimization() -> dict:
    results = []

    for x0 in START_POINTS:
        try:
            if SCIPY_AVAILABLE:
                res = scipy_minimize(
                    chi2_vs_desi, x0,
                    method="Nelder-Mead",
                    options={"maxiter": 5000, "xatol": 1e-7, "fatol": 1e-7},
                )
                opt_x = list(res.x)
                opt_chi2 = float(res.fun)
            else:
                res = nelder_mead_fallback(chi2_vs_desi, x0, BOUNDS)
                opt_x = res["x"]
                opt_chi2 = float(res["fun"])

            w2_opt, z_t_opt, w_t_opt = opt_x[0], opt_x[1], opt_x[2]
            w2_opt = max(-1.5, min(0.0, w2_opt))
            z_t_opt = max(0.1, min(3.0, z_t_opt))
            w_t_opt = max(0.05, min(1.5, w_t_opt))

            w_eff_at_z = {
                f"z={z:.3f}": round(weff_b(z, w2_opt, z_t_opt, w_t_opt), 6)
                for z in DESI_Z
            }
            all_negative = all(v < 0 for v in w_eff_at_z.values())

            results.append({
                "x0": x0,
                "opt": {"w2": round(w2_opt, 6), "z_t": round(z_t_opt, 6), "w_t": round(w_t_opt, 6)},
                "chi2": round(opt_chi2, 6),
                "passes": opt_chi2 < 10.0,
                "w_eff_always_negative": all_negative,
                "w_eff_at_desi_z": w_eff_at_z,
            })
        except Exception as exc:
            results.append({"x0": x0, "error": str(exc)})

    valid = [r for r in results if "chi2" in r]
    best = min(valid, key=lambda r: r["chi2"]) if valid else None

    scan_reference = {"chi2": 14.8, "w2": -0.50, "z_t": 1.0, "w_t": 0.50}

    improvement = None
    if best:
        improvement = round(scan_reference["chi2"] - best["chi2"], 4)

    desi_profile = []
    if best:
        w2_b = best["opt"]["w2"]
        z_t_b = best["opt"]["z_t"]
        w_t_b = best["opt"]["w_t"]
        for z, w_target in zip(DESI_Z, DESI_W):
            w_c = weff_b(z, w2_b, z_t_b, w_t_b)
            desi_profile.append({
                "z": z,
                "w_eff_opt": round(w_c, 6),
                "w_cpl_target": w_target,
                "delta": round(w_c - w_target, 6),
            })

    passes = best["passes"] if best else False
    best_chi2 = best["chi2"] if best else None

    p_rll_05_outcome: str
    if best is None:
        p_rll_05_outcome = "INDETERMINATE — optimization failed"
    elif passes:
        p_rll_05_outcome = f"CONFIRMED — χ²_opt={best_chi2:.4f} < 10 [E]"
    else:
        p_rll_05_outcome = f"NOT YET CONFIRMED — χ²_opt={best_chi2:.4f} > 10 [C → requer scan mais amplo ou modelo diferente]"

    return {
        "meta": {
            "script": "optimize_weff_opcao_b.py",
            "date": "2026-07-08",
            "phase": "FASE 13",
            "prediction_id": "P-RLL-05",
            "description": "Opção B scipy.optimize.minimize — test se χ²<10 é atingível",
            "scipy_available": SCIPY_AVAILABLE,
            "n_start_points": len(START_POINTS),
        },
        "scan_reference": scan_reference,
        "optimization_results": results,
        "best": best,
        "best_improvement_vs_scan": improvement,
        "desi_profile_at_best": desi_profile,
        "falsifier": {
            "P-RLL-05": {
                "claim": "Opção B cruzará χ²_DESI < 10 com otimização contínua",
                "threshold": "chi2 < 10",
                "result": best_chi2,
                "outcome": p_rll_05_outcome,
            }
        },
        "epistemic_status": p_rll_05_outcome,
    }


def main() -> int:
    result = run_optimization()
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "optimize_weff_opcao_b.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    best = result["best"]
    print("=== Opção B — Otimização Contínua (scipy.minimize / Nelder-Mead) ===")
    print(f"scipy disponível: {result['meta']['scipy_available']}")
    print(f"Pontos de partida testados: {result['meta']['n_start_points']}")
    print()
    if best:
        print(f"Melhor ponto encontrado:")
        print(f"  w2 = {best['opt']['w2']:.6f}")
        print(f"  z_t = {best['opt']['z_t']:.6f}")
        print(f"  w_t = {best['opt']['w_t']:.6f}")
        print(f"  χ² = {best['chi2']:.4f}")
        print(f"  w_eff sempre negativo: {best['w_eff_always_negative']}")
        print(f"  Passa χ²<10: {best['passes']}")
        print(f"  Melhoria vs scan discreto (χ²=14.8): {result['best_improvement_vs_scan']:+.4f}")
        print()
        print(f"Perfil w_eff no ponto ótimo:")
        print(f"{'z':>7}  {'w_eff_opt':>11}  {'w_CPL':>8}  {'Δ':>9}")
        for row in result["desi_profile_at_best"]:
            print(
                f"{row['z']:>7.3f}  {row['w_eff_opt']:>11.6f}  "
                f"{row['w_cpl_target']:>8.4f}  {row['delta']:>9.6f}"
            )
    else:
        print("Nenhum resultado válido.")
    print()
    print(f"=== P-RLL-05 ===")
    print(result["epistemic_status"])
    print(f"\nOutput: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
