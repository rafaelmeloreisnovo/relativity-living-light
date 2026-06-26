from __future__ import annotations

import math
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
Q16 = 65536
H_Q16 = 56756
INV_H_Q16 = 75674
Z_H_Q16 = 10138


def test_sqrt3_2_freestanding_object_builds_without_libc() -> None:
    cmd = [
        "gcc",
        "-ffreestanding",
        "-fno-builtin",
        "-nostdlib",
        "-c",
        "core/lowlevel_runtime/c/pantheon_freestanding.c",
        "-Icore/lowlevel_runtime/include",
        "-o",
        "/tmp/sqrt3_2_pantheon_freestanding.o",
    ]
    cp = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    assert cp.returncode == 0, cp.stderr


def test_sqrt3_2_q16_vectors_and_rollback() -> None:
    c = r'''
#include <stdio.h>
#include "core/lowlevel_runtime/include/pantheon_freestanding.h"
int main(void){
  rll_i64 one = 65536ll;
  rll_i64 projected = rll_sqrt3_2_project_q16(one);
  rll_i64 restored = rll_sqrt3_2_reverse_q16(projected);
  rll_i64 decayed = rll_sqrt3_2_decay_q16(2ll * one, 3ll * one);
  rll_hex_q16 p0 = rll_sqrt3_2_hex_grid_q16(0ll, 2ll, one);
  rll_hex_q16 p1 = rll_sqrt3_2_hex_grid_q16(1ll, 2ll, one);
  rll_sqrt3_2_pivot_q16 pivot = rll_sqrt3_2_cosmo_pivot_q16();
  printf("%lld %lld %lld %lld %lld %lld %lld %u %u\n",
    (long long)projected,
    (long long)restored,
    (long long)decayed,
    (long long)p0.x_q16,
    (long long)p0.y_q16,
    (long long)p1.x_q16,
    (long long)p1.y_q16,
    (unsigned)pivot.a_q16,
    (unsigned)pivot.z_q16);
  return 0;
}
'''
    src = Path("/tmp/sqrt3_2_vec.c")
    exe = Path("/tmp/sqrt3_2_vec")
    src.write_text(c)
    cp = subprocess.run(
        [
            "gcc",
            str(src),
            "core/lowlevel_runtime/c/pantheon_freestanding.c",
            "-I.",
            "-Icore/lowlevel_runtime/include",
            "-o",
            str(exe),
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    assert cp.returncode == 0, cp.stderr
    run = subprocess.run([str(exe)], capture_output=True, text=True)
    assert run.returncode == 0
    out = [int(x) for x in run.stdout.strip().split()]
    assert out[0] == H_Q16
    assert abs(out[1] - Q16) <= 1
    assert out[2] == (3 * Q16) + ((2 * Q16 * H_Q16) >> 16)
    assert out[3:7] == [2 * Q16, 0, (2 * Q16) + (Q16 >> 1), H_Q16]
    assert out[7:] == [H_Q16, Z_H_Q16]


def test_cosmology_pivot_q16_matches_h_redshift_definition() -> None:
    a_h = math.sqrt(3.0) / 2.0
    z_h = (1.0 / a_h) - 1.0
    assert round(a_h * Q16) == H_Q16
    assert round((2.0 / math.sqrt(3.0) - 1.0) * Q16) == Z_H_Q16
    assert math.isclose(z_h, 0.15470053837925168, abs_tol=1e-15)
