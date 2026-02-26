#!/usr/bin/env python3
"""Validação editorial simples de links markdown para capítulos alterados."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable, List, Sequence

REPO_ROOT = Path(__file__).resolve().parent.parent
BOOK_DIR = REPO_ROOT / "book"

MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def git_changed_book_files(base_ref: str = "origin/main") -> List[Path]:
    cmd = [
        "git",
        "diff",
        "--name-only",
        "--diff-filter=ACMRT",
        f"{base_ref}...HEAD",
        "--",
        "book/*.md",
    ]
    result = subprocess.run(cmd, cwd=REPO_ROOT, check=False, capture_output=True, text=True)
    if result.returncode != 0:
        return []
    files = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    return [REPO_ROOT / f for f in files if Path(f).name != "README.md"]


def normalize_target(path_value: str) -> str:
    return path_value.split("#", 1)[0].split("?", 1)[0].strip()


def iter_relative_links(md_text: str) -> Iterable[str]:
    for target in MD_LINK_RE.findall(md_text):
        cleaned = normalize_target(target)
        if not cleaned:
            continue
        if cleaned.startswith(("http://", "https://", "mailto:", "tel:")):
            continue
        if cleaned.startswith("#"):
            continue
        yield cleaned



def validate_nav_sequence(file_path: Path, text: str) -> List[str]:
    errors: List[str] = []
    lowered = text.lower()
    required_tokens = ["capítulo anterior", "sumário", "capítulo próximo"]
    for token in required_tokens:
        if token not in lowered:
            errors.append(f"{file_path}: ausência de '{token}' no capítulo.")

    nav_line = ""
    for line in text.splitlines()[:12]:
        if "capítulo anterior" in line.lower() and "sumário" in line.lower() and "capítulo próximo" in line.lower():
            nav_line = line
            break

    if not nav_line:
        errors.append(f"{file_path}: linha de navegação (anterior/sumário/próximo) não encontrada no topo.")
        return errors

    nav_links = list(iter_relative_links(nav_line))
    if len(nav_links) < 2:
        errors.append(f"{file_path}: linha de navegação deve conter ao menos links relativos para sumário e capítulo vizinho.")
    else:
        for target in nav_links:
            target_path = (file_path.parent / target).resolve()
            if not target_path.exists():
                errors.append(f"{file_path}: link de navegação quebrado -> {target}")

    return errors


def validate_file(file_path: Path) -> List[str]:
    text = file_path.read_text(encoding="utf-8")
    errors: List[str] = []

    for target in iter_relative_links(text):
        target_path = (file_path.parent / target).resolve()
        if not target_path.exists():
            errors.append(f"{file_path}: link relativo quebrado -> {target}")

    errors.extend(validate_nav_sequence(file_path, text))
    return errors


def collect_target_files(args: Sequence[str]) -> List[Path]:
    if args:
        files = [Path(arg) for arg in args]
        return [p if p.is_absolute() else (REPO_ROOT / p) for p in files]

    changed = git_changed_book_files()
    if changed:
        return changed

    return sorted(p for p in BOOK_DIR.glob("*.md") if p.name != "README.md")


def main(argv: Sequence[str]) -> int:
    files = collect_target_files(argv[1:])

    if not files:
        print("Nenhum capítulo para validar.")
        return 0

    errors: List[str] = []
    for file_path in files:
        if not file_path.exists():
            errors.append(f"{file_path}: arquivo informado não existe.")
            continue
        errors.extend(validate_file(file_path))

    if errors:
        print("Validação de links: FALHA")
        for err in errors:
            print(f"- {err}")
        return 1

    print("Validação de links: OK (zero links relativos quebrados)")
    print(f"Capítulos validados: {len(files)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
