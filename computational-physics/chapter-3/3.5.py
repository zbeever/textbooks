from vpython import sphere, vector, color, rate
from math import cos, sin, pi
from numpy import arange, empty

# Constants
c1 = 30 # Planet radii scale factor
c2 = 16000 # Planet orbital radii scale factor
c3 = 1 # Sun scale factor
c4 = 10 # Orbital frequency scale factor

if __name__ == "__main__":
    planet_colors = [color.white, color.orange, color.blue, color.red, color.orange, color.white]

    planet_radii = [2440, 6052, 6371, 3386, 69137, 57316]
    planet_radii_scaled = [c1 * radius for radius in planet_radii]

    planet_orbital_radii = [57.9, 108.2, 149.6, 227.9, 778.5, 1433.4]
    planet_orbital_radii_scaled = [c2 * radius for radius in planet_orbital_radii]

    planet_orbital_periods = [88.0, 224.7, 365.3, 687.0, 4331.6, 10759.2]
    planet_orbital_freqs = [c4 * 2 * pi / period for period in planet_orbital_periods]

    sun_radius = c3 * 695500

    sun = sphere(pos=vector(0, 0, 0), radius=sun_radius, color=color.yellow)
    planets = [sphere(pos=vector(planet_orbital_radii_scaled[n], 0, 0), radius=planet_radii_scaled[n], color=planet_colors[n]) for n in range(len(planet_radii))]

    for theta in arange(0, 24*pi, 0.1):
        rate(30)
        for n in range(len(planet_radii)):
            planets[n].pos = vector(planet_orbital_radii_scaled[n] * cos(planet_orbital_freqs[n] * theta), 0, planet_orbital_radii_scaled[n] * sin(planet_orbital_freqs[n] * theta))