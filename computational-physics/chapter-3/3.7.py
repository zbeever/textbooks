import numpy as np
from pylab import imshow, show
from math import log

# Constants
n = 2000
width = 2
height = 2
iterations = 1000

if __name__ == "__main__":
    n_rows, n_cols = int(n / 2), int(n)

    real_axis = np.linspace(-0.5 - width / 2, -0.5 + width / 2, num=n_cols)
    imaginary_axis = np.linspace(height / 2, 0, num=n_rows)

    complex_grid = np.zeros((n_rows, n_cols), dtype=np.complex)
    real, imag = np.meshgrid(real_axis, imaginary_axis)
    complex_grid.real = real
    complex_grid.imag = imag

    mandelbrot_top = np.zeros((n_rows,n_cols), dtype=np.float)

    z_grid = np.zeros_like(complex_grid)
    to_do = np.ones((n_rows, n_cols), dtype=bool)

    for iteration in range(iterations):
        z_grid[to_do] = z_grid[to_do]**2 + complex_grid[to_do]
        mask = np.logical_and((z_grid.real**2 + z_grid.imag**2) > 4, to_do)
        mandelbrot_top[mask] = log(iteration + 1)
        to_do = np.logical_and(to_do, np.logical_not(mask))

    mandelbrot_bottom = np.flipud(mandelbrot_top)[1:,:]

    imshow(np.vstack((mandelbrot_top, mandelbrot_bottom)), aspect=1)
    show()