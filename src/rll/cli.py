from __future__ import annotations

import argparse
import runpy
from pathlib import Path


def _repo_root() -> Path:
    return Path(__file__).resolve().parents[2]


def _run_script(path: Path) -> None:
    runpy.run_path(str(path), run_name="__main__")


def _select_real_flow(with_bayes: bool, with_covariance: bool) -> Path:
    root = _repo_root()
    if with_bayes or with_covariance:
        return root / "docs" / "panteon_likelihood.py"
    return root / "docs" / "rll_validation_real.py"


def cmd_run(args: argparse.Namespace) -> None:
    root = _repo_root()

    if args.data == "synthetic":
        script = root / "data" / "pipelines" / "structure_d" / "run_all.py"
    else:
        script = _select_real_flow(args.with_bayes, args.with_covariance)

    if args.model != "rll":
        print(f"Aviso: --model={args.model} será tratado no fluxo comparativo já existente.")

    print(f"[rll] Executando fluxo: {script}")
    _run_script(script)


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
