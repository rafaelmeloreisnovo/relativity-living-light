from __future__ import annotations

import math


def test_sqrt3_2_kernel_constants() -> None:
    h = math.sqrt(3.0) / 2.0
    assert math.isclose(h, math.sin(math.radians(60.0)), abs_tol=1e-15)
    assert math.isclose(h, math.cos(math.radians(30.0)), abs_tol=1e-15)
    assert math.isclose(h * h, 0.75, rel_tol=0.0, abs_tol=1e-15)
    assert round(h * 65536.0) == 56756


def test_recursive_decay_milestones() -> None:
    h = math.sqrt(3.0) / 2.0
    assert math.isclose(math.log(0.5) / math.log(h), 4.81884167930642, abs_tol=1e-12)
    assert math.isclose(math.log(0.1) / math.log(h), 16.00784555930218, abs_tol=1e-12)
    assert math.isclose(math.log(0.01) / math.log(h), 32.01569111860436, abs_tol=1e-12)
    assert math.isclose(1.0 / (1.0 - h), 7.464101615137752, abs_tol=1e-12)


def test_hex_grid_vertical_spacing_and_reverse_route() -> None:
    h = math.sqrt(3.0) / 2.0
    side = 3.0
    y0 = side * h * 0
    y1 = side * h * 1
    assert math.isclose(y1 - y0, side * h, abs_tol=1e-15)

    x0 = 42.0
    forward = x0 * h
    reverse = forward * (2.0 / math.sqrt(3.0))
    assert math.isclose(reverse, x0, rel_tol=0.0, abs_tol=1e-14)


def test_regression_angle_boundary() -> None:
    theta = math.radians(60.0)
    r2 = math.cos(theta) ** 2
    residual_ratio = math.sqrt(1.0 - r2)
    assert math.isclose(r2, 0.25, abs_tol=1e-15)
    assert math.isclose(residual_ratio, math.sqrt(3.0) / 2.0, abs_tol=1e-15)
