import argparse
import json
import os

import numpy as np
import pandas as pd

from .data_access import load_active_datasets, load_run_config
from .likelihood import aic, bic, chi2, chi2_with_covariance, evaluate_model, estimate_log_evidence, write_bayes_factor_interpretation
from .models import model_LCDM_Hz, model_LCDM_fs8, model_RLL_like_Hz, model_RLL_like_fs8
from .reporting import run_reporting_pipeline

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
RESULTS = os.path.join(BASE_DIR, "results", "structure_d")
DEFAULT_CONFIG = os.path.join("data", "pipelines", "structure_d", "datasets_config.json")
DEFAULT_PROFILE = "structure_d_default"

REQUIRED_OUTPUTS = [
    "model_comparison.csv",
    "covariance_usage.csv",
    "rll_regime_summary.csv",
    "reproduction_contract.json",
]
OPTIONAL_OUTPUTS = {
    "bayes_evidence.csv": "optional Bayesian summary; generated only when --bayes is used",
    "bayes_factor_interpretation.csv": "optional Bayesian interpretation table; generated only when --bayes is used",
}

EXPECTED_SCHEMA_BY_OUTPUT = {
    "model_comparison.csv": [
        "model",
        "chi2",
        "AIC",
        "BIC",
        "N",
        "k",
        "datasets_used",
        "run_name",
        "profile_name",
        "covariance_policy",
    ],
    "covariance_usage.csv": [
        "dataset_id",
        "block",
        "covariance_mode",
        "has_full_covariance",
        "has_diagonal_sigma",
    ],
}


MODEL_BY_DATASET = {
    "hz": (model_LCDM_Hz, model_RLL_like_Hz),
    "fsigma8": (model_LCDM_fs8, model_RLL_like_fs8),
}


def _dataset_block_name(dataset_id, entry):
    observable = str(entry.get("observable", dataset_id)).lower()
    if dataset_id in {"hz", "real_hz"} or "hz" in observable:
        return "Hz"
    if dataset_id in {"fsigma8"} or "fs" in observable:
        return "fσ8"
    if "bao" in observable:
        return "BAO"
    if "sne" in observable:
        return "SNe"
    if "lens" in observable:
        return "lenses"
    return str(entry.get("observable", dataset_id))


def _apply_covariance_policy(datasets, covariance_policy):
    for entry in datasets.values():
        if covariance_policy == "diagonal_only" and entry.get("covariance") is not None:
            entry["errors"] = np.sqrt(np.diag(np.asarray(entry["covariance"], dtype=float)))
            entry["covariance"] = None
    return covariance_policy


def _chi2_from_entry(entry, model_values):
    if entry.get("errors") is not None:
        return chi2(entry["values"], model_values, entry["errors"])
    return chi2_with_covariance(entry["values"], model_values, entry["covariance"])


def run_classic_metrics(cfg_meta, datasets, covariance_policy):
    lcdm = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55)
    rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)

    rows = []
    cov_rows = []
    chi2_lcdm = 0.0
    chi2_rll = 0.0
    n_obs = 0

    for dataset_id in cfg_meta["active_datasets"]:
        entry = datasets[dataset_id]
        cov_rows.append(
            {
                "dataset_id": dataset_id,
                "block": _dataset_block_name(dataset_id, entry),
                "covariance_mode": "full" if entry.get("covariance") is not None else "diagonal",
                "has_full_covariance": bool(entry.get("covariance") is not None),
                "has_diagonal_sigma": bool(entry.get("errors") is not None),
            }
        )

        model_pair = MODEL_BY_DATASET.get(dataset_id)
        if model_pair is None or entry.get("z") is None:
            continue

        model_lcdm, model_rll = model_pair
        z = np.asarray(entry["z"], dtype=float)
        chi2_lcdm += _chi2_from_entry(entry, model_lcdm(z, lcdm))
        chi2_rll += _chi2_from_entry(entry, model_rll(z, rll))
        n_obs += len(entry["values"])

    if n_obs == 0:
        raise ValueError("no supported datasets (hz/fsigma8) were active for classical metrics")

    rows.append(
        {
            "model": "LCDM",
            "chi2": float(chi2_lcdm),
            "AIC": aic(chi2_lcdm, 4),
            "BIC": bic(chi2_lcdm, 4, n_obs),
            "N": int(n_obs),
            "k": 4,
            "datasets_used": ",".join(cfg_meta["active_datasets"]),
            "run_name": cfg_meta.get("run_name", "unknown"),
            "profile_name": cfg_meta.get("profile_name", DEFAULT_PROFILE),
            "covariance_policy": covariance_policy,
        }
    )
    rows.append(
        {
            "model": "RLL_like+AGN",
            "chi2": float(chi2_rll),
            "AIC": aic(chi2_rll, 7),
            "BIC": bic(chi2_rll, 7, n_obs),
            "N": int(n_obs),
            "k": 7,
            "datasets_used": ",".join(cfg_meta["active_datasets"]),
            "run_name": cfg_meta.get("run_name", "unknown"),
            "profile_name": cfg_meta.get("profile_name", DEFAULT_PROFILE),
            "covariance_policy": covariance_policy,
        }
    )

    out_model = os.path.join(RESULTS, "model_comparison.csv")
    out_cov = os.path.join(RESULTS, "covariance_usage.csv")
    evaluate_model(rows, out_model)
    evaluate_model(cov_rows, out_cov)
    return pd.DataFrame(rows), out_model, out_cov


def run_optional_bayes_summary(df_model):
    rows = []
    for _, row in df_model.iterrows():
        logz, logz_err = estimate_log_evidence(bic_value=float(row["BIC"]))
        rows.append(
            {
                "model": row["model"],
                "log_evidence": logz,
                "log_evidence_std": logz_err,
                "source": "bic_proxy",
            }
        )

    out_evidence = os.path.join(RESULTS, "bayes_evidence.csv")
    out_interp = os.path.join(RESULTS, "bayes_factor_interpretation.csv")
    evaluate_model(rows, out_evidence)
    write_bayes_factor_interpretation(out_interp)
    return [out_evidence, out_interp]


def _write_reproduction_contract(profile_name, covariance_policy, bayes, produced_optional):
    contract = {
        "command": "python -m data.pipelines.structure_d.run_all",
        "profile": profile_name,
        "covariance_policy": covariance_policy,
        "required_outputs": REQUIRED_OUTPUTS,
        "optional_outputs": [
            {
                "file": name,
                "produced": name in produced_optional,
                "reason": reason,
            }
            for name, reason in OPTIONAL_OUTPUTS.items()
        ],
        "bayes_enabled": bool(bayes),
    }
    out_contract = os.path.join(RESULTS, "reproduction_contract.json")
    with open(out_contract, "w", encoding="utf-8") as fp:
        json.dump(contract, fp, ensure_ascii=False, indent=2)
    return out_contract


def _assert_required_outputs():
    missing = []
    for filename in REQUIRED_OUTPUTS:
        path = os.path.join(RESULTS, filename)
        if not os.path.exists(path):
            missing.append(filename)
    if missing:
        raise RuntimeError(f"required outputs were not generated: {missing}")


def _validate_output_schema(filename, expected_header):
    path = os.path.join(RESULTS, filename)
    actual_header = list(pd.read_csv(path, nrows=0).columns)
    if actual_header != expected_header:
        raise RuntimeError(
            f"schema mismatch for {filename}: expected {expected_header}, got {actual_header}"
        )


def main(config_path=DEFAULT_CONFIG, profile_name=DEFAULT_PROFILE, covariance_policy=None, bayes=False):
    os.makedirs(RESULTS, exist_ok=True)

    cfg = load_run_config(config_path)
    cfg_meta, datasets = load_active_datasets(config_path, profile_name=profile_name)
    effective_profile = cfg_meta.get("profile_name") or cfg.get("default_profile", DEFAULT_PROFILE)
    effective_policy = _apply_covariance_policy(datasets, covariance_policy or cfg.get("covariance_policy", "prefer_full"))

    df_model, out_model, out_cov = run_classic_metrics(cfg_meta, datasets, effective_policy)

    hz = datasets.get("hz")
    fs8 = datasets.get("fsigma8")
    if hz is not None and fs8 is not None:
        hz_df = pd.DataFrame({"z": hz["z"], "Hz": hz["values"], "sigma": hz["errors"]})
        fs8_df = pd.DataFrame({"z": fs8["z"], "fs8": fs8["values"], "sigma": fs8["errors"]})
        rll = dict(H0=70.0, Om=0.3, Ol=0.7, sigma8=0.8, gamma=0.55, alpha=0.06, z_peak=2.0, width=1.2, beta=0.00)
        run_reporting_pipeline(params=rll, hz_data=hz_df, fs8_data=fs8_df)

    produced_optional = []
    if bayes:
        for path in run_optional_bayes_summary(df_model):
            produced_optional.append(os.path.basename(path))

    out_contract = _write_reproduction_contract(effective_profile, effective_policy, bayes, produced_optional)
    _assert_required_outputs()
    for filename, expected_header in EXPECTED_SCHEMA_BY_OUTPUT.items():
        _validate_output_schema(filename, expected_header)

    print(df_model.to_string(index=False))
    print(f"[classic] wrote: {out_model}")
    print(f"[classic] wrote: {out_cov}")
    print(f"[classic] wrote: {os.path.join(RESULTS, 'rll_regime_summary.csv')}")
    print(f"[classic] wrote: {out_contract}")
    if bayes:
        for name in produced_optional:
            print(f"[bayes] wrote: {os.path.join(RESULTS, name)}")


def _build_parser():
    parser = argparse.ArgumentParser(description="Executa o pipeline structure_d")
    parser.add_argument("--config", default=DEFAULT_CONFIG)
    parser.add_argument("--profile", default=os.environ.get("STRUCTURE_D_PROFILE", DEFAULT_PROFILE))
    parser.add_argument("--covariance-policy", default=None, choices=["prefer_full", "diagonal_only", "full_required"])
    parser.add_argument("--bayes", action="store_true", help="Gera artefatos bayesianos opcionais")
    return parser


if __name__ == "__main__":
    args = _build_parser().parse_args()
    main(config_path=args.config, profile_name=args.profile, covariance_policy=args.covariance_policy, bayes=args.bayes)
