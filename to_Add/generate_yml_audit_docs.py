#!/usr/bin/env python3
"""
tools/generate_yml_audit_docs.py
Lê RLL_JSON_EVOLUTION_WATCHER.yml + EVOLUTION_TRAIL.jsonl e gera:
  - docs/audit/EPISTEMIC_AUDIT.md    (tabela de estados por fonte)
  - docs/audit/ORPHAN_REGISTRY.md    (artefatos latentes/esquecidos)
  - docs/audit/SCHEMA_DRIFT_LOG.md   (histórico de drifts detectados)
  - docs/audit/CONTRADICTION_LOG.md  (contradições registradas)

Uso:
  python tools/generate_yml_audit_docs.py \
    --config RLL_JSON_EVOLUTION_WATCHER.yml \
    --trail  artifacts/EVOLUTION_TRAIL.jsonl \
    --output docs/audit/
"""

import argparse
import json
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

# ---------------------------------------------------------------------------
# Carregadores
# ---------------------------------------------------------------------------

def load_config(path: str) -> Dict[str, Any]:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_trail(path: str) -> List[Dict]:
    p = Path(path)
    if not p.exists():
        return []
    events = []
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                pass
    return events


# ---------------------------------------------------------------------------
# Análise da trilha
# ---------------------------------------------------------------------------

def latest_state_per_source(events: List[Dict]) -> Dict[str, Dict]:
    """Último evento por source_id."""
    latest = {}
    for ev in events:
        sid = ev.get("source_id", "?")
        latest[sid] = ev
    return latest


def all_drifts(events: List[Dict]) -> List[Dict]:
    return [ev for ev in events if ev.get("schema_drift")]


def all_contradictions(events: List[Dict]) -> List[Dict]:
    return [ev for ev in events if ev.get("epistemic_after") == "CONTRADICTION"]


def all_rollbacks(events: List[Dict]) -> List[Dict]:
    return [ev for ev in events if ev.get("action") == "ROLLBACK"]


def epistemic_counts(latest: Dict[str, Dict]) -> Dict[str, List[str]]:
    counts: Dict[str, List[str]] = defaultdict(list)
    for sid, ev in latest.items():
        counts[ev.get("epistemic_after", "TOKEN_VAZIO")].append(sid)
    return dict(counts)


# ---------------------------------------------------------------------------
# Gerador: EPISTEMIC_AUDIT.md
# ---------------------------------------------------------------------------

def gen_epistemic_audit(cfg: Dict, latest: Dict, counts: Dict,
                        generated_utc: str) -> str:
    sources = cfg.get("sources", [])

    lines = [
        "# EPISTEMIC AUDIT — RLL JSON Evolution Watcher",
        f"",
        f"**Gerado:** `{generated_utc}`  ",
        f"**Config:** `RLL_JSON_EVOLUTION_WATCHER.yml`  ",
        f"",
        "## Resumo por estado epistêmico",
        "",
        "| Estado | Nº | Fontes |",
        "|---|---|---|",
    ]

    order = ["VERIFIED", "DECLARED_BY_AUTHOR", "TOKEN_VAZIO", "CONTRADICTION"]
    icons = {
        "VERIFIED":           "✅",
        "DECLARED_BY_AUTHOR": "🟡",
        "TOKEN_VAZIO":        "⚠️",
        "CONTRADICTION":      "🔴",
    }
    for state in order:
        srcs = counts.get(state, [])
        if srcs:
            lines.append(
                f"| {icons[state]} **{state}** | {len(srcs)} "
                f"| {', '.join(f'`{s}`' for s in srcs)} |"
            )

    lines += [
        "",
        "## Detalhamento por fonte",
        "",
        "| ID | Epistêmico (config) | Epistêmico (último evento) "
        "| Último action | Drift | Artifact |",
        "|---|---|---|---|---|---|",
    ]

    for src in sources:
        sid   = src["id"]
        ep_cfg = src.get("epistemic", "TOKEN_VAZIO")
        ev     = latest.get(sid, {})
        ep_now = ev.get("epistemic_after", "—")
        action = ev.get("action", "—")
        drift  = "🔀" if ev.get("schema_drift") else "—"
        art    = f"`{ev.get('artifact_path', '—')}`" if ev.get("artifact_path") else "—"

        arrow = ""
        if ep_cfg != ep_now and ep_now != "—":
            arrow = f" → {ep_now}"

        lines.append(
            f"| `{sid}` | {ep_cfg}{arrow} | {ep_now} | {action} | {drift} | {art} |"
        )

    lines += [
        "",
        "## Estados epistêmicos — definições",
        "",
        "| Estado | Significado |",
        "|---|---|",
        "| ✅ VERIFIED | Lido em commit, tag, release ou manifesto assinado |",
        "| 🟡 DECLARED_BY_AUTHOR | Declarado por Rafael, sem prova independente ainda |",
        "| ⚠️ TOKEN_VAZIO | Evidência necessária ainda não localizada |",
        "| 🔴 CONTRADICTION | Evidência encontrada contradiz a alegação |",
        "",
        "> *Metáfora ilumina, mas não valida; dado, predição, cálculo e falsificador "
        "sustentam a camada científica.* — README RLL",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Gerador: ORPHAN_REGISTRY.md
# ---------------------------------------------------------------------------

def gen_orphan_registry(cfg: Dict, generated_utc: str) -> str:
    trail_cfg = cfg.get("artifact_evolution_trail", {})
    orphans   = trail_cfg.get("registered_orphan_artifacts", [])

    lines = [
        "# ORPHAN ARTIFACT REGISTRY",
        "",
        f"**Gerado:** `{generated_utc}`",
        "",
        "Documentos identificados como fora da trilha canônica.",
        "Cada um tem um estado epistêmico e uma condição de promoção.",
        "",
        "| Arquivo | Epistêmico | Status | Promover para | Condição |",
        "|---|---|---|---|---|",
    ]

    for o in orphans:
        p        = Path(o["path"])
        exists   = "✓ existe" if p.exists() else "✗ ausente"
        ep       = o.get("epistemic", "TOKEN_VAZIO")
        status   = o.get("status", "?")
        promote  = o.get("promote_to", "—")
        cond     = o.get("condition", "—")
        action   = o.get("action", "—")
        lines.append(
            f"| `{o['path']}` ({exists}) | {ep} | {status} | {promote} | {cond or action} |"
        )

    lines += [
        "",
        "## Protocolo de promoção",
        "",
        "1. Verificar conteúdo do arquivo (leitura, não inferência)",
        "2. Atualizar estado epistêmico para `DECLARED_BY_AUTHOR` ou `VERIFIED`",
        "3. Mover para `docs/canonicos/` com número sequencial",
        "4. Registrar evento `ORPHAN_PROMOTED` na trilha `EVOLUTION_TRAIL.jsonl`",
        "5. Atualizar `results/manifest.json`",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Gerador: SCHEMA_DRIFT_LOG.md
# ---------------------------------------------------------------------------

def gen_schema_drift_log(drifts: List[Dict], generated_utc: str) -> str:
    lines = [
        "# SCHEMA DRIFT LOG",
        "",
        f"**Gerado:** `{generated_utc}`",
        f"**Total de drifts registrados:** {len(drifts)}",
        "",
    ]

    if not drifts:
        lines.append("*Nenhum drift de schema detectado ainda.*\n")
        return "\n".join(lines)

    lines += [
        "| Timestamp | Fonte | FP antes | FP depois | Action |",
        "|---|---|---|---|---|",
    ]

    for ev in drifts:
        ts  = ev.get("timestamp_utc", "?")[:19]
        sid = ev.get("source_id", "?")
        fpb = ev.get("fingerprint_before", "")[:8] or "—"
        fpa = ev.get("fingerprint_after",  "")[:8] or "—"
        act = ev.get("action", "?")
        lines.append(f"| `{ts}` | `{sid}` | `{fpb}` | `{fpa}` | {act} |")

    lines += [
        "",
        "## Interpretação",
        "",
        "- FP antes ≠ FP depois = campos do JSON mudaram entre execuções",
        "- `WARN_AND_STAGE`: campo novo apareceu (não quebra downstream)",
        "- `FAILOVER`: campo obrigatório desapareceu (quebra downstream)",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Gerador: CONTRADICTION_LOG.md
# ---------------------------------------------------------------------------

def gen_contradiction_log(contradictions: List[Dict],
                          rollbacks: List[Dict], generated_utc: str) -> str:
    lines = [
        "# CONTRADICTION LOG",
        "",
        f"**Gerado:** `{generated_utc}`",
        f"**Total de contradições:** {len(contradictions)}",
        f"**Total de rollbacks:** {len(rollbacks)}",
        "",
        "> Uma contradição significa que a evidência encontrada contradiz",
        "> uma alegação previamente classificada como VERIFIED ou DECLARED_BY_AUTHOR.",
        "> Isso não invalida o framework — invalida aquela alegação específica,",
        "> naquele dataset, com aquele método.",
        "",
    ]

    if contradictions:
        lines += [
            "## Contradições registradas",
            "",
            "| Timestamp | Fonte | Notas |",
            "|---|---|---|",
        ]
        for ev in contradictions:
            ts    = ev.get("timestamp_utc", "?")[:19]
            sid   = ev.get("source_id", "?")
            notes = ev.get("notes", "?")[:80]
            lines.append(f"| `{ts}` | `{sid}` | {notes} |")
        lines.append("")

    if rollbacks:
        lines += [
            "## Rollbacks executados",
            "",
            "| Timestamp | Fonte | Artifact path |",
            "|---|---|---|",
        ]
        for ev in rollbacks:
            ts  = ev.get("timestamp_utc", "?")[:19]
            sid = ev.get("source_id", "?")
            art = ev.get("artifact_path", "—")
            lines.append(f"| `{ts}` | `{sid}` | `{art}` |")
        lines.append("")

    if not contradictions and not rollbacks:
        lines.append("*Nenhuma contradição ou rollback registrado ainda.*\n")

    lines += [
        "## Protocolo pós-contradição",
        "",
        "1. **Não reverter imediatamente** — registrar na trilha primeiro",
        "2. Verificar se o gate `optimizer_scaling_guard` passou na mesma execução",
        "3. Se sim: a contradição é real — o parâmetro RLL não é significativo neste dataset",
        "4. Se não: a contradição pode ser artefactual — re-executar com método correto",
        "5. Atualizar estado epistêmico via `rll_json_watcher.py --rollback` se necessário",
        "6. Documentar conclusão neste log antes de fechar o issue",
        "",
    ]

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="RLL_JSON_EVOLUTION_WATCHER.yml")
    parser.add_argument("--trail",  default="artifacts/EVOLUTION_TRAIL.jsonl")
    parser.add_argument("--output", default="docs/audit/")
    args = parser.parse_args()

    cfg    = load_config(args.config)
    events = load_trail(args.trail)
    outdir = Path(args.output)
    outdir.mkdir(parents=True, exist_ok=True)

    now = datetime.now(timezone.utc).isoformat()[:19] + "Z"

    latest = latest_state_per_source(events)
    counts = epistemic_counts(latest)
    drifts = all_drifts(events)
    contras = all_contradictions(events)
    rolls   = all_rollbacks(events)

    # --- Gerar arquivos ---
    docs = {
        "EPISTEMIC_AUDIT.md":    gen_epistemic_audit(cfg, latest, counts, now),
        "ORPHAN_REGISTRY.md":    gen_orphan_registry(cfg, now),
        "SCHEMA_DRIFT_LOG.md":   gen_schema_drift_log(drifts, now),
        "CONTRADICTION_LOG.md":  gen_contradiction_log(contras, rolls, now),
    }

    for fname, content in docs.items():
        p = outdir / fname
        p.write_text(content, encoding="utf-8")
        print(f"  [OK] {p}")

    # --- Resumo no terminal ---
    print(f"\n=== Audit Docs Generated ===")
    print(f"  Output dir   : {outdir}")
    print(f"  Sources      : {len(cfg.get('sources', []))}")
    print(f"  Trail events : {len(events)}")
    print(f"  Drifts       : {len(drifts)}")
    print(f"  Contradictions: {len(contras)}")
    print(f"  Rollbacks    : {len(rolls)}")
    print()
    for state in ["VERIFIED", "DECLARED_BY_AUTHOR", "TOKEN_VAZIO", "CONTRADICTION"]:
        srcs = counts.get(state, [])
        if srcs:
            print(f"  {state:<25} : {len(srcs)} — {srcs}")


if __name__ == "__main__":
    main()
