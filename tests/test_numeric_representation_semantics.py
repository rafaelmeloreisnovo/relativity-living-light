from __future__ import annotations


def test_leading_zero_integer_value_equivalence_base10() -> None:
    left = "000123"
    right = "123"
    assert int(left, 10) == int(right, 10)


def test_leading_zero_representation_is_different() -> None:
    left = "000123"
    right = "123"
    assert left != right
    assert len(left) != len(right)


def test_indexing_conventions_are_distinct() -> None:
    values = ["0", "1", "2", "3"]
    zero_indexed = values.index("1")
    one_indexed = zero_indexed + 1
    assert zero_indexed == 1
    assert one_indexed == 2
    assert zero_indexed != one_indexed


def test_value_representation_and_state_layers_are_separate() -> None:
    left = {"raw": "000123", "value": int("000123", 10), "prefix_zeroes": 3}
    right = {"raw": "123", "value": int("123", 10), "prefix_zeroes": 0}
    assert left["value"] == right["value"]
    assert left["raw"] != right["raw"]
    assert left["prefix_zeroes"] != right["prefix_zeroes"]
