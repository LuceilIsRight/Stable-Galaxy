import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation, FFMpegWriter

# Set random seed for reproducibility
np.random.seed(42)

# Parameters for the spiral galaxy
num_stars_arms = 400000
num_stars_bulge = 20000
num_arms = 6
arm_spread = 0.03
radius_max = 3
a = 0.4
b = 0.25
bulge_radius = 0.8

# Velocity in km/s
velocity = 1278

# Generate logarithmic spiral positions for the arms
theta = np.linspace(0, 4 * np.pi, num_stars_arms)
r = a * np.exp(b * theta)
r = np.clip(r, 0, radius_max)

# Initialize arrays for star positions, velocities, and sizes (arms)
stars_x = []
stars_y = []
stars_z = []
stars_r = []
velocities = []
star_sizes = []

for arm in range(num_arms):
    theta_offset = (2 * np.pi / num_arms) * arm
    theta_arm = theta + theta_offset
    r_scatter = r + np.random.normal(0, arm_spread * 1.5, num_stars_arms)  # Increased noise
    r_scatter = np.clip(r_scatter, 0, radius_max)
    theta_scatter = theta_arm + np.random.normal(0, (arm_spread / 10) * 1.5, num_stars_arms)  # Increased noise
    x = r_scatter * np.cos(theta_scatter)
    y = r_scatter * np.sin(theta_scatter)
    # Thinner disc with subtle pinch-off
    z_base = np.random.normal(0, 0.05 * r_scatter * 1.5, num_stars_arms)  # Increased noise
    z_warp = 0.1 * r_scatter * np.sin(theta_arm)
    z_thickness = 1 - (r_scatter / radius_max)**3
    z = (z_base + z_warp) * z_thickness

    # Calculate tangential velocity vectors
    radial_magnitude = np.sqrt(x**2 + y**2)
    mask = radial_magnitude > 1e-6
    vx = np.zeros(num_stars_arms)
    vy = np.zeros(num_stars_arms)
    vz = np.zeros(num_stars_arms)
    vx[mask] = -y[mask] / radial_magnitude[mask] * velocity
    vy[mask] = x[mask] / radial_magnitude[mask] * velocity

    # Star sizes for glow effect
    sizes = np.random.uniform(0.3, 1.0, num_stars_arms)  # Varied sizes for glow

    stars_x.extend(x)
    stars_y.extend(y)
    stars_z.extend(z)
    stars_r.extend(r_scatter)
    velocities.append(np.stack((vx, vy, vz), axis=1))
    star_sizes.extend(sizes)

# Generate stars for the central bulge
bulge_r = np.random.normal(loc=0.2, scale=0.08 * 1.5, size=num_stars_bulge)  # Increased noise
bulge_r = np.abs(bulge_r) * bulge_radius
bulge_r = np.clip(bulge_r, 0, bulge_radius)
bulge_theta = np.random.uniform(0, 2 * np.pi, num_stars_bulge)
bulge_phi = np.random.uniform(0, np.pi, num_stars_bulge)
bulge_x = bulge_r * np.sin(bulge_phi) * np.cos(bulge_theta)
bulge_y = bulge_r * np.sin(bulge_phi) * np.sin(bulge_theta)
bulge_z = bulge_r * np.cos(bulge_phi)

# Calculate velocities for bulge stars
bulge_radial_magnitude = np.sqrt(bulge_x**2 + bulge_y**2)
bulge_mask = bulge_radial_magnitude > 1e-6
bulge_vx = np.zeros(num_stars_bulge)
bulge_vy = np.zeros(num_stars_bulge)
bulge_vz = np.zeros(num_stars_bulge)
bulge_velocity = velocity * 0.2
bulge_vx[bulge_mask] = -bulge_y[bulge_mask] / bulge_radial_magnitude[bulge_mask] * bulge_velocity
bulge_vy[bulge_mask] = bulge_x[bulge_mask] / bulge_radial_magnitude[bulge_mask] * bulge_velocity

# Star sizes for bulge glow
bulge_sizes = np.random.uniform(0.5, 1.2, num_stars_bulge)  # Larger sizes for brighter glow

# Combine arm and bulge stars
stars_x.extend(bulge_x)
stars_y.extend(bulge_y)
stars_z.extend(bulge_z)
velocities.append(np.stack((bulge_vx, bulge_vy, bulge_vz), axis=1))
stars_r.extend(bulge_r)
star_sizes.extend(bulge_sizes)

# Convert to numpy arrays
stars_x = np.array(stars_x)
stars_y = np.array(stars_y)
stars_z = np.array(stars_z)
velocities = np.vstack(velocities)
stars_r = np.array(stars_r)
star_sizes = np.array(star_sizes)

# Normalize radius for red-to-blue gradient with noise
norm_r = (stars_r - stars_r.min()) / (stars_r.max() - stars_r.min())
colors = np.zeros((len(stars_x), 4))  # RGBA
for i in range(len(stars_x)):
    noise = np.random.normal(0, 0.15)  # Increased color noise
    if stars_r[i] < bulge_radius * 0.5:
        bulge_factor = 1 - (stars_r[i] / (bulge_radius * 0.5))
        r = np.clip(1 + noise, 0, 1)  # Red only at center
        g = np.clip((0.5 + noise) * bulge_factor**2, 0, 1)  # Quick fade to yellow/orange
        b = np.clip((0.1 + noise) * bulge_factor**2, 0, 1)  # Minimal blue in bulge
        a = 1.0  # Higher alpha for glow
        colors[i] = [r, g, b, a]
    else:
        arm_factor = 1 - norm_r[i]
        r = np.clip(0 + noise * 0.1, 0, 0.1)  # No red in arms
        g = np.clip((0.2 + noise) * arm_factor, 0, 1)  # Fade green
        b = np.clip(0.8 + (0.2 * (1 - arm_factor)) + noise, 0, 1)  # Blue at edges
        a = 0.9  # Higher alpha for glow
        colors[i] = [r, g, b, a]

# Set up the 3D plot with higher DPI for sharpness
fig = plt.figure(figsize=(10, 4), facecolor='black', dpi=150)
ax = fig.add_subplot(111, projection='3d')
scatter = ax.scatter(stars_x, stars_y, stars_z, c=colors, s=star_sizes)

# Styling
ax.set_facecolor('black')
ax.set_box_aspect([2.5, 1, 0.2])
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('black')
ax.yaxis.pane.set_edgecolor('black')
ax.zaxis.pane.set_edgecolor('black')
ax.set_title('Rotating 3D Spiral Galaxy - Angled View', color='white')
ax.view_init(elev=20, azim=60)

# Set axis limits
ax.set_xlim(-radius_max, radius_max)
ax.set_ylim(-radius_max, radius_max)
ax.set_zlim(-radius_max * 0.2, radius_max * 0.2)

# Animation parameters
dt = 0.000005
fps = 20
duration = 2
frames = int(fps * duration)
interval = 1000 // fps

# Initial positions
initial_positions = np.stack((stars_x, stars_y, stars_z), axis=1)

# Wrapping function
def wrap_positions(pos):
    r = np.sqrt(pos[:, 0]**2 + pos[:, 1]**2)
    theta = np.arctan2(pos[:, 1], pos[:, 0])
    mask = r > radius_max
    if np.any(mask):
        scale_factor = radius_max / r[mask]
        pos[mask, 0] *= scale_factor
        pos[mask, 1] *= scale_factor
    return pos

# Animation update function
def update(frame):
    current_positions = initial_positions + (velocities * dt * frame)
    current_positions = wrap_positions(current_positions)
    if frame % 10 == 0:
        print(f"Frame {frame}:")
        print(f"x range: {current_positions[:, 0].min()} to {current_positions[:, 0].max()}")
        print(f"y range: {current_positions[:, 1].min()} to {current_positions[:, 1].max()}")
        print(f"z range: {current_positions[:, 2].min()} to {current_positions[:, 2].max()}")
    ax.clear()
    new_scatter = ax.scatter(current_positions[:, 0], current_positions[:, 1], current_positions[:, 2], c=colors, s=star_sizes)
    ax.set_facecolor('black')
    ax.set_box_aspect([2.5, 1, 0.2])
    ax.grid(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_zlabel('')
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.xaxis.pane.set_edgecolor('black')
    ax.yaxis.pane.set_edgecolor('black')
    ax.zaxis.pane.set_edgecolor('black')
    ax.set_title('Rotating 3D Spiral Galaxy - Angled View', color='white')
    ax.view_init(elev=20, azim=60)
    ax.set_xlim(-radius_max, radius_max)
    ax.set_ylim(-radius_max, radius_max)
    ax.set_zlim(-radius_max * 0.2, radius_max * 0.2)
    print(f"Updating frame {frame}")
    return [new_scatter]

# Create animation
anim = FuncAnimation(fig, update, frames=range(frames), interval=interval, blit=False, repeat=False)

# Save animation as video
try:
    writer = FFMpegWriter(fps=fps, metadata=dict(artist='Me'), bitrate=1800)
    anim.save('galaxy_rotation_angled.mp4', writer=writer)
    print("Animation saved as 'galaxy_rotation_angled.mp4'. Play it to see the motion.")
except Exception as e:
    print(f"Failed to save animation: {e}")
    print("Please install ffmpeg (e.g., 'pip install ffmpeg-python' or system package manager) to save the animation.")

# Attempt to show the animation interactively
try:
    plt.show(block=True)
except Exception as e:
    print(f"Interactive animation failed: {e}")
    print("Please check the saved 'galaxy_rotation_angled.mp4' file for the animation.")
