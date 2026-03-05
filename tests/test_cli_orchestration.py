from __future__ import annotations

from argparse import Namespace
from pathlib import Path

import pytest

from rll import cli


def test_calcular_plano_execucao_synthetic(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    root = tmp_path
    monkeypatch.setattr(cli, "_repo_root", lambda: root)

    args = Namespace(data="synthetic", model="rll", with_bayes=False, with_covariance=False)
    plan = cli._calcular_plano_execucao(args)

    assert plan.script == root / "data" / "pipelines" / "structure_d" / "run_all.py"
    assert plan.warning_message is None


def test_calcular_plano_execucao_real_with_warning(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    root = tmp_path
    monkeypatch.setattr(cli, "_repo_root", lambda: root)

    args = Namespace(data="real", model="both", with_bayes=True, with_covariance=False)
    plan = cli._calcular_plano_execucao(args)

    assert plan.script == root / "docs" / "panteon_likelihood.py"
    assert "--model=both" in (plan.warning_message or "")


def test_validar_plano_execucao_raises_for_missing_script(tmp_path: Path) -> None:
    plan = cli.ExecutionPlan(script=tmp_path / "missing.py", model="rll")

    with pytest.raises(FileNotFoundError):
        cli._validar_plano_execucao(plan)


def test_persistir_execucao_returns_serializable_payload(tmp_path: Path) -> None:
    script = tmp_path / "flow.py"
    plan = cli.ExecutionPlan(script=script, model="lcdm")

    payload = cli._persistir_execucao(plan)

    assert payload == {"script": str(script), "model": "lcdm"}


def test_cmd_run_uses_orchestration_hooks(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    script = tmp_path / "flow.py"
    script.write_text("print('ok')\n", encoding="utf-8")
    plan = cli.ExecutionPlan(script=script, model="rll")
    args = Namespace(data="synthetic", model="rll", with_bayes=False, with_covariance=False)

    calls: list[str] = []

    def fake_calcular(received_args: Namespace) -> cli.ExecutionPlan:
        assert received_args is args
        calls.append("calcular")
        return plan

    def fake_validar(received_plan: cli.ExecutionPlan) -> None:
        assert received_plan is plan
        calls.append("validar")

    def fake_persistir(received_plan: cli.ExecutionPlan) -> dict[str, str]:
        assert received_plan is plan
        calls.append("persistir")
        return {"script": str(received_plan.script), "model": received_plan.model}

    def fake_logar(received_plan: cli.ExecutionPlan) -> None:
        assert received_plan is plan
        calls.append("logar")

    def fake_run_script(received_script: Path) -> None:
        assert received_script == script
        calls.append("run_script")

    monkeypatch.setattr(cli, "_calcular_plano_execucao", fake_calcular)
    monkeypatch.setattr(cli, "_validar_plano_execucao", fake_validar)
    monkeypatch.setattr(cli, "_persistir_execucao", fake_persistir)
    monkeypatch.setattr(cli, "_logar_execucao", fake_logar)
    monkeypatch.setattr(cli, "_run_script", fake_run_script)

    cli.cmd_run(args)

    assert calls == ["calcular", "validar", "persistir", "logar", "run_script"]
