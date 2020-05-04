from math import floor, sqrt

def find_primes(max_number):
    if type(max_number) != int:
        raise ValueError(int)

    if max_number < 2:
        return []

    primes = [2]

    for n in range(3, max_number + 1):
        sqrt_n = int(floor(sqrt(n)))
        for k in primes:
            if n % k == 0:
                break
            else:
                if k >= sqrt_n:
                    primes.append(n)
                    break

    return primes

if __name__ == "__main__":
    print(find_primes(int(input("What is the upper bound?"))))