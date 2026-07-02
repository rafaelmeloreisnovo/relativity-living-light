#!/usr/bin/env python3
"""
rll_json_watcher.py — consumidor primário de RLL_JSON_EVOLUTION_WATCHER.yml

Fluxo por fonte:
  1. Pre-flight global
  2. fetch (primary → mirrors → failsafe)
  3. fingerprint: detecta drift de schema
  4. tests: gates epistêmicos
  5. rollback se trigger
  6. grava evento em EVOLUTION_TRAIL.jsonl e results/manifest.json

Uso:
  python rll_json_watcher.py --config RLL_JSON_EVOLUTION_WATCHER.yml
  python rll_json_watcher.py --config ... --source desi_dr2_bao
  python rll_json_watcher.py --config ... --dry-run
  python rll_json_watcher.py --config ... --rollback --source desi_dr2_bao --checkpoint latest
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

# ---------------------------------------------------------------------------
# Tipos auxiliares
# ---------------------------------------------------------------------------
EpistemicState = str  # VERIFIED | DECLARED_BY_AUTHOR | TOKEN_VAZIO | CONTRADICTION

EPISTEMIC_ORDER = {
    "VERIFIED": 4,
    "DECLARED_BY_AUTHOR": 3,
    "TOKEN_VAZIO": 2,
    "CONTRADICTION": 1,
}


def downgrade_epistemic(current: str, reason: str) -> str:
    """Sempre move para estado mais conservador; nunca promove sem gate explícito."""
    if current == "VERIFIED":
        return "TOKEN_VAZIO"
    return current


# ---------------------------------------------------------------------------
# Carregamento de configuração
# ---------------------------------------------------------------------------

def load_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    return cfg


# ---------------------------------------------------------------------------
# Fingerprint de schema
# ---------------------------------------------------------------------------

def compute_fingerprint(data: Dict[str, Any], depth: int = 2) -> str:
    """sha256 das chaves ordenadas até `depth` níveis."""
    def extract_keys(obj, prefix="", current_depth=0):
        keys = []
        if isinstance(obj, dict) and current_depth < depth:
            for k, v in obj.items():
                full = f"{prefix}.{k}" if prefix else k
                keys.append(full)
                keys.extend(extract_keys(v, full, current_depth + 1))
        return keys

    sorted_keys = sorted(set(extract_keys(data)))
    payload = "\n".join(sorted_keys).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_fingerprint(ref_path: str) -> Optional[str]:
    p = Path(ref_path)
    if p.exists():
        return p.read_text(encoding="utf-8").strip()
    return None


def save_fingerprint(ref_path: str, fp: str) -> None:
    p = Path(ref_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(fp + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Fetch
# ---------------------------------------------------------------------------

def fetch_source(source_cfg: Dict[str, Any], dry_run: bool = False) -> Optional[Dict[str, Any]]:
    """
    Tenta primary → mirrors → failsafe.
    Retorna (data_dict, origin_label) ou (None, 'FAILED').
    """
    import urllib.request

    attempts = [{"url": source_cfg["primary"]["url"], "label": "primary"}]
    for m in source_cfg.get("mirrors", []):
        attempts.append({"url": m["url"], "label": f"mirror_p{m['priority']}"})

    if dry_run:
        print(f"  [DRY-RUN] would fetch {len(attempts)} URL(s) for {source_cfg['id']}")
        return {"_dry_run": True}, "dry_run"

    for attempt in attempts:
        url = attempt["url"].replace("\n", "").replace(" ", "")
        label = attempt["label"]
        try:
            with urllib.request.urlopen(url, timeout=30) as resp:
                raw = resp.read()
            data = json.loads(raw)
            print(f"  [OK] fetched {source_cfg['id']} from {label}")
            return data, label
        except Exception as exc:
            print(f"  [WARN] {label} failed for {source_cfg['id']}: {exc}")

    # failsafe
    fs = source_cfg.get("failsafe", {})
    if fs.get("enabled"):
        snap = Path(fs["snapshot_path"])
        if snap.exists():
            print(f"  [FAILSAFE] using snapshot for {source_cfg['id']}: {snap}")
            data = json.loads(snap.read_text(encoding="utf-8"))
            return data, "FAILSAFE"

    print(f"  [FAIL] all sources exhausted for {source_cfg['id']}")
    return None, "FAILED"


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def run_tests(data: Dict[str, Any], tests: List[Dict], source_id: str) -> List[Dict]:
    """Executa gates; retorna lista de resultados."""
    results = []
    for t in tests:
        tid = t["id"]
        check = t["check"]
        on_fail = t.get("on_fail", "WARN")
        passed = False
        note = ""

        try:
            if check == "has_keys":
                missing = [k for k in t.get("required", []) if k not in data]
                passed = len(missing) == 0
                note = f"missing: {missing}" if not passed else ""

            elif check == "range":
                val = data.get(t["field"])
                if val is not None:
                    passed = t["min"] <= float(val) <= t["max"]
                    note = f"value={val}"
                else:
                    passed = False
                    note = "field absent"

            elif check == "all_positive":
                vals = [data.get(f) for f in t.get("fields", [])]
                passed = all(v is not None and float(v) > 0 for v in vals)
                note = f"values={vals}"

            elif check == "field_equals":
                passed = data.get(t["field"]) == t["value"]
                note = f"got={data.get(t['field'])}"

            elif check == "row_count_min":
                n = len(data) if isinstance(data, list) else data.get("_row_count", 0)
                passed = n >= t["min"]
                note = f"count={n}"

            elif check == "fingerprint_match":
                current_fp = compute_fingerprint(data)
                ref_fp = load_fingerprint(t["ref_path"])
                if ref_fp is None:
                    # primeiro run: salvar e passar
                    save_fingerprint(t["ref_path"], current_fp)
                    passed = True
                    note = "fingerprint initialized"
                elif current_fp != ref_fp:
                    passed = False
                    note = f"drift detected: {ref_fp[:8]}→{current_fp[:8]}"
                    on_fail = t.get("on_drift", "WARN_AND_STAGE")
                else:
                    passed = True

            elif check == "custom":
                script = t.get("script", "")
                args = t.get("args", [])
                r = subprocess.run([sys.executable, script] + args, capture_output=True)
                passed = r.returncode == 0
                note = r.stdout.decode()[:200] if not passed else ""

            else:
                passed = True  # check desconhecido: não bloqueia
                note = f"unknown check type: {check}"

        except Exception as exc:
            passed = False
            note = str(exc)

        results.append({
            "test_id": tid,
            "passed": passed,
            "on_fail": on_fail,
            "note": note,
        })

        status = "PASS" if passed else f"FAIL({on_fail})"
        print(f"    [{status}] {tid}: {note}")

    return results


# ---------------------------------------------------------------------------
# Rollback
# ---------------------------------------------------------------------------

def create_checkpoint(source_id: str, data: Dict, cfg: Dict) -> Optional[str]:
    rb = cfg.get("rollback", {})
    if not rb.get("enabled"):
        return None

    ckdir = Path(rb["checkpoints_dir"])
    ckdir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    ckpath = ckdir / f"{source_id}_{ts}.json"
    ckpath.write_text(json.dumps(data, indent=2), encoding="utf-8")

    # manter apenas keep_last
    keep = rb.get("keep_last", 5)
    checkpoints = sorted(ckdir.glob(f"{source_id}_*.json"))
    for old in checkpoints[:-keep]:
        old.unlink()

    print(f"  [CHECKPOINT] saved: {ckpath}")
    return str(ckpath)


def do_rollback(source_id: str, rollback_cfg: Dict, checkpoint: str = "latest") -> bool:
    ckdir = Path(rollback_cfg["checkpoints_dir"])
    checkpoints = sorted(ckdir.glob(f"{source_id}_*.json"))
    if not checkpoints:
        print(f"  [ROLLBACK] no checkpoints found for {source_id}")
        return False
    target = checkpoints[-1] if checkpoint == "latest" else Path(checkpoint)
    if not target.exists():
        print(f"  [ROLLBACK] checkpoint not found: {target}")
        return False

    failsafe_path = Path(f"data/failsafe/{source_id}_FROZEN.json")
    failsafe_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(target, failsafe_path)
    print(f"  [ROLLBACK] restored {source_id} from {target} → {failsafe_path}")
    return True


# ---------------------------------------------------------------------------
# Trilha de evolução
# ---------------------------------------------------------------------------

def emit_trail_event(trail_log: str, event: Dict) -> None:
    p = Path(trail_log)
    p.parent.mkdir(parents=True, exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(json.dumps(event, ensure_ascii=False) + "\n")


def update_manifest(manifest_path: str, source_id: str, event: Dict) -> None:
    p = Path(manifest_path)
    if p.exists():
        try:
            manifest = json.loads(p.read_text(encoding="utf-8"))
        except Exception:
            manifest = {}
    else:
        manifest = {"version": "1.0", "artifacts": {}, "generated_utc": ""}

    manifest.setdefault("artifacts", {})[source_id] = {
        "last_updated": event["timestamp_utc"],
        "action":       event["action"],
        "epistemic":    event["epistemic_after"],
        "schema_drift": event.get("schema_drift", False),
        "artifact_path": event.get("artifact_path", ""),
    }
    manifest["generated_utc"] = datetime.now(timezone.utc).isoformat()

    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


# ---------------------------------------------------------------------------
# Orquestrador principal
# ---------------------------------------------------------------------------

def process_source(source_cfg: Dict, global_cfg: Dict, dry_run: bool = False) -> Dict:
    sid = source_cfg["id"]
    print(f"\n>>> [{sid}]")

    trail_cfg = global_cfg.get("artifact_evolution_trail", {})
    trail_log = trail_cfg.get("trail_log", "artifacts/EVOLUTION_TRAIL.jsonl")
    manifest_path = "results/manifest.json"

    ts = datetime.now(timezone.utc).isoformat()
    ep_before = source_cfg.get("epistemic", "TOKEN_VAZIO")
    ep_after = ep_before
    action = "FETCH"
    schema_drift = False
    artifact_path = ""
    fingerprint_before = ""
    fingerprint_after = ""

    # 1. fetch
    data, origin = fetch_source(source_cfg, dry_run)

    if data is None:
        ep_after = "TOKEN_VAZIO"
        action = "FAILSAFE_EXHAUSTED"
        emit_trail_event(trail_log, {
            "timestamp_utc": ts, "source_id": sid, "action": action,
            "schema_drift": False, "epistemic_before": ep_before,
            "epistemic_after": ep_after, "fingerprint_before": "",
            "fingerprint_after": "", "artifact_path": "", "notes": "all sources failed",
        })
        update_manifest(manifest_path, sid, {
            "timestamp_utc": ts, "action": action, "epistemic_after": ep_after,
            "schema_drift": False,
        })
        return {"source_id": sid, "action": action, "epistemic": ep_after}

    if origin == "FAILSAFE":
        ep_after = source_cfg.get("failsafe", {}).get("epistemic", "TOKEN_VAZIO")
        action = "FAILSAFE"

    # 2. fingerprint
    if not dry_run:
        fingerprint_after = compute_fingerprint(data)
        for t in source_cfg.get("tests", []):
            if t.get("check") == "fingerprint_match":
                stored = load_fingerprint(t["ref_path"])
                if stored and stored != fingerprint_after:
                    schema_drift = True
                    fingerprint_before = stored
                    drift_action = t.get("on_drift", "WARN_AND_STAGE")
                    print(f"  [SCHEMA DRIFT] {sid}: {stored[:8]}→{fingerprint_after[:8]}")
                    if drift_action == "FAILOVER" or t.get("on_breaking") == "FAILOVER":
                        action = "FAILOVER"
                elif stored is None:
                    save_fingerprint(t["ref_path"], fingerprint_after)

    # 3. tests
    test_results = run_tests(data, source_cfg.get("tests", []), sid) if not dry_run else []
    fail_count = sum(1 for r in test_results if not r["passed"])

    for r in test_results:
        if not r["passed"]:
            if r["on_fail"] == "CONTRADICTION":
                ep_after = "CONTRADICTION"
            elif r["on_fail"] == "FAILOVER":
                action = "FAILOVER"
            elif r["on_fail"] in ("WARN", "WARN_AND_STAGE"):
                pass  # não bloqueia

    # 4. rollback automático?
    rb_cfg = source_cfg.get("rollback", {})
    triggers = rb_cfg.get("trigger_on", [])
    should_rollback = (
        (ep_after == "CONTRADICTION" and "CONTRADICTION" in triggers) or
        (schema_drift and "BREAKING_SCHEMA" in triggers) or
        (fail_count >= 3 and "fail_count_gte_3" in triggers)
    )

    if should_rollback and not dry_run:
        print(f"  [AUTO-ROLLBACK] triggered for {sid}")
        do_rollback(sid, rb_cfg)
        action = "ROLLBACK"

    # 5. checkpoint antes de salvar
    if not dry_run and action not in ("ROLLBACK", "FAILSAFE_EXHAUSTED"):
        cp = create_checkpoint(sid, data, source_cfg)

    # 6. artifact upload
    at_cfg = source_cfg.get("artifact_trail", {})
    if at_cfg.get("enabled") and not dry_run:
        ts_clean = ts.replace(":", "").replace("-", "").replace("T", "_")[:15]
        artifact_path = at_cfg.get("path_template", f"artifacts/{sid}_{{timestamp}}.json")
        artifact_path = artifact_path.replace("{timestamp}", ts_clean)
        Path(artifact_path).parent.mkdir(parents=True, exist_ok=True)
        Path(artifact_path).write_text(json.dumps(data, indent=2, ensure_ascii=False))
        print(f"  [ARTIFACT] saved: {artifact_path}")

    # 7. trilha de evolução
    event = {
        "timestamp_utc":      ts,
        "source_id":          sid,
        "action":             action,
        "schema_drift":       schema_drift,
        "epistemic_before":   ep_before,
        "epistemic_after":    ep_after,
        "fingerprint_before": fingerprint_before,
        "fingerprint_after":  fingerprint_after,
        "artifact_path":      artifact_path,
        "rll_paths_affected": source_cfg.get("rll_paths", []),
        "notes": f"origin={origin} fail_count={fail_count}",
    }

    if not dry_run:
        emit_trail_event(trail_log, event)
        update_manifest(manifest_path, sid, event)

    print(f"  [DONE] {sid}: {ep_before} → {ep_after} | action={action}")
    return {"source_id": sid, "action": action, "epistemic": ep_after}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="RLL JSON Evolution Watcher")
    parser.add_argument("--config",      required=True)
    parser.add_argument("--source",      default=None, help="ID de fonte específica")
    parser.add_argument("--dry-run",     action="store_true")
    parser.add_argument("--rollback",    action="store_true")
    parser.add_argument("--rollback-all",action="store_true")
    parser.add_argument("--checkpoint",  default="latest")
    args = parser.parse_args()

    cfg = load_config(args.config)
    sources = cfg.get("sources", [])

    if args.source:
        sources = [s for s in sources if s["id"] == args.source]
        if not sources:
            print(f"[ERROR] source '{args.source}' not found in config")
            sys.exit(1)

    if args.rollback or args.rollback_all:
        for s in sources:
            rb = s.get("rollback", {})
            if rb.get("enabled"):
                do_rollback(s["id"], rb, args.checkpoint)
        return

    print(f"\n=== RLL JSON Evolution Watcher ===")
    print(f"config: {args.config}")
    print(f"dry_run: {args.dry_run}")
    print(f"sources: {len(sources)}")
    print(f"{'='*34}\n")

    summary = []
    for s in sources:
        result = process_source(s, cfg, dry_run=args.dry_run)
        summary.append(result)

    print("\n=== SUMMARY ===")
    for r in summary:
        print(f"  {r['source_id']:<30} epistemic={r['epistemic']:<25} action={r['action']}")

    contradictions = [r for r in summary if r["epistemic"] == "CONTRADICTION"]
    if contradictions:
        print(f"\n[ALERT] {len(contradictions)} source(s) in CONTRADICTION state:")
        for c in contradictions:
            print(f"  → {c['source_id']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
