import math

from rll.dha_fisher import (
    base_frequency_from_tensor_grid,
    run_reference_forecast,
    spiral_modulated_frequency,
)


def test_dha_frequencies_for_1000_states():
    omega = base_frequency_from_tensor_grid(1000)
    assert math.isclose(omega, 0.909, rel_tol=5e-3)

    omega2 = spiral_modulated_frequency(omega)
    assert math.isclose(omega2, 0.787, rel_tol=5e-3)


def test_reference_forecast_is_finite_and_positive_snr():
    result = run_reference_forecast(n_vectors=1000, amplitude_a0=0.02)
    assert result["err_A0"] > 0
    assert result["err_omega"] > 0
    assert result["snr_A0"] > 0
