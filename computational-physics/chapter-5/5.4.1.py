from utils import integrate_simpson
from math import pi, cos, sin
from numpy import arange
from pylab import plot, show

def J(m, x):
    return integrate_simpson(lambda theta : cos(m * theta - x * sin(theta)), 0, pi, 1000) / pi

if __name__ == '__main__':
    x = arange(0, 20, 0.1)
    bessel = [
        [J(0, k) for k in x],
        [J(1, k) for k in x],
        [J(2, k) for k in x]
    ]

    plot(x, bessel[0])
    plot(x, bessel[1])
    plot(x, bessel[2])
    show()