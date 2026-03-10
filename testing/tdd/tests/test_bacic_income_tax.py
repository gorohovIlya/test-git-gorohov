# | Годовой доход | Ставка | Расчет налога |
# | :--- | :--- | :--- |
# | **До 2,4 млн руб.** | 13% | 13% от дохода |
# | **2,4 – 5 млн руб.** | 15% | 312 000 + 15% с суммы превышения |
# | **5 – 20 млн руб.** | 18% | 702 000 + 18% с суммы превышения |
# | **20 – 50 млн руб.** | 20% | 3 402 000 + 20% с суммы превышения |
# | **Свыше 50 млн руб.** | 22% | 9 402 000 + 22% с суммы превышения |

#TODO make tests to check different types of numbers
import pytest
from income_tax import calculate_income_tax

def test_income_tax_tier1_basic():
    assert calculate_income_tax(2_000_000) == 260_000

def test_income_tax_tier2_basic():
    # 4_000_000 -> 2_400_000 * 0.13 + 1_600_000 * 0.15
    assert calculate_income_tax(4_000_000) == 552_000

def test_income_tax_tier3_basic():
    assert calculate_income_tax(10_000_000) == 1_602_000

def test_income_tax_tier4_basic():
    assert calculate_income_tax(30_000_000) == 5_402_000

def test_income_tax_tier5_basic():
    assert calculate_income_tax(60_000_000) == 11_602_000

@pytest.mark.xfail
def test_income_tax_negative_income():
    assert calculate_income_tax(-1_000)
