from utils import gaussxw
from math import exp
from numpy import linspace
from pylab import plot, show, xlabel, ylabel

N = 50
x, w = gaussxw(N)

def cv(T, x, w):
    V = 1e-3
    rho = 6.022e28
    theta = 428
    boltzmann = 1.38e-23

    value = 9 * V * rho * boltzmann * (T / theta)**3

    b = theta / T
    
    xp = 0.5 * b * x + 0.5 * b
    wp = 0.5 * b * w

    s = 0.0
    for k in range(N):
        s += wp[k] * (xp[k]**4 * exp(xp[k])) / ((exp(xp[k]) - 1)**2)
    
    return s * value

if __name__ == '__main__':
    T = linspace(5, 500, 100)
    cv = [cv(k, x, w) for k in T]

    plot(T, cv)
    xlabel("Temperature (K)")
    ylabel("Heat Capcity (J/K)")
    show()