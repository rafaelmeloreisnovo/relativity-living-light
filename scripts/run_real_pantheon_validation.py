from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_RESULTS = ROOT / "data" / "results"
MODEL_COMPARISON_JSON = DATA_RESULTS / "model_comparison.json"
PANTHEON_SUMMARY_JSON = DATA_RESULTS / "pantheon_fit_summary.json"


def _run(cmd: list[str], env: dict[str, str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, check=False, env=env)


def _normalize_model_comparison(summary: dict) -> dict:
    source = str(PANTHEON_SUMMARY_JSON.relative_to(ROOT))
    rll = summary.get("rll", {})
    lcdm = summary.get("lcdm", {})

    def _metric(model_block: dict, *keys: str) -> float | None:
        for key in keys:
            if key in model_block:
                return model_block[key]
        return None

    rll_chi2 = _metric(rll, "chi2")
    lcdm_chi2 = _metric(lcdm, "chi2")
    rll_aic = _metric(rll, "aic", "AIC")
    lcdm_aic = _metric(lcdm, "aic", "AIC")
    rll_bic = _metric(rll, "bic", "BIC")
    lcdm_bic = _metric(lcdm, "bic", "BIC")

    return {
        "pipeline": summary.get("pipeline", "pantheon_oficial_prova_observacional"),
        "dataset": summary.get("dataset", "pantheon+"),
        "generated_at": summary.get("generated_at") or summary.get("timestamp_utc") or datetime.now(timezone.utc).isoformat(),
        "source": source,
        "source_summary": source,
        "n_obs": summary.get("n_obs"),
        "covariance_used": True,
        "models": {
            "rll": {
                "k_params": 5,
                "chi2": rll_chi2,
                "aic": rll_aic,
                "bic": rll_bic,
                "log_likelihood": _metric(rll, "log_likelihood"),
                "best_fit_params": rll.get("best_fit_params", rll.get("best_fit")),
            },
            "lcdm": {
                "k_params": 2,
                "chi2": lcdm_chi2,
                "aic": lcdm_aic,
                "bic": lcdm_bic,
                "log_likelihood": _metric(lcdm, "log_likelihood"),
                "best_fit_params": lcdm.get("best_fit_params", lcdm.get("best_fit")),
            },
        },
        "delta": {
            "delta_chi2_rll_minus_lcdm": (rll_chi2 - lcdm_chi2) if (rll_chi2 is not None and lcdm_chi2 is not None) else None,
            "delta_aic_rll_minus_lcdm": (rll_aic - lcdm_aic) if (rll_aic is not None and lcdm_aic is not None) else None,
            "delta_bic_rll_minus_lcdm": (rll_bic - lcdm_bic) if (rll_bic is not None and lcdm_bic is not None) else None,
            "interpretation_guardrail": "Quantitative comparison only; do not infer model superiority from these deltas alone.",
            "claim_boundary": "No superiority claim unless real-data metrics pass predefined thresholds.",
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Run minimal real Pantheon+ validation and emit auditable model_comparison.json")
    parser.add_argument("--skip-verify", action="store_true", help="Skip verify_pantheon_inputs step")
    parser.add_argument("--skip-preflight", action="store_true", help="Skip rll preflight-real step")
    args = parser.parse_args()

    env = os.environ.copy()
    env["PYTHONPATH"] = str(ROOT / "src")

    steps: list[tuple[str, list[str]]] = []
    if not args.skip_verify:
        steps.append(("verify", [sys.executable, "scripts/verify_pantheon_inputs.py", "--json"]))
    if not args.skip_preflight:
        steps.append(("preflight", [sys.executable, "-m", "rll.cli", "preflight-real", "--json"]))
    steps.append(("run_real", [sys.executable, "-m", "rll.cli", "run", "--data", "real", "--model", "both", "--with-covariance"]))

    for label, cmd in steps:
        completed = _run(cmd, env)
        if completed.returncode != 0:
            sys.stderr.write(f"[rll-real-validation] step={label} failed with code {completed.returncode}\n")
            sys.stderr.write(completed.stdout)
            sys.stderr.write(completed.stderr)
            raise SystemExit(completed.returncode)

    if not PANTHEON_SUMMARY_JSON.exists():
        raise FileNotFoundError(
            f"Expected summary not found: {PANTHEON_SUMMARY_JSON}. "
            "Real pipeline did not produce the required artifact."
        )

    summary = json.loads(PANTHEON_SUMMARY_JSON.read_text(encoding="utf-8"))
    normalized = _normalize_model_comparison(summary)
    DATA_RESULTS.mkdir(parents=True, exist_ok=True)
    MODEL_COMPARISON_JSON.write_text(json.dumps(normalized, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"[rll-real-validation] wrote {MODEL_COMPARISON_JSON}")


if __name__ == "__main__":
    main()
