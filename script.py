def sum(a,b):
    return a + b


def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    if isinstance(a, list) or isinstance(b, list):
        raise ValueError("Could not divide lists")
    if isinstance(a, list) or isinstance(b, list):
        raise ValueError("Could not divide lists")
    return a / b

def mul(a, b):
    return a * b

