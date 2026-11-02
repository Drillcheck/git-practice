from kitchen.menu import MENU


def total(items):
    subtotal = sum(MENU[name] * qty for name, qty in items.items())
    return subtotal * 1.1  # service charge 10%
