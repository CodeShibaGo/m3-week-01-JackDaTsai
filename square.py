import math


def is_square(n):
    # Check if n is not an integer or less than 0
    if not isinstance(n, int) or n < 0:
        # If it is, raise a ValueError
        raise ValueError("Input must be a positive integer")

    sqrt_n = math.sqrt(n)

    if sqrt_n % 1 == 0:  # If the square root is an integer
        return True
    else:  # If the square root is not an integer
        return False
