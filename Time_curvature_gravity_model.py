import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11        # Gravitational constant, m^3/kg/s^2
M = 5.972e24           # Mass of Earth, kg
c = 3e8                # Speed of light, m/s

# Define radial distances from Earth's center (in meters)
r = np.linspace(6.371e6, 1e7, 1000)  # From Earth's surface to 10,000 km
R_s = 2 * G * M / c**2               # Schwarzschild radius

# Gravitational time dilation factor from Schwarzschild solution
# t_0 = t_f * sqrt(1
