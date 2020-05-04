from math import atan2, sqrt, pi

if __name__ == "__main__":
    x = float(input("Enter the x-coordinate: "))
    y = float(input("Enter the y-coordinate: "))

    """
    Use the standard change of variables r = sqrt(x^2 + y^2) and theta = atan(y/x)
    """

    r = sqrt(x**2 + y**2)
    theta = atan2(y, x) * 180 / pi

    print("r =", r, "and theta=", theta)