def litres(time):
    # Check if time is less than 0
    if time < 0:
        # If it is, raise a ValueError
        raise ValueError("Time cannot be negative")
    # If it's not, proceed with the function as normal
    return int(time / 2)
