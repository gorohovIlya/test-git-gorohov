
def add(a, b):
    return a + b

def add_with_bug(a, b):
    return a * b

def tax_calculator_bugged(income):
    return income * 0.15

def tax_calculator(income):
    return round(income * 0.15, 2)