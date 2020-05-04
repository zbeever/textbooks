from numpy import loadtxt, sum
from pylab import scatter, show, plot

# Constants
e = 1.602e-19
h = 6.626e-34

if __name__ == "__main__":
    data = loadtxt("./resources/millikan.txt")

    x = data[:,0]
    y = data[:,1]
    N = len(x)

    Ex = sum(x) / N
    Ey = sum(y) / N
    Exx = sum(x**2) / N
    Exy = sum(x * y) / N

    m = (Exy - Ex*Ey) / (Exx - Ex**2)
    c = (Exx*Ey - Ex*Exy)/(Exx - Ex**2)

    y_fitted_line = m * x + c

    """
    In this scenario, the data represent V = (h/e)v - phi, so we may multiply m by e to find h
    """

    print("The found value of h,", m*e, "is", (h-m*e)/h * 100, "percent off from the accepted value of h.")

    plot(x, y_fitted_line)
    scatter(x, y)
    show()