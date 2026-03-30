import pytest
from taxes import calculate_property_tax
# Tests for calculate_property_tax
def test_property_tax_basic():
    assert calculate_property_tax(10_000_000) == 220_000  # 10_000_000 * 0.022


def test_property_tax_zero_value():
    assert calculate_property_tax(0) == 0


def test_property_tax_with_custom_rate():
    assert calculate_property_tax(10_000_000, rate=0.015) == 150_000


def test_property_tax_large_value():
    assert calculate_property_tax(100_000_000) == 2_200_000  # 100_000_000 * 0.022


@pytest.mark.xfail
def test_property_tax_negative_value():
    assert calculate_property_tax(-5_000_000)
