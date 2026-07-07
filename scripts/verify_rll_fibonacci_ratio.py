#!/usr/bin/env python3
"""Verify TOKEN_VAZIO H-UNIV-01 P3: does f(z_{n+1})/f(z_n) → φ as n → ∞?

RLL logistic transition: f(z) = 1 / (1 + exp((z - z_t) / w_t))

This script tests whether sampling f(z) at Fibonacci-scaled z values produces
a ratio converging to the golden ratio φ = (1+√5)/2 ≈ 1.618...

Result is intentionally agnostic: it reports convergence or divergence without
claiming physical significance. That assessment is TOKEN_VAZIO H-UNIV-01.
"""
from __future__ import annotations

import json
import math
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
RESULTS_DIR = REPO / "results"

PHI = (1 + math.sqrt(5)) / 2  # golden ratio ≈ 1.61803

# Standard RLL parameters (TOKEN_VAZIO P1 — no first-principles derivation)
Z_T = 1.0
W_T = 0.3

# Fibonacci sequence up to N terms
N_TERMS = 30
Z_MAX = 5.0  # redshift scale for normalization


def fibonacci_sequence(n: int) -> list[int]:
    seq = [0, 1]
    for _ in range(n - 2):
        seq.append(seq[-1] + seq[-2])
    return seq[:n]


def f_rll(z: float, z_t: float = Z_T, w_t: float = W_T) -> float:
    """RLL logistic transition function."""
    return 1.0 / (1.0 + math.exp((z - z_t) / w_t))


def run_fibonacci_ratio_check() -> dict:
    fib = fibonacci_sequence(N_TERMS)
    fib_max = fib[-1]

    # Scale Fibonacci indices to z ∈ [0, Z_MAX]
    z_values = [Z_MAX * k / fib_max for k in fib[1:]]  # skip fib[0]=0 to avoid z=0

    f_values = [f_rll(z) for z in z_values]

    ratios = []
    for i in range(len(f_values) - 1):
        if f_values[i + 1] > 1e-15:
            ratio = f_values[i] / f_values[i + 1]
            ratios.append({
                "n": i + 1,
                "z_n": round(z_values[i], 6),
                "z_n1": round(z_values[i + 1], 6),
                "f_z_n": round(f_values[i], 8),
                "f_z_n1": round(f_values[i + 1], 8),
                "ratio": round(ratio, 8),
                "delta_phi": round(abs(ratio - PHI), 8),
            })

    # Check last few ratios for convergence
    last_ratios = [r["ratio"] for r in ratios[-5:]] if len(ratios) >= 5 else []
    final_ratio = ratios[-1]["ratio"] if ratios else None
    final_delta = abs(final_ratio - PHI) if final_ratio is not None else None

    # Convergence criterion: |ratio - φ| < 0.01 in last step
    converges = final_delta is not None and final_delta < 0.01

    # Monotone approach? Check if delta_phi is decreasing
    deltas = [r["delta_phi"] for r in ratios]
    monotone_approach = all(deltas[i] >= deltas[i + 1] for i in range(len(deltas) - 1)) if len(deltas) > 1 else None

    return {
        "meta": {
            "script": "verify_rll_fibonacci_ratio.py",
            "date": "2026-07-07",
            "token_vazio_id": "H-UNIV-01",
            "priority": "P3",
            "description": "f(z) logística RLL amostrada em z-values escalados pela sequência de Fibonacci",
        },
        "parameters": {
            "z_t": Z_T,
            "w_t": W_T,
            "z_max": Z_MAX,
            "n_terms": N_TERMS,
            "phi": round(PHI, 8),
        },
        "ratios": ratios,
        "summary": {
            "final_ratio": round(final_ratio, 8) if final_ratio else None,
            "final_delta_phi": round(final_delta, 8) if final_delta else None,
            "converges_to_phi": converges,
            "monotone_approach": monotone_approach,
            "last_5_ratios": [round(r, 6) for r in last_ratios],
        },
        "epistemic_status": (
            "[E] convergência numérica confirmada — não implica identidade física"
            if converges
            else "[H] sem convergência numérica clara com os parâmetros testados"
        ),
        "interpretation": (
            "A razão f(z_n)/f(z_{n+1}) com z escalado por Fibonacci converge para φ "
            "neste regime paramétrico. Isso é uma observação numérica [E]. "
            "A relação causal ou física permanece TOKEN_VAZIO H-UNIV-01."
            if converges
            else "Sem convergência para φ neste regime. H-UNIV-01 não suportada numericamente."
        ),
    }


def main() -> int:
    result = run_fibonacci_ratio_check()

    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    out_path = RESULTS_DIR / "fibonacci_ratio_verification.json"
    out_path.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")

    converges = result["summary"]["converges_to_phi"]
    final_ratio = result["summary"]["final_ratio"]
    final_delta = result["summary"]["final_delta_phi"]

    print(f"φ (golden ratio)    = {PHI:.8f}")
    print(f"Final ratio f(z_n)/f(z_{{n+1}}) = {final_ratio}")
    print(f"|ratio - φ|         = {final_delta}")
    print(f"Converges to φ      = {converges}")
    print(f"Epistemic status    : {result['epistemic_status']}")
    print(f"\nOutput: {out_path}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
