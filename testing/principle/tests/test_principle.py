# import sys
# sys.path.append("../src")

#TODO make it with `pip install -e .`

from math_demo import add, add_with_bug, tax_calculator_bugged, tax_calculator

def test_addition():
    assert add(2, 2) == 4
    print("Test ADDITION PASSED")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    # assert add_with_bug(7, 6) == 13
    print("Test BUGGED ADDITION PASSED")

def test_addition_duplicate():
    assert add(6, 7) == 6 + 7
    print("Test DUPLICATE ADDITION PASSED")

def test_addition_overkill():
    for i in range(0, 2 ** 32):
        for j in range(0, 2 ** 32): # violation of duplication
            assert add(i, j) == i + j
            assert add(-i, j) == -i + j
            assert add(-i, -j) == -i + -j
            assert add(i, -j) == i - j

def test_addition_clusters():
    assert add(7, 6) == 13
    assert add(0, 6) == 6
    assert add(7, 0) == 7
    assert add(10, -11) == -1
    assert add(-10, -11) == -21
    assert add(-5, 0) == -5
    assert add(0, -2) == -2
    print("Tests CLUSTERS PASSED")

def test_addition_comutative():
    assert add(9, 5) == 14
    assert add(5, 9) == 14
    print("Test COMMUTATIVITY PASSED")

def test_tax_calculator_pesticide():
    # only integers don't allow some tests
    assert tax_calculator_bugged(1000) == 150
    assert tax_calculator_bugged(100) == 15
    assert tax_calculator_bugged(10) == 1.5
    assert tax_calculator_bugged(1) == 0.15
    assert tax_calculator_bugged(234) == 35.1
    print("Test TAX CALCULATOR PESTICIDE PASSED")
    # assert tax_calculator_bugged(2.34) == 0.35 -> ERROR

def test_tax_calculator():
    assert tax_calculator(1000) == 150
    assert tax_calculator(100) == 15
    assert tax_calculator(10) == 1.5
    assert tax_calculator(1) == 0.15
    assert tax_calculator(2.34) == 0.35
    print("Test TAX CALCULATOR PASSED")

def test_negative_income():
    # Иногда правильным поведением кода является упасть
    try:
        tax_calculator(-100)
        print("Test NEGATIVE INCOME FAILED")
    except ValueError as ve:
        print("Test NEGATIVE INCOME PASSED")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_clusters()
    test_addition_comutative()
    test_tax_calculator_pesticide()
    test_negative_income()
    # test_addition_overkill() # try it on your risk