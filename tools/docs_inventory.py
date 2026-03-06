#!/usr/bin/env python3
"""Gera e valida inventário completo de .md/.zip do repositório."""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import re
import subprocess
from pathlib import Path
from zipfile import BadZipFile, ZipFile

COUNT_PATTERN = re.compile(r"\*\*Total de arquivos catalogados:\*\*\s*(\d+)")


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def rel_posix(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def first_heading(md_path: Path) -> str:
    try:
        with md_path.open("r", encoding="utf-8", errors="replace") as handle:
            for raw in handle:
                line = raw.strip()
                if line.startswith("#"):
                    return line.lstrip("#").strip()[:120] or "(sem título)"
    except OSError:
        return "(erro de leitura)"
    return "(sem heading)"


def zip_summary(zip_path: Path) -> str:
    try:
        with ZipFile(zip_path, "r") as zf:
            return f"{len(zf.infolist())} entradas"
    except (OSError, BadZipFile):
        return "(zip inválido)"


def sha256_short(file_path: Path, size: int = 12) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as handle:
        while True:
            chunk = handle.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()[:size]


def collect_items(root: Path) -> list[dict[str, str | int]]:
    items: list[dict[str, str | int]] = []
    for path in sorted(root.rglob("*"), key=lambda p: p.as_posix()):
        if not path.is_file():
            continue
        if ".git" in path.parts:
            continue

        suffix = path.suffix.lower()
        if suffix not in {".md", ".zip"}:
            continue

        rel = rel_posix(path, root)
        size = path.stat().st_size
        hash_short = sha256_short(path)
        detected = first_heading(path) if suffix == ".md" else zip_summary(path)

        items.append(
            {
                "tipo": suffix[1:],
                "caminho": rel,
                "conteudo": detected,
                "tamanho": size,
                "hash": hash_short,
            }
        )
    return items


def git_ref(root: Path) -> str:
    try:
        return (
            subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=root)
            .decode("utf-8")
            .strip()
        )
    except Exception:
        return "(sem commit git)"


def render_inventory(root: Path, items: list[dict[str, str | int]]) -> str:
    generated_at = dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")
    commit = git_ref(root)

    lines: list[str] = []
    lines.append("# Inventário Completo de Documentação e Bundles")
    lines.append("## Varredura integral de arquivos `.md` e `.zip` do repositório")
    lines.append("")
    lines.append("## Escopo deste arquivo")
    lines.append("")
    lines.append("Este arquivo é o **inventário bruto** do acervo documental.")
    lines.append("")
    lines.append("- Registra a varredura completa de arquivos `.md` e `.zip` com metadados técnicos.")
    lines.append("- Não define prioridade de leitura nem trilha canônica.")
    lines.append("- Para navegação oficial, use [`docs/INDICE_MESTRE.md`](INDICE_MESTRE.md).")
    lines.append("- Para porta de entrada do projeto, use [`README.md`](../README.md).")
    lines.append("")
    lines.append("**Critério:** todos os `.md` e `.zip` encontrados por varredura recursiva no repositório, com título detectado, tamanho e hash SHA-256 abreviado.")
    lines.append("")
    lines.append(f"**Gerado em:** {generated_at}")
    lines.append(f"**Commit de referência:** `{commit}`")
    lines.append(f"**Total de arquivos catalogados:** {len(items)}")
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("| Tipo | Caminho | Título/Conteúdo detectado | Tamanho (bytes) | SHA-256 (12) |")
    lines.append("|---|---|---:|---:|---|")

    for item in items:
        detected = str(item["conteudo"]).replace("|", "\\|").replace("`", "'")
        lines.append(
            f"| {item['tipo']} | `{item['caminho']}` | {detected} | {item['tamanho']} | `{item['hash']}` |"
        )

    lines.append("")
    return "\n".join(lines)


def write_inventory(output: Path, content: str) -> None:
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding="utf-8")


def read_published_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    match = COUNT_PATTERN.search(text)
    if not match:
        raise ValueError(f"Contagem não encontrada em: {path}")
    return int(match.group(1))


def run_check(root: Path, output: Path) -> int:
    actual = len(collect_items(root))
    published = read_published_count(output)
    if actual != published:
        print(
            f"ERRO: contagem divergente em {rel_posix(output, root)} -> publicada={published}, real={actual}",
        )
        return 1
    print(f"OK: contagem publicada={published} e real={actual}.")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        default="docs/DOCUMENTATION_FULL_INVENTORY.md",
        help="Arquivo de saída do inventário (relativo à raiz do repositório).",
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Valida se a contagem publicada confere com a varredura atual.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()
    output = root / args.output

    if args.check:
        return run_check(root, output)

    items = collect_items(root)
    rendered = render_inventory(root, items)
    write_inventory(output, rendered)
    print(f"Inventário atualizado: {rel_posix(output, root)} ({len(items)} itens)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
