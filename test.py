from script import sum, divide, mul

def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a, b) == result

def test_divide():
    a = 4
    b = 2
    result = 0.5
    assert divide(a, b) == result

def test_divison_problem():
    try:
        divide("A", "B")
        assert "Error"
    except ValueError as e:
        print("Test fails")

def test_mul():
    a = 4
    b = 9
    result = 36
    assert mul(a, b) == result

if __name__ == "__main__":
    test_divide() 
    test_sum()
    test_mul()
    test_division_problem()


