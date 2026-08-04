from kitchen.menu import MENU


def lines(items, off=0.0):
    rows = [f"{name:<20}x{qty:<3}{MENU[name] * qty:>8.2f}" for name, qty in items.items()]
    if off:
        rows.append(f"{'lunch discount':<24}{-off:>8.2f}")
    return rows
