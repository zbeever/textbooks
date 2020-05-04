from math import pi, sqrt

# Constants
L = 50 # The furthest integer coordinate of our cube
M = 0

if __name__ == "__main__":
    """
    Look at a crystal of atoms arranged in a cubic latice with a 'cube' of 6 having an edge width of a. We can index these atoms with
    coordinates ai, aj, ak, where i, j, k are integers. Suppose these atoms alternate in charge polarity, with a positively charged
    atom at the center of our coordinate system. Then the total electric potential experienced by this atom is

    sum(+-e/(4*pi*epsilon_0*a*sqrt(i^2+j^2+k^2)))_ijk, not i=j=k=0, where the sign of the individual terms is determined by whether
    the sum of coordinates is even or odd (corresponding to charge polarity). The number multiplying e/(4*pi*epsilon_0*a) is called the
    Madelung constant.
    """

    for i in range(-L, L):
        for j in range(-L, L):
            for k in range(-L, L):
                if i == j == k == 0:
                    continue
                if (i + j + k) % 2 == 0:
                    M += 1/sqrt(i**2 + j**2 + k**2)
                else:
                    M -= 1/sqrt(i**2 + j**2 + k**2)

    print("The Madelung constant is approximately", M)