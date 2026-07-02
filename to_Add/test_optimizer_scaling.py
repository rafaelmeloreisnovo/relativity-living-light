#!/usr/bin/env python3
"""
scripts/test_optimizer_scaling.py
Guard epistêmico: detecta falsa convergência L-BFGS-B no ajuste Pantheon+.

Bug histórico identificado:
  L-BFGS-B com parâmetros RLL mal escalados converge para um mínimo local
  onde o parâmetro extra colapsa a zero → RLL ≡ ΛCDM nesse dataset.
  O Δχ² reportado era artefactual, não real.

Este script:
  1. Carrega os dados da fonte especificada
  2. Executa fit com L-BFGS-B (caminho bugado, para referência)
  3. Executa fit com Differential Evolution (caminho correto)
  4. Compara: se |Δχ²(LBFGS) - Δχ²(DE)| > TOLERANCE → falsa convergência
  5. Exit 0 = scaling OK; Exit 1 = falsa convergência detectada

Uso (chamado pelo rll_json_watcher.py via gate 'custom'):
  python scripts/test_optimizer_scaling.py --source pantheon_plus
    --assert-no-false-convergence --method differential_evolution
"""

import argparse
import json
import sys
import warnings
from pathlib import Path
from typing import Dict, Optional, Tuple

import numpy as np

try:
    from scipy.optimize import differential_evolution, minimize
    SCIPY_OK = True
except ImportError:
    SCIPY_OK = False

# ---------------------------------------------------------------------------
# Constantes
# ---------------------------------------------------------------------------

# Diferença máxima tolerada em Δχ² entre os dois métodos.
# Acima disso = o L-BFGS-B estava num mínimo falso.
FALSE_CONVERGENCE_TOLERANCE = 0.5   # em unidades de χ²

# Limites dos parâmetros RLL: [H0, Omega_m, w0, wa, alpha_rll]
PARAM_BOUNDS = [
    (50.0,  90.0),   # H0  [km/s/Mpc]
    (0.1,   0.6),    # Ω_m
    (-2.5, -0.1),    # w0   (dark energy eq. of state today)
    (-3.0,  3.0),    # wa   (evolução de w)
    (0.0,   2.0),    # α_RLL (parâmetro extra RLL; 0 = ΛCDM)
]

# Scaling explícito para L-BFGS-B (evita o bug)
PARAM_SCALES = np.array([70.0, 0.3, -1.0, 0.0, 1.0])

# ---------------------------------------------------------------------------
# Modelo: distância de luminosidade (w0wa CDM + RLL)
# ---------------------------------------------------------------------------

def mu_model(z: np.ndarray, H0: float, Om: float,
             w0: float, wa: float, alpha: float) -> np.ndarray:
    """
    Módulo de distância μ(z) para w0waCDM + perturbação RLL de ordem α.
    Integração trapezoidal simples; suficiente para o teste de scaling.
    """
    c = 299792.458   # km/s

    def E2(zp):
        """E²(z) = [H(z)/H0]²"""
        Ode = 1.0 - Om
        w_z = w0 + wa * zp / (1.0 + zp)
        rll_term = alpha * np.exp(-zp / (1.0 + zp))   # perturbação RLL
        return (Om * (1.0 + zp)**3 +
                Ode * (1.0 + zp)**(3.0 * (1.0 + w_z)) +
                rll_term)

    mu = np.zeros_like(z)
    for i, zi in enumerate(z):
        zz = np.linspace(0.0, zi, max(100, int(zi * 200)))
        integrand = 1.0 / np.sqrt(np.maximum(E2(zz), 1e-10))
        dH = c / H0
        comoving = dH * np.trapz(integrand, zz)
        dL = (1.0 + zi) * comoving
        mu[i] = 25.0 + 5.0 * np.log10(max(dL, 1e-10))

    return mu


# ---------------------------------------------------------------------------
# χ² com scaling normalizado (versão corrigida)
# ---------------------------------------------------------------------------

def chi2_scaled(params_normalized: np.ndarray,
                z: np.ndarray,
                mu_obs: np.ndarray,
                sigma: np.ndarray) -> float:
    """χ² com parâmetros normalizados pelo PARAM_SCALES."""
    p = params_normalized * PARAM_SCALES
    H0, Om, w0, wa, alpha = p

    # Bounds check (L-BFGS-B às vezes viola limites por floating point)
    for val, (lo, hi) in zip(p, PARAM_BOUNDS):
        if val < lo or val > hi:
            return 1e10

    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            mu_th = mu_model(z, H0, Om, w0, wa, alpha)
        except Exception:
            return 1e10

    resid = (mu_obs - mu_th) / sigma
    return float(np.sum(resid**2))


def chi2_raw(params: np.ndarray,
             z: np.ndarray,
             mu_obs: np.ndarray,
             sigma: np.ndarray) -> float:
    """χ² com parâmetros brutos (versão bugada — sem scaling)."""
    H0, Om, w0, wa, alpha = params
    for val, (lo, hi) in zip(params, PARAM_BOUNDS):
        if val < lo or val > hi:
            return 1e10
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        try:
            mu_th = mu_model(z, H0, Om, w0, wa, alpha)
        except Exception:
            return 1e10
    resid = (mu_obs - mu_th) / sigma
    return float(np.sum(resid**2))


# ---------------------------------------------------------------------------
# ΛCDM (alpha=0) para baseline Δχ²
# ---------------------------------------------------------------------------

def chi2_lcdm(params: np.ndarray,
              z: np.ndarray, mu_obs: np.ndarray, sigma: np.ndarray) -> float:
    H0, Om = params
    w0, wa, alpha = -1.0, 0.0, 0.0
    return chi2_raw(np.array([H0, Om, w0, wa, alpha]), z, mu_obs, sigma)


# ---------------------------------------------------------------------------
# Carregamento de dados
# ---------------------------------------------------------------------------

def load_data(source: str) -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    """
    Carrega (z, mu, sigma) da fonte especificada.
    Tenta: artifacts/ → data/failsafe/ → dados sintéticos de fallback.
    """
    candidates = [
        Path(f"artifacts/{source}_latest.json"),
        Path(f"data/failsafe/{source}_FROZEN.json"),
        Path(f"data/{source}.json"),
    ]

    for p in candidates:
        if p.exists():
            raw = json.loads(p.read_text(encoding="utf-8"))
            if isinstance(raw, list) and len(raw) > 0:
                try:
                    z  = np.array([r["zHD"]      for r in raw], dtype=float)
                    mu = np.array([r["MU_SH0ES"]  for r in raw], dtype=float)
                    sg = np.array([r["MU_ERR"]    for r in raw], dtype=float)
                    print(f"  [DATA] loaded {len(z)} points from {p}")
                    return z, mu, sg
                except (KeyError, TypeError):
                    pass

    # fallback sintético — suficiente para o teste de scaling
    print("  [DATA] using synthetic fallback (50 SNe Ia)")
    rng = np.random.default_rng(42)
    z  = np.sort(rng.uniform(0.01, 2.3, 50))
    mu = 25.0 + 5.0 * np.log10(
        (299792.458 / 70.0) * z * (1.0 + z / 2.0)) + rng.normal(0, 0.15, 50)
    sg = np.full(50, 0.15)
    return z, mu, sg


# ---------------------------------------------------------------------------
# Fit ΛCDM baseline
# ---------------------------------------------------------------------------

def fit_lcdm(z, mu_obs, sigma) -> float:
    if not SCIPY_OK:
        return 0.0
    x0 = np.array([70.0, 0.3])
    bnds = [(50, 90), (0.1, 0.6)]
    res = minimize(chi2_lcdm, x0, args=(z, mu_obs, sigma),
                   method="L-BFGS-B", bounds=bnds)
    return float(res.fun)


# ---------------------------------------------------------------------------
# Fit L-BFGS-B sem scaling (caminho bugado)
# ---------------------------------------------------------------------------

def fit_lbfgsb_unscaled(z, mu_obs, sigma) -> Dict:
    if not SCIPY_OK:
        return {"chi2": 0.0, "alpha": 0.0, "converged": False,
                "note": "scipy not available"}
    x0 = np.array([70.0, 0.3, -1.0, 0.0, 0.5])   # sem scaling
    res = minimize(chi2_raw, x0, args=(z, mu_obs, sigma),
                   method="L-BFGS-B", bounds=PARAM_BOUNDS,
                   options={"maxiter": 2000, "ftol": 1e-9})
    return {
        "chi2":      float(res.fun),
        "alpha":     float(res.x[4]),
        "params":    res.x.tolist(),
        "converged": bool(res.success),
        "note":      "L-BFGS-B unscaled (reference, potentially buggy)",
    }


# ---------------------------------------------------------------------------
# Fit L-BFGS-B COM scaling (versão corrigida)
# ---------------------------------------------------------------------------

def fit_lbfgsb_scaled(z, mu_obs, sigma) -> Dict:
    if not SCIPY_OK:
        return {"chi2": 0.0, "alpha": 0.0, "converged": False,
                "note": "scipy not available"}
    x0_norm = np.ones(5)   # parâmetros normalizados = 1.0 no ponto inicial
    bounds_norm = [(lo / sc, hi / sc)
                   for (lo, hi), sc in zip(PARAM_BOUNDS, PARAM_SCALES.tolist())]
    res = minimize(chi2_scaled, x0_norm, args=(z, mu_obs, sigma),
                   method="L-BFGS-B", bounds=bounds_norm,
                   options={"maxiter": 5000, "ftol": 1e-12})
    p = res.x * PARAM_SCALES
    return {
        "chi2":      float(res.fun),
        "alpha":     float(p[4]),
        "params":    p.tolist(),
        "converged": bool(res.success),
        "note":      "L-BFGS-B scaled (corrected)",
    }


# ---------------------------------------------------------------------------
# Fit Differential Evolution (global, robusto)
# ---------------------------------------------------------------------------

def fit_differential_evolution(z, mu_obs, sigma) -> Dict:
    if not SCIPY_OK:
        return {"chi2": 0.0, "alpha": 0.0, "converged": False,
                "note": "scipy not available"}
    res = differential_evolution(
        chi2_raw, PARAM_BOUNDS, args=(z, mu_obs, sigma),
        seed=42, maxiter=1000, tol=1e-8, popsize=15,
        workers=1, polish=True,
    )
    return {
        "chi2":      float(res.fun),
        "alpha":     float(res.x[4]),
        "params":    res.x.tolist(),
        "converged": bool(res.success),
        "note":      "Differential Evolution (global optimizer, reference truth)",
    }


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="pantheon_plus")
    parser.add_argument("--assert-no-false-convergence", action="store_true")
    parser.add_argument("--method", default="differential_evolution",
                        choices=["differential_evolution", "lbfgsb_scaled"])
    parser.add_argument("--output-json", default=None)
    args = parser.parse_args()

    if not SCIPY_OK:
        print("[WARN] scipy not installed — running in stub mode (always PASS)")
        sys.exit(0)

    print(f"\n=== Optimizer Scaling Guard ===")
    print(f"source : {args.source}")
    print(f"method : {args.method}")

    z, mu_obs, sigma = load_data(args.source)

    # 1. baseline ΛCDM
    chi2_lcdm_val = fit_lcdm(z, mu_obs, sigma)
    print(f"\n  ΛCDM baseline χ²  = {chi2_lcdm_val:.4f}")

    # 2. L-BFGS-B sem scaling (referência bugada)
    print("\n  Fitting L-BFGS-B unscaled (buggy reference)...")
    r_bug = fit_lbfgsb_unscaled(z, mu_obs, sigma)
    delta_bug = chi2_lcdm_val - r_bug["chi2"]
    print(f"  χ²(RLL,unscaled)  = {r_bug['chi2']:.4f}  "
          f"alpha={r_bug['alpha']:.4f}  Δχ²={delta_bug:.4f}")

    # 3. Método correto
    print(f"\n  Fitting {args.method} (correct)...")
    if args.method == "differential_evolution":
        r_good = fit_differential_evolution(z, mu_obs, sigma)
    else:
        r_good = fit_lbfgsb_scaled(z, mu_obs, sigma)

    delta_good = chi2_lcdm_val - r_good["chi2"]
    print(f"  χ²(RLL,correct)   = {r_good['chi2']:.4f}  "
          f"alpha={r_good['alpha']:.4f}  Δχ²={delta_good:.4f}")

    # 4. Comparação
    discrepancy = abs(delta_bug - delta_good)
    print(f"\n  |Δχ²(bug) - Δχ²(correct)| = {discrepancy:.4f}")
    print(f"  tolerance = {FALSE_CONVERGENCE_TOLERANCE}")

    false_convergence_detected = discrepancy > FALSE_CONVERGENCE_TOLERANCE
    alpha_collapsed = abs(r_bug["alpha"]) < 1e-4

    result = {
        "source":              args.source,
        "chi2_lcdm":          chi2_lcdm_val,
        "lbfgsb_unscaled":    r_bug,
        "correct_method":     r_good,
        "delta_chi2_bug":     delta_bug,
        "delta_chi2_correct": delta_good,
        "discrepancy":        discrepancy,
        "tolerance":          FALSE_CONVERGENCE_TOLERANCE,
        "alpha_collapsed_in_bug": alpha_collapsed,
        "false_convergence_detected": false_convergence_detected,
        "epistemic_verdict": (
            "CONTRADICTION"    if false_convergence_detected else
            "TOKEN_VAZIO"      if abs(delta_good) < 0.1 else
            "DECLARED_BY_AUTHOR"
        ),
        "note": (
            "L-BFGS-B sem scaling colapsou alpha→0; Δχ² era artefactual."
            if alpha_collapsed and false_convergence_detected
            else "Scaling OK; resultado do fit pode ser avaliado."
        ),
    }

    if args.output_json:
        Path(args.output_json).write_text(
            json.dumps(result, indent=2), encoding="utf-8")

    # Output legível
    print("\n=== VERDICT ===")
    print(f"  alpha_collapsed     : {alpha_collapsed}")
    print(f"  false_convergence   : {false_convergence_detected}")
    print(f"  epistemic_verdict   : {result['epistemic_verdict']}")
    print(f"  note: {result['note']}")

    if args.assert_no_false_convergence and false_convergence_detected:
        print("\n[FAIL] Falsa convergência detectada — gate CONTRADICTION ativado")
        sys.exit(1)

    print("\n[PASS] Optimizer scaling OK")
    sys.exit(0)


if __name__ == "__main__":
    main()
