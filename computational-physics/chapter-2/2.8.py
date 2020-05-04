from numpy import array

if __name__ == "__main__":
    a = array([1, 2, 3, 4], int)
    b = array([2, 4, 6, 8], int)

    print(b / a + 1)
    print(b / (a + 1))
    print(1 / a)