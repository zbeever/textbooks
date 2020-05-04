from utils import adap_integrate_trap, R, romberg_integrate
from math import sin, sqrt
import sys

def f(x):
    return sin(sqrt(100*x))**2

if __name__ == '__main__':
    print(adap_integrate_trap(f, 0, 1, 1e-6, True)) # Achieves the desired accuracy with N = 4096 slices
    print(" ")
    print(romberg_integrate(f, 0, 1, 1e-6, True)) # Achieves the desired accuracy with N = 128 slices