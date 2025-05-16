"""
Orbital Rotation Model (Polar Framework)
----------------------------------------
This script simulates Earth's orbital motion around a central point (e.g., the Sun)
using a simplified polar coordinate model with curvature and time-aware adjustments.
What It Does

Simulates Earth rotating around the Sun in a polar-based model.
Converts polar coordinates to Cartesian for plotting.
Includes an optional elliptical correction to match Kepler's laws.
Easy to extend with time-curvature or polar asymmetry effects.

Author: Open Earth Polar Model Community
"""

import numpy as np
import matplotlib.pyplot as plt

# Constants (assume units in AU and Earth-years for simplicity)
R = 1.0             # Mean orbital radius (1 Astronomical Unit)
T = 1.0             # Orbital period (1 Earth year)
omega = 2 * np.pi / T  # Angular velocity (rad/year)

# Time domain
num_points = 500
t = np.linspace(0, T, num_points)

# Polar coordinates
theta = omega * t
r = R * np.ones_like(theta)  # Constant radius in circular orbit

# Convert to Cartesian for visualization
x = r * np.cos(theta)
y = r * np.sin(theta)

# Optional: Add curvature modulation to test elliptical influence (Kepler-like)
eccentricity = 0.0167  # Earth's actual orbital eccentricity
r_elliptical = R * (1 - eccentricity**2) / (1 + eccentricity * np.cos(theta))
x_e = r_elliptical * np.cos(theta)
y_e = r_elliptical * np.sin(theta)

# Plot the circular and elliptical orbits
plt.figure(figsize=(8, 8))
plt.plot(x, y, label='Circular Orbit (R = 1 AU)', linestyle='--')
plt.plot(x_e, y_e, label='Elliptical Orbit (e = 0.0167)', color='orange')
plt.scatter([0], [0], color='yellow', label='Sun (Origin)', s=100, zorder=5)
plt.title('Orbital Rotation Model in Polar Coordinates')
plt.xlabel('X (AU)')
plt.ylabel('Y (AU)')
plt.axis('equal')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
