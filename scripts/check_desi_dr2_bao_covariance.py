#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

C_KM_S = 299792.458
DATA_DIR = Path("data/real/cosmology/desi_bao_dr2_cobaya")
MEAN = DATA_DIR / "desi_gaussian_bao_ALL_GCcomb_mean.tsv"
COV = DATA_DIR / "desi_gaussian_bao_ALL_GCcomb_cov.tsv"


def read_mean(path: Path) -> list[tuple[float, float, str]]:
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("z") or line.startswith("#"):
            continue
        z, value, q = line.split()
        rows.append((float(z), float(value), q))
    return rows


def read_matrix(path: Path) -> list[list[float]]:
    return [[float(x) for x in line.split()] for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def invert(a: list[list[float]]) -> list[list[float]]:
    n = len(a)
    m = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(a)]
    for i in range(n):
        pivot = max(range(i, n), key=lambda r: abs(m[r][i]))
        if abs(m[pivot][i]) < 1e-18:
            raise ValueError("singular covariance")
        m[i], m[pivot] = m[pivot], m[i]
        div = m[i][i]
        m[i] = [v / div for v in m[i]]
        for r in range(n):
            if r == i:
                continue
            fac = m[r][i]
            m[r] = [rv - fac * iv for rv, iv in zip(m[r], m[i])]
    return [row[n:] for row in m]


def e_lcdm(z: float, om: float) -> float:
    return math.sqrt(om * (1.0 + z) ** 3 + (1.0 - om))


def e_w0wa(z: float, om: float, w0: float, wa: float) -> float:
    a = 1.0 / (1.0 + z)
    de = (1.0 - om) * a ** (-3.0 * (1.0 + w0 + wa)) * math.exp(-3.0 * wa * (1.0 - a))
    return math.sqrt(om * a ** -3 + de)


def e_rll(z: float, om: float, os0: float, zt: float, wt: float) -> float:
    a = 1.0 / (1.0 + z)
    f = 1.0 / (1.0 + math.exp(max(-700.0, min(700.0, (z - zt) / wt))))
    rf = f + (1.0 - f) * a ** -3
    return math.sqrt(om * a ** -3 + (1.0 - om - os0) + os0 * rf)


def integrate(func, z: float, n: int = 800) -> float:
    if z == 0.0:
        return 0.0
    if n % 2:
        n += 1
    h = z / n
    s = 1.0 / func(0.0) + 1.0 / func(z)
    for i in range(1, n):
        coef = 4 if i % 2 else 2
        s += coef / func(i * h)
    return s * h / 3.0


def prediction(z: float, q: str, model: str, args) -> float:
    if model == "lcdm":
        ez = lambda x: e_lcdm(x, args.omega_m)
    elif model == "w0wa":
        ez = lambda x: e_w0wa(x, args.omega_m, args.w0, args.wa)
    elif model == "rll":
        ez = lambda x: e_rll(x, args.omega_m, args.omega_s0, args.zt, args.wt)
    else:
        raise ValueError(model)
    dh = C_KM_S / (100.0 * args.h * ez(z))
    dm = C_KM_S / (100.0 * args.h) * integrate(ez, z)
    if q == "DH_over_rs":
        return dh / args.rd
    if q == "DM_over_rs":
        return dm / args.rd
    if q == "DV_over_rs":
        return (z * dm * dm * dh) ** (1.0 / 3.0) / args.rd
    raise ValueError(q)


def chi2(obs: list[float], pred: list[float], cov: list[list[float]]) -> float:
    inv = invert(cov)
    r = [o - p for o, p in zip(obs, pred)]
    return sum(r[i] * inv[i][j] * r[j] for i in range(len(r)) for j in range(len(r)))


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--mean", default=str(MEAN))
    p.add_argument("--cov", default=str(COV))
    p.add_argument("--out", default="results/desi_dr2_bao_covariance_chi2.json")
    p.add_argument("--omega-m", type=float, default=0.315)
    p.add_argument("--h", type=float, default=0.674)
    p.add_argument("--rd", type=float, default=147.09)
    p.add_argument("--w0", type=float, default=-1.0)
    p.add_argument("--wa", type=float, default=0.0)
    p.add_argument("--omega-s0", type=float, default=0.059)
    p.add_argument("--zt", type=float, default=1.164)
    p.add_argument("--wt", type=float, default=0.405)
    args = p.parse_args()
    rows = read_mean(Path(args.mean))
    cov = read_matrix(Path(args.cov))
    obs = [v for _, v, _ in rows]
    if len(rows) != 13 or len(cov) != 13 or any(len(r) != 13 for r in cov):
        raise SystemExit("DESI DR2 BAO core must be 13 rows with 13x13 covariance")
    results = {}
    for model in ("lcdm", "w0wa", "rll"):
        pred = [prediction(z, q, model, args) for z, _, q in rows]
        results[model] = {"chi2_bao_desi_dr2": chi2(obs, pred, cov), "n": len(rows)}
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"status": "desi_dr2_bao_covariance_chi2", "results": results}, indent=2), encoding="utf-8")
    print(json.dumps({"status": "desi_dr2_bao_covariance_chi2", "results": results}, indent=2))


if __name__ == "__main__":
    main()
