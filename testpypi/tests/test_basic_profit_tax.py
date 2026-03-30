import pytest
from taxes import calculate_profit_tax
# Tests for calculate_profit_tax
def test_profit_tax_basic():
    assert calculate_profit_tax(1_000_000) == 200_000  # 1_000_000 * 0.20


def test_profit_tax_zero_profit():
    assert calculate_profit_tax(0) == 0


def test_profit_tax_large_profit():
    assert calculate_profit_tax(10_000_000) == 2_000_000  # 10_000_000 * 0.20


@pytest.mark.xfail
def test_profit_tax_negative_profit():
    assert calculate_profit_tax(-5_000)
