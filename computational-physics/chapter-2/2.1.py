from math import sqrt

# Constants
g = 9.81 # m/s^2

if __name__ == "__main__":
    h = float( input("Enter the height of the tower (in meters): ") ) # m

    """
    Solve for t in y = (1/2)gt^2 (the position of a point mass with an initial velocity of zero under the sole influence of gravity)
    """
    t = sqrt( 2 * h / g )

    print("The total time the ball is in flight is", t, "seconds.")