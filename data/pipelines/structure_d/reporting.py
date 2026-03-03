import os
from typing import Dict, Iterable, List, Optional, Sequence, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from .models import model_RLL_like_Hz, model_RLL_like_fs8

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RESULTS_DIR = os.path.join(BASE_DIR, "results", "structure_d")
FIGS_DIR = os.path.join(RESULTS_DIR, "figs")


def _as_dataframe(data: Optional[Union[str, pd.DataFrame]]) -> Optional[pd.DataFrame]:
    """Normaliza entrada para DataFrame.

    Aceita caminho CSV ou DataFrame já carregado. Retorna ``None`` para entrada nula.
    """
    if data is None:
        return None
    if isinstance(data, pd.DataFrame):
        return data.copy()
    return pd.read_csv(data)


def build_redshift_grid(
    hz_data: Optional[Union[str, pd.DataFrame]] = None,
    fs8_data: Optional[Union[str, pd.DataFrame]] = None,
    mode: str = "union",
    z_min: float = 0.0,
    z_max: float = 2.5,
    n_points: int = 300,
) -> np.ndarray:
    """Constrói grade de redshift para relatórios.

    Defaults reproduzíveis:
      - ``mode='union'``: união ordenada dos redshifts observacionais em ``hz_data`` e ``fs8_data``.
      - ``mode='continuous'``: grade contínua com ``n_points`` em ``[z_min, z_max]``.

    Parameters
    ----------
    hz_data, fs8_data
        DataFrames (com coluna ``z``) ou caminhos CSV.
    mode
        ``'union'`` ou ``'continuous'``.
    z_min, z_max, n_points
        Faixa/configuração para grade contínua.
    """
    mode_norm = str(mode).strip().lower()
    hz_df = _as_dataframe(hz_data)
    fs8_df = _as_dataframe(fs8_data)

    if mode_norm == "continuous":
        if n_points < 2:
            raise ValueError("n_points deve ser >= 2 para grade contínua")
        return np.linspace(float(z_min), float(z_max), int(n_points), dtype=float)

    if mode_norm != "union":
        raise ValueError("mode deve ser 'union' ou 'continuous'")

    grids: List[np.ndarray] = []
    if hz_df is not None:
        grids.append(hz_df["z"].to_numpy(dtype=float))
    if fs8_df is not None:
        grids.append(fs8_df["z"].to_numpy(dtype=float))

    if not grids:
        return np.linspace(float(z_min), float(z_max), int(n_points), dtype=float)

    return np.unique(np.concatenate(grids))


def relative_step(value: float, eps: float = 1e-4) -> float:
    """Retorna passo relativo estável: ``delta = eps * max(|p|, 1)``."""
    return float(eps) * max(abs(float(value)), 1.0)


def compute_parameter_sensitivities(
    z_grid: Sequence[float],
    params: Dict[str, float],
    parameter_names: Optional[Iterable[str]] = None,
    step_eps: float = 1e-4,
    deriv_eps: float = 1e-12,
) -> Tuple[pd.DataFrame, Dict[str, Dict[str, np.ndarray]]]:
    """Calcula sensibilidades numéricas por parâmetro/observável com diferença central.

    Defaults reproduzíveis:
      - ``step_eps=1e-4`` para passo relativo por parâmetro;
      - ``deriv_eps=1e-12`` para proteção de divisões numéricas.

    Retorna:
      1) DataFrame long-format com colunas ``z``, ``observable``, ``parameter``, ``sensitivity``;
      2) Estrutura hierárquica ``{observable: {parameter: array_por_z}}``.
    """
    z_arr = np.asarray(z_grid, dtype=float)
    if parameter_names is None:
        parameter_names = list(params.keys())
    pnames = [p for p in parameter_names if p in params]

    nested = {"Hz": {}, "fσ8": {}}
    rows: List[Dict[str, float]] = []

    for pname in pnames:
        base_value = float(params[pname])
        delta = max(relative_step(base_value, eps=step_eps), float(deriv_eps))

        p_up = dict(params)
        p_dn = dict(params)
        p_up[pname] = base_value + delta
        p_dn[pname] = base_value - delta

        hz_up = model_RLL_like_Hz(z_arr, p_up)
        hz_dn = model_RLL_like_Hz(z_arr, p_dn)
        fs8_up = model_RLL_like_fs8(z_arr, p_up)
        fs8_dn = model_RLL_like_fs8(z_arr, p_dn)

        sens_hz = (hz_up - hz_dn) / (2.0 * delta + float(deriv_eps))
        sens_fs8 = (fs8_up - fs8_dn) / (2.0 * delta + float(deriv_eps))

        nested["Hz"][pname] = sens_hz
        nested["fσ8"][pname] = sens_fs8

        for idx, z_val in enumerate(z_arr):
            rows.append(
                {
                    "z": float(z_val),
                    "observable": "Hz",
                    "parameter": pname,
                    "sensitivity": float(sens_hz[idx]),
                    "abs_sensitivity": float(abs(sens_hz[idx])),
                }
            )
            rows.append(
                {
                    "z": float(z_val),
                    "observable": "fσ8",
                    "parameter": pname,
                    "sensitivity": float(sens_fs8[idx]),
                    "abs_sensitivity": float(abs(sens_fs8[idx])),
                }
            )

    sens_df = pd.DataFrame(rows)
    return sens_df, nested


def split_groups(sensitivity_df: pd.DataFrame) -> Dict[str, pd.DataFrame]:
    """Define grupos:

    - crescimento: sensibilidades de ``fσ8``;
    - expansão: sensibilidades de ``Hz``.
    """
    return {
        "growth": sensitivity_df[sensitivity_df["observable"] == "fσ8"].copy(),
        "expansion": sensitivity_df[sensitivity_df["observable"] == "Hz"].copy(),
    }


def compute_dominance_metric(sensitivity_df: pd.DataFrame, eps: float = 1e-12) -> pd.DataFrame:
    """Calcula ``R(z) = soma_sens_crescimento(z) / soma_sens_expansao(z)`` com proteção ``eps``."""
    groups = split_groups(sensitivity_df)

    growth_sum = (
        groups["growth"].groupby("z", as_index=False)["abs_sensitivity"].sum().rename(columns={"abs_sensitivity": "growth_sum"})
    )
    exp_sum = (
        groups["expansion"]
        .groupby("z", as_index=False)["abs_sensitivity"]
        .sum()
        .rename(columns={"abs_sensitivity": "expansion_sum"})
    )

    rz = growth_sum.merge(exp_sum, on="z", how="outer").fillna(0.0).sort_values("z")
    rz["R"] = rz["growth_sum"] / (rz["expansion_sum"] + float(eps))
    return rz


def classify_regime(
    dominance_df: pd.DataFrame,
    threshold: float = 1.2,
    use_inverse_threshold: bool = True,
) -> pd.DataFrame:
    """Classifica regime por ``z``.

    Regras default:
      - ``growth_dominated`` se ``R > threshold``;
      - ``expansion_dominated`` se ``R < 1/threshold`` (quando ``use_inverse_threshold=True``);
      - ``balanced`` caso contrário.
    """
    inv = 1.0 / float(threshold) if use_inverse_threshold else float(threshold)

    out = dominance_df.copy()
    out["dominant_regime"] = "balanced"
    out.loc[out["R"] > float(threshold), "dominant_regime"] = "growth_dominated"
    out.loc[out["R"] < inv, "dominant_regime"] = "expansion_dominated"
    return out


def _default_bins(z_values: np.ndarray, n_bins: int = 6) -> np.ndarray:
    zmin = float(np.min(z_values))
    zmax = float(np.max(z_values))
    if n_bins < 1:
        raise ValueError("n_bins deve ser >= 1")
    if zmax <= zmin:
        return np.array([zmin, zmin + 1.0], dtype=float)
    return np.linspace(zmin, zmax, n_bins + 1)


def compute_degeneracy_by_bin(
    sensitivity_df: pd.DataFrame,
    bins: Optional[Sequence[float]] = None,
    n_bins: int = 6,
) -> Dict[str, pd.DataFrame]:
    """Calcula matriz de correlação entre vetores de sensibilidade por parâmetro em cada bin de z."""
    df = sensitivity_df.copy()
    if df.empty:
        return {}

    z_vals = df["z"].to_numpy(dtype=float)
    edges = np.asarray(bins, dtype=float) if bins is not None else _default_bins(z_vals, n_bins=n_bins)

    out: Dict[str, pd.DataFrame] = {}
    for i in range(len(edges) - 1):
        z0 = float(edges[i])
        z1 = float(edges[i + 1])
        m = (df["z"] >= z0) & (df["z"] < z1 if i < len(edges) - 2 else df["z"] <= z1)
        bdf = df[m].copy()
        if bdf.empty:
            continue

        pivot = (
            bdf.pivot_table(index=["observable", "z"], columns="parameter", values="sensitivity", aggfunc="mean")
            .sort_index()
            .fillna(0.0)
        )
        corr = pivot.corr()
        out[f"bin_{i:02d}"] = corr
    return out


def plot_sensitivity_curves(sensitivity_df: pd.DataFrame, output_path: str) -> None:
    """Plota curvas de sensibilidade por parâmetro/observável versus z."""
    fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)
    observables = ["Hz", "fσ8"]

    for ax, obs in zip(axes, observables):
        sdf = sensitivity_df[sensitivity_df["observable"] == obs]
        for pname, g in sdf.groupby("parameter"):
            g = g.sort_values("z")
            ax.plot(g["z"], g["sensitivity"], label=pname, linewidth=1.6)
        ax.set_ylabel(f"d{obs}/dp")
        ax.set_title(f"Sensibilidade - {obs}")
        ax.grid(alpha=0.2)
        ax.legend(loc="best", fontsize=8)

    axes[-1].set_xlabel("z")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def plot_degeneracy_heatmaps(corr_by_bin: Dict[str, pd.DataFrame], output_dir: str) -> List[str]:
    """Gera heatmap (matriz de correlação) por bin de redshift."""
    paths: List[str] = []
    for bin_name, corr in corr_by_bin.items():
        fig, ax = plt.subplots(figsize=(7, 6))
        cax = ax.imshow(corr.values, vmin=-1.0, vmax=1.0, cmap="coolwarm")
        ax.set_xticks(np.arange(corr.shape[1]))
        ax.set_yticks(np.arange(corr.shape[0]))
        ax.set_xticklabels(corr.columns, rotation=45, ha="right")
        ax.set_yticklabels(corr.index)
        ax.set_title(f"Degenerescência ({bin_name})")
        fig.colorbar(cax, ax=ax, label="corr")
        fig.tight_layout()

        path = os.path.join(output_dir, f"degeneracy_heatmap_{bin_name}.png")
        fig.savefig(path, dpi=180)
        plt.close(fig)
        paths.append(path)
    return paths


def plot_regime_curve(classified_df: pd.DataFrame, output_path: str, threshold: float = 1.2) -> None:
    """Plota curva ``R(z)`` com faixas de regime."""
    df = classified_df.sort_values("z")
    inv = 1.0 / float(threshold)

    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.plot(df["z"], df["R"], color="black", linewidth=2.0, label="R(z)")
    ax.axhline(float(threshold), color="tab:green", linestyle="--", linewidth=1.2)
    ax.axhline(inv, color="tab:blue", linestyle="--", linewidth=1.2)

    ax.fill_between(df["z"], float(threshold), np.maximum(df["R"].max(), float(threshold) * 1.05), color="tab:green", alpha=0.14)
    ax.fill_between(df["z"], 0.0, inv, color="tab:blue", alpha=0.14)
    ax.fill_between(df["z"], inv, float(threshold), color="gray", alpha=0.10)

    ax.set_ylim(bottom=0.0)
    ax.set_xlabel("z")
    ax.set_ylabel("R(z)")
    ax.set_title("Métrica de dominância crescimento/expansão")
    ax.grid(alpha=0.2)
    ax.legend(loc="best")
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def _top_parameters_in_bin(bin_df: pd.DataFrame, top_n: int = 3) -> str:
    scores = (
        bin_df.groupby("parameter", as_index=False)["abs_sensitivity"].mean().sort_values("abs_sensitivity", ascending=False)
    )
    top = scores.head(top_n)["parameter"].tolist()
    return ";".join(top)


def build_regime_summary(
    classified_df: pd.DataFrame,
    sensitivity_df: pd.DataFrame,
    bins: Optional[Sequence[float]] = None,
    n_bins: int = 6,
) -> pd.DataFrame:
    """Monta resumo por bin com ``z_min``, ``z_max``, ``R_mean``, regime dominante e parâmetros-chave."""
    z_vals = classified_df["z"].to_numpy(dtype=float)
    edges = np.asarray(bins, dtype=float) if bins is not None else _default_bins(z_vals, n_bins=n_bins)

    rows = []
    for i in range(len(edges) - 1):
        z0 = float(edges[i])
        z1 = float(edges[i + 1])
        m_r = (classified_df["z"] >= z0) & (classified_df["z"] < z1 if i < len(edges) - 2 else classified_df["z"] <= z1)
        m_s = (sensitivity_df["z"] >= z0) & (sensitivity_df["z"] < z1 if i < len(edges) - 2 else sensitivity_df["z"] <= z1)

        b_r = classified_df[m_r]
        b_s = sensitivity_df[m_s]
        if b_r.empty:
            continue

        mode = b_r["dominant_regime"].mode()
        dominant = str(mode.iloc[0]) if not mode.empty else "balanced"
        rows.append(
            {
                "z_min": z0,
                "z_max": z1,
                "R_mean": float(b_r["R"].mean()),
                "dominant_regime": dominant,
                "top_parameters": _top_parameters_in_bin(b_s, top_n=3) if not b_s.empty else "",
                "notes": "inverse-threshold classification" if np.isfinite(z0) else "",
            }
        )
    return pd.DataFrame(rows)


def run_reporting_pipeline(
    params: Dict[str, float],
    hz_data: Optional[Union[str, pd.DataFrame]] = None,
    fs8_data: Optional[Union[str, pd.DataFrame]] = None,
    grid_mode: str = "union",
    z_min: float = 0.0,
    z_max: float = 2.5,
    n_points: int = 300,
    threshold: float = 1.2,
    bins: Optional[Sequence[float]] = None,
    n_bins: int = 6,
    step_eps: float = 1e-4,
    metric_eps: float = 1e-12,
) -> Dict[str, str]:
    """Executa fluxo completo de reporting e persiste artefatos versionáveis.

    Arquivos principais gerados em ``results/structure_d``:
      - ``rll_regime_summary.csv``;
      - ``sensitivity_long.csv`` (auxiliar);
      - ``dominance_by_z.csv`` (auxiliar);
      - ``degeneracy_corr_<bin>.csv`` (auxiliar).

    Figuras geradas em ``results/structure_d/figs``:
      - ``sensitivity_curves.png``;
      - ``degeneracy_heatmap_<bin>.png``;
      - ``dominance_regime_curve.png``.
    """
    os.makedirs(RESULTS_DIR, exist_ok=True)
    os.makedirs(FIGS_DIR, exist_ok=True)

    z_grid = build_redshift_grid(
        hz_data=hz_data,
        fs8_data=fs8_data,
        mode=grid_mode,
        z_min=z_min,
        z_max=z_max,
        n_points=n_points,
    )

    sensitivity_df, _ = compute_parameter_sensitivities(
        z_grid=z_grid,
        params=params,
        step_eps=step_eps,
        deriv_eps=metric_eps,
    )

    dominance_df = compute_dominance_metric(sensitivity_df, eps=metric_eps)
    classified_df = classify_regime(dominance_df, threshold=threshold, use_inverse_threshold=True)
    corr_by_bin = compute_degeneracy_by_bin(sensitivity_df, bins=bins, n_bins=n_bins)
    summary_df = build_regime_summary(classified_df, sensitivity_df, bins=bins, n_bins=n_bins)

    sensitivity_csv = os.path.join(RESULTS_DIR, "sensitivity_long.csv")
    dominance_csv = os.path.join(RESULTS_DIR, "dominance_by_z.csv")
    summary_csv = os.path.join(RESULTS_DIR, "rll_regime_summary.csv")

    sensitivity_df.to_csv(sensitivity_csv, index=False)
    classified_df.to_csv(dominance_csv, index=False)
    summary_df.to_csv(summary_csv, index=False)

    corr_csv_paths = []
    for bin_name, corr_df in corr_by_bin.items():
        path = os.path.join(RESULTS_DIR, f"degeneracy_corr_{bin_name}.csv")
        corr_df.to_csv(path, index=True)
        corr_csv_paths.append(path)

    sensitivity_fig = os.path.join(FIGS_DIR, "sensitivity_curves.png")
    regime_fig = os.path.join(FIGS_DIR, "dominance_regime_curve.png")

    plot_sensitivity_curves(sensitivity_df, sensitivity_fig)
    heatmaps = plot_degeneracy_heatmaps(corr_by_bin, FIGS_DIR)
    plot_regime_curve(classified_df, regime_fig, threshold=threshold)

    return {
        "summary_csv": summary_csv,
        "sensitivity_csv": sensitivity_csv,
        "dominance_csv": dominance_csv,
        "sensitivity_fig": sensitivity_fig,
        "regime_fig": regime_fig,
        "heatmaps": ";".join(heatmaps),
        "degeneracy_csvs": ";".join(corr_csv_paths),
    }
