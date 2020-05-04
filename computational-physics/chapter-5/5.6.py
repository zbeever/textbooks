from utils import integrate_trap

def f(x):
    return x**4 - 2*x + 1

if __name__ == '__main__':
    twenty_slices = integrate_trap(f, 0, 2, 20)
    ten_slices = integrate_trap(f, 0, 2, 10)

    error = abs((1/3) * (twenty_slices - ten_slices))
    exact_error = abs(4.4 - twenty_slices)

    """
    Our approximate error differs from our exact error because our formula neglects higher order terms in h.
    """

    print("Our answer of", twenty_slices, "is off from the accepted value of 4.4 by approximately", error)
    print("It is exactly off by", exact_error)
    print("Our approximate error differs from our exact error by", abs(error - exact_error) / exact_error * 100, "percent.")