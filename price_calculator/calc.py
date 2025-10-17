from decimal import Decimal, ROUND_HALF_UP


def calculate_total(costs: dict, items: list, tax_pct: float) -> float:
    """Calculate total cost for items with tax.

    - costs: dict mapping item names to their prices (numbers)
    - items: list of item names bought
    - tax_pct: tax percentage to apply (e.g., 10 for 10%)

    Items missing from costs are ignored. Result rounded to 2 decimals
    using ROUND_HALF_UP.
    """
    subtotal = Decimal('0')
    for item in items:
        if item in costs:
            try:
                # Use string conversion to avoid binary float issues
                subtotal += Decimal(str(costs[item]))
            except Exception:
                # Skip invalid cost types
                continue

    tax_multiplier = Decimal('1') + (Decimal(str(tax_pct)) / Decimal('100'))
    total = (subtotal * tax_multiplier).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    return float(total)
