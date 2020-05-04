from utils import gaussxw
from math import sqrt, cos, sin, pi
from numpy import linspace
from pylab import plot, show, xlabel, ylabel

N = 50
x, w = gaussxw(N)

def intensity(x, z, points, weights):
    wavelength = 1

    u = x * sqrt(2 / (wavelength * z))
    
    xp = 0.5 * u * points + 0.5 * u
    wp = 0.5 * u * weights

    C = 0.0
    for k in range(N):
        C += wp[k] * cos(0.5 * pi * xp[k]**2)

    S = 0.0
    for k in range(N):
        S += wp[k] * sin(0.5 * pi * xp[k]**2)

    return ( (2*C + 1)**2 + (2*S + 1)**2) / 8

if __name__ == '__main__':
    pos = linspace(-5, 5, 100)
    amp = [intensity(k, 3, x, w) for k in pos]

    plot(pos, amp)
    xlabel('x (m)')
    ylabel('Intensity')
    show()