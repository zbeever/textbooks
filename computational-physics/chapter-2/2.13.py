def catalan_number(n):
    if type(n) != int:
        raise ValueError(int)
    if n < 0:
        raise Exception('n must be greater than 0')

    if n == 0:
        return 1
    else:
        return (4*n - 2)/(n + 1) * catalan_number(n - 1)

def g(m, n):
    if type(m) != int or type(n) != int:
        raise ValueError(int)

    if n == 0:
        return m
    else:
        return g(n, m % n)

if __name__ == "__main__":
    print(catalan_number(100))
    print(g(108, 192))