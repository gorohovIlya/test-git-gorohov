def calculate_income_tax(income,
                         investment=False,
                         is_family_with_children=False,
                         has_benefits=False):
    result = 0
    # start, addition, taxrate
    tiers = [
        (0, 0, 0.13),
        (2_400_000, 312_000, 0.15),
        (5_000_000, 702_000, 0.18),
        (20_000_000, 3_402_000, 0.20),
        (50_000_000, 9_402_000, 0.22)
    ]
    for start, addition, taxrate in tiers[::-1]:
        if income > start:
            result = (income - start) * taxrate + addition
            return result
    raise RuntimeError(f"Error in tax calculation {income}")
    