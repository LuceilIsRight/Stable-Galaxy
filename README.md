Spiral Galaxy Animation
This project contains two Python scripts, galaxytop.py and galaxyangled.py, that generate 3D animations of a rotating spiral galaxy using Matplotlib. Each script simulates a galaxy with spiral arms and a central bulge, rendered with a color gradient and star glow effect, and saves the output as an MP4 video.
Prerequisites
To run these scripts, you need the following Python packages installed:

matplotlib
numpy
ffmpeg-python (optional, for saving animations)
FFmpeg (required for saving MP4 videos; install via system package manager, e.g., apt install ffmpeg on Ubuntu or brew install ffmpeg on macOS)

Install the Python dependencies using pip:
pip install matplotlib numpy ffmpeg-python

Scripts
galaxytop.py
This script generates a top-down view of a rotating spiral galaxy with 40,000 stars in the spiral arms and 20,000 stars in the central bulge. The animation shows the galaxy rotating over 2 seconds at 20 FPS, saved as galaxy_rotation_top.mp4.
Key Features:

Viewpoint: Top-down (90° elevation).
Spiral arms: 6 logarithmic spirals with added noise for realism.
Central bulge: Spherical distribution of stars.
Color gradient: Red-to-yellow in the bulge, transitioning to blue in the outer arms.
Star sizes: Varied for a glowing effect.
Velocity: Tangential velocities of 1278 km/s for arm stars and 20% of that for bulge stars.
Animation: Stars move in circular orbits, with positions wrapped to stay within the galaxy's radius.

galaxyangled.py
This script is similar to galaxytop.py but renders the galaxy from an angled perspective (20° elevation, 60° azimuth) with 400,000 stars in the spiral arms for a denser appearance. The output is saved as galaxy_rotation_angled.mp4.
Key Features:

Viewpoint: Angled (20° elevation, 60° azimuth) for a 3D perspective.
Higher star count: 400,000 stars in the spiral arms for increased density.
Other features (spiral arms, bulge, colors, velocities, animation) are identical to galaxytop.py except for slightly adjusted noise parameters for arm spread.

# Usage

Ensure all prerequisites are installed.

Run each script individually:

'''python 
galaxytop.py

or

python
-----------------------------------------------------
galaxyangled.py


The script will:
Generate the galaxy model.
Create a 2-second animation.
Save it as galaxy_rotation_top.mp4 or galaxy_rotation_angled.mp4.
Attempt to display the animation interactively (if supported by your environment).


If the interactive display fails, check the saved MP4 file for the animation.

# Output

galaxy_rotation_top.mp4: Animation of the galaxy from a top-down view.
galaxy_rotation_angled.mp4: Animation of the galaxy from an angled view.

# Notes

The scripts use a random seed (np.random.seed(42)) for reproducibility.
If FFmpeg is not installed, the animation will fail to save, and an error message will prompt you to install it.
The animation parameters (e.g., FPS, duration, velocity) can be modified in the scripts for different effects.
The high star count in galaxyangled.py may require significant computational resources.

# Troubleshooting

FFmpeg Error: Ensure FFmpeg is installed and accessible in your system’s PATH.
Performance Issues: Reduce num_stars_arms or num_stars_bulge in the scripts to lower computational load.
No Interactive Display: Some environments (e.g., certain IDEs or headless servers) may not support interactive Matplotlib animations. Check the saved MP4 file instead.
