from tax.income import tax_calculator

def test_income_tax():
    assert tax_calculator(100) == 15
    print("Test tax passed")

if __name__ == "__main__":
    test_income_tax()