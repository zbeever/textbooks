from math import sqrt

# Constants
m = 9.11e-31 # kg
h_bar = 6.582e-16 # eV*s
E = 10 # eV
V = 9 # eV

if __name__ == "__main__":
    """
    These are found by solving the Schrodinger equation for a one-dimensional potential step. The wave functions on either side of the steps
    must agree up to their first derivative. This gives four coeffecients, which can be thought of as weighting four individual wave functions -
    waves that enter and leave both sides. Normalizing the wave function, we then assign a probability of 1 to an incoming wave from the left
    and 0 to an incoming wave from the right. This allows us to solve for the amplitudes of the other two regions. Squaring these gives the
    probability that the particle reflects or transmits.
    """

    k1 = sqrt(2 * m * E) / h_bar
    k2 = sqrt(2*m*(E - V)) / h_bar

    T = 4*k1*k2 / (k1 + k2)**2
    R = ((k1 - k2)/(k1 + k2))**2

    print("The probability of transmission is", T, "and the probability of reflection is", R)