from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_freestanding_build_compiles() -> None:
    cmd = [
        "gcc",
        "-ffreestanding",
        "-fno-builtin",
        "-nostdlib",
        "-c",
        "core/lowlevel_runtime/c/pantheon_freestanding.c",
        "-Icore/lowlevel_runtime/include",
        "-o",
        "/tmp/pantheon_freestanding.o",
    ]
    cp = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr


def test_known_vectors_fnv1a_and_crc32() -> None:
    c = r'''
#include <stdio.h>
#include "core/lowlevel_runtime/include/pantheon_freestanding.h"
int main(void){
  const rll_u8 s[] = "123456789";
  rll_u64 h = rll_fnv1a64(s, 9ull);
  rll_u32 c = rll_crc32(s, 9ull);
  printf("%llx %08x\n", (unsigned long long)h, (unsigned)c);
  return 0;
}
'''
    src = ROOT / "/tmp/rll_vec.c"
    src.write_text(c)
    exe = ROOT / "/tmp/rll_vec"
    cp = subprocess.run([
        "gcc", str(src), "core/lowlevel_runtime/c/pantheon_freestanding.c", "-I.", "-Icore/lowlevel_runtime/include", "-o", str(exe)
    ], cwd=ROOT, capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr
    run = subprocess.run([str(exe)], capture_output=True, text=True)
    assert run.returncode == 0
    out = run.stdout.strip().split()
    assert out[0].lower() == "6d5573923c6cdfc".lower()
    assert out[1].lower() == "cbf43926"
