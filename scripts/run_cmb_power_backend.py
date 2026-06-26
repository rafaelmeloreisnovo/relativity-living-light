#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

RLL_BACKGROUND_C = Path("src/rll/class_rll_background.c")
RLL_KERNEL = Path("src/rll/rll_perturbation_kernel.py")
RLL_TRANSFER_CONTRACT = Path("src/rll/rll_transfer_bridge_contract.json")
RLL_CLASS_TRANSFER = Path("src/rll/class_transfer_adapter_contract.json")


def rll_background_status() -> dict:
    bg_exists = RLL_BACKGROUND_C.exists()
    kernel_exists = RLL_KERNEL.exists()
    transfer_contract_exists = RLL_TRANSFER_CONTRACT.exists()
    class_transfer_exists = RLL_CLASS_TRANSFER.exists()
    return {
        "rll_background_exact": bool(bg_exists),
        "background_source": str(RLL_BACKGROUND_C),
        "linear_perturbation_kernel": bool(kernel_exists),
        "kernel_source": str(RLL_KERNEL),
        "transfer_bridge_contract": bool(transfer_contract_exists),
        "transfer_contract_source": str(RLL_TRANSFER_CONTRACT),
        "class_transfer_adapter_contract": bool(class_transfer_exists),
        "class_transfer_source": str(RLL_CLASS_TRANSFER),
        "provides": ["E2(a)", "H/H0", "w_eff(a)", "Omega_m(a)", "Omega_s(a)", "dlnH_dlna", "delta_m(a)", "growth_rate(a)", "transfer handoff contract"],
        "perturbations_exact": "TOKEN_VAZIO",
        "linear_kernel_status": "linear_kernel_available_background_coupled" if kernel_exists else "TOKEN_VAZIO",
        "transfer_bridge": "contract_available" if transfer_contract_exists else "TOKEN_VAZIO",
        "class_transfer_adapter": "contract_available" if class_transfer_exists else "TOKEN_VAZIO",
        "cmb_cl_exact": "TOKEN_VAZIO",
        "nonlinear_pk_exact": "TOKEN_VAZIO",
    }


def rll_status(engine: str) -> dict:
    status = rll_background_status()
    status.update({
        "engine": engine,
        "available": True,
        "model": "rll",
        "status": "rll_exact_background_available",
        "extended_status": "rll_background_kernel_transfer_adapter_contract_available",
        "reason": "RLL exact background is present; linear kernel and transfer contracts may be present, while exact Cl and nonlinear P(k) still require native backend integration",
    })
    return status


def try_camb(args: argparse.Namespace) -> dict:
    if args.model == "rll":
        return rll_status("camb")
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
    results = camb.get_results(pars)
    cmb = results.get_cmb_power_spectra(pars, CMB_unit="muK")
    matter = results.get_matter_power_spectrum(minkh=args.kmin, maxkh=args.kmax, npoints=args.k_points)
    return {"engine": "camb", "available": True, "model": args.model, "nonlinear": bool(args.nonlinear), "cmb_keys": sorted(cmb.keys()), "matter_kh_sample": list(matter[0][: min(5, len(matter[0]))]), "matter_z": list(matter[1]), "matter_pk_first_row_sample": list(matter[2][0][: min(5, len(matter[2][0]))])}


def try_classy(args: argparse.Namespace) -> dict:
    if args.model == "rll":
        return rll_status("classy")
    try:
        from classy import Class  # type: ignore
    except Exception as exc:
        return {"engine": "classy", "available": False, "reason": repr(exc)}
    params = {"h": args.h, "Omega_b": args.omega_b, "Omega_cdm": args.omega_m - args.omega_b, "A_s": args.As, "n_s": args.ns, "tau_reio": args.tau, "output": "tCl,pCl,lCl,mPk", "l_max_scalars": args.lmax, "P_k_max_h/Mpc": args.kmax, "z_pk": ",".join(str(z) for z in args.redshifts), "non linear": "halofit" if args.nonlinear else "none"}
    if args.model == "w0wa":
        params.update({"Omega_fld": 1.0 - args.omega_m, "w0_fld": args.w0, "wa_fld": args.wa})
    cosmo = Class(); cosmo.set(params); cosmo.compute()
    cl = cosmo.raw_cl(args.lmax)
    pk_sample = {str(z): cosmo.pk(args.kmin * args.h, z) for z in args.redshifts}
    cosmo.struct_cleanup(); cosmo.empty()
    return {"engine": "classy", "available": True, "model": args.model, "nonlinear": bool(args.nonlinear), "cl_keys": sorted(cl.keys()), "pk_sample": pk_sample}


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
    out = Path(args.out_json); out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(summary, indent=2), encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
