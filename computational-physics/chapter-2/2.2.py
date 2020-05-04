from math import sqrt, pi

# Constants
G = 6.67e-11 # m^3/(kg*s^2)
M = 5.97e24 # kg
R = 6.371e6 # m

if __name__ == "__main__":
    T = float(input("Enter the period of the orbit (in seconds): "))

    """
    As the gravitational force is the centripetal force (and hence equals m*v^2 / r), equate the two and solve for h, where r = (h + R)
    
    G*M*m / r^2 = m*v^2 / r
    """
    h = ((G * M * T**2) / (4 * pi**2))**(1/3) - R

    print("The altitude of the orbit is", h / 1e3, "kilometers.")