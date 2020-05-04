from math import sqrt, pi

def f(x):
    return sqrt(1 - x**2)

def integrate(func, lower, upper, steps=100):
    width = upper - lower
    stepSize = width / steps

    integral = sum([(stepSize * func(lower + stepSize * n)) for n in range(steps)])
    return integral

if __name__ == "__main__":
    result = integrate(f, -1, 1, int(1e6))
    print(result, "is off from", pi / 2, "by", abs(pi / 2 - result)/(pi / 2) * 100, "percent.")