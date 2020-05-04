from math import inf
from numpy import ones,copy,cos,tan,pi,linspace

def gaussxw(N):
    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))

    # Calculate the weights
    w = 2*(N+1)*(N+1)/(N*N*(1-x*x)*dp*dp)

    return x,w

def gaussxwab(N,a,b):
    x,w = gaussxw(N)
    return 0.5*(b-a)*x+0.5*(b+a),0.5*(b-a)*w

def integrate_list(list, a, b):
    if a == b:
        return 0
    else:
        I = 0.5 * (list[a] + list[b])
        for j in range(1, b - a):
            I += list[a + j]
        return I

def integrate_trap(func, a, b, N=10):
    assert(N > 0)
    if a == b:
        return 0
    else:
        h = (b - a) / N
        I = func(a) + func(b)
        for k in range(1, N):
            I += 2 * func(a + k * h)
        return 0.5 * h * I

def integrate_simpson(func, a, b, N=10):
    assert(N % 2 == 0 and N > 0)
    if a == b:
        return 0
    else:
        h = (b - a) / N
        I = func(a) + func(b)
        for k in range(1, N):
            if k % 2 == 0:
                I += 2 * func(a + k * h)
            else:
                I += 4 * func(a + k * h)
        return (1/3) * h * I

def adap_integrate_trap(func, a, b, target, show_progress=False):
    N = 1
    h = (b - a)
    I = h * 0.5 * (func(a) + func(b))

    while True:
        error = -I

        N *= 2
        h = (b - a) / N

        I = 0.5 * I
        for k in range(1, N, 2):
            I += h * func(a + k * h)

        error += I
        error *= (1/3)

        if show_progress:
            print("N:", N, "-- I:", I, "-- Error:", abs(error))

        if abs(error) < abs(target):
            return I

def R(i, m, func, a, b):
    if m == 1:
        return integrate_trap(func, a, b, 2**i)
    else:
        return R(i, m-1, func, a, b) + 1/(4**(m-1) - 1) * (R(i, m-1, func, a, b) - R(i-1, m-1, func, a, b))

def romberg_integrate(func, a, b, target, show_progress=False):
    R_vals = [
        [integrate_trap(func, a, b, 1)]
    ]

    if show_progress:
        print("R_11: ", R_vals[-1][-1], sep="")

    while True:
        i = len(R_vals)
        R_vals.append([integrate_trap(func, a, b, 2**i)])

        for m in range(i):
            if show_progress:
                print("R_", i + 1, m + 1, ": ", R_vals[-1][-1], "  ", sep="", end="")

            R_vals[-1].append((4**(m + 1) * R_vals[-1][m] - R_vals[-2][m]) / (4**(m + 1) - 1))

        if show_progress:
            print("R_", i + 1, i + 1, ": ", R_vals[-1][-1], sep="")

        error = (R_vals[i][i - 1] - R_vals[i - 1][i - 1]) / (4**i - 1)

        if abs(error) < abs(target):
            return R_vals[-1][-1]

def adap_integrate_simpson(func, a, b, target, show_progress=False):
    N = 2
    h = (b - a) / N

    S = (1 / 3) * (func(a) + func(b) + 2 * sum([func(a + k * h) for k in range(2, N, 2)]))
    T = (2 / 3) * sum([func(a + k * h) for k in range(1, N, 2)])
    I = h * (S + 2*T)

    while True:
        N *= 2
        h = (b - a) / N
        error = -I

        S = S + T
        T = (2 / 3) * sum([func(a + k * h) for k in range(1, N, 2)])
        I = h * (S + 2*T)

        error += I
        error *= (1 / 15)

        if show_progress:
            print("N:", N, "-- I:", I, "-- Error:", abs(error))

        if abs(error) < abs(target):
            return I