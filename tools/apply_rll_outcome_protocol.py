#!/usr/bin/env python3
"""Apply the RLL outcome protocol for every possible evidence-scan result.

The purpose is operational: after the evidence scanner produces a claim_status,
this tool turns that status into a deterministic action plan.

It does not run cosmological fits and it does not change scientific results.
It converts the result state into safe next actions, allowed wording, forbidden
wording, and required follow-up artifacts.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCAN = ROOT / "results" / "audit" / "rll_model_evidence_scan.json"
DEFAULT_OUT_JSON = ROOT / "results" / "audit" / "rll_outcome_action_plan.json"
DEFAULT_OUT_MD = ROOT / "results" / "audit" / "rll_outcome_action_plan.md"
DEFAULT_MATRIX_JSON = ROOT / "data" / "inputs" / "cosmology_joint" / "rll_outcome_action_matrix.json"
DEFAULT_MATRIX_MD = ROOT / "docs" / "RLL_OUTCOME_ACTION_MATRIX.md"


@dataclass(frozen=True)
class OutcomeRule:
    status: str
    meaning: str
    allowed_wording: str
    forbidden_wording: list[str]
    required_actions: list[str]
    required_artifacts: list[str]
    release_policy: str
    close_or_update_issues: str


def build_rules() -> dict[str, OutcomeRule]:
    rules = [
        OutcomeRule(
            status="CLAIM_BLOCKED",
            meaning="The current result table does not support a positive RLL claim, or a required governance gate failed.",
            allowed_wording="Nesta rodada, o claim positivo do RLL está bloqueado; o relatório deve explicar o motivo, comparar com CPL e registrar TOKEN_VAZIO/PENDING onde aplicável.",
            forbidden_wording=[
                "RLL vence",
                "RLL é favorecido",
                "RLL prova",
                "RLL faz melhor aos dados",
                "RLL supera CPL",
            ],
            required_actions=[
                "keep positive superiority wording blocked",
                "publish only negative/diagnostic interpretation",
                "run or schedule H0/r_d ablation if H0_all_equal is true",
                "report Delta AICc/BIC vs CPL",
                "report Os0/zt/wt and whether Os0 collapsed",
                "mark missing covariance, Pantheon, CMB or growth blocks as TOKEN_VAZIO/PENDING",
            ],
            required_artifacts=[
                "results/audit/rll_model_evidence_scan.json",
                "results/audit/rll_academic_claim_gate_report.md",
                "docs/RLL_DATA_FIT_DECISION_TREE.md",
                "data/inputs/cosmology_joint/h0_rd_ablation_matrix.json",
            ],
            release_policy="Do not publish as discovery. Allow only audit/diagnostic report.",
            close_or_update_issues="Keep #420/#421/#422/#423 open unless the blocking reasons are fully resolved by new artifacts.",
        ),
        OutcomeRule(
            status="PASS_LIMITED",
            meaning="RLL is not worse than CPL by scanned AICc/BIC criteria in this table, but stronger academic gates remain.",
            allowed_wording="RLL não é pior que CPL nesta tabela pelos critérios escaneados; o resultado é limitado e ainda depende de covariância, ablação, MCMC e benchmark físico.",
            forbidden_wording=[
                "RLL está provado",
                "RLL é verdade física",
                "RLL encerra ΛCDM",
                "RLL dispensa CPL",
            ],
            required_actions=[
                "label the result PASS_LIMITED, not confirmed",
                "run H0/r_d ablation and rescan every ablation CSV",
                "materialize covariance policies before strong claim",
                "run MCMC/nested sampling before publication-grade inference",
                "run CLASS/CAMB or keep growth claim blocked",
            ],
            required_artifacts=[
                "results/audit/rll_model_evidence_scan.json",
                "results/structure_d/ablation/*.csv",
                "results/audit/rll_academic_claim_gate_report.md",
                "covariance manifests and hashes for used datasets",
            ],
            release_policy="Allow limited methodological/preprint wording; block discovery wording.",
            close_or_update_issues="Update #421/#423 with ablation scans; keep #420/#422 open until registry-derived k and report wiring are complete.",
        ),
        OutcomeRule(
            status="PARTIAL",
            meaning="Some calculation exists, but covariance, baseline, dataset, registry or benchmark coverage is incomplete.",
            allowed_wording="Resultado parcial: há cálculo, mas a interpretação fica limitada por lacunas explícitas de covariância, baseline, dataset ou benchmark.",
            forbidden_wording=[
                "RLL vence",
                "RLL é favorecido",
                "RLL comprovado",
            ],
            required_actions=[
                "state every missing block explicitly",
                "separate computed values from TOKEN_VAZIO",
                "avoid ranking claims if CPL or covariance is missing",
                "add missing dataset/covariance manifests before rerun",
            ],
            required_artifacts=[
                "partial evidence scan JSON",
                "claim boundary section in report",
                "TOKEN_VAZIO list",
            ],
            release_policy="Allow internal report only unless limitations are front-page visible.",
            close_or_update_issues="Open/update issue for each missing block; do not close governance issues.",
        ),
        OutcomeRule(
            status="TOKEN_VAZIO",
            meaning="There is not enough evidence to calculate the requested claim safely.",
            allowed_wording="TOKEN_VAZIO: não há evidência computacional suficiente para responder sem inventar resultado.",
            forbidden_wording=[
                "probably wins",
                "likely proves",
                "deve estar certo",
                "parece confirmado",
            ],
            required_actions=[
                "stop claim generation",
                "identify missing file, dataset, covariance, baseline or run",
                "create a reproducibility task before interpretation",
            ],
            required_artifacts=[
                "missing-evidence ledger",
                "issue with exact missing artifact path",
            ],
            release_policy="No scientific claim. Only gap ledger.",
            close_or_update_issues="Create or update issue with missing evidence; keep claim blocked.",
        ),
        OutcomeRule(
            status="AUDIT_FAIL",
            meaning="A governance script, registry, schema, N-k-dof, JSON or report-language check failed.",
            allowed_wording="A auditoria falhou; nenhum claim científico deve ser emitido até correção do gate.",
            forbidden_wording=[
                "ignore audit",
                "publish anyway",
                "manual override without artifact",
            ],
            required_actions=[
                "fix the failing gate",
                "rerun registry validator and evidence scanner",
                "record the failed command and exact error",
            ],
            required_artifacts=[
                "CI log or local transcript",
                "fixed gate output",
            ],
            release_policy="Block release/report claim until audit passes.",
            close_or_update_issues="Open/update audit-failure issue; do not close root governance issue.",
        ),
        OutcomeRule(
            status="RUNTIME_PENDING",
            meaning="Governance metadata exists, but the actual cosmological run or ablation fit has not been executed.",
            allowed_wording="PENDING: a matriz/rota existe, mas o fit cosmológico ainda não foi executado para esta política.",
            forbidden_wording=[
                "ablation completed",
                "fit confirms",
                "run proves",
            ],
            required_actions=[
                "execute the ablation or mark as pending",
                "do not overwrite prior evidence without run_id",
                "scan each generated CSV independently",
            ],
            required_artifacts=[
                "results/structure_d/ablation/<run_id>.csv",
                "scan JSON for each run_id",
            ],
            release_policy="Allow roadmap/status only; block result interpretation.",
            close_or_update_issues="Keep #423 open until ablation CSVs exist and are scanned.",
        ),
    ]
    return {rule.status: rule for rule in rules}


def load_scan(path: Path) -> dict[str, Any] | None:
    if not path.exists():
        return None
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise SystemExit(f"FAIL: invalid scan JSON {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise SystemExit(f"FAIL: scan JSON root must be object: {path}")
    return data


def current_commit() -> str | None:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip()
    except Exception:
        return None


def infer_status(scan: dict[str, Any] | None) -> str:
    if scan is None:
        return "TOKEN_VAZIO"
    raw = scan.get("claim_status")
    if raw is None:
        return "AUDIT_FAIL"
    status = str(raw).strip().upper()
    if status in {"CLAIM_BLOCKED", "PASS_LIMITED", "PARTIAL", "TOKEN_VAZIO", "AUDIT_FAIL", "RUNTIME_PENDING"}:
        return status
    return "PARTIAL"


def write_matrix(rules: dict[str, OutcomeRule], json_path: Path, md_path: Path) -> None:
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "rll.outcome_action_matrix.v1",
        "purpose": "Map every possible RLL evidence/governance outcome to deterministic operational actions.",
        "rules": [asdict(rule) for rule in rules.values()],
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines: list[str] = []
    lines.append("# RLL Outcome Action Matrix")
    lines.append("")
    lines.append("> Auto-generated by `tools/apply_rll_outcome_protocol.py`.")
    lines.append("")
    lines.append("| status | meaning | release_policy |")
    lines.append("|---|---|---|")
    for rule in rules.values():
        lines.append(f"| `{rule.status}` | {rule.meaning} | {rule.release_policy} |")
    lines.append("")
    lines.append("## Rule details")
    for rule in rules.values():
        lines.append("")
        lines.append(f"### {rule.status}")
        lines.append("")
        lines.append(f"Allowed wording: {rule.allowed_wording}")
        lines.append("")
        lines.append("Required actions:")
        for action in rule.required_actions:
            lines.append(f"- {action}")
        lines.append("")
        lines.append("Required artifacts:")
        for artifact in rule.required_artifacts:
            lines.append(f"- `{artifact}`")
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_plan(status: str, rule: OutcomeRule, scan: dict[str, Any] | None, json_path: Path, md_path: Path) -> None:
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "rll.outcome_action_plan.v1",
        "commit_sha": current_commit(),
        "selected_status": status,
        "rule": asdict(rule),
        "scan_summary": None if scan is None else {
            "claim_status": scan.get("claim_status"),
            "claim_summary": scan.get("claim_summary"),
            "best_by_AICc": scan.get("best_by_AICc"),
            "best_by_BIC": scan.get("best_by_BIC"),
            "H0_all_equal": scan.get("H0_all_equal"),
            "blocking_reasons": scan.get("blocking_reasons", []),
            "warnings": scan.get("warnings", []),
        },
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    lines: list[str] = []
    lines.append("# RLL Outcome Action Plan")
    lines.append("")
    lines.append("> Auto-generated by `tools/apply_rll_outcome_protocol.py`.")
    lines.append("")
    lines.append(f"- selected_status: **{status}**")
    lines.append(f"- commit_sha: `{payload['commit_sha'] or 'TOKEN_VAZIO'}`")
    if scan is not None:
        lines.append(f"- best_by_AICc: `{scan.get('best_by_AICc', 'TOKEN_VAZIO')}`")
        lines.append(f"- best_by_BIC: `{scan.get('best_by_BIC', 'TOKEN_VAZIO')}`")
        lines.append(f"- H0_all_equal: `{scan.get('H0_all_equal', 'TOKEN_VAZIO')}`")
    lines.append("")
    lines.append("## Meaning")
    lines.append("")
    lines.append(rule.meaning)
    lines.append("")
    lines.append("## Allowed wording")
    lines.append("")
    lines.append(rule.allowed_wording)
    lines.append("")
    lines.append("## Forbidden wording")
    lines.append("")
    for item in rule.forbidden_wording:
        lines.append(f"- {item}")
    lines.append("")
    lines.append("## Required actions")
    lines.append("")
    for action in rule.required_actions:
        lines.append(f"- [ ] {action}")
    lines.append("")
    lines.append("## Required artifacts")
    lines.append("")
    for artifact in rule.required_artifacts:
        lines.append(f"- `{artifact}`")
    lines.append("")
    lines.append("## Release policy")
    lines.append("")
    lines.append(rule.release_policy)
    lines.append("")
    lines.append("## Issue policy")
    lines.append("")
    lines.append(rule.close_or_update_issues)
    md_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Apply the RLL outcome protocol for the current evidence scan.")
    parser.add_argument("--scan", type=Path, default=DEFAULT_SCAN)
    parser.add_argument("--out-json", type=Path, default=DEFAULT_OUT_JSON)
    parser.add_argument("--out-md", type=Path, default=DEFAULT_OUT_MD)
    parser.add_argument("--matrix-json", type=Path, default=DEFAULT_MATRIX_JSON)
    parser.add_argument("--matrix-md", type=Path, default=DEFAULT_MATRIX_MD)
    parser.add_argument("--status", default=None, help="Override status for matrix validation/testing")
    parser.add_argument("--write-matrix", action="store_true", help="Write the canonical outcome matrix files")
    parser.add_argument("--no-write", action="store_true", help="Validate only")
    args = parser.parse_args()

    rules = build_rules()
    scan = load_scan(args.scan)
    status = args.status.upper() if args.status else infer_status(scan)
    if status not in rules:
        raise SystemExit(f"FAIL: unsupported outcome status: {status}")
    rule = rules[status]

    if not args.no_write:
        if args.write_matrix:
            write_matrix(rules, args.matrix_json, args.matrix_md)
            print(f"wrote: {args.matrix_json}")
            print(f"wrote: {args.matrix_md}")
        write_plan(status, rule, scan, args.out_json, args.out_md)
        print(f"wrote: {args.out_json}")
        print(f"wrote: {args.out_md}")

    print(f"PASS: outcome protocol selected {status}")
    print(f"release_policy={rule.release_policy}")


if __name__ == "__main__":
    main()
