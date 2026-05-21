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
    return {
        "pipeline": summary.get("pipeline", "pantheon_oficial_prova_observacional"),
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "source_summary": str(PANTHEON_SUMMARY_JSON.relative_to(ROOT)),
        "n_obs": summary["n_obs"],
        "rll": {
            "chi2": summary["rll"]["chi2"],
            "AIC": summary["rll"]["AIC"],
            "BIC": summary["rll"]["BIC"],
            "best_fit": summary["rll"].get("best_fit", {}),
            "n_params": 5,
        },
        "lcdm": {
            "chi2": summary["lcdm"]["chi2"],
            "AIC": summary["lcdm"]["AIC"],
            "BIC": summary["lcdm"]["BIC"],
            "best_fit": summary["lcdm"].get("best_fit", {}),
            "n_params": 2,
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
