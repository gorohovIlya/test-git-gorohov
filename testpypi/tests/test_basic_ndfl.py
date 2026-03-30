import pytest
from taxes import calculate_ndfl
# Tests for calculate_ndfl
def test_ndfl_tier1_basic():
    assert calculate_ndfl(2_000_000) == 260_000  # 2_000_000 * 0.13


def test_ndfl_tier2_basic():
    # 4_000_000 -> 2_400_000 * 0.13 + 1_600_000 * 0.15
    assert calculate_ndfl(4_000_000) == 552_000


def test_ndfl_tier3_basic():
    # 10_000_000 -> 2_400_000 * 0.13 + (5_000_000 - 2_400_000) * 0.15 + (10_000_000 - 5_000_000) * 0.18
    assert calculate_ndfl(10_000_000) == 1_602_000


def test_ndfl_tier4_basic():
    assert calculate_ndfl(30_000_000) == 5_402_000


def test_ndfl_tier5_basic():
    assert calculate_ndfl(60_000_000) == 11_602_000


def test_ndfl_exact_tier_boundary():
    # Exact tier boundary should use the lower tier calculation
    assert calculate_ndfl(2_400_000) == 312_000  # 2_400_000 * 0.13


def test_ndfl_just_above_tier_boundary():
    # Just above 2,400,000 should use tier 2
    assert calculate_ndfl(2_400_001) == 312_000 + 0.15  # 312_000 + 1 * 0.15


@pytest.mark.xfail
def test_ndfl_negative_income():
    assert calculate_ndfl(-1_000)


def test_ndfl_zero_income():
    assert calculate_ndfl(0) == 0
