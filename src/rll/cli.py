from __future__ import annotations

import argparse
import json
import runpy
import sys
from dataclasses import dataclass
from pathlib import Path

from rll import eft_exhaustion, latentes


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _run_script(path: Path, module: str | None = None, script_args: list[str] | None = None) -> None:
    script_args = script_args or []
    original_argv = sys.argv[:]
    sys.argv = [str(path), *script_args]
    try:
        if module:
            repo = str(_repo_root())
            if repo not in sys.path:
                sys.path.insert(0, repo)
            runpy.run_module(module, run_name="__main__", alter_sys=True)
            return
        runpy.run_path(str(path), run_name="__main__")
    finally:
        sys.argv = original_argv


def _select_legacy_real_flow(with_bayes: bool, with_covariance: bool) -> Path:
    root = _repo_root()
    if with_bayes or with_covariance:
        return root / "docs" / "panteon_likelihood.py"
    return root / "docs" / "rll_validation_real.py"


def _pantheon_required_files() -> list[Path]:
    root = _repo_root()
    return [
        root / "data" / "pantheon" / "lcparam_full_long_zhel.txt",
        root / "data" / "pantheon" / "Pantheon+SH0ES_STAT+SYS.cov",
    ]


def _check_pantheon_files() -> tuple[list[Path], list[Path]]:
    required = _pantheon_required_files()
    missing = [path for path in required if not path.exists()]
    return required, missing


@dataclass(frozen=True)
class ExecutionPlan:
    script: Path
    model: str
    module: str | None = None
    script_args: tuple[str, ...] = ()
    warning_message: str | None = None


def _normalise_adversary(adversary: str) -> str:
    return "w0wa" if adversary == "w0waCDM" else adversary


def _real_model_selection_args(args: argparse.Namespace) -> list[str]:
    adversary = getattr(args, "adversary", "lcdm")
    forwarded = ["--adversary", _normalise_adversary(adversary)]
    if getattr(args, "with_bayes", False):
        forwarded.append("--with-bayes")
    if getattr(args, "with_growth", False):
        forwarded.append("--with-growth")
    if getattr(args, "bao_diagonal", False):
        forwarded.append("--bao-diagonal")
    return forwarded


def _calcular_plano_execucao(args: argparse.Namespace) -> ExecutionPlan:
    root = _repo_root()
    data = getattr(args, "data", "synthetic")
    model = getattr(args, "model", "rll")
    with_bayes = getattr(args, "with_bayes", False)
    with_covariance = getattr(args, "with_covariance", False)
    with_growth = getattr(args, "with_growth", False)
    adversary_supplied = hasattr(args, "adversary")
    adversary = getattr(args, "adversary", "lcdm")

    if data == "synthetic":
        script = root / "data" / "pipelines" / "structure_d" / "run_all.py"
        module = "data.pipelines.structure_d.run_all"
        warning_message = None
        script_args: tuple[str, ...] = ()
    else:
        use_model_selection = (adversary_supplied and adversary != "lcdm") or with_growth
        if use_model_selection:
            script = root / "rll_vs_lcdm.py"
            module = None
            script_args = tuple(_real_model_selection_args(args))
            warning_message = None
        else:
            script = _select_legacy_real_flow(with_bayes, with_covariance)
            module = None
            script_args = ()
            warning_message = (
                f"Aviso: --model={model} será tratado no fluxo real legado. "
                "Para comparação defensável use --adversary w0wa ou --adversary both."
            )

    if model not in {"rll", "both", "lcdm", "w0wa"}:
        warning_message = f"Aviso: --model={model} será tratado no fluxo comparativo disponível."

    return ExecutionPlan(
        script=script,
        model=model,
        module=module,
        script_args=script_args,
        warning_message=warning_message,
    )


def _validar_plano_execucao(plan: ExecutionPlan) -> None:
    if not plan.script.exists():
        raise FileNotFoundError(f"Script não encontrado: {plan.script}")


def _persistir_execucao(plan: ExecutionPlan) -> dict[str, object]:
    payload: dict[str, object] = {
        "script": str(plan.script),
        "model": plan.model,
    }
    if plan.script_args:
        payload["script_args"] = list(plan.script_args)
    if plan.module:
        payload["module"] = plan.module
    return payload


def _logar_execucao(plan: ExecutionPlan) -> None:
    if plan.warning_message:
        print(plan.warning_message)
    args_suffix = f" {' '.join(plan.script_args)}" if plan.script_args else ""
    print(f"[rll] Executando fluxo: {plan.script}{args_suffix}")


def cmd_run(args: argparse.Namespace) -> None:
    plan = _calcular_plano_execucao(args)
    _validar_plano_execucao(plan)
    _persistir_execucao(plan)
    _logar_execucao(plan)
    if plan.module or plan.script_args:
        _run_script(plan.script, plan.module, list(plan.script_args))
    else:
        _run_script(plan.script)


def cmd_preflight_real(args: argparse.Namespace) -> None:
    required, missing = _check_pantheon_files()
    payload = {
        "check": "preflight-real",
        "required": [str(path) for path in required],
        "missing": [str(path) for path in missing],
        "passed": not missing,
    }

    if getattr(args, "json", False):
        print(json.dumps(payload, indent=2, sort_keys=True))
    else:
        print("[rll] Preflight real-data validation (Pantheon+)")
        for path in required:
            status = "OK" if path.exists() else "MISSING"
            print(f" - {status}: {path}")
        if not missing:
            print("[rll] Preflight passed.")

    if missing:
        raise SystemExit(2)


def cmd_latentes(args: argparse.Namespace) -> None:
    forwarded = [
        "--catalog",
        str(args.catalog),
        "--schema",
        str(args.schema),
        "--root",
        str(args.root),
        args.latentes_command,
    ]
    if args.latentes_json:
        forwarded.append("--json")
    if args.dry_run:
        forwarded.append("--dry-run")
    if args.source_id:
        forwarded.extend(["--source-id", args.source_id])
    raise SystemExit(latentes.main(forwarded))


def cmd_eft_exhaust(args: argparse.Namespace) -> None:
    forwarded = [
        "--out-dir", str(args.out_dir),
        "--omega-m", str(args.omega_m),
        "--omega-r", str(args.omega_r),
        "--alpha", str(args.alpha),
        "--k", str(args.k),
        "--a-t", str(args.a_t),
        "--grid", str(args.grid),
    ]
    if args.omega_lambda is not None:
        forwarded.extend(["--omega-lambda", str(args.omega_lambda)])
    raise SystemExit(eft_exhaustion.main(forwarded))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="rll",
        description="CLI para execução dos fluxos do Relativity Living Light",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run_parser = subparsers.add_parser("run", help="Executa pipelines sintético ou real")
    run_parser.add_argument(
        "--data",
        choices=["synthetic", "real"],
        default="synthetic",
        help="Seleciona origem de dados/fluxo",
    )
    run_parser.add_argument(
        "--model",
        choices=["rll", "lcdm", "w0wa", "both"],
        default="rll",
        help="Seleção de modelo para fluxo comparativo",
    )
    run_parser.add_argument(
        "--adversary",
        choices=["lcdm", "w0wa", "w0waCDM", "both"],
        default="both",
        help="Adversário estatístico para o RLL no fluxo real",
    )
    run_parser.add_argument(
        "--with-bayes",
        action="store_true",
        help="No fluxo real, emite fator de Bayes aproximado via BIC/Schwarz",
    )
    run_parser.add_argument(
        "--with-growth",
        action="store_true",
        help="No fluxo real, registra gate fσ8/TOKEN_VAZIO sem fabricar crescimento de estrutura",
    )
    run_parser.add_argument(
        "--with-covariance",
        action="store_true",
        help="Compatibilidade com fluxo legado Pantheon+ com matriz de covariância",
    )
    run_parser.add_argument(
        "--bao-diagonal",
        action="store_true",
        help="No fluxo rll_vs_lcdm.py, força BAO diagonal sem covariância resumida",
    )
    run_parser.set_defaults(func=cmd_run)

    preflight_parser = subparsers.add_parser(
        "preflight-real",
        help="Valida presença dos arquivos Pantheon+ necessários para execução real",
    )
    preflight_parser.add_argument(
        "--json",
        action="store_true",
        help="Emite resultado em JSON para automação",
    )
    preflight_parser.set_defaults(func=cmd_preflight_real)


    eft_parser = subparsers.add_parser(
        "eft-exhaust",
        help="Executa motor conservador de exaustão/falsificação EFT do RLL",
    )
    eft_parser.add_argument("--out-dir", type=Path, default=Path("validacao_real/results/eft_exhaustion"))
    eft_parser.add_argument("--omega-m", type=float, default=0.315)
    eft_parser.add_argument("--omega-r", type=float, default=9.0e-5)
    eft_parser.add_argument("--omega-lambda", type=float, default=None)
    eft_parser.add_argument("--alpha", type=float, default=0.0)
    eft_parser.add_argument("--k", type=float, default=10.0)
    eft_parser.add_argument("--a-t", type=float, default=0.5)
    eft_parser.add_argument("--grid", type=int, default=256)
    eft_parser.set_defaults(func=cmd_eft_exhaust)

    latentes_parser = subparsers.add_parser(
        "latentes",
        help="Executa validação/orquestração seca do catálogo RLL-LATENTES",
    )
    latentes_parser.add_argument(
        "latentes_command",
        choices=["validate", "plan", "fetch", "score", "report", "verify"],
        help="Subcomando RLL-LATENTES",
    )
    latentes_parser.add_argument("--catalog", type=Path, default=latentes.DEFAULT_CATALOG)
    latentes_parser.add_argument("--schema", type=Path, default=latentes.DEFAULT_SCHEMA)
    latentes_parser.add_argument("--root", type=Path, default=Path("."))
    latentes_parser.add_argument("--source-id", default=None)
    latentes_parser.add_argument("--json", dest="latentes_json", action="store_true")
    latentes_parser.add_argument("--dry-run", action="store_true")
    latentes_parser.set_defaults(func=cmd_latentes)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
