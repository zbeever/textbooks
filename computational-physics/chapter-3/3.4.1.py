from vpython import sphere, vector, color

# Constants
L = 2
R = 0.3

if __name__ == "__main__":
    for i in range(-L, L+1):
        for j in range(-L, L+1):
            for k in range(-L, L+1):
                if ((i + j + k) % 2) == 0:
                    sphere(pos=vector(i,j,k), radius=R, color=color.blue)
                else:
                    sphere(pos=vector(i,j,k), radius=R, color=color.white)