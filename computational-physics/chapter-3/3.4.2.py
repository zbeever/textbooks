from vpython import sphere, vector, color

# Constants
L = 2
R1 = 0.3
R2 = 0.2

if __name__ == "__main__":
    for i in range(-L, L+1):
        for j in range(-L, L+1):
            for k in range(-L, L+1):
                sphere(pos=vector(i, j, k), radius=R1, color=color.blue)
                if (i != L) and (j != L):
                    sphere(pos=vector(i + 0.5, j + 0.5, k), radius=R2, color=color.white)
                if (i != L) and (k != L):
                    sphere(pos=vector(i + 0.5, j, k + 0.5), radius=R2, color=color.white)
                if (j != L) and (k != L):
                    sphere(pos=vector(i, j + 0.5, k + 0.5), radius=R2, color=color.white)