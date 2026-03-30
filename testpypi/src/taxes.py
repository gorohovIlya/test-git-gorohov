def calculate_ndfl(income):
    result = 0
    tiers= [(0, 0, 0.13), (2_400_000, 312_000, 0.15), (5_000_000, 702_000, 0.18),
            (20_000_000, 3_402_000, 0.2), (50_000_000,9_402_000, 0.22)]
    for start, addition, taxrate in tiers[::-1]:
        if income > start:
            return (income - start) * taxrate + addition
    raise RuntimeError(f"Error in tax calculation!")

def calculate_profit_tax(profit):
    result = 0
    tiers = [(0, 0, 0.20)]
    for start, addition, taxrate in tiers[::-1]:
        if profit > start:
            return (profit - start) * taxrate + addition
    raise RuntimeError(f"Error in tax calculation!")


def calculate_vat(amount, rate=0.20):
    tiers = [(0, 0, rate)]
    for start, addition, taxrate in tiers[::-1]:
        if amount > start:
            return (amount - start) * taxrate + addition
    raise RuntimeError(f"Error in tax calculation!")


def calculate_property_tax(property_value, rate=0.022):
    tiers = [(0, 0, rate)]
    for start, addition, taxrate in tiers[::-1]:
        if property_value > start:
            return (property_value - start) * taxrate + addition
    raise RuntimeError(f"Error in tax calculation!")