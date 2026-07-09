from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools import bootstrap_failsafe as bf
from tools import rll_json_watcher as watcher


@pytest.fixture()
def isolated_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    (tmp_path / "data" / "real").mkdir(parents=True)
    (tmp_path / "data" / "real" / "fixture_source.csv").write_text("z,H_obs\n0.1,69.0\n", encoding="utf-8")

    for mod in (bf, watcher):
        monkeypatch.setattr(mod, "ROOT", tmp_path, raising=False)
        monkeypatch.setattr(mod, "FAILSAFE_DIR", tmp_path / "data" / "failsafe", raising=False)
        monkeypatch.setattr(mod, "FINGERPRINT_DIR", tmp_path / "schemas" / "fingerprints", raising=False)
    monkeypatch.setattr(bf, "TRAIL_PATH", tmp_path / "artifacts" / "EVOLUTION_TRAIL.jsonl")
    monkeypatch.setattr(bf, "MANIFEST_PATH", tmp_path / "results" / "evolution_watcher_manifest.json")
    return tmp_path


def _config() -> dict:
    return {
        "meta": {"purpose": "test"},
        "schema_fingerprints": {"algorithm": "sha256"},
        "sources": [
            {
                "id": "fixture_source",
                "label": "fixture",
                "local_paths": ["data/real/fixture_source.csv"],
                "epistemic_initial": "VERIFIED",
                "rll_paths_affected": ["C05_hubble_tension_evolving_de"],
            }
        ],
        "global_failover": {},
        "rollback_global": {},
        "artifact_evolution_trail": {},
    }


def _events() -> list[dict]:
    return [json.loads(line) for line in bf.TRAIL_PATH.read_text(encoding="utf-8").splitlines()]


def test_watch_one_fetches_when_no_prior_fingerprint(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = config["sources"][0]

    result = watcher.watch_one(source, schema, manifest, dry_run=False)

    assert result["status"] == "FETCH"
    events = _events()
    assert events[-1]["action"] == "FETCH"
    assert events[-1]["schema_drift"] is False
    assert events[-1]["epistemic_after"] == "VERIFIED"


def test_watch_one_skips_when_unchanged(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = config["sources"][0]

    watcher.watch_one(source, schema, manifest, dry_run=False)
    result = watcher.watch_one(source, schema, manifest, dry_run=False)

    assert result["status"] == "SKIP_EXISTING"
    assert _events()[-1]["schema_drift"] is False


def test_watch_one_detects_drift_and_flags_update(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = config["sources"][0]

    watcher.watch_one(source, schema, manifest, dry_run=False)
    (isolated_repo / "data" / "real" / "fixture_source.csv").write_text("z,H_obs\n0.1,70.0\n", encoding="utf-8")
    result = watcher.watch_one(source, schema, manifest, dry_run=False)

    assert result["status"] == "UPDATE"
    assert result["schema_drift"] is True
    event = _events()[-1]
    assert event["action"] == "UPDATE"
    assert event["schema_drift"] is True
    assert event["fingerprint_before"] != event["fingerprint_after"]


def test_watch_one_reports_failsafe_when_file_missing(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = config["sources"][0]

    watcher.watch_one(source, schema, manifest, dry_run=False)
    (isolated_repo / "data" / "real" / "fixture_source.csv").unlink()
    result = watcher.watch_one(source, schema, manifest, dry_run=False)

    assert result["status"] == "FAILSAFE"
    event = _events()[-1]
    assert event["action"] == "FAILSAFE"
    assert event["epistemic_after"] == "TOKEN_VAZIO"


def test_rollback_restores_state_but_never_promotes_to_verified(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = config["sources"][0]

    bf.bootstrap_one(source, schema, manifest, force=False, dry_run=False)
    (isolated_repo / "data" / "real" / "fixture_source.csv").write_text("z,H_obs\n0.1,99.0\n", encoding="utf-8")
    watcher.watch_one(source, schema, manifest, dry_run=False)

    result = watcher.rollback_one(source, schema, manifest, dry_run=False)

    assert result["status"] == "ROLLBACK"
    assert result["epistemic_after"] != "VERIFIED"
    event = _events()[-1]
    assert event["action"] == "ROLLBACK"
    assert event["epistemic_after"] != "VERIFIED"


def test_rollback_without_checkpoint_reports_no_checkpoint(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = config["sources"][0]

    result = watcher.rollback_one(source, schema, manifest, dry_run=False)

    assert result["status"] == "no_checkpoint_to_rollback_to"


def test_dry_run_does_not_mutate_manifest_or_fingerprint(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = config["sources"][0]

    watcher.watch_one(source, schema, manifest, dry_run=True)

    assert not bf.TRAIL_PATH.exists()
    assert not (bf.FINGERPRINT_DIR / "fixture_source.sha256").exists()


def test_main_end_to_end_via_config_file(isolated_repo: Path, tmp_path: Path) -> None:
    import yaml

    bf.bootstrap_one(_config()["sources"][0], bf.load_event_schema(), bf.load_manifest(), force=False, dry_run=False)

    config_path = tmp_path / "config.yml"
    config_path.write_text(yaml.safe_dump(_config()), encoding="utf-8")

    rc = watcher.main(["--config", str(config_path), "--emit-summary"])

    assert rc == 0
    manifest = json.loads(bf.MANIFEST_PATH.read_text(encoding="utf-8"))
    assert manifest["sources"]["fixture_source"]["last_action"] == "SKIP_EXISTING"
