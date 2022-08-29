# credit: https://github.com/vassilikitsios/fractals/blob/master/fractals.ipynb

import numpy as np


def iterate_mandelbrot(c, iterate_max, z=0):
    for n in range(iterate_max+1):
        z = z*z + c
        if abs(z) > 2:
            return n
    return None


def calculate_mandelbrot_image(xmin, xmax, Nx, ymin, ymax, iterate_max, center, scale):
    delta = (xmax-xmin)/Nx
    Ny = round((ymax-ymin)/delta)
    x = np.linspace(xmin, xmax, Nx)
    y = np.linspace(ymin, ymax, Ny)
    fractal = np.array(np.zeros((Nx, Ny), dtype=complex))
    for i in range(0, Nx):
        for j in range(0, Ny):
            c = complex(x[i]*scale-center[0], y[j]*scale-center[1])
            n = iterate_mandelbrot(c, iterate_max)
            if n is None:
                fractal[i, j] = 1.0
            else:
                fractal[i, j] = n/iterate_max
    return x, y, fractal
