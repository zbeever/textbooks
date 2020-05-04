def factorial_int(n):
    if (n <= 1):
        return 1
    return int(n) * factorial_int(int(n - 1))

def factorial_float(n):
    if (n <= 1):
        return 1
    return float(n) * factorial_float(float(n - 1))

if __name__ == "__main__":
    """
    200!, when stored as a float, quickly exceeds 10e308, and so gets stored as an infinite number. Because Python stores
    integers to arbitrary precision, we may still calculate the factorial by storing it as an integer.
    """
    print("factorial_float(200) =", factorial_float(200))
    print("factorial_int(200) =", factorial_int(200))