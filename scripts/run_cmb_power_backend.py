#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def try_camb(args: argparse.Namespace) -> dict:
    try:
        import camb  # type: ignore
        from camb import model  # type: ignore
    except Exception as exc:
        return {"engine": "camb", "available": False, "reason": repr(exc)}

    pars = camb.CAMBparams()
    ombh2 = args.omega_b * args.h * args.h
    omch2 = (args.omega_m - args.omega_b) * args.h * args.h
    pars.set_cosmology(H0=100.0 * args.h, ombh2=ombh2, omch2=omch2, mnu=args.mnu, omk=0.0, tau=args.tau)
    pars.InitPower.set_params(As=args.As, ns=args.ns)
    pars.set_for_lmax(args.lmax, lens_potential_accuracy=1)
    pars.set_matter_power(redshifts=args.redshifts, kmax=args.kmax)
    pars.NonLinear = model.NonLinear_both if args.nonlinear else model.NonLinear_none
    if args.model == "w0wa":
        pars.set_dark_energy(w=args.w0, wa=args.wa, dark_energy_model="ppf")
    if args.model == "rll":
        return {
            "engine": "camb",
            "available": True,
            "model": "rll",
            "status": "TOKEN_VAZIO",
            "reason": "stock CAMB does not implement the RLL logistic background; use lcdm/w0wa or add a custom background module",
        }
    results = camb.get_results(pars)
    cmb = results.get_cmb_power_spectra(pars, CMB_unit="muK")
    matter = results.get_matter_power_spectrum(minkh=args.kmin, maxkh=args.kmax, npoints=args.k_points)
    return {
        "engine": "camb",
        "available": True,
        "model": args.model,
        "nonlinear": bool(args.nonlinear),
        "cmb_keys": sorted(cmb.keys()),
        "matter_kh_sample": list(matter[0][: min(5, len(matter[0]))]),
        "matter_z": list(matter[1]),
        "matter_pk_first_row_sample": list(matter[2][0][: min(5, len(matter[2][0]))]),
    }


def try_classy(args: argparse.Namespace) -> dict:
    try:
        from classy import Class  # type: ignore
    except Exception as exc:
        return {"engine": "classy", "available": False, "reason": repr(exc)}
    if args.model == "rll":
        return {
            "engine": "classy",
            "available": True,
            "model": "rll",
            "status": "TOKEN_VAZIO",
            "reason": "stock CLASS needs a custom RLL background module for exact logistic RLL perturbations",
        }
    params = {
        "h": args.h,
        "Omega_b": args.omega_b,
        "Omega_cdm": args.omega_m - args.omega_b,
        "A_s": args.As,
        "n_s": args.ns,
        "tau_reio": args.tau,
        "output": "tCl,pCl,lCl,mPk",
        "l_max_scalars": args.lmax,
        "P_k_max_h/Mpc": args.kmax,
        "z_pk": ",".join(str(z) for z in args.redshifts),
        "non linear": "halofit" if args.nonlinear else "none",
    }
    if args.model == "w0wa":
        params.update({"Omega_fld": 1.0 - args.omega_m, "w0_fld": args.w0, "wa_fld": args.wa})
    cosmo = Class()
    cosmo.set(params)
    cosmo.compute()
    cl = cosmo.raw_cl(args.lmax)
    pk_sample = {str(z): cosmo.pk(args.kmin * args.h, z) for z in args.redshifts}
    cosmo.struct_cleanup()
    cosmo.empty()
    return {
        "engine": "classy",
        "available": True,
        "model": args.model,
        "nonlinear": bool(args.nonlinear),
        "cl_keys": sorted(cl.keys()),
        "pk_sample": pk_sample,
    }


def build_parser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser()
    ap.add_argument("--engine", choices=["auto", "camb", "classy"], default="auto")
    ap.add_argument("--model", choices=["lcdm", "w0wa", "rll"], default="lcdm")
    ap.add_argument("--nonlinear", action="store_true")
    ap.add_argument("--h", type=float, default=0.674)
    ap.add_argument("--omega-m", type=float, default=0.315)
    ap.add_argument("--omega-b", type=float, default=0.049)
    ap.add_argument("--mnu", type=float, default=0.06)
    ap.add_argument("--tau", type=float, default=0.054)
    ap.add_argument("--As", type=float, default=2.1e-9)
    ap.add_argument("--ns", type=float, default=0.965)
    ap.add_argument("--w0", type=float, default=-1.0)
    ap.add_argument("--wa", type=float, default=0.0)
    ap.add_argument("--lmax", type=int, default=2500)
    ap.add_argument("--kmin", type=float, default=1.0e-4)
    ap.add_argument("--kmax", type=float, default=10.0)
    ap.add_argument("--k-points", type=int, default=200)
    ap.add_argument("--redshifts", type=float, nargs="+", default=[0.0, 0.5, 1.0, 2.0])
    ap.add_argument("--out-json", default="results/cmb_power_backend_summary.json")
    return ap


def main() -> None:
    args = build_parser().parse_args()
    attempts = []
    if args.engine in ("auto", "camb"):
        attempts.append(try_camb(args))
    if args.engine in ("auto", "classy") and not any(a.get("available") for a in attempts):
        attempts.append(try_classy(args))
    summary = {"request": vars(args), "attempts": attempts}
    out = Path(args.out_json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
