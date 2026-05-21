from __future__ import annotations

import argparse
import runpy
import sys
from dataclasses import dataclass
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _run_script(path: Path, module: str | None = None) -> None:
    if module:
        repo = str(_repo_root())
        if repo not in sys.path:
            sys.path.insert(0, repo)
        original_argv = sys.argv[:]
        sys.argv = [str(path)]
        try:
            runpy.run_module(module, run_name="__main__", alter_sys=True)
        finally:
            sys.argv = original_argv
        return
    runpy.run_path(str(path), run_name="__main__")


def _select_real_flow(with_bayes: bool, with_covariance: bool) -> Path:
    root = _repo_root()
    if with_bayes or with_covariance:
        return root / "docs" / "panteon_likelihood.py"
    return root / "docs" / "rll_validation_real.py"


@dataclass(frozen=True)
class ExecutionPlan:
    script: Path
    model: str
    module: str | None = None
    warning_message: str | None = None


def _calcular_plano_execucao(args: argparse.Namespace) -> ExecutionPlan:
    root = _repo_root()

    if args.data == "synthetic":
        script = root / "data" / "pipelines" / "structure_d" / "run_all.py"
        module = "data.pipelines.structure_d.run_all"
    else:
        script = _select_real_flow(args.with_bayes, args.with_covariance)
        module = None

    warning_message = None
    if args.model != "rll":
        warning_message = (
            f"Aviso: --model={args.model} será tratado no fluxo comparativo já existente."
        )

    return ExecutionPlan(script=script, model=args.model, module=module, warning_message=warning_message)


def _validar_plano_execucao(plan: ExecutionPlan) -> None:
    if not plan.script.exists():
        raise FileNotFoundError(f"Script não encontrado: {plan.script}")


def _persistir_execucao(plan: ExecutionPlan) -> dict[str, str]:
    payload = {
        "script": str(plan.script),
        "model": plan.model,
    }
    if plan.module:
        payload["module"] = plan.module
    return payload


def _logar_execucao(plan: ExecutionPlan) -> None:
    if plan.warning_message:
        print(plan.warning_message)
    print(f"[rll] Executando fluxo: {plan.script}")


def cmd_run(args: argparse.Namespace) -> None:
    plan = _calcular_plano_execucao(args)
    _validar_plano_execucao(plan)
    _persistir_execucao(plan)
    _logar_execucao(plan)
    if plan.module:
        _run_script(plan.script, plan.module)
    else:
        _run_script(plan.script)


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
        choices=["rll", "lcdm", "both"],
        default="rll",
        help="Seleção de modelo (fluxos atuais executam comparativo RLL vs LCDM)",
    )
    run_parser.add_argument(
        "--with-bayes",
        action="store_true",
        help="No fluxo real, prioriza pipeline Pantheon+ com comparação AIC/BIC",
    )
    run_parser.add_argument(
        "--with-covariance",
        action="store_true",
        help="No fluxo real, prioriza pipeline Pantheon+ com matriz de covariância",
    )
    run_parser.set_defaults(func=cmd_run)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
