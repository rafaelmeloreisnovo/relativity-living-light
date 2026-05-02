#!/usr/bin/env python3
"""IML pipeline: load DAISE-style inputs, compute attractor metrics and falsifiability checks."""
from __future__ import annotations

import argparse
import json
import math
import hashlib
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, List

ALPHA = 0.25


@dataclass
class StepResult:
    t: int
    C: float
    H: float
    phi: float
    state: List[float]


def toroidal_map(x: Dict[str, Any]) -> List[float]:
    payload = json.dumps(x, sort_keys=True).encode("utf-8")
    digest = hashlib.sha256(payload).digest()
    # s in [0,1)^7
    return [int.from_bytes(digest[i : i + 4], "big") / 2**32 for i in range(0, 28, 4)]


def entropy_milli(data: List[int]) -> float:
    if not data:
        return 0.0
    unique = len(set(data))
    transitions = sum(1 for i in range(1, len(data)) if data[i] != data[i - 1])
    return unique * 6000 / 256 + transitions * 2000 / max(1, len(data) - 1)


def run_sequence(inp: Dict[str, Any], steps: int) -> Dict[str, Any]:
    data = inp.get("dados", [])
    if not isinstance(data, list):
        raise ValueError("'dados' deve ser lista de inteiros")

    H_in = min(1.0, entropy_milli(data) / 8000.0)
    C_in = float(inp.get("coerencia_in", 0.7))
    C = float(inp.get("coerencia0", 0.5))
    H = float(inp.get("entropia0", 0.5))

    series: List[StepResult] = []
    x_state = {
        "dados": data,
        "entropia": H,
        "hash": hashlib.sha256(bytes([d % 256 for d in data])).hexdigest(),
        "estado": inp.get("estado", "ACTIVE"),
    }

    for t in range(steps):
        C = (1 - ALPHA) * C + ALPHA * C_in
        H = (1 - ALPHA) * H + ALPHA * H_in
        phi = (1 - H) * C

        x_state["entropia"] = H
        s = toroidal_map(x_state)
        series.append(StepResult(t=t + 1, C=C, H=H, phi=phi, state=s))

    last = series[-1]
    falsifiable = {
        "attractor_cardinality_target": 42,
        "cycle_42_verified": False,
        "pi_max_constraint_ok": last.H <= 0.9,
        "non_void_constraint_ok": x_state["estado"] != "VOID",
    }

    # Simple 42-cycle proxy test from xn+42=xn using deterministic recurrence.
    x = 0.314159
    seq = []
    for _ in range(84):
        x = (math.sqrt(3) / 2) * x - math.pi * math.sin(math.radians(279))
        seq.append(round(x % 1.0, 12))
    falsifiable["cycle_42_verified"] = seq[:42] == seq[42:]

    return {
        "alpha": ALPHA,
        "input_entropy": H_in,
        "input_coherence": C_in,
        "steps": [asdict(s) for s in series],
        "final": asdict(last),
        "falsifiability": falsifiable,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="JSON input path")
    parser.add_argument("--output", required=True, help="JSON output path")
    parser.add_argument("--steps", type=int, default=42)
    args = parser.parse_args()

    inp = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = run_sequence(inp, args.steps)
    out = Path(args.output)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")


if __name__ == "__main__":
    main()
