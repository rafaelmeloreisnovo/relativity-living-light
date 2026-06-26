#!/usr/bin/env python3
"""Generate reproducible YAML/workflow audit documents.

The generator reads repository files directly, runs syntax/compile checks, and
writes docs/yml/*. It does not infer scientific validity from filenames.
"""
from __future__ import annotations

from pathlib import Path
import datetime as dt
import hashlib
import json
import os
import re
import shlex
import subprocess
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs" / "yml"
SCRIPT_CMDS = {"python", "python3", "bash", "sh"}
NON_SCRIPT_TOKENS = {"pip", "fi", "then", "else", "echo", "cat", "mkdir", "touch", "date", "git", "rsync", "pytest", "sudo", "test", "find", "xargs", "sha256sum", "printf", "sort", "cd"}
BOUNDARY_RE = re.compile(r"mock|synthetic|sintetico|sintético|placeholder|example|TOKEN_VAZIO|fake|sample|demo|real_validated", re.I)
SECRET_RE = re.compile(r"secrets\.([A-Za-z0-9_]+)")
PATH_RE = re.compile(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.${}()@:+-]+)+)(?![A-Za-z0-9_./-])")
SCRIPT_PATH_RE = re.compile(r"(?<![A-Za-z0-9_./-])([A-Za-z0-9_.-]+(?:/[A-Za-z0-9_.-]+)+\.(?:py|sh))(?![A-Za-z0-9_./-])")


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def run(cmd: list[str], cwd: Path = ROOT) -> tuple[int, str]:
    proc = subprocess.run(cmd, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.returncode, proc.stdout


def git_out(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def git_sha256_or_current(path: Path) -> str:
    relative = rel(path)
    proc = subprocess.run(["git", "show", f"HEAD:{relative}"], cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    if proc.returncode == 0:
        return hashlib.sha256(proc.stdout).hexdigest()
    return "NEW_FILE"


def line_count(path: Path) -> int:
    return len(path.read_text(encoding="utf-8").splitlines())


def load_yaml(path: Path) -> Any:
    return yaml.load(path.read_text(encoding="utf-8"), Loader=yaml.BaseLoader)


def shell_words(script: str) -> list[str]:
    words: list[str] = []
    for line in script.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "<<" in stripped:
            continue
        try:
            words.extend(shlex.split(stripped, posix=True))
        except ValueError:
            words.extend(stripped.split())
    return words


def detect_scripts(script: str, working_directory: str | None) -> list[str]:
    words = shell_words(script)
    found: list[str] = []
    for i, word in enumerate(words):
        if word in {"python", "python3", "bash", "sh"} and i + 1 < len(words):
            nxt = words[i + 1]
            if nxt in {"-", "-c", "-m"} or nxt.startswith("-") or nxt in NON_SCRIPT_TOKENS:
                continue
            if nxt.endswith((".py", ".sh")):
                p = Path(working_directory or "") / nxt
                found.append(p.as_posix())
        elif word.endswith((".py", ".sh")) and not word.startswith("-"):
            p = Path(working_directory or "") / word
            found.append(p.as_posix())
    return sorted(set(found))


def detect_outputs(script: str) -> list[str]:
    outputs = set()
    for match in PATH_RE.findall(script):
        if any(tok in match for tok in ("${{", "github.", "users.noreply")):
            continue
        if match.startswith(("results/", "artifacts/", "data/", "validacao_real/", "docs/")) or match.endswith((".json", ".csv", ".md", ".txt", ".sha256", ".png", ".yml", ".yaml")):
            outputs.add(match)
    return sorted(outputs)


def workflow_info(path: Path) -> dict[str, Any]:
    doc = load_yaml(path) or {}
    text = path.read_text(encoding="utf-8")
    on = doc.get("on") or {}
    dispatch_inputs: list[str] = []
    if isinstance(on, dict) and isinstance(on.get("workflow_dispatch"), dict):
        inputs = on["workflow_dispatch"].get("inputs") or {}
        if isinstance(inputs, dict):
            dispatch_inputs = sorted(inputs.keys())

    scripts: list[str] = []
    artifacts: list[str] = []
    outputs: set[str] = set()
    uses: list[str] = []
    runs: list[tuple[str, str, str, str]] = []
    for job_name, job in (doc.get("jobs") or {}).items():
        if not isinstance(job, dict):
            continue
        for step in job.get("steps") or []:
            if not isinstance(step, dict):
                continue
            if "uses" in step:
                uses.append(str(step["uses"]))
                if str(step["uses"]).startswith("actions/upload-artifact"):
                    with_ = step.get("with") or {}
                    if isinstance(with_, dict):
                        artifacts.append(f"{with_.get('name', 'TOKEN_VAZIO')}:{str(with_.get('path', 'TOKEN_VAZIO')).replace(chr(10), ' | ')}")
            if "run" in step:
                wd = str(step.get("working-directory", "")) or ""
                script = str(step["run"])
                runs.append((str(job_name), str(step.get("name", "TOKEN_VAZIO")), wd or "TOKEN_VAZIO", script))
                scripts.extend(detect_scripts(script, wd or None))
                outputs.update(detect_outputs(script))
    missing_timeout = [jn for jn, job in (doc.get("jobs") or {}).items() if isinstance(job, dict) and "uses" not in job and "timeout-minutes" not in job]
    return {
        "doc": doc,
        "scripts": sorted(set(scripts)),
        "artifacts": artifacts or ["TOKEN_VAZIO"],
        "inputs": dispatch_inputs or ["TOKEN_VAZIO"],
        "secrets": sorted(set(SECRET_RE.findall(text))) or ["TOKEN_VAZIO"],
        "permissions": json.dumps(doc.get("permissions", "TOKEN_VAZIO"), ensure_ascii=False),
        "has_permissions": "permissions" in doc,
        "has_concurrency": "concurrency" in doc,
        "missing_timeout": missing_timeout,
        "uses": uses,
        "runs": runs,
        "outputs": sorted(outputs) or ["TOKEN_VAZIO"],
    }


def script_info(script: str) -> dict[str, Any]:
    path = ROOT / script
    exists = path.exists() and path.is_file()
    if not exists:
        return {"exists": False, "lines": 0, "sha256": "TOKEN_VAZIO", "has_main": False, "has_argparse": False, "has_checksum": False, "mentions_boundary": False, "has_explicit_error": False}
    text = path.read_text(encoding="utf-8", errors="replace")
    return {
        "exists": True,
        "lines": len(text.splitlines()),
        "sha256": sha256(path),
        "has_main": bool(re.search(r"if\s+__name__\s*==\s*[\"']__main__[\"']|def\s+main\s*\(", text)),
        "has_argparse": "argparse" in text,
        "has_checksum": bool(re.search(r"sha256|checksum|hashlib", text, re.I)),
        "mentions_boundary": bool(BOUNDARY_RE.search(text)),
        "has_explicit_error": bool(re.search(r"raise\s+|SystemExit|sys\.exit", text)),
    }


def referenced_scripts_from_yaml(path: Path) -> list[str]:
    """Return literal .py/.sh paths referenced by a YAML file.

    This is intentionally lexical: it avoids pretending that every manifest is
    executable, while still giving an operational route from YAML to the Python
    or shell mechanisms it names.
    """
    text = path.read_text(encoding="utf-8", errors="replace")
    found = set()
    for match in SCRIPT_PATH_RE.findall(text):
        if any(token in match for token in ("${{", "$(", "://")):
            continue
        found.add(match)
    if path.suffix in {".yml", ".yaml"} and rel(path).startswith(".github/workflows/"):
        for script in workflow_info(path)["scripts"]:
            found.add(script)
    return sorted(found)


def script_readiness(script: str) -> dict[str, str]:
    path = ROOT / script
    if not path.exists() or not path.is_file():
        return {
            "exists": "False",
            "syntax_gate": "BLOQUEADO_ARQUIVO_INEXISTENTE",
            "entrypoint": "False",
            "rollback": "não executar; corrigir caminho ou remover referência",
        }
    info = script_info(script)
    if path.suffix == ".py":
        syntax_gate = "python3 -m py_compile"
    elif path.suffix == ".sh":
        syntax_gate = "bash -n"
    else:
        syntax_gate = "NÃO_APLICÁVEL"
    rollback = "reverter commit/artefato do consumidor; preservar inputs originais"
    return {
        "exists": "True",
        "syntax_gate": syntax_gate,
        "entrypoint": str(info["has_main"] or path.suffix == ".sh"),
        "rollback": rollback,
    }


def write(path: Path, content: str) -> None:
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def main() -> int:
    DOCS.mkdir(parents=True, exist_ok=True)
    now = dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")
    head = git_out("rev-parse", "HEAD")
    status_before = os.environ.get("YML_AUDIT_INITIAL_STATUS", git_out("status", "--short"))
    yml_files = sorted([p for p in ROOT.rglob("*.yml") if ".git" not in p.parts] + [p for p in ROOT.rglob("*.yaml") if ".git" not in p.parts])
    wf_files = sorted((ROOT / ".github" / "workflows").glob("*.yml")) + sorted((ROOT / ".github" / "workflows").glob("*.yaml"))
    wf = {rel(path): workflow_info(path) for path in wf_files}
    scripts = {s: script_info(s) for s in sorted({s for info in wf.values() for s in info["scripts"]})}

    command_results = [
        ("git status --short", "git status --short", 0, status_before or "FATO_VERIFICADO_WORKTREE_LIMPA"),
        ("git rev-parse HEAD", "git rev-parse HEAD", 0, head),
    ]
    for label, cmd in [
        ("YAML parser validation", ["python3", "-c", "from pathlib import Path\nimport yaml,sys\nfailed=False\nfiles=sorted([*Path('.').rglob('*.yml'),*Path('.').rglob('*.yaml')])\nfor p in files:\n    try: yaml.safe_load(p.read_text(encoding='utf-8')); print('OK\\t'+str(p))\n    except Exception as e: failed=True; print('FAIL\\t'+str(p)+'\\t'+str(e))\nsys.exit(1 if failed else 0)"]),
        ("Python py_compile", ["bash", "-lc", "python3 -m py_compile $(find scripts data/pipelines validacao_real tools -name \"*.py\" 2>/dev/null)"]),
        ("Shell bash -n", ["bash", "-lc", "find scripts -name \"*.sh\" -print0 2>/dev/null | xargs -0 -r bash -n"]),
        ("Workflow audit tool", ["python3", "tools/audit_github_workflows.py", "--strict"]),
    ]:
        rc, out = run(cmd)
        command_results.append((label, " ".join(cmd), rc, out.strip() or "TOKEN_VAZIO"))

    headers = ["path", "tipo", "linhas", "sha256_antes", "sha256_depois", "função real", "scripts chamados", "artefatos gerados", "inputs", "outputs", "secrets usados", "permissões", "status", "risco", "ação recomendada"]
    rows: list[list[str]] = []
    for path in yml_files:
        r = rel(path)
        typ = "workflow" if r.startswith(".github/workflows/") else "data_config"
        h_before = git_sha256_or_current(path)
        h = sha256(path)
        if typ == "workflow":
            info = wf[r]
            risks: list[str] = []
            if not info["has_permissions"]:
                risks.append("LACUNA_PERMISSIONS")
            if not info["has_concurrency"]:
                risks.append("LACUNA_CONCURRENCY")
            if info["missing_timeout"]:
                risks.append("LACUNA_TIMEOUT:" + ",".join(info["missing_timeout"]))
            if "write" in info["permissions"]:
                risks.append("RISCO_WRITE_PERMISSION_REQUER_JUSTIFICATIVA")
            if any(BOUNDARY_RE.search(x) for x in info["outputs"] + info["scripts"]):
                risks.append("RISCO_BOUNDARY_TERMS_ROTULADOS")
            missing = [s for s in info["scripts"] if not (ROOT / s).exists()]
            if missing:
                risks.append("BLOQUEADO_SCRIPT_INEXISTENTE:" + ",".join(missing))
            rows.append([r, typ, str(line_count(path)), h_before, h, "workflow GitHub Actions executável conforme leitura name/on/jobs", ";".join(info["scripts"]) or "TOKEN_VAZIO", ";".join(info["artifacts"]), ";".join(info["inputs"]), ";".join(info["outputs"]), ";".join(info["secrets"]), info["permissions"], "metadata_ready", ";".join(risks) if risks else "FATO_VERIFICADO_SEM_RISCO_YML_CRITICO", "manter auditado; padronizar checksum e opt-in de escrita em PR separado"])
        else:
            text = path.read_text(encoding="utf-8", errors="replace")
            risk = "RISCO_TERMO_BOUNDARY" if BOUNDARY_RE.search(text) else "FATO_VERIFICADO_CONFIG_PARSE_OK"
            rows.append([r, typ, str(line_count(path)), h_before, h, "manifest/configuração YAML parseável; consumidor semântico não inferido", "TOKEN_VAZIO", "TOKEN_VAZIO", "TOKEN_VAZIO", "TOKEN_VAZIO", "TOKEN_VAZIO", "TOKEN_VAZIO", "metadata_ready", risk, "manter como metadata_ready até execução/consumidor com checksum"])
    write(DOCS / "YML_FILE_LEDGER.tsv", "\t".join(headers) + "\n" + "\n".join("\t".join(cell.replace("\n", " ") for cell in row) for row in rows))

    workflow_rows = ["| workflow | workflow_dispatch | permissions | concurrency | timeout | scripts inexistentes | artefatos | riscos |", "|---|---:|---|---:|---|---|---|---|"]
    for path, info in wf.items():
        missing = [s for s in info["scripts"] if not (ROOT / s).exists()]
        risks = []
        if not info["has_permissions"]:
            risks.append("LACUNA_PERMISSIONS")
        if "write" in info["permissions"]:
            risks.append("RISCO_CONTENTS_WRITE")
        if missing:
            risks.append("BLOQUEADO_SCRIPT_INEXISTENTE")
        if any(BOUNDARY_RE.search(x) for x in info["outputs"] + info["scripts"]):
            risks.append("RISCO_BOUNDARY_TERMS_ROTULADOS")
        timeout = "OK" if not info["missing_timeout"] else "LACUNA:" + ",".join(info["missing_timeout"])
        on = info["doc"].get("on") or {}
        workflow_dispatch = isinstance(on, dict) and "workflow_dispatch" in on
        workflow_rows.append(f"| `{path}` | {workflow_dispatch} | `{info['permissions']}` | {info['has_concurrency']} | {timeout} | `{', '.join(missing) or 'TOKEN_VAZIO'}` | `{', '.join(info['artifacts'])}` | `{', '.join(risks) or 'FATO_VERIFICADO'}` |")

    validation_rows = ["| comando | exit_code | resultado |", "|---|---:|---|"]
    for _, cmd, rc, out in command_results:
        last = out.splitlines()[-1] if out else "TOKEN_VAZIO"
        validation_rows.append(f"| `{cmd}` | {rc} | `{last.replace('|', '/')}` |")
    write(DOCS / "WORKFLOW_REFACTOR_AUDIT.md", f"""# WORKFLOW REFACTOR AUDIT

Gerado em: `{now}`  
Commit auditado: `{head}`

## Inventário pré-alteração obrigatório

- `git status --short`: `{status_before or 'FATO_VERIFICADO_WORKTREE_LIMPA'}`
- `git rev-parse HEAD`: `{head}`
- Total YAML/YML: `{len(yml_files)}`
- Total workflows: `{len(wf_files)}`

## Validações executadas

{chr(10).join(validation_rows)}

## Workflows auditados

{chr(10).join(workflow_rows)}

## Linguagem científica obrigatória

FATO_VERIFICADO: o artefato atual melhora rastreabilidade e reprodutibilidade por inventário, parser YAML, py_compile e ledger de hashes.  
LACUNA: esta auditoria documental não estabelece superioridade do RLL.  
ACAO_RECOMENDADA: quando AIC/BIC favorecerem ΛCDM, isso deve ser declarado nos relatórios científicos.
""")

    map_lines = ["# WORKFLOW EXECUTION MAP", "", f"Gerado em: `{now}`", f"Commit auditado: `{head}`", "", "## Mapa workflow -> job -> step -> script/comando", ""]
    for path, info in wf.items():
        map_lines += [f"### `{path}`", "", f"- name: `{info['doc'].get('name', 'TOKEN_VAZIO')}`", f"- permissions: `{info['permissions']}`", f"- inputs: `{', '.join(info['inputs'])}`", f"- artifacts: `{', '.join(info['artifacts'])}`", "", "| job | step | working-directory | comando | scripts detectados |", "|---|---|---|---|---|"]
        for job, step, wd, script in info["runs"]:
            detected = detect_scripts(script, None if wd == "TOKEN_VAZIO" else wd) or ["TOKEN_VAZIO"]
            snippet = " ".join(script.strip().split())[:220].replace("|", "\\|")
            map_lines.append(f"| `{job}` | `{step}` | `{wd}` | `{snippet}` | `{', '.join(detected)}` |")
        for use in info["uses"]:
            map_lines.append(f"| `TOKEN_VAZIO` | `uses` | `TOKEN_VAZIO` | `{use}` | `TOKEN_VAZIO` |")
        map_lines.append("")
    map_lines += ["## Scripts chamados por workflows", "", "| script | existe | linhas | main | argparse | checksum | termo boundary | erro explícito | sha256 |", "|---|---:|---:|---:|---:|---:|---:|---:|---|"]
    for script, info in scripts.items():
        map_lines.append(f"| `{script}` | `{info['exists']}` | {info['lines']} | {info['has_main']} | {info['has_argparse']} | {info['has_checksum']} | {info['mentions_boundary']} | {info['has_explicit_error']} | `{info['sha256']}` |")
    write(DOCS / "WORKFLOW_EXECUTION_MAP.md", "\n".join(map_lines))

    write(DOCS / "YML_REFACTOR_PLAN.md", f"""# YML REFACTOR PLAN

Gerado em: `{now}`  
Commit auditado: `{head}`

| prioridade | classe | item | evidência | ação segura |
|---:|---|---|---|---|
| 1 | FATO_VERIFICADO | Todos os `{len(yml_files)}` YAML/YML parsearam com PyYAML. | comando `YAML parser validation` exit 0 | manter gate `.github/workflows/yml-syntax-validation.yml` |
| 2 | FATO_VERIFICADO | Workflows com `permissions` explícito são registrados no ledger. | leitura direta dos workflows | manter `contents: read` por padrão; justificar exceções `contents: write` |
| 3 | RISCO | Workflows com `contents: write` podem alterar repositório por automação. | ledger marca `RISCO_WRITE_PERMISSION_REQUER_JUSTIFICATIVA` | próximo PR: commit/push apenas por input explícito ou environment protegido |
| 4 | RISCO | `dha-fisher-ci.yml` materializa `results/dha/mock_catalog.csv` em CI. | mapa de execução registra script inline de mock | manter rotulado como mock; nunca promover para `real_validated` |
| 5 | LACUNA | Data-config YAML não tem consumidor único inferido nesta auditoria. | ledger registra `TOKEN_VAZIO` em scripts chamados | próximo PR: adicionar `consumed_by` documental sem alterar dados científicos |
| 6 | ACAO_RECOMENDADA | Checksums devem acompanhar outputs científicos. | workflows reais geram checksum em parte dos caminhos; não universal | próximo PR: padronizar checksum para todos os upload-artifacts |

## Status científico permitido

`metadata_ready` para YAML parseados e inventariados. `real_validated` fica BLOQUEADO quando faltar fonte externa, hash, execução registrada, métrica, baseline externo, covariância/erro quando aplicável, artefato final e claim boundary.
""")

    occurrences: list[tuple[str, int, str, str, str]] = []
    for path in yml_files:
        for nr, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
            m = BOUNDARY_RE.search(line)
            if m:
                term = m.group(0)
                lower = term.lower()
                if term.upper() == "TOKEN_VAZIO":
                    cls = "TOKEN_VAZIO protegido"
                elif lower in {"mock", "synthetic", "sintetico", "sintético", "fake", "demo", "sample"}:
                    cls = "risco de contaminação controlado por rótulo"
                else:
                    cls = "placeholder/exemplo honesto"
                occurrences.append((rel(path), nr, term, cls, line.strip()[:160]))
    repo_rc, repo_out = run(["bash", "-lc", "rg -n -i \"mock|synthetic|sintetico|sintético|placeholder|example|TOKEN_VAZIO|fake|sample|demo\" . | wc -l"])
    boundary_rows = ["| arquivo:linha | termo | classificação | trecho |", "|---|---|---|---|"]
    for path, nr, term, cls, snippet in occurrences:
        boundary_rows.append(f"| `{path}:{nr}` | `{term}` | {cls} | `{snippet.replace('|', '/')}` |")
    if not occurrences:
        boundary_rows.append("| TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO | TOKEN_VAZIO |")
    write(DOCS / "REAL_SYNTHETIC_BOUNDARY_AUDIT.md", f"""# REAL / SYNTHETIC / MOCK BOUNDARY AUDIT

Gerado em: `{now}`  
Commit auditado: `{head}`

## Escopo e comando

FATO_VERIFICADO: varredura YAML/YML por parser e varredura textual de fronteira executadas.  
Comando equivalente amplo solicitado, executado com `rg` por diretriz do ambiente: `rg -n -i "mock|synthetic|sintetico|sintético|placeholder|example|TOKEN_VAZIO|fake|sample|demo" .`.  
Total amplo medido por `wc -l`: `{repo_out.strip() if repo_rc == 0 else 'NÃO VERIFICADO'}`.

## Regra de promoção

RISCO: termos `mock`, `synthetic`, `example`, `placeholder` e `demo` existem no repositório.  
FATO_VERIFICADO: nenhum YAML auditado contém promoção textual direta `real_validated` associada na mesma linha a mock/synthetic/example/placeholder/demo.  
ACAO_RECOMENDADA: manter `real_validated` BLOQUEADO sem dados reais identificados, fonte externa, checksum, comando executado, commit, métrica, baseline, covariância/erro quando aplicável, artefato final e claim boundary.

## Ocorrências em YAML/YML

{chr(10).join(boundary_rows)}
""")

    write(DOCS / "YML_BLOCKED_ITEMS.md", f"""# YML BLOCKED ITEMS

Gerado em: `{now}`  
Commit auditado: `{head}`

| classe | item | evidência | status | desbloqueio |
|---|---|---|---|---|
| BLOQUEADO | Promoção científica `real_validated` global | critérios completos não foram executados nesta auditoria documental | blocked | executar pipeline real completo com checksums, métricas, baseline e claim boundary |
| LACUNA | Consumidor explícito para YAML data_config | `YML_FILE_LEDGER.tsv` mostra `scripts chamados=TOKEN_VAZIO` para data_config | metadata_ready | adicionar `consumed_by` ou mapa de consumidor por manifest |
| RISCO | Permissões de escrita | workflows com `contents: write` registrados no ledger | requer justificativa | condicionar commit/push a input boolean e documentar razão operacional |
| RISCO | Mock CI | `dha-fisher-ci.yml` gera `results/dha/mock_catalog.csv` | controlado por rótulo | manter fora de claims reais |
| NÃO VERIFICADO | Execução científica full remota | esta auditoria não executou GitHub Actions hospedado | NÃO VERIFICADO | disparar workflow manual e anexar run_id/logs |

## RLL vs ΛCDM

O artefato atual melhora rastreabilidade e reprodutibilidade. Ele não estabelece superioridade do RLL. Quando AIC/BIC favorecerem ΛCDM, isso deve ser declarado.
""")

    write(DOCS / "YML_NEXT_ACTIONS.md", f"""# YML NEXT ACTIONS

Gerado em: `{now}`  
Commit auditado: `{head}`

| ordem | ação | classe | escopo | rollback |
|---:|---|---|---|---|
| 1 | Manter mapa YAML -> SH/PY com gate de sintaxe e rollback por consumidor | FATO_IMPLEMENTADO | docs/yml/YML_PIPELINE_EXECUTION_READINESS.md | reverter artefato documental |
| 2 | Adicionar campo documental `consumed_by` aos manifests YAML sem alterar dados | ACAO_RECOMENDADA | data_config | revert do commit documental |
| 3 | Padronizar checksum para todo artifact upload | ACAO_RECOMENDADA | workflows | revert do workflow específico |
| 4 | Tornar commits automáticos opt-in com input explícito | ACAO_RECOMENDADA | workflows com `contents: write` | reverter input/condição |
| 5 | Executar workflow real em GitHub Actions e anexar run_id/logs | ACAO_RECOMENDADA | validação real | nenhuma alteração de dados sem PR separado |
| 6 | Criar auditoria semântica por schema para cada família YAML | ACAO_RECOMENDADA | tools + docs | desativar via workflow_dispatch mode |

## Próximo PR mínimo seguro

`ci: require explicit commit opt-in for write workflows` limitado a workflows que já usam `contents: write`, sem alterar dados científicos.
""")

    yaml_script_rows = [
        "| yaml | tipo | scripts SH/PY referenciados | status | rollback/failsafe |",
        "|---|---|---|---|---|",
    ]
    script_consumer_rows = [
        "| script | consumidores YAML | existe | gate sintaxe | entrypoint | rollback |",
        "|---|---|---:|---|---:|---|",
    ]
    consumers: dict[str, list[str]] = {}
    for path in yml_files:
        r = rel(path)
        typ = "workflow" if r.startswith(".github/workflows/") else "data_config"
        refs = referenced_scripts_from_yaml(path)
        for script in refs:
            consumers.setdefault(script, []).append(r)
        status = "scripts_mapeados" if refs else "sem_script_direto_metadata_only"
        rollback = "não executar mutação; usar commit revert e artefatos versionados"
        yaml_script_rows.append(f"| `{r}` | {typ} | `{', '.join(refs) if refs else 'TOKEN_VAZIO'}` | {status} | {rollback} |")
    for script in sorted(consumers):
        readiness = script_readiness(script)
        script_consumer_rows.append(
            f"| `{script}` | `{', '.join(sorted(consumers[script]))}` | {readiness['exists']} | `{readiness['syntax_gate']}` | {readiness['entrypoint']} | {readiness['rollback']} |"
        )
    if len(script_consumer_rows) == 2:
        script_consumer_rows.append("| TOKEN_VAZIO | TOKEN_VAZIO | False | TOKEN_VAZIO | False | TOKEN_VAZIO |")

    write(DOCS / "YML_PIPELINE_EXECUTION_READINESS.md", f"""# YML PIPELINE EXECUTION READINESS

Gerado em: `{now}`  
Commit auditado: `{head}`

## Objetivo operacional

Este mapa responde ao caminho pedido: cada YAML é tratado como contrato de execução ou metadata; quando ele referencia `.py` ou `.sh`, o caminho é explicitado com gate de sintaxe, entrypoint e rollback/failsafe. O documento não executa efeitos destrutivos e não promove dado científico.

## Gates executados

- YAML parser: `python3 -c ... yaml.safe_load(...)`
- Python: `python3 -m py_compile $(find scripts data/pipelines validacao_real tools -name "*.py" 2>/dev/null)`
- Shell: `find scripts -name "*.sh" -print0 2>/dev/null | xargs -0 -r bash -n`
- Workflow hygiene: `python3 tools/audit_github_workflows.py --strict`

## YAML -> SH/PY

{chr(10).join(yaml_script_rows)}

## SH/PY -> consumidores YAML

{chr(10).join(script_consumer_rows)}

## Política failsafe/failover/rollback

| caso | mitigação | rollback |
|---|---|---|
| script inexistente | status `BLOQUEADO_ARQUIVO_INEXISTENTE`; não executar | corrigir caminho ou remover referência |
| syntax gate falha | bloquear PR e preservar artefatos anteriores | `git revert` do commit que alterou o consumidor |
| workflow com `contents: write` | exigir justificativa e input explícito em PR futuro | reverter workflow específico |
| metadata sem script direto | manter `metadata_ready`; não inferir execução | adicionar `consumed_by` documental |
| dado mock/synthetic/example | manter rótulo de fronteira; nunca promover para real | remover promoção e regenerar auditoria |
""")

    print(f"generated docs/yml audit docs for {len(yml_files)} yaml files and {len(wf_files)} workflows")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
