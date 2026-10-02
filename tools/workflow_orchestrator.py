#!/usr/bin/env python3
from __future__ import annotations

import argparse
import glob
import json
import os
import time
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any
from urllib import error, parse, request

import yaml

API_ROOT = "https://api.github.com"
RUN_DISCOVERY_CLOCK_SKEW = timedelta(minutes=2)


@dataclass
class WorkflowSelection:
    workflow_id: str
    file: str
    stage: int
    wait_for_completion: bool
    timeout_minutes: int
    inputs: dict[str, Any]


class ActionsClient:
    def __init__(self, repository: str, token: str) -> None:
        self.repository = repository
        self.token = token
        self._workflow_cache: dict[str, dict[str, Any]] = {}

    def _request(self, method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
        body = None
        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": "token " + self.token,
            "X-GitHub-Api-Version": "2022-11-28",
        }
        if payload is not None:
            body = json.dumps(payload).encode("utf-8")
            headers["Content-Type"] = "application/json"

        req = request.Request(f"{API_ROOT}{path}", data=body, method=method, headers=headers)
        try:
            with request.urlopen(req, timeout=30) as response:
                raw = response.read().decode("utf-8")
                if not raw.strip():
                    return {}
                return json.loads(raw)
        except error.HTTPError as exc:
            detail = exc.read().decode("utf-8")
            raise RuntimeError(f"GitHub API {method} {path} failed: {exc.code} {detail}") from exc

    def workflow_by_file(self, workflow_file: str) -> dict[str, Any]:
        if workflow_file in self._workflow_cache:
            return self._workflow_cache[workflow_file]
        data = self._request("GET", f"/repos/{self.repository}/actions/workflows/{parse.quote(workflow_file)}")
        self._workflow_cache[workflow_file] = data
        return data

    def dispatch(self, workflow_file: str, ref: str, inputs: dict[str, Any]) -> None:
        payload: dict[str, Any] = {"ref": ref}
        if inputs:
            payload["inputs"] = {k: format_workflow_input(v) for k, v in inputs.items()}
        self._request("POST", f"/repos/{self.repository}/actions/workflows/{parse.quote(workflow_file)}/dispatches", payload)

    def list_workflow_runs(self, workflow_id: int, branch: str) -> list[dict[str, Any]]:
        query = parse.urlencode({"event": "workflow_dispatch", "branch": branch, "per_page": 20})
        data = self._request("GET", f"/repos/{self.repository}/actions/workflows/{workflow_id}/runs?{query}")
        return data.get("workflow_runs", [])

    def run(self, run_id: int) -> dict[str, Any]:
        return self._request("GET", f"/repos/{self.repository}/actions/runs/{run_id}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Dispatch and optionally wait for a catalog of workflows.")
    parser.add_argument("--catalog", required=True, help="Path to workflow catalog YAML.")
    parser.add_argument("--profile", required=True, help="Catalog profile name.")
    parser.add_argument("--ref", required=True, help="Git ref to dispatch against.")
    parser.add_argument("--wait", action="store_true", help="Wait for completion for selected workflows.")
    parser.add_argument("--fail-fast", action="store_true", help="Stop orchestration on first failure.")
    parser.add_argument("--dry-run", action="store_true", help="Only print the selected execution plan.")
    parser.add_argument(
        "--overrides",
        default="{}",
        help="JSON object mapping workflow ids to input overrides.",
    )
    parser.add_argument("--output-dir", required=True, help="Directory for JSON/MD orchestration reports.")
    return parser.parse_args()


def format_workflow_input(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def load_and_expand_catalog(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("catalog must be a YAML mapping")
    if "profiles" not in data:
        raise ValueError("catalog must contain profiles")

    workflow_items = data.get("workflows")
    workflow_dirs = data.get("workflow_catalog_dirs")
    workflow_files = data.get("workflow_files")
    if workflow_items is None and workflow_dirs is None and workflow_files is None:
        raise ValueError("catalog must contain workflows, workflow_catalog_dirs, or workflow_files")

    if workflow_items is None:
        workflow_items = []
    if not isinstance(workflow_items, list):
        raise ValueError("workflows must be a YAML list when provided")

    if workflow_dirs is not None:
        if not isinstance(workflow_dirs, list) or not all(isinstance(item, str) for item in workflow_dirs):
            raise ValueError("workflow_catalog_dirs must be a YAML list of paths")
        for dir_item in workflow_dirs:
            dir_path = (path.parent / dir_item).resolve()
            if not dir_path.exists() or not dir_path.is_dir():
                raise ValueError(f"workflow catalog directory not found: {dir_item}")
            manifests = sorted(
                file_path
                for file_path in dir_path.rglob("*")
                if file_path.is_file() and file_path.suffix.lower() in {".yml", ".yaml"}
            )
            for manifest in manifests:
                manifest_data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
                if manifest_data is None:
                    continue
                if isinstance(manifest_data, dict) and isinstance(manifest_data.get("workflows"), list):
                    workflow_items.extend(manifest_data["workflows"])
                    continue
                if isinstance(manifest_data, dict):
                    workflow_items.append(manifest_data)
                    continue
                raise ValueError(f"invalid workflow manifest: {manifest}")

    if workflow_files is not None:
        if not isinstance(workflow_files, list) or not all(
            isinstance(item, str) for item in workflow_files
        ):
            raise ValueError("workflow_files must be a YAML list of glob patterns")
        repo_root = path.parent.parent.parent.resolve()
        existing_files = {
            Path(str(item.get("file"))).name
            for item in workflow_items
            if isinstance(item, dict) and item.get("file")
        }
        for pattern in workflow_files:
            matches = sorted(Path(item).resolve() for item in glob.glob(str(path.parent / pattern)))
            if not matches:
                raise ValueError(f"workflow file pattern matched nothing: {pattern}")
            for workflow_path in matches:
                if workflow_path.name == "unified-workflow-session-orchestrator.yml":
                    continue
                if workflow_path.name in existing_files:
                    continue
                workflow_data = yaml.safe_load(workflow_path.read_text(encoding="utf-8")) or {}
                workflow_on = workflow_data.get("on", workflow_data.get(True, {})) or {}
                if "workflow_dispatch" not in workflow_on:
                    raise ValueError(
                        f"workflow must support workflow_dispatch for orchestration: "
                        f"{workflow_path.relative_to(repo_root)}"
                    )
                dispatch = workflow_on["workflow_dispatch"]
                input_config = dispatch.get("inputs", {}) if isinstance(dispatch, dict) else {}
                inputs = {}
                if isinstance(input_config, dict):
                    for input_name, config in input_config.items():
                        if isinstance(config, dict) and "default" in config:
                            inputs[input_name] = config["default"]
                workflow_id = workflow_path.stem.replace("-", "_").lower()
                tags = ["all"]
                if "real" in workflow_id or "data" in workflow_id:
                    tags.append("real_data")
                if any(token in workflow_id for token in ("validate", "test", "ci", "syntax", "check")):
                    tags.append("validation")
                stage = 70
                if "syntax" in workflow_id:
                    stage = 10
                elif workflow_id == "start_manual_here":
                    stage = 20
                elif workflow_id == "real_data_complete_execution":
                    stage = 30
                elif workflow_id == "rll_real_data_orchestrator":
                    stage = 40
                elif "formula" in workflow_id:
                    stage = 50
                elif "iml" in workflow_id:
                    stage = 60
                workflow_items.append(
                    {
                        "id": workflow_id,
                        "file": workflow_path.name,
                        "stage": stage,
                        "enabled": True,
                        "tags": tags,
                        "wait_for_completion": True,
                        "timeout_minutes": 60,
                        "inputs": inputs,
                    }
                )

    data["workflows"] = workflow_items
    execution = data.get("execution") or {}
    if not isinstance(execution, dict):
        raise ValueError("execution must be a YAML mapping")
    mode = execution.get("mode", "sequential")
    if mode != "sequential":
        raise ValueError("execution.mode must be 'sequential'")
    if execution.get("stage_barrier", True) is not True:
        raise ValueError("execution.stage_barrier must be true")
    max_in_flight = execution.get("max_in_flight", 1)
    # bool is a subclass of int, but true/false are invalid concurrency values.
    if isinstance(max_in_flight, bool) or not isinstance(max_in_flight, int):
        raise ValueError("execution.max_in_flight must be an integer")
    if max_in_flight != 1:
        raise ValueError("execution.max_in_flight must be 1")
    data["execution"] = {
        "mode": mode,
        "stage_barrier": True,
        "max_in_flight": max_in_flight,
    }
    return data


def select_workflows(catalog: dict[str, Any], profile: str) -> list[WorkflowSelection]:
    profiles = catalog.get("profiles") or {}
    profile_cfg = profiles.get(profile)
    if not isinstance(profile_cfg, dict):
        raise ValueError(f"profile '{profile}' not found in catalog")

    include_tags = set(profile_cfg.get("include_tags") or [])
    if not include_tags:
        raise ValueError(f"profile '{profile}' must include at least one include_tag")

    selected: list[WorkflowSelection] = []
    for item in catalog.get("workflows", []):
        if not isinstance(item, dict):
            continue
        if not item.get("enabled", True):
            continue
        tags = set(item.get("tags") or [])
        if tags and tags.isdisjoint(include_tags):
            continue
        selected.append(
            WorkflowSelection(
                workflow_id=str(item.get("id", item.get("file", "unknown"))),
                file=str(item["file"]),
                stage=int(item.get("stage", 9999)),
                wait_for_completion=bool(item.get("wait_for_completion", True)),
                timeout_minutes=int(item.get("timeout_minutes", 30)),
                inputs=dict(item.get("inputs") or {}),
            )
        )

    selected.sort(key=lambda x: (x.stage, x.workflow_id))
    return selected


def apply_overrides(
    selected: list[WorkflowSelection], overrides_json: str
) -> list[WorkflowSelection]:
    try:
        overrides = json.loads(overrides_json)
    except json.JSONDecodeError as exc:
        raise ValueError("--overrides must be valid JSON") from exc
    if not isinstance(overrides, dict):
        raise ValueError("--overrides must be a JSON object")

    by_id = {workflow.workflow_id: workflow for workflow in selected}
    unknown = sorted(set(overrides) - set(by_id))
    if unknown:
        raise ValueError(f"override references unselected workflow(s): {', '.join(unknown)}")

    result = list(selected)
    result_by_id = {workflow.workflow_id: workflow for workflow in result}
    for workflow_id, values in overrides.items():
        if not isinstance(values, dict):
            raise ValueError(f"overrides.{workflow_id} must be a JSON object")
        workflow = result_by_id[workflow_id]
        workflow.inputs = {**workflow.inputs, **values}
    return result


def branch_from_ref(ref: str) -> str:
    if ref.startswith("refs/heads/"):
        return ref.removeprefix("refs/heads/")
    return ref


def find_dispatched_run(
    client: ActionsClient,
    workflow_numeric_id: int,
    branch: str,
    dispatched_at: datetime,
    known_run_ids: set[int] | None = None,
    timeout_seconds: int = 180,
) -> dict[str, Any]:
    deadline = time.time() + timeout_seconds
    # Allow for GitHub API clock skew and dispatch queue latency while excluding
    # runs observed before dispatch through known_run_ids.
    threshold = dispatched_at - RUN_DISCOVERY_CLOCK_SKEW
    known_run_ids = known_run_ids or set()
    while time.time() < deadline:
        runs = client.list_workflow_runs(workflow_numeric_id, branch)
        candidates = []
        for run in runs:
            if int(run["id"]) in known_run_ids:
                continue
            created_raw = str(run["created_at"])
            created = datetime.fromisoformat(
                created_raw.removesuffix("Z") + "+00:00" if created_raw.endswith("Z") else created_raw
            )
            if created >= threshold:
                candidates.append((created, run))
        if candidates:
            return max(candidates, key=lambda item: item[0])[1]
        time.sleep(5)
    raise RuntimeError("dispatched workflow run was not found in time")


def wait_for_completion(client: ActionsClient, run_id: int, timeout_minutes: int) -> dict[str, Any]:
    deadline = time.time() + timeout_minutes * 60
    while time.time() < deadline:
        run = client.run(run_id)
        if run.get("status") == "completed":
            return run
        time.sleep(15)
    raise RuntimeError(f"timed out waiting for run {run_id} after {timeout_minutes} minutes")


def write_reports(output_dir: Path, payload: dict[str, Any]) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "orchestration_summary.json").write_text(
        json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )

    lines = [
        "# Unified Workflow Session Orchestrator Report",
        "",
        f"- profile: `{payload['profile']}`",
        f"- ref: `{payload['ref']}`",
        f"- dry_run: `{payload['dry_run']}`",
        f"- wait: `{payload['wait']}`",
        f"- failed: `{payload['failed']}`",
        "",
        "| stage | id | file | dispatch | status | conclusion | run_url |",
        "|---:|---|---|---|---|---|---|",
    ]

    for row in payload["workflows"]:
        lines.append(
            "| {stage} | `{id}` | `{file}` | {dispatch} | `{status}` | `{conclusion}` | {url} |".format(
                stage=row.get("stage", ""),
                id=row.get("id", ""),
                file=row.get("file", ""),
                dispatch=row.get("dispatch", ""),
                status=row.get("status", ""),
                conclusion=row.get("conclusion", ""),
                url=row.get("html_url", ""),
            )
        )

    (output_dir / "ORCHESTRATION_REPORT.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    catalog = load_and_expand_catalog(Path(args.catalog))
    selected = apply_overrides(select_workflows(catalog, args.profile), args.overrides)
    branch = branch_from_ref(args.ref)

    payload: dict[str, Any] = {
        "schema": "rll.unified_workflow_session_orchestrator.v1",
        "profile": args.profile,
        "ref": args.ref,
        "dry_run": args.dry_run,
        "wait": args.wait,
        "execution": catalog["execution"],
        "failed": False,
        "overrides": json.loads(args.overrides),
        "workflows": [],
    }

    if not selected:
        payload["failed"] = True
        payload["error"] = "No workflows selected for this profile."
        write_reports(Path(args.output_dir), payload)
        return 1

    token = os.environ.get("GITHUB_TOKEN", "")
    repository = os.environ.get("GITHUB_REPOSITORY", "")
    if not args.dry_run and (not token or not repository):
        raise RuntimeError("GITHUB_TOKEN and GITHUB_REPOSITORY are required for workflow dispatch")

    client = ActionsClient(repository=repository, token=token) if not args.dry_run else None

    for workflow in selected:
        record: dict[str, Any] = {
            "id": workflow.workflow_id,
            "file": workflow.file,
            "stage": workflow.stage,
            "dispatch": "skipped",
            "status": "not_requested",
            "conclusion": "n/a",
            "html_url": "",
        }
        try:
            if args.dry_run:
                record["dispatch"] = "dry_run"
                record["status"] = "planned"
                payload["workflows"].append(record)
                continue

            assert client is not None
            meta = client.workflow_by_file(workflow.file)
            workflow_numeric_id = int(meta["id"])
            known_run_ids = {
                int(run["id"])
                for run in client.list_workflow_runs(workflow_numeric_id, branch)
            }
            dispatched_at = datetime.now(timezone.utc)
            client.dispatch(workflow.file, args.ref, workflow.inputs)
            record["dispatch"] = "ok"
            record["status"] = "dispatched"

            # The canonical session is deliberately single-flight: completion
            # is the barrier before the next workflow is dispatched.
            run = find_dispatched_run(
                client,
                workflow_numeric_id,
                branch,
                dispatched_at,
                known_run_ids=known_run_ids,
            )
            final_run = wait_for_completion(client, int(run["id"]), workflow.timeout_minutes)
            record["status"] = str(final_run.get("status", "unknown"))
            record["conclusion"] = str(final_run.get("conclusion", "unknown"))
            record["html_url"] = str(final_run.get("html_url", ""))
            if record["conclusion"] != "success":
                payload["failed"] = True
                if args.fail_fast:
                    payload["workflows"].append(record)
                    break
            payload["workflows"].append(record)
        except (RuntimeError, ValueError, KeyError) as exc:
            record["dispatch"] = "error"
            record["status"] = "failed"
            record["conclusion"] = "error"
            record["error"] = str(exc)
            payload["failed"] = True
            payload["workflows"].append(record)
            if args.fail_fast:
                break

    write_reports(Path(args.output_dir), payload)
    return 1 if payload["failed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
