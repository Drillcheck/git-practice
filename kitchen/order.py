from kitchen.menu import MENU


def total(items):
    return round(sum(MENU[name] * qty for name, qty in items.items()), 2)
