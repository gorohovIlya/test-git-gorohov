
def add(a, b):
    return a + b

def add_with_bug(a, b):
    return a * b

def tax_calculator_bugged(income):
    return income * 0.15

def tax_calculator(income):
    if income < 0:
        raise ValueError("Could not have negative income")
    return round(income * 0.15, 2)