from utils import integrate_simpson

def f(x):
    return x**4 - 2*x + 1

if __name__ == '__main__':
    for k in range(1, 4):
        value = integrate_simpson(f, 0, 2, 10**k)
        print("Using", 10**k, "slices, our integral gives a value of", value, ", which is off from 4.4 by", abs(4.4 - value) / 4.4 * 100, "percent.")