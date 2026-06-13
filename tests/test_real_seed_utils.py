from scripts.validation.real_seed_utils import parse_range, parse_pm, parse_asymmetric_radius


def test_parse_range_keeps_range_endpoints_positive():
    assert parse_range("2.5-4.5") == [2.5, 4.5]
    assert parse_range("1.2-2.0") == [1.2, 2.0]


def test_parse_pm_returns_positive_uncertainties():
    parsed = parse_pm("2.08±0.07")
    assert parsed == {"value": 2.08, "minus": 0.07, "plus": 0.07}


def test_parse_asymmetric_radius_positive_components():
    parsed = parse_asymmetric_radius("13.7+2.6-1.5")
    assert parsed == {"value": 13.7, "plus": 2.6, "minus": 1.5}
