"""Relatórios de regimes cosmológicos para o pipeline Structure D.

Este módulo centraliza configuração explícita para auditoria:

- ``DOMINANCE_THRESHOLD``: limiar absoluto em ``R(z)`` usado para separar
  dominância de regime e região balanceada.
- Regra de fronteira ``balanced`` vs. dominâncias:
  ``-DOMINANCE_THRESHOLD <= R(z) <= DOMINANCE_THRESHOLD``.
- Estratégia de binning em redshift: fixa por ``n_bins`` (padrão) ou,
  alternativamente, bins manuais definidos em ``REDSHIFT_MANUAL_BINS``.
- ``SENSITIVITY_EPS``: passo padrão para derivadas numéricas centrais.

Os valores acima são serializados no campo ``notes`` do
``rll_regime_summary.csv`` e também em ``rll_regime_metadata.csv``.
"""

from __future__ import annotations

import os
from typing import Iterable, Sequence

import numpy as np
import pandas as pd

# 1) Limiar principal de dominância.
DOMINANCE_THRESHOLD = 0.10

# 2) Regra explícita de fronteiras para classificação.
BALANCED_MIN = -DOMINANCE_THRESHOLD
BALANCED_MAX = DOMINANCE_THRESHOLD

# 3) Estratégia de binning em redshift.
REDSHIFT_BINNING_STRATEGY = "fixed_n_bins"
REDSHIFT_N_BINS = 8
# Exemplo de configuração manual alternativa:
# REDSHIFT_BINNING_STRATEGY = "manual"
# REDSHIFT_MANUAL_BINS = (0.0, 0.3, 0.7, 1.2, 2.0, 3.0)
REDSHIFT_MANUAL_BINS: tuple[float, ...] = ()

# 4) Passo de sensibilidade para derivadas numéricas.
SENSITIVITY_EPS = 1.0e-4


def classify_regime(r_value: float) -> str:
    """Classifica regime de acordo com R(z) e a convenção de fronteira."""
    if r_value < BALANCED_MIN:
        return "lcdm_dominant"
    if r_value > BALANCED_MAX:
        return "rll_dominant"
    return "balanced"


def numerical_derivative_central(func, x: float, eps: float = SENSITIVITY_EPS) -> float:
    """Derivada numérica central com passo configurável e auditável."""
    step = float(eps)
    if not np.isfinite(step) or step <= 0.0:
        raise ValueError("eps must be finite and strictly positive")
    return float((func(x + step) - func(x - step)) / (2.0 * step))


def _audit_notes(n_bins: int, manual_bins: Sequence[float]) -> str:
    manual_repr = "none"
    if manual_bins:
        manual_repr = "[" + ",".join(f"{float(v):.6g}" for v in manual_bins) + "]"
    return (
        f"dominance_threshold={DOMINANCE_THRESHOLD};"
        f"balanced_rule=[{BALANCED_MIN},{BALANCED_MAX}];"
        f"binning_strategy={REDSHIFT_BINNING_STRATEGY};"
        f"n_bins={int(n_bins)};"
        f"manual_bins={manual_repr};"
        f"sensitivity_eps={SENSITIVITY_EPS}"
    )


def _resolve_bin_edges(z_values: np.ndarray, n_bins: int, manual_bins: Sequence[float] | None) -> np.ndarray:
    if REDSHIFT_BINNING_STRATEGY == "manual":
        if not manual_bins:
            raise ValueError("manual binning requires manual_bins")
        edges = np.asarray(manual_bins, dtype=float)
    else:
        if n_bins <= 0:
            raise ValueError("n_bins must be strictly positive")
        z_min = float(np.nanmin(z_values))
        z_max = float(np.nanmax(z_values))
        if z_max <= z_min:
            z_max = z_min + 1.0e-12
        edges = np.linspace(z_min, z_max, n_bins + 1, dtype=float)

    if np.any(~np.isfinite(edges)):
        raise ValueError("bin edges must be finite")
    if np.any(np.diff(edges) <= 0):
        raise ValueError("bin edges must be strictly increasing")
    return edges


def summarize_regimes_by_redshift(
    z_values: Iterable[float],
    r_values: Iterable[float],
    n_bins: int = REDSHIFT_N_BINS,
    manual_bins: Sequence[float] | None = None,
) -> pd.DataFrame:
    """Resume regimes por bin de redshift usando R(z)."""
    z_arr = np.asarray(list(z_values), dtype=float)
    r_arr = np.asarray(list(r_values), dtype=float)

    if z_arr.shape != r_arr.shape:
        raise ValueError("z_values and r_values must have the same shape")
    finite_mask = np.isfinite(z_arr) & np.isfinite(r_arr)
    if not np.any(finite_mask):
        raise ValueError("no finite z/r pairs available")

    z = z_arr[finite_mask]
    r = r_arr[finite_mask]
    edges = _resolve_bin_edges(z, n_bins=n_bins, manual_bins=manual_bins)

    notes = _audit_notes(n_bins=n_bins, manual_bins=manual_bins or REDSHIFT_MANUAL_BINS)
    rows = []
    for idx in range(len(edges) - 1):
        z_lo = float(edges[idx])
        z_hi = float(edges[idx + 1])
        if idx == len(edges) - 2:
            mask = (z >= z_lo) & (z <= z_hi)
        else:
            mask = (z >= z_lo) & (z < z_hi)

        if not np.any(mask):
            rows.append(
                {
                    "z_bin": idx,
                    "z_min": z_lo,
                    "z_max": z_hi,
                    "n_points": 0,
                    "R_mean": np.nan,
                    "R_median": np.nan,
                    "R_std": np.nan,
                    "regime": "no_data",
                    "notes": notes,
                }
            )
            continue

        r_bin = r[mask]
        r_mean = float(np.mean(r_bin))
        rows.append(
            {
                "z_bin": idx,
                "z_min": z_lo,
                "z_max": z_hi,
                "n_points": int(r_bin.size),
                "R_mean": r_mean,
                "R_median": float(np.median(r_bin)),
                "R_std": float(np.std(r_bin, ddof=0)),
                "regime": classify_regime(r_mean),
                "notes": notes,
            }
        )

    return pd.DataFrame(rows)


def write_regime_reports(
    z_values: Iterable[float],
    r_values: Iterable[float],
    results_dir: str,
    summary_filename: str = "rll_regime_summary.csv",
    metadata_filename: str = "rll_regime_metadata.csv",
    n_bins: int = REDSHIFT_N_BINS,
    manual_bins: Sequence[float] | None = None,
) -> tuple[str, str]:
    """Escreve resumo por redshift + metadado auxiliar para auditoria."""
    os.makedirs(results_dir, exist_ok=True)

    summary_df = summarize_regimes_by_redshift(
        z_values=z_values,
        r_values=r_values,
        n_bins=n_bins,
        manual_bins=manual_bins,
    )
    summary_path = os.path.join(results_dir, summary_filename)
    summary_df.to_csv(summary_path, index=False)

    notes = _audit_notes(n_bins=n_bins, manual_bins=manual_bins or REDSHIFT_MANUAL_BINS)
    metadata = pd.DataFrame(
        [
            {
                "dominance_threshold": DOMINANCE_THRESHOLD,
                "balanced_min": BALANCED_MIN,
                "balanced_max": BALANCED_MAX,
                "binning_strategy": REDSHIFT_BINNING_STRATEGY,
                "n_bins": int(n_bins),
                "manual_bins": "[" + ",".join(map(str, manual_bins or REDSHIFT_MANUAL_BINS)) + "]",
                "sensitivity_eps": SENSITIVITY_EPS,
                "notes": notes,
            }
        ]
    )
    metadata_path = os.path.join(results_dir, metadata_filename)
    metadata.to_csv(metadata_path, index=False)
    return summary_path, metadata_path
