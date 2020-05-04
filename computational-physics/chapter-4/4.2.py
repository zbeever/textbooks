from math import sqrt

def quadratic_formula(a, b, c):
    """
    This implementation of the quadratic formula avoids the errors that arise in the subtraction of nearly equal numbers.
    """

    A = b
    B = sqrt(b**2 - 4*a*c)
    C = 2*a
    D = 2*c

    return -D/(A + B), -(A + B)/C

if __name__ == "__main__":
    print(quadratic_formula(0.001, 1000, 0.001))