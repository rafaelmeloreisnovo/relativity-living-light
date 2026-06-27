#!/usr/bin/env python3
"""
compute_weff_cpl_mapping.py
Gerado: 2026-06-27 | ∆RafaelVerboΩ | RAFCODE-Φ

Calcula w_eff(z) do RLL e mapeia no plano w0-wa CPL.
Encontra (Os0, zt, wt) que minimiza distância a CPL DESI DR2.

Uso no Termux:
  python3 compute_weff_cpl_mapping.py --out results/weff_mapping.csv
  python3 compute_weff_cpl_mapping.py --scan --out results/weff_scan.csv
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import sys
from pathlib import Path


# ── Física RLL ──────────────────────────────────────────────────────────────

def f_rll(z: float, zt: float, wt: float) -> float:
    """Fração de superposição: f(z) = 1 / (1 + exp((z-zt)/wt))."""
    try:
        return 1.0 / (1.0 + math.exp((z - zt) / wt))
    except OverflowError:
        return 0.0 if z > zt else 1.0


def rho_s_normalized(z: float, zt: float, wt: float) -> float:
    """ρ_s(z)/ρ_s0 = f(z) + (1-f(z))·(1+z)³."""
    a = 1.0 / (1.0 + z)
    fz = f_rll(z, zt, wt)
    return fz + (1.0 - fz) * (1.0 + z) ** 3


def drho_dlna(z: float, zt: float, wt: float, h: float = 1e-6) -> float:
    """d(ρ_s)/d(ln a) — derivada numérica."""
    a = 1.0 / (1.0 + z)
    ln_a = math.log(a)

    def rho_at_a(aa: float) -> float:
        zz = 1.0 / aa - 1.0
        ff = f_rll(zz, zt, wt)
        return ff + (1.0 - ff) * (1.0 / aa) ** 3

    return (rho_at_a(math.exp(ln_a + h)) - rho_at_a(math.exp(ln_a - h))) / (2.0 * h)


def w_eff_rll(z: float, zt: float, wt: float) -> float:
    """Equação de estado efetiva: w = -1 - (1/3)·d(ln ρ)/d(ln a)."""
    rf = rho_s_normalized(z, zt, wt)
    if rf <= 1e-10:
        return -1.0
    dr = drho_dlna(z, zt, wt)
    return -1.0 - dr / (3.0 * rf)


def w_cpl(z: float, w0: float, wa: float) -> float:
    """CPL: w(z) = w0 + wa·(1 - a)."""
    a = 1.0 / (1.0 + z)
    return w0 + wa * (1.0 - a)


def w0_wa_eff_rll(zt: float, wt: float) -> tuple[float, float]:
    """
    Aproxima w0_eff e wa_eff do RLL via Taylor em a=1:
      w0_eff = w_eff(z=0)
      wa_eff = -dw_eff/da|_{a=1} (definição CPL)
    """
    w0e = w_eff_rll(0.0, zt, wt)
    h = 1e-4
    # dw/da|_{a=1} via z: a=1/(1+z), z=0 → a=1; z=h → a~1-h
    z_plus = h / (1.0 - h)  # a = 1-h → z = h/(1-h)
    dw_da = (w_eff_rll(0.0, zt, wt) - w_eff_rll(z_plus, zt, wt)) / h
    wa_e = -dw_da
    return w0e, wa_e


# ── Dados DESI DR2 (embutidos para não depender de arquivo) ─────────────────

DESI_DR2_CPL_BESTFIT = {
    "w0": -0.838,
    "wa": -0.620,
    "source": "DESI DR2 Results V Table 1 (BAO+CMB+SNe combo)",
}

DESI_TRACERS = [
    # (z_eff, w_cpl_desi)  — calculado com w0=-0.838, wa=-0.620
    (0.295, w_cpl(0.295, -0.838, -0.620)),
    (0.510, w_cpl(0.510, -0.838, -0.620)),
    (0.706, w_cpl(0.706, -0.838, -0.620)),
    (0.934, w_cpl(0.934, -0.838, -0.620)),
    (1.321, w_cpl(1.321, -0.838, -0.620)),
    (1.484, w_cpl(1.484, -0.838, -0.620)),
    (2.330, w_cpl(2.330, -0.838, -0.620)),
]
SIGMA_W = 0.08  # incerteza típica em w(z) via BAO+CMB


def chi2_weff_vs_desi(zt: float, wt: float) -> float:
    """chi2 entre w_eff_RLL(z_i) e w_CPL_DESI(z_i)."""
    return sum(
        (w_eff_rll(z, zt, wt) - w_desi) ** 2 / SIGMA_W**2
        for z, w_desi in DESI_TRACERS
    )


# ── CLI ──────────────────────────────────────────────────────────────────────

def build_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="w_eff RLL → CPL mapping")
    p.add_argument("--zt", type=float, default=1.0)
    p.add_argument("--wt", type=float, default=0.3)
    p.add_argument("--os0", type=float, default=0.02)
    p.add_argument("--scan", action="store_true",
                   help="Varredura (zt, wt) para achar mínimo chi2")
    p.add_argument("--out", default="results/weff_mapping.csv")
    p.add_argument("--out-json", default="results/weff_mapping_summary.json")
    return p.parse_args()


def run_single(args: argparse.Namespace) -> None:
    zt, wt = args.zt, args.wt
    rows = []
    z_list = [0.0, 0.1, 0.2, 0.295, 0.4, 0.510, 0.6, 0.706,
              0.8, 0.934, 1.0, 1.321, 1.484, 1.8, 2.0, 2.330]
    for z in z_list:
        we = w_eff_rll(z, zt, wt)
        wc = w_cpl(z, DESI_DR2_CPL_BESTFIT["w0"], DESI_DR2_CPL_BESTFIT["wa"])
        fz = f_rll(z, zt, wt)
        rows.append({
            "z": z, "w_eff_rll": round(we, 6),
            "w_cpl_desi": round(wc, 6),
            "f_z": round(fz, 6),
            "delta_w": round(we - wc, 6),
        })

    w0e, wae = w0_wa_eff_rll(zt, wt)
    chi2 = chi2_weff_vs_desi(zt, wt)

    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    with open(args.out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    summary = {
        "parameters": {"zt": zt, "wt": wt, "os0": args.os0},
        "w0_eff_rll": round(w0e, 6),
        "wa_eff_rll": round(wae, 6),
        "w0_cpl_desi": DESI_DR2_CPL_BESTFIT["w0"],
        "wa_cpl_desi": DESI_DR2_CPL_BESTFIT["wa"],
        "chi2_weff_vs_desi_7pts": round(chi2, 4),
        "diagnosis": (
            "COMPATIVEL" if chi2 < 15.0 else
            "MARGINAL" if chi2 < 40.0 else "INCOMPATIVEL"
        ),
        "claim_allowed": False,
        "note": "claim_allowed=false ate comparacao BAO direta materializada",
    }
    Path(args.out_json).parent.mkdir(parents=True, exist_ok=True)
    Path(args.out_json).write_text(json.dumps(summary, indent=2))

    print(f"\n=== w_eff RLL (zt={zt}, wt={wt}) ===")
    print(f"  w0_eff={w0e:.4f}  wa_eff={wae:.4f}")
    print(f"  DESI CPL best: w0={DESI_DR2_CPL_BESTFIT['w0']}  wa={DESI_DR2_CPL_BESTFIT['wa']}")
    print(f"  chi2 vs DESI = {chi2:.2f}  → {summary['diagnosis']}")
    print(f"  CSV: {args.out}")
    print(f"  JSON: {args.out_json}")


def run_scan(args: argparse.Namespace) -> None:
    zt_vals = [round(0.3 + i * 0.1, 1) for i in range(18)]   # 0.3..2.0
    wt_vals = [round(0.1 + i * 0.05, 2) for i in range(14)]  # 0.1..0.75

    rows = []
    best = {"chi2": 1e9, "zt": None, "wt": None}
    for zt in zt_vals:
        for wt in wt_vals:
            chi2 = chi2_weff_vs_desi(zt, wt)
            w0e, wae = w0_wa_eff_rll(zt, wt)
            rows.append({
                "zt": zt, "wt": wt,
                "chi2_vs_desi": round(chi2, 4),
                "w0_eff": round(w0e, 6),
                "wa_eff": round(wae, 6),
                "diagnosis": (
                    "COMPATIVEL" if chi2 < 15.0 else
                    "MARGINAL" if chi2 < 40.0 else "INCOMPATIVEL"
                ),
            })
            if chi2 < best["chi2"]:
                best = {"chi2": chi2, "zt": zt, "wt": wt,
                        "w0_eff": w0e, "wa_eff": wae}

    scan_out = args.out.replace(".csv", "_scan.csv")
    Path(scan_out).parent.mkdir(parents=True, exist_ok=True)
    with open(scan_out, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n=== VARREDURA (zt,wt) — {len(rows)} combinações ===")
    print(f"  Melhor: zt={best['zt']}  wt={best['wt']}")
    print(f"  chi2_min={best['chi2']:.2f}")
    print(f"  w0_eff={best['w0_eff']:.4f}  wa_eff={best['wa_eff']:.4f}")
    desi_w0 = DESI_DR2_CPL_BESTFIT["w0"]
    desi_wa = DESI_DR2_CPL_BESTFIT["wa"]
    print(f"  DESI CPL: w0={desi_w0}  wa={desi_wa}")
    print(f"  Δw0={best['w0_eff']-desi_w0:.4f}  Δwa={best['wa_eff']-desi_wa:.4f}")
    print(f"  CSV: {scan_out}")

    compativel = [r for r in rows if r["diagnosis"] == "COMPATIVEL"]
    print(f"  Regiões compatíveis (chi2<15): {len(compativel)} de {len(rows)}")
    if compativel:
        print("  Primeiras 5 compatíveis:")
        for r in compativel[:5]:
            print(f"    zt={r['zt']}  wt={r['wt']}  chi2={r['chi2_vs_desi']}")


def main() -> int:
    args = build_args()
    if args.scan:
        run_scan(args)
    else:
        run_single(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
