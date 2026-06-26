import json
import math
from pathlib import Path


def test_orbital_output_claim_is_blocked():
    path = Path("data/results/orbital_dynamics/angular_momentum_shape_validation.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert payload["module"] == "orbital_shape_angular_momentum"
    assert payload["claim_allowed"] is False
    assert all(item["claim_allowed"] is False for item in payload["items"])


def test_orbital_output_has_expected_earth_speed_proxy():
    path = Path("data/results/orbital_dynamics/angular_momentum_shape_validation.json")
    payload = json.loads(path.read_text(encoding="utf-8"))
    earth = next(item for item in payload["items"] if item["body_system"] == "Earth")
    speed = earth["calculations_v1"]["mean_orbital_speed_proxy_km_s"]
    assert math.isclose(speed, 29.78053393903363, rel_tol=1e-12)
