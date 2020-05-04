def partial_factorial(n_initial, n_final):
    total = 1
    for m in range(n_initial, n_final + 1):
        total *= m
    return total

def binomial(n, k):
    return int( partial_factorial(n - k + 1, n) / partial_factorial(1, k) )

def pascals_triangle(n):
    for i in range(1, n + 1):
        for j in range(i + 1):
            print(binomial(i, j), end=" ")
        print("") # Line break

def coin_prob(num_heads, num_total):
    return binomial(num_total, num_heads)/(2**num_total)

if __name__ == "__main__":
    total_prob = 0
    for i in range(60, 101):
        total_prob += coin_prob(i, 100)

    print(total_prob)