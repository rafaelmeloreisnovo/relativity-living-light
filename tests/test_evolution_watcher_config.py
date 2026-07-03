from __future__ import annotations

import json
from pathlib import Path

import jsonschema
import yaml

from tools import bootstrap_failsafe as bf

ROOT = Path(__file__).resolve().parents[1]
CONFIG_PATH = ROOT / "RLL_JSON_EVOLUTION_WATCHER.yml"
CAMINHOS_PATH = ROOT / "CAMINHOS_VALIDACAO_NOVOS.yml"


def _known_rll_path_ids() -> set[str]:
    data = yaml.safe_load(CAMINHOS_PATH.read_text(encoding="utf-8"))
    return {str(item["id"]) for item in data["caminhos"]}


def test_committed_config_loads_and_declares_required_sections() -> None:
    config = bf.load_config(CONFIG_PATH)
    assert config["schema"] == "rll.evolution_watcher_config.v1"
    assert isinstance(config["sources"], list) and len(config["sources"]) >= 5


def test_every_registered_real_source_local_path_exists() -> None:
    config = bf.load_config(CONFIG_PATH)
    for source in bf.real_sources(config):
        for rel_path in source["local_paths"]:
            assert (ROOT / rel_path).exists(), f"{source['id']}: missing {rel_path}"


def test_every_rll_paths_affected_id_is_a_known_canonical_route() -> None:
    known = _known_rll_path_ids()
    config = bf.load_config(CONFIG_PATH)
    for source in bf.real_sources(config):
        for path_id in source.get("rll_paths_affected", []):
            assert path_id in known, f"{source['id']}: unknown rll_paths_affected id {path_id}"


def test_every_real_source_has_a_primary_source_url() -> None:
    config = bf.load_config(CONFIG_PATH)
    for source in bf.real_sources(config):
        assert source.get("primary_source", {}).get("url"), f"{source['id']}: missing primary_source.url"


def test_committed_evolution_trail_events_conform_to_schema_and_never_promote_rollback_to_verified() -> None:
    trail_path = ROOT / "artifacts" / "EVOLUTION_TRAIL.jsonl"
    if not trail_path.exists():
        return
    schema = json.loads((ROOT / "schemas" / "evolution_event.schema.json").read_text(encoding="utf-8"))
    for line in trail_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        event = json.loads(line)
        jsonschema.validate(event, schema)
        if event["action"] == "ROLLBACK":
            assert event["epistemic_after"] != "VERIFIED"
