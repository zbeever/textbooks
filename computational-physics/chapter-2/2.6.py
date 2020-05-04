from math import sqrt, pi

# Constants
M = 1.9891e30 # kg
G = 6.6738e-11 # m^3/kg*s^2

if __name__ == "__main__":
    l1 = float(input("Enter the distance of the object from the Sun at perihelion: "))
    v1 = float(input("Enter the velocity of the object at perihelion: "))

    """
    Given v1*l1 = v2*l2 and the fact that H is conserved, we can equate H at aphelion and perihelion and then solve for a quadratic
    equation in v2: v2^2 - 2*G*M/v1*l1 * v2 - (v1^2 - 2*G*M/l1) = 0
    """

    b = -(2*G*M)/(v1*l1)
    c = -(v1**2 - (2*G*M)/l1)

    v2 = (-b - sqrt(b**2 - 4*c)) / 2 # Aphelion velocity
    l2 = (l1 * v1) / v2 # Aphelion distance

    a = 0.5*(l1 + l2) # The semi-major axis
    b = sqrt(l1*l2) # The semi-minor axis
    T = (2*pi*a*b)/(l1*v1) # The orbital period
    e = (l2-l1)/(l2+l1) # The orbital eccentricity

    print("Aphelion length is", l2 / 1e3, "kilometers. The object's speed at that point is", v2 / 1e3, "kilometers per second. Its orbital period is", T / (365*24*60*60), "years. Its eccentricity is", e)