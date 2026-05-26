from kitchen.menu import MENU


def lines(items):
    return [f"{name:<20}x{qty:<3}{MENU[name] * qty:>8.2f}" for name, qty in items.items()]
