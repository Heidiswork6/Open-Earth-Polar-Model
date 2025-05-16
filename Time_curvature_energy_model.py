import numpy as np
import matplotlib.pyplot as plt

# Constants
G = 6.67430e-11  # gravitational constant (m³/kg/s²)
M = 5.972e24     # mass of Earth (kg)
c = 3.0e8        # speed of light (m/s)
Rs = 2 * G * M / c**2  # Schwarzschild radius for Earth (m)

# Radius range from Earth's surface to upper atmosphere
r = np.linspace(6.371e6, 6.371e6 + 1e6, 500)

# Newtonian gravitational field strength
g = G * M / r**2

# Time dilation factor from general relativity
time_dilation = np.sqrt(1 - Rs / r)

# Energy field model: combines gravity and time dilation as a proxy
energy_field = g * time_dilation

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(r / 1000, g, label='Gravitational Field (m/s²)', color='blue')
plt.plot(r / 1000, time_dilation, label='Time Dilation Factor
