RATE = 0.15


def discount(amount, hour):
    """Lunch discount for orders from 11:00 until 15:00."""
    if 11 <= hour < 15:
        return round(amount * RATE, 2)
    return 0.0
