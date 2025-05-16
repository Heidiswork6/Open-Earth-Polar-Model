import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
EARTH_RADIUS = 6371  # in kilometers
ROTATION_PERIOD = 24 * 3600  # seconds in a day

# Time parameters
time_steps = 1000
times = np.linspace(0, ROTATION_PERIOD, time_steps)

# Earth's rotation angle (theta) over time around polar axis
rotation_angles = 2 * np.pi * times / ROTATION_PERIOD

# 3D coordinates of a point on the equator
def rotate_point(angle):
    x = EARTH_RADIUS * np.cos(angle)
    y = EARTH_RADIUS * np.sin(angle)
    z = 0
    return x, y, z

trajectory = np.array([rotate_point(theta) for theta in rotation_angles])

# Plotting the rotation path
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')

ax.plot3D(trajectory[:, 0], trajectory[:, 1], trajectory[:, 2], color='blue', label='Equatorial Rotation Path')
ax.scatter(0, 0, 0, color='black', label='Polar Axis Center (North Pole)')
ax.set_title("Earth Rotation Around Polar Axis")
ax.set_xlabel("X (km)")
ax.set_ylabel("Y (km)")
ax.set_zlabel("Z (km)")
ax.legend()

plt.tight_layout()
plt.show()
