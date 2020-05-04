from pylab import imshow, show, gray
from numpy import loadtxt

if __name__ == "__main__":
    data = loadtxt("./resources/stm.txt")
    imshow(data, origin="lower")
    gray()
    show()