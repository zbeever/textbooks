from numpy import loadtxt
from pylab import plot, show

if __name__ == "__main__":
    data = loadtxt("./resources/sunspots.txt")

    x = data[:,0][0:1000]
    y_original = data[:,1][0:1000]

    r = 5

    def running_average(data_chunk):
        return 1/(2*r+1) * sum(data_chunk)

    y_averaged = []

    for i in range(len(x[r:-r])):
        y_averaged.append(running_average(y_original[(i-r):(i+r)]))

    plot(x, y_original, "k-")
    plot(x[r:-r], y_averaged, "r--")

    show()