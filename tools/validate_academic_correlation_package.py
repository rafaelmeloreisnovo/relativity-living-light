#!/usr/bin/env python3
"""Validate the ACADEMIC_CORR_001 relational package.

Structural validator only. It checks package/graph coherence and claim gates.
It does not execute cosmology, prove mathematics or promote scientific claims.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_PACKAGE = ROOT / "results/relational_validation/packages/ACADEMIC_CORR_001/package.yml"
DEFAULT_GRAPH = ROOT / "results/relational_validation/packages/ACADEMIC_CORR_001/relation_graph.json"
PACKAGE_SCHEMA = ROOT / "schemas/relational_validation_package.schema.json"
GRAPH_SCHEMA = ROOT / "schemas/relation_graph.schema.json"

ALLOWED_STATES = {
    "RELATIONAL_PENDING",
    "RELATIONAL_TESTED",
    "RELATIONAL_CONVERGENCE_CANDIDATE",
    "RELATIONAL_CONVERGENCE_BLOCKED",
    "RELATIONAL_VALIDATED_REVIEW_READY",
    "RELATIONAL_REFUTED",
}

REQUIRED_PACKAGE_KEYS = {
    "schema",
    "claim_id",
    "relation_graph_id",
    "state",
    "claim",
    "source_paths",
    "log_paths",
    "artifact_paths",
    "metric_names",
    "baseline_or_adversary",
    "uncertainty_or_covariance_status",
    "contradiction_check",
    "reproducibility_command",
    "claim_allowed",
    "claim_blocked",
    "next_gate",
}

REQUIRED_CLAIM_KEYS = {
    "text",
    "domain",
    "claim_boundary",
    "claim_allowed",
    "claim_blocked",
}

REQUIRED_GRAPH_KEYS = {
    "schema",
    "graph_id",
    "claim_id",
    "claim_allowed",
    "status",
    "boundary",
    "nodes",
    "edges",
    "next_gate",
}

TOKEN_VAZIO_FIELDS = {
    "metric_names",
    "uncertainty_or_covariance_status",
    "contradiction_check",
    "reproducibility_command",
}

PROMOTION_STATES = {
    "RELATIONAL_TESTED",
    "RELATIONAL_CONVERGENCE_CANDIDATE",
    "RELATIONAL_VALIDATED_REVIEW_READY",
}


def fail(message: str) -> None:
    raise SystemExit(f"academic correlation package validation failed: {message}")


def load_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"missing package: {path}")
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"package is not a mapping: {path}")
    return data


def load_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        fail(f"missing graph: {path}")
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        fail(f"graph is not an object: {path}")
    return data


def require_keys(data: dict[str, Any], required: set[str], label: str) -> None:
    missing = sorted(required - set(data))
    if missing:
        fail(f"{label} missing keys: {missing}")


def require_list(value: Any, label: str) -> list[Any]:
    if not isinstance(value, list):
        fail(f"{label} must be a list")
    return value


def has_token_vazio(value: Any) -> bool:
    if isinstance(value, str):
        return "TOKEN_VAZIO" in value
    if isinstance(value, list):
        return any(has_token_vazio(item) for item in value)
    if isinstance(value, dict):
        return any(has_token_vazio(item) for item in value.values())
    return False


def require_repo_paths(paths: list[Any], label: str) -> None:
    for item in paths:
        if not isinstance(item, str) or not item.strip():
            fail(f"{label} contains invalid path: {item!r}")
        candidate = ROOT / item
        if not candidate.exists():
            fail(f"{label} path does not exist: {item}")


def validate_package(package: dict[str, Any]) -> None:
    require_keys(package, REQUIRED_PACKAGE_KEYS, "package")

    if package["schema"] != "rll.relational_validation_package.v1":
        fail("package schema mismatch")
    if package["state"] not in ALLOWED_STATES:
        fail(f"invalid package state: {package['state']}")
    if package["claim_allowed"] is not False:
        fail("package claim_allowed must remain false")

    claim = package["claim"]
    if not isinstance(claim, dict):
        fail("claim must be a mapping")
    require_keys(claim, REQUIRED_CLAIM_KEYS, "claim")
    if claim["claim_allowed"] is not False:
        fail("claim.claim_allowed must remain false")

    for key in ["source_paths", "log_paths", "artifact_paths", "metric_names", "claim_blocked"]:
        require_list(package[key], key)

    require_repo_paths(package["source_paths"], "source_paths")
    require_repo_paths(package["artifact_paths"], "artifact_paths")

    if package["state"] in PROMOTION_STATES:
        token_fields = [key for key in TOKEN_VAZIO_FIELDS if has_token_vazio(package.get(key))]
        if token_fields:
            fail(f"promoted state cannot retain TOKEN_VAZIO fields: {token_fields}")


def validate_graph(graph: dict[str, Any], package: dict[str, Any]) -> None:
    require_keys(graph, REQUIRED_GRAPH_KEYS, "graph")

    if graph["schema"] != "rll.relation_graph.v1":
        fail("graph schema mismatch")
    if graph["claim_allowed"] is not False:
        fail("graph claim_allowed must remain false")
    if graph["status"] not in ALLOWED_STATES:
        fail(f"invalid graph status: {graph['status']}")

    if graph["claim_id"] != package["claim_id"]:
        fail("graph claim_id does not match package claim_id")
    if graph["graph_id"] != package["relation_graph_id"]:
        fail("graph_id does not match package relation_graph_id")
    if graph["status"] != package["state"]:
        fail("graph status does not match package state")

    nodes = require_list(graph["nodes"], "graph.nodes")
    edges = require_list(graph["edges"], "graph.edges")
    if not nodes:
        fail("graph must contain at least one node")
    if not edges:
        fail("graph must contain at least one edge")

    node_ids: set[str] = set()
    for idx, node in enumerate(nodes):
        if not isinstance(node, dict):
            fail(f"graph.nodes[{idx}] must be an object")
        for key in ["id", "kind"]:
            if not isinstance(node.get(key), str) or not node[key].strip():
                fail(f"graph.nodes[{idx}] missing non-empty {key}")
        if node["id"] in node_ids:
            fail(f"duplicate graph node id: {node['id']}")
        node_ids.add(node["id"])

    for idx, edge in enumerate(edges):
        if not isinstance(edge, dict):
            fail(f"graph.edges[{idx}] must be an object")
        for key in ["from", "to", "edge_type"]:
            if not isinstance(edge.get(key), str) or not edge[key].strip():
                fail(f"graph.edges[{idx}] missing non-empty {key}")
        if edge["from"] not in node_ids:
            fail(f"graph.edges[{idx}] references missing source node: {edge['from']}")
        if edge["to"] not in node_ids:
            fail(f"graph.edges[{idx}] references missing target node: {edge['to']}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--package", type=Path, default=DEFAULT_PACKAGE)
    parser.add_argument("--graph", type=Path, default=DEFAULT_GRAPH)
    args = parser.parse_args()

    if not PACKAGE_SCHEMA.exists():
        fail(f"missing package schema: {PACKAGE_SCHEMA}")
    if not GRAPH_SCHEMA.exists():
        fail(f"missing graph schema: {GRAPH_SCHEMA}")

    package = load_yaml(args.package)
    graph = load_json(args.graph)
    validate_package(package)
    validate_graph(graph, package)

    print("OK: academic correlation package is structurally coherent and claim-bounded")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
