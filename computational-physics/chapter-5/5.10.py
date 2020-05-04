from utils import gaussxw
from math import exp, sqrt, cos
from numpy import linspace
from pylab import plot, show, xlabel, ylabel

N = 20
x, w = gaussxw(N)

def V(x):
    return x**4

def T(a, x, w, V):
    m = 1

    value = sqrt(8 * m)

    xp = 0.5 * a * x + 0.5 * a
    wp = 0.5 * a * w
    
    s = 0.0
    for k in range(N):
        s += wp[k] * 1/sqrt(V(a) - V(xp[k]))
    
    return s * value

if __name__ == '__main__':
    amp = linspace(0.1, 2, 100)
    T = [T(k, x, w, V) for k in amp]

    plot(amp, T)
    xlabel('Starting Position (m)')
    ylabel('Period (s)')
    show()