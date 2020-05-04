from math import sqrt

# Constants
x = 10 # ly

def gamma(b):
    return 1 / sqrt(1 - b**2)

if __name__ == "__main__":
    b = float(input("Enter the speed of the ship relative to c: "))

    """
    The Lorentz transformation tells us t_prime = gamma(t - b*x). At the moment our traveller reaches the planet, t = x / b. So we have
    t_prime = x*gamma(1/b - b). This reduces to t when b << 1, showing the low-limit accuracy of Galilean relativity.
    """

    t = x / b
    t_prime = x * gamma(b) * (1 / b - b)

    print("From Earth, it seems to take", t, "years, while to the traveller it takes", t_prime)