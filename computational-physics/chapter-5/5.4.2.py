from utils import integrate_simpson
from math import pi, cos, sin, sqrt
from numpy import arange, reshape, empty
from pylab import imshow, show, hot

def J(m, x):
    return integrate_simpson(lambda theta : cos(m * theta - x * sin(theta)), 0, pi, 1000) / pi

def I(k, r):
    return (J(1, k*r)/(k*r))**2

if __name__ == '__main__':
    k = 2 * pi / 500e-9
    r_max = 1e-6
    N = 100

    data = empty([N, N])

    for i in range(N):
        for j in range(N):
            x = (2 * i - N) / N * 7e-7
            y = (2 * j - N) / N * 7e-7
            r2 = x**2 + y**2

            if r2 == 0:
                data[i][j] = 0.25
            else:
                data[i][j] = I(k, sqrt(r2))
    
    imshow(data, vmax=0.01)
    hot()
    show()