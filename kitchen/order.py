from kitchen.discount import discount
from kitchen.menu import MENU


def total(items):
    if not items:
        return 0.0
    return sum(MENU[name] * qty for name, qty in items.items())


def total_at(items, hour):
    amount = total(items)
    return round(amount - discount(amount, hour), 2)
