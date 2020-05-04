from numpy import array, amax, argmax
from math import sqrt

# Constants
a1 = 15.8e6
a2 = 18.3e6
a3 = 0.714e6
a4 = 23.2

def a5(A, Z):
    if (A % 2) != 0:
        return 0
    elif (A % 2) == 0 & (Z % 2) == 0:
        return 12e6
    else:
        return -12e6

if __name__ == "__main__":
    all_atomic_numbers = range(1, 101)
    largest_energies = array(list(all_atomic_numbers), float)

    for Z in all_atomic_numbers:
        possible_masses = range(Z, 3*Z + 1)
        binding_energies = array(list(possible_masses), float)

        for A in possible_masses:
            B = a1*A - a2*A**(2/3) - a3*(Z**2)/(A**(1/3)) - a4*(A - 2*Z)**2/A + a5(A, Z)/sqrt(A) # The semi-empirical mass formula
            binding_energies[A-Z] = B/A

        largest_energies[Z-1] = amax(binding_energies)

    print(argmax(largest_energies) + 1)