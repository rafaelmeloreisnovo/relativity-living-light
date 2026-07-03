from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools import bootstrap_failsafe as bf


@pytest.fixture()
def isolated_repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    (tmp_path / "data" / "real").mkdir(parents=True)
    (tmp_path / "data" / "real" / "fixture_source.csv").write_text("z,H_obs\n0.1,69.0\n", encoding="utf-8")

    monkeypatch.setattr(bf, "ROOT", tmp_path)
    monkeypatch.setattr(bf, "TRAIL_PATH", tmp_path / "artifacts" / "EVOLUTION_TRAIL.jsonl")
    monkeypatch.setattr(bf, "MANIFEST_PATH", tmp_path / "results" / "evolution_watcher_manifest.json")
    monkeypatch.setattr(bf, "FAILSAFE_DIR", tmp_path / "data" / "failsafe")
    monkeypatch.setattr(bf, "FINGERPRINT_DIR", tmp_path / "schemas" / "fingerprints")
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
                "rll_paths_affected": [],
            },
            {"id": "_template_nova_fonte", "template_only": True},
        ],
        "global_failover": {},
        "rollback_global": {},
        "artifact_evolution_trail": {},
    }


def test_load_config_requires_all_sections(tmp_path: Path) -> None:
    import yaml

    incomplete = tmp_path / "incomplete.yml"
    incomplete.write_text(yaml.safe_dump({"meta": {}}), encoding="utf-8")

    with pytest.raises(SystemExit):
        bf.load_config(incomplete)


def test_real_sources_excludes_template() -> None:
    sources = bf.real_sources(_config())
    assert [s["id"] for s in sources] == ["fixture_source"]


def test_fingerprint_source_is_stable_and_sensitive_to_content(isolated_repo: Path) -> None:
    fp1, files1 = bf.fingerprint_source(isolated_repo, ["data/real/fixture_source.csv"])
    fp2, _ = bf.fingerprint_source(isolated_repo, ["data/real/fixture_source.csv"])
    assert fp1 == fp2
    assert len(files1) == 1
    assert files1[0]["path"] == "data/real/fixture_source.csv"

    (isolated_repo / "data" / "real" / "fixture_source.csv").write_text("z,H_obs\n0.1,70.0\n", encoding="utf-8")
    fp3, _ = bf.fingerprint_source(isolated_repo, ["data/real/fixture_source.csv"])
    assert fp3 != fp1


def test_fingerprint_source_missing_file_raises(isolated_repo: Path) -> None:
    with pytest.raises(SystemExit):
        bf.fingerprint_source(isolated_repo, ["data/real/does_not_exist.csv"])


def test_bootstrap_one_writes_failsafe_snapshot_and_valid_trail_event(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = bf.real_sources(config)[0]

    result = bf.bootstrap_one(source, schema, manifest, force=False, dry_run=False)

    assert result["status"] == "bootstrapped"
    failsafe_path = bf.FAILSAFE_DIR / "fixture_source_FROZEN.json"
    fingerprint_path = bf.FINGERPRINT_DIR / "fixture_source.sha256"
    assert failsafe_path.exists()
    assert fingerprint_path.exists()

    snapshot = json.loads(failsafe_path.read_text(encoding="utf-8"))
    assert snapshot["source_id"] == "fixture_source"
    assert snapshot["epistemic_state"] == "VERIFIED"

    assert bf.TRAIL_PATH.exists()
    events = [json.loads(line) for line in bf.TRAIL_PATH.read_text(encoding="utf-8").splitlines()]
    assert len(events) == 1
    assert events[0]["action"] == "BOOTSTRAP"
    assert events[0]["source_id"] == "fixture_source"
    assert events[0]["epistemic_after"] == "VERIFIED"


def test_bootstrap_one_skips_when_already_bootstrapped_without_force(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = bf.real_sources(config)[0]

    bf.bootstrap_one(source, schema, manifest, force=False, dry_run=False)
    second = bf.bootstrap_one(source, schema, manifest, force=False, dry_run=False)

    assert second["status"] == "already_bootstrapped"
    events = bf.TRAIL_PATH.read_text(encoding="utf-8").splitlines()
    assert len(events) == 1


def test_bootstrap_one_dry_run_writes_nothing(isolated_repo: Path) -> None:
    config = _config()
    schema = bf.load_event_schema()
    manifest = bf.load_manifest()
    source = bf.real_sources(config)[0]

    bf.bootstrap_one(source, schema, manifest, force=False, dry_run=True)

    assert not bf.TRAIL_PATH.exists()
    assert not (bf.FAILSAFE_DIR / "fixture_source_FROZEN.json").exists()


def test_main_bootstraps_all_registered_sources(isolated_repo: Path, tmp_path: Path) -> None:
    config_path = tmp_path / "config.yml"
    import yaml

    config_path.write_text(yaml.safe_dump(_config()), encoding="utf-8")

    rc = bf.main(["--config", str(config_path)])

    assert rc == 0
    manifest = json.loads(bf.MANIFEST_PATH.read_text(encoding="utf-8"))
    assert "fixture_source" in manifest["sources"]
    assert manifest["sources"]["fixture_source"]["epistemic_state"] == "VERIFIED"
