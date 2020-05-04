from numpy import loadtxt
from pylab import plot, show
from utils import integrate_list

if __name__ == '__main__':
    data = loadtxt('./resources/velocities.txt')

    t = data[:,0]
    v = data[:,1]
    x = []

    for i in range(len(v)):
        x.append(integrate_list(v, 0, i))
    
    plot(t, v)
    plot(t, x)
    show()