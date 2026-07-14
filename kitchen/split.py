def split(amount, guests):
    share = round(amount / guests, 2)
    return [share] * guests
