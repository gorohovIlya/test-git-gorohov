import unittest
from tax.income import tax_calculator

class TestTaxCalculator(unittest.TestCase):

    def test_income(self):
        self.assertEqual(tax_calculator(100),  13.0)

    def test_integers_cents(self):
        self.assertEqual(tax_calculator(10.5), 1.36)

if __name__ == "__main__":
    unittest.main()