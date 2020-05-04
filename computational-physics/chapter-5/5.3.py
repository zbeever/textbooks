from math import exp
from pylab import plot, show
from numpy import arange
from utils import integrate_simpson

def E(t):
    return exp(-t**2)

if __name__ == '__main__':
    t = arange(-3, 3, 0.1)
    int_vals = [integrate_simpson(E, 0, k) for k in t]
    func_vals = [E(k) for k in t]

    plot(t, func_vals)
    plot(t, int_vals)
    show()