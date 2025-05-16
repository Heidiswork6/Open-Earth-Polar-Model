import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Constants
AU = 1.496e11  # Astronomical Unit in meters
earth_orbit_radius = AU
moon_orbit_radius = 3.84e8  # Average Earth-Moon distance in meters
sun_position = np.array([0, 0, 0])
moon_inclination = np.radians(5.14)

# Time samples
num_frames = 360
t = np.linspace(0, 2 * np.pi, num_frames)

# Earth orbit
earth_x = earth_orbit_radius * np.cos(t)
earth_y = earth_orbit_radius * np.sin(t)
earth_z = np.zeros_like(t)

# Moon orbit (relative to Earth)
moon_x = moon_orbit_radius * np.cos(13 * t)
moon_y = moon_orbit_radius * np.sin(13 * t)
moon_z = moon_orbit_radius * np.sin(moon_inclination) * np.cos(13 * t)

# Set up 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim(-1.5 * AU, 1.5 * AU)
ax.set_ylim(-1.5 * AU, 1.5 * AU)
ax.set_zlim(-0.5 * AU, 0.5 * AU)
ax.set_xlabel('X (m)')
ax.set_ylabel('Y (m)')
ax.set_zlabel('Z (m)')
ax.set_title('3D Orbital Rotation Model')

# Plot handles
sun_plot, = ax.plot([0], [0], [0], 'yo', markersize=10, label='Sun')
earth_plot, = ax.plot([], [], [], 'bo', markersize=6, label='Earth')
moon_plot, = ax.plot([], [], [], 'go', markersize=4, label='Moon')
earth_orbit_plot, = ax.plot(earth_x, earth_y, earth_z, 'b--', linewidth=0.5)
moon_orbit_plot, = ax.plot([], [], [], 'g--', linewidth=0.5)

def init():
    earth_plot.set_data([], [])
    earth_plot.set_3d_properties([])
    moon_plot.set_data([], [])
    moon_plot.set_3d_properties([])
    moon_orbit_plot.set_data([], [])
    moon_orbit_plot.set_3d_properties([])
    return earth_plot, moon_plot, moon_orbit_plot

def update(i):
    ex, ey, ez = earth_x[i], earth_y[i], earth_z[i]
    earth_plot.set_data(ex, ey)
    earth_plot.set_3d_properties(ez)

    mx = ex + moon_x[i]
    my = ey + moon_y[i]
    mz = ez + moon_z[i]
    moon_plot.set_data(mx, my)
    moon_plot.set_3d_properties(mz)

    moon_orbit_plot.set_data(ex + moon_x[:i], ey + moon_y[:i])
    moon_orbit_plot.set_3d_properties(ez + moon_z[:i])

    return earth_plot, moon_plot, moon_orbit_plot

ani = FuncAnimation(fig, update, frames=num_frames, init_func=init,
                    blit=False, interval=50)

plt.legend()
plt.tight_layout()
plt.show()
