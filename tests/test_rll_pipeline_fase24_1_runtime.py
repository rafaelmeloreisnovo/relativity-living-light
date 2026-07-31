from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "tools" / "rll_pipeline_fase24_1_runtime.py"


def load_runtime():
    spec = importlib.util.spec_from_file_location("rll_pipeline_fase24_1_runtime_test", MODULE_PATH)
    assert spec is not None and spec.loader is not None
    runtime = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = runtime
    spec.loader.exec_module(runtime)
    runtime.install()
    return runtime


def step(runtime, number: int):
    return next(item for item in runtime.core.STEPS if item.number == number)


def test_stale_paths_are_aligned_to_live_workflows() -> None:
    runtime = load_runtime()
    assert step(runtime, 7).commands[0].argv[-1] == "tools/docs_inventory.py"
    assert step(runtime, 9).commands[0].argv[-1] == "tools/verify_real_source_signatures.py"
    assert step(runtime, 11).commands[0].argv[-1] == "scripts/data_scan/build_raw_data_manifest_status.py"
    assert step(runtime, 12).commands[0].argv[-1] == "scripts/data_scan/build_real_seed_ingestion_plan.py"


def test_cli_contract_drift_is_removed() -> None:
    runtime = load_runtime()
    assert "--desi-only" not in step(runtime, 15).commands[0].argv
    assert "--output-dir" in step(runtime, 15).commands[0].argv
    assert "--bayes-factor" not in step(runtime, 22).candidates[0].argv
    assert "--output" in step(runtime, 29).commands[0].argv


def test_bayesian_jobs_use_real_profile() -> None:
    runtime = load_runtime()
    inference = step(runtime, 21).candidates[0].argv
    proxy = step(runtime, 22).candidates[0].argv
    assert inference[inference.index("--profile") + 1] == "structure_d_real_validation"
    assert inference[inference.index("--bayes-mode") + 1] == "inference"
    assert proxy[proxy.index("--profile") + 1] == "structure_d_real_validation"
    assert proxy[proxy.index("--bayes-mode") + 1] == "bic_proxy"


def test_failed_falsifier_blocks_science_gate() -> None:
    runtime = load_runtime()
    contract = {"falsifiers": [{"id": "F-COS-04", "state": "VERIFIED", "outcome": "FAIL"}]}
    decision = runtime.gate_decision("completo", [], contract)
    assert decision["status"] == "BLOCKED"
    assert decision["falsifier_failures"] == ["F-COS-04"]
    assert decision["claim_allowed"] is False


def test_json_and_csv_metrics_use_current_run_files(tmp_path, monkeypatch) -> None:
    runtime = load_runtime()
    monkeypatch.setattr(runtime, "ROOT", tmp_path)
    nested = tmp_path / "nested.json"
    nested.write_text(json.dumps({"assessment": {"best": {"zt_bao": 0.9}}}), encoding="utf-8")
    table = tmp_path / "bayes.csv"
    table.write_text("model,log_bayes_factor\nRLL,-6.19\n", encoding="utf-8")
    assert runtime.find_json_metric((("nested.json", ("assessment.best.zt_bao",)),))["value"] == 0.9
    assert runtime.find_csv_metric((("bayes.csv", ("log_bayes_factor",)),))["value"] == -6.19


def test_balance_input_is_materialized_from_real_structure_d(tmp_path, monkeypatch) -> None:
    runtime = load_runtime()
    source = tmp_path / "results" / "structure_d" / "model_comparison_real.csv"
    target_root = tmp_path / "artifacts" / "linear" / "current_run"
    source.parent.mkdir(parents=True)
    target_root.mkdir(parents=True)
    source.write_text("model,chi2,AIC,BIC\nlcdm,10,14,18\nrll_like,11,17,23\n", encoding="utf-8")
    monkeypatch.setattr(runtime, "ROOT", tmp_path)
    monkeypatch.setattr(runtime, "CURRENT_RUN", target_root)
    assert runtime.materialize_balance_input() == 0
    payload = json.loads((target_root / "structure_d_real_metrics.json").read_text(encoding="utf-8"))
    assert payload["claim_allowed"] is False
    assert payload["models"][1]["model"] == "RLL"
