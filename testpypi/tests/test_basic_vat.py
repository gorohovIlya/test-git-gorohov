import pytest
from taxes import calculate_vat
# Tests for calculate_vat
def test_vat_basic():
    assert calculate_vat(1_000_000) == 200_000  # 1_000_000 * 0.20


def test_vat_zero_amount():
    assert calculate_vat(0) == 0


def test_vat_with_custom_rate():
    assert calculate_vat(1_000_000, rate=0.10) == 100_000


def test_vat_large_amount():
    assert calculate_vat(10_000_000) == 2_000_000  # 10_000_000 * 0.20


@pytest.mark.xfail
def test_vat_negative_amount():
    assert calculate_vat(-1_000)
