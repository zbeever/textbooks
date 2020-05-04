from math import sin, sqrt
from utils import adap_integrate_simpson

def f(x):
    return sin(sqrt(100*x))**2

if __name__ == '__main__':
    print(adap_integrate_simpson(f, 0, 1, 1e-6, True)) # Achieves the desired accuracy with N = 256 slices