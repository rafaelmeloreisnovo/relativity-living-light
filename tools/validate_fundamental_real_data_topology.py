#!/usr/bin/env python3
"""Validate the RLL fundamental real-data and methodology topology.

This gate verifies identity and structural integration. A PASS never validates
RLL as a physical theory and never changes claim_allowed from false.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

import yaml

try:
    import jsonschema
except ImportError:  # optional outside CI
    jsonschema = None

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "data/manifests/dados_reais_fundamentais_v1.json"
METHODOLOGY = ROOT / "docs/canonicos/METODOLOGIA_COERENTE_RLL.md"
FOREST = ROOT / "data/knowledge_forest/rll_route_forest_blueprint.json"
FOREST_SCHEMA = ROOT / "schemas/rll_route_forest_blueprint.schema.json"
REGISTRY = ROOT / "rll_equation_registry.yml"
DATASETS_CONFIG = ROOT / "data/pipelines/structure_d/datasets_config.json"
WATCHER = ROOT / "RLL_JSON_EVOLUTION_WATCHER.yml"

REQUIRED_DATASETS = {
    "real_hz",
    "real_bao_legacy",
    "real_desi_dr2_bao",
    "real_fsigma8",
    "real_cmb_shift",
    "real_pantheon_plus_shoes",
}
REQUIRED_TREES = {"T-REAL-DATA", "T-METHODOLOGY"}
REQUIRED_NODES = {
    "N-RD-ROOT", "N-RD-HZ", "N-RD-BAO", "N-RD-DESI-DR2",
    "N-RD-FSIGMA8", "N-RD-CMB", "N-RD-PANTHEON",
    "N-METH-ROOT", "N-METH-INGEST", "N-METH-LIKELIHOOD",
    "N-METH-MODEL-SELECT", "N-METH-CLAIM-GATE",
    "N-METH-PANTHEON-SNE", "N-METH-MCMC-CHAINS",
}
REQUIRED_ROUTES = {
    "RT-RD-SCIENCE", "RT-METH-FALSIFIER", "RT-RD-METH-INGEST",
    "RT-RD-HZ-LIKELIHOOD", "RT-RD-BAO-LIKELIHOOD",
    "RT-RD-GROWTH-CLAIM-GATE", "RT-RD-CMB-MODEL-SELECT",
}
REQUIRED_EQUATIONS = {"rll_friedmann_e2", "logistic_transition", "null_limit_lcdm"}
METHODOLOGY_PHASES = {"ingest", "likelihood", "model_selection", "claim_gate"}
FUNDAMENTAL_ACTIVE = {
    "real_hz", "real_bao", "real_cmb_shift", "real_fsigma8", "real_desi_dr2_bao"
}


def fail(message: str) -> None:
    raise SystemExit(f"fundamental-real-data-topology: {message}")


def load_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(f"invalid JSON {path.relative_to(ROOT)}: {exc}")
    if not isinstance(data, dict):
        fail(f"JSON root must be an object: {path.relative_to(ROOT)}")
    return data


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as exc:
        fail(f"invalid YAML {path.relative_to(ROOT)}: {exc}")
    if not isinstance(data, dict):
        fail(f"YAML root must be a mapping: {path.relative_to(ROOT)}")
    return data


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def validate_manifest() -> dict[str, Any]:
    manifest = load_json(MANIFEST)
    if manifest.get("schema_version") != "rll.dados_reais_fundamentais.v1":
        fail("unexpected fundamental manifest schema")
    if manifest.get("claim_allowed") is not False:
        fail("fundamental manifest attempted to promote claim_allowed")

    datasets = manifest.get("datasets")
    if not isinstance(datasets, list) or len(datasets) < 6:
        fail("manifest must contain at least six datasets")
    ids = {row.get("dataset_id") for row in datasets}
    if not REQUIRED_DATASETS.issubset(ids):
        fail(f"missing datasets: {sorted(REQUIRED_DATASETS - ids)}")
    if manifest.get("dataset_count") != len(datasets):
        fail("dataset_count mismatch")

    verified = partial = 0
    checked: list[dict[str, Any]] = []
    for row in datasets:
        dataset_id = row.get("dataset_id")
        if row.get("claim_allowed") is not False:
            fail(f"dataset promoted claim_allowed: {dataset_id}")
        local = ROOT / str(row.get("local_path", ""))
        if not local.is_file():
            fail(f"missing local dataset: {dataset_id} -> {local.relative_to(ROOT)}")
        actual_sha = sha256_file(local)
        if actual_sha != row.get("sha256"):
            fail(f"SHA-256 mismatch for {dataset_id}: {actual_sha}")

        failsafe_path = ROOT / str(row.get("failsafe_snapshot", ""))
        failsafe = load_json(failsafe_path)
        files = failsafe.get("files") or []
        match = next((item for item in files if item.get("path") == row.get("local_path")), None)
        if not match or match.get("sha256") != actual_sha:
            fail(f"failsafe mismatch for {dataset_id}")

        state = row.get("epistemic_state")
        if state == "VERIFIED":
            verified += 1
        elif state == "PARTIAL":
            partial += 1
        else:
            fail(f"unsupported epistemic_state for {dataset_id}: {state}")
        checked.append({"dataset_id": dataset_id, "state": state, "sha256": actual_sha})

    if verified != manifest.get("verified_dataset_count"):
        fail("verified_dataset_count mismatch")
    if partial != manifest.get("partial_dataset_count"):
        fail("partial_dataset_count mismatch")

    voids = manifest.get("token_vazio")
    if not isinstance(voids, list) or not voids:
        fail("TOKEN_VAZIO ledger is missing")
    for item in voids:
        if item.get("state") != "TOKEN_VAZIO" or not item.get("required_for") or not item.get("fill_path"):
            fail(f"invalid TOKEN_VAZIO entry: {item}")
    return {"datasets": checked, "verified": verified, "partial": partial, "token_vazio": len(voids)}


def validate_methodology() -> dict[str, Any]:
    text = METHODOLOGY.read_text(encoding="utf-8")
    required_sections = [f"## {number}." for number in range(1, 7)]
    missing = [section for section in required_sections if section not in text]
    if missing:
        fail(f"methodology missing sections: {missing}")
    required_refs = [
        "data/manifests/dados_reais_fundamentais_v1.json",
        "data/knowledge_forest/rll_route_forest_blueprint.json",
        "tools/validate_schemas_claim_boundary.py",
        "claim_allowed=false",
    ]
    for ref in required_refs:
        if ref not in text:
            fail(f"methodology missing canonical reference: {ref}")
    return {"sections": 6, "bytes": len(text.encode("utf-8"))}


def validate_forest() -> dict[str, Any]:
    forest = load_json(FOREST)
    if forest.get("claim_allowed") is not False:
        fail("forest attempted to promote claim_allowed")
    if jsonschema is not None:
        jsonschema.validate(forest, load_json(FOREST_SCHEMA))
    trees = forest.get("trees") or {}
    nodes = forest.get("nodes") or {}
    routes = forest.get("routes") or {}
    if not REQUIRED_TREES.issubset(trees):
        fail(f"forest missing trees: {sorted(REQUIRED_TREES - set(trees))}")
    if not REQUIRED_NODES.issubset(nodes):
        fail(f"forest missing nodes: {sorted(REQUIRED_NODES - set(nodes))}")
    if not REQUIRED_ROUTES.issubset(routes):
        fail(f"forest missing routes: {sorted(REQUIRED_ROUTES - set(routes))}")
    if routes["RT-METH-FALSIFIER"].get("status") != "partial_resolution":
        fail("RT-METH-FALSIFIER must remain partial_resolution")
    for node_id in ("N-FALSIFIER-GAP", "N-TEMPORAL-MEMORY-GAP"):
        refs = nodes[node_id].get("refs") or []
        if "data/manifests/dados_reais_fundamentais_v1.json" not in refs:
            fail(f"{node_id} is not connected to the fundamental manifest")
    return {"trees": len(trees), "nodes": len(nodes), "routes": len(routes)}


def validate_registry() -> dict[str, Any]:
    registry = load_yaml(REGISTRY)
    equations = registry.get("equations")
    if not isinstance(equations, list) or not equations:
        fail("equation registry is empty")
    ids = {item.get("id") for item in equations}
    if not REQUIRED_EQUATIONS.issubset(ids):
        fail(f"missing critical equations: {sorted(REQUIRED_EQUATIONS - ids)}")
    for item in equations:
        equation_id = item.get("id")
        validators = item.get("real_data_validators")
        phase = item.get("methodology_phase")
        if not isinstance(validators, list):
            fail(f"real_data_validators missing for {equation_id}")
        unknown = set(validators) - REQUIRED_DATASETS
        if unknown:
            fail(f"unknown dataset validator(s) for {equation_id}: {sorted(unknown)}")
        if phase not in METHODOLOGY_PHASES:
            fail(f"invalid methodology_phase for {equation_id}: {phase}")
    central = next(item for item in equations if item.get("id") == "rll_friedmann_e2")
    if "Omega_s0" not in central.get("equation", "") or "Omega_P0" not in central.get("equation", ""):
        fail("rll_friedmann_e2 is incomplete")
    return {"equations": len(equations), "critical": sorted(REQUIRED_EQUATIONS)}


def validate_pipeline_profile() -> dict[str, Any]:
    config = load_json(DATASETS_CONFIG)
    if config.get("default_profile") != "structure_d_fundamentals":
        fail("structure_d_fundamentals is not the default profile")
    profile = (config.get("profiles") or {}).get("structure_d_fundamentals")
    if not isinstance(profile, dict):
        fail("structure_d_fundamentals profile is missing")
    active = set(profile.get("active_datasets") or [])
    if active != FUNDAMENTAL_ACTIVE:
        fail(f"unexpected fundamental active datasets: {sorted(active)}")
    if profile.get("synthetic_allowed") is not False or profile.get("claim_allowed") is not False:
        fail("fundamental profile must block synthetic promotion and claims")
    datasets = config.get("datasets") or {}
    for dataset_id in active:
        row = datasets.get(dataset_id)
        if not isinstance(row, dict):
            fail(f"profile references missing dataset: {dataset_id}")
        if str(row.get("dataset_type", "")).startswith("synthetic") or "/synthetic/" in str(row.get("path", "")):
            fail(f"synthetic dataset leaked into fundamental profile: {dataset_id}")
    partial = set(profile.get("partial_datasets") or [])
    if partial != {"real_pantheon_plus_shoes"}:
        fail("Pantheon+ must be explicit and partial, not silently active")
    return {"default_profile": config["default_profile"], "active": sorted(active), "partial": sorted(partial)}


def validate_watcher() -> dict[str, Any]:
    watcher = load_yaml(WATCHER)
    sources = [item for item in watcher.get("sources", []) if not item.get("template_only")]
    ids = {item.get("id") for item in sources}
    if "bao_legacy" not in ids:
        fail("BAO legacy is absent from RLL_JSON_EVOLUTION_WATCHER.yml")
    return {"tracked_sources": len(ids), "source_ids": sorted(ids)}


def run() -> dict[str, Any]:
    return {
        "schema": "rll.fundamental_real_data_topology_receipt.v1",
        "state": "PASS",
        "claim_allowed": False,
        "manifest": validate_manifest(),
        "methodology": validate_methodology(),
        "forest": validate_forest(),
        "equation_registry": validate_registry(),
        "pipeline": validate_pipeline_profile(),
        "watcher": validate_watcher(),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write-receipt", type=Path)
    args = parser.parse_args()
    receipt = run()
    rendered = json.dumps(receipt, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if args.write_receipt:
        target = args.write_receipt if args.write_receipt.is_absolute() else ROOT / args.write_receipt
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(rendered, encoding="utf-8")
    print(rendered, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
