# Constants
Cn = 1
n = 0

if __name__ == "__main__":
    """
    Outputs all Catalan numbers less than a billion. The Catalan numbers are given by

    C0 = 1
    Cn+1 = (4n + 2)/(n+2) * Cn
    """

    while Cn < 1e9:
        print(Cn)
        Cn = int(((4*n + 2) / (n + 2)) * Cn)
        n += 1