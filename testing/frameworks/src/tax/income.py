def tax_calculator(income):
    if income < 0:
        raise ValueError("Could not have negative income")
    return round(income * 0.13, 2)