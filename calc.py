MENU = {
    "kimchi stew": 9.0,
    "bibimbap": 10.5,
    "tteokbokki": 7.0,
    "barley tea": 1.5,
}


def total(items):
    return sum(MENU[name] * qty for name, qty in items.items())
