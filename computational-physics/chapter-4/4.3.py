def f(x):
    return x*(x+1)

def derivative(func, x, epsilon=1e-2):
    return (f(x + epsilon) - f(x)) / epsilon

if __name__ == "__main__":
    """
    Computing the derivative by brute force doesn't always yield the most accurate answer. Precision loss resulting from
    the error introduced when subtracting two nearly equal numbers ruins the accuracy increase we initially receive by
    reducing the size of epsilon.
    """

    for k in range(0, 14, 2):
        epsilon = 10**(-k - 2)
        print(derivative(f, 1, epsilon), "is off by", abs(derivative(f, 1, epsilon) - 3) / 3 * 100, "percent.")