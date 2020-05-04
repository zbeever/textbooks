from numpy import arange, ones
from pylab import scatter, show

# Constants
n = 500

if __name__ == "__main__":
    """
    Each tested value of r is plotted along the horizontal axis, so a fixed point is represented by a single point in a 'column.'
    A limit cycle is represented by a set of points in a 'column,' and chaos is represented by a large number of irregularly spaced points in a 'column.'

    The value of r for which chaos occurs is approximately 3.57, matching the Feigenbaum constant
    """

    r = arange(1, 4, 0.01)
    x = ones([len(r)]) * 0.5
    for n in range(n):
        x = r * x * (1 - x)
    for n in range(n):
        x = r * x * (1 - x)
        scatter(r, x, marker=".", color="black")
    xlabel("r")
    ylabel("x")
    show()
