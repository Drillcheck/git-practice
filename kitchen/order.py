from kitchen.menu import MENU
from kitchen import tax


def total(items):
    subtotal = sum(MENU[name] * qty for name, qty in items.items())
    return tax.apply(subtotal)
