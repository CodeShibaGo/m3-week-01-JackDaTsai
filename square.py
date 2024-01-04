import math


def is_square(n):
    # pass
    sqrt_n = math.sqrt(n)

    if sqrt_n % 1 == 0:  # If the square root is an integer
        return True
    else:  # If the square root is not an integer
        return False
