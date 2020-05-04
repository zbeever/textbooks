from pylab import show, plot
from numpy import linspace, pi, cos, sin, exp

if __name__ == "__main__":
    # Deltoid Curve
    theta_0to2pi = linspace(0, 2*pi, 100)
    x_deltoid = 2*cos(theta_0to2pi) + cos(2*theta_0to2pi)
    y_deltoid = 2*sin(theta_0to2pi) - sin(2*theta_0to2pi)

    plot(x_deltoid, y_deltoid, "k-")
    show()

    # Galilean Spiral
    theta_0to10pi = linspace(0, 10*pi, 500)
    r_galilean = theta_0to10pi**2
    x_galilean = r_galilean*cos(theta_0to10pi)
    y_galilean = r_galilean*sin(theta_0to10pi)

    plot(x_galilean, y_galilean, "k-")
    show()

    #Fey's Curve
    theta_0to24pi = linspace(0, 24*pi, 1200)
    r_fey = exp(cos(theta_0to24pi)) - 2*cos(4*theta_0to24pi) + (sin(theta_0to24pi/12))**5
    x_fey = r_fey*cos(theta_0to24pi)
    y_fey = r_fey*sin(theta_0to24pi)

    plot(x_fey, y_fey, "k-")
    show()