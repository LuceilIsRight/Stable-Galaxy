# Stable-Galaxy

A Python visualisation project that creates animated, three-dimensional spiral galaxies using NumPy and Matplotlib.

The project explores how particle distributions, spiral-arm geometry, colour gradients, and camera perspectives can be combined to create compelling astronomical-style animations.

**Project type:** Scientific visualisation / procedural animation

## Features

- Generates a spiral-galaxy-style particle distribution.
- Creates a central bulge and spiral arms.
- Supports top-down and angled viewing perspectives.
- Uses colour gradients and particle sizes to create a glowing visual effect.
- Animates particle positions over time.
- Exports MP4 animations when FFmpeg is installed.
- Uses NumPy and Matplotlib for numerical operations and rendering.

## Example Views

The project contains two main scripts:

| Script | Intended view |
|---|---|
| `galaxytop.py` | Top-down galaxy view |
| `galaxyangled.py` | Angled three-dimensional perspective |

The scripts are configured to produce the following output files:

- `galaxy_rotation_top.mp4`
- `galaxy_rotation_angled.mp4`

Actual output names may depend on the version of the source code.

## Technologies

- Python
- NumPy
- Matplotlib
- FFmpeg for MP4 encoding
- `ffmpeg-python` where used by the script

## Requirements

Install Python and pip. The project has been documented with these dependencies:

- NumPy
- Matplotlib
- `ffmpeg-python` for the optional Python interface to FFmpeg

FFmpeg itself must also be installed and accessible on your PATH for MP4 export.

## Installation

Clone the repository:

```bash
git clone https://github.com/LuceilIsRight/Stable-Galaxy.git
cd Stable-Galaxy
```

Create a virtual environment.

**Windows (PowerShell):**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Linux/macOS:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the Python dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install numpy matplotlib ffmpeg-python
```

Verify FFmpeg is available:

```bash
ffmpeg -version
```

## Running the Animations

Generate the top-down view:

```bash
python galaxytop.py
```

Generate the angled view:

```bash
python galaxyangled.py
```

The scripts generate their configured animations. Depending on your environment, the animation may be saved to a video file, displayed interactively, or both.

If rendering is slow, start with a smaller particle count and lower output resolution. Increase the workload only after confirming that the script runs correctly.

## Customisation

The scripts contain parameters controlling aspects of the visualisation, including:

- Number of particles in the arms and central bulge.
- Spiral-arm geometry and noise.
- Viewing angle and camera perspective.
- Particle colours and apparent sizes.
- Animation duration and frame rate.
- Output resolution.

Consult the source code for the exact variable names and current default values.

## Scientific Interpretation

**This project is primarily a procedural visualisation, not a self-consistent dynamical simulation of a real galaxy.**

The generated appearance is controlled by prescribed particle distributions and motion. The use of a spiral shape or orbital-looking motion does not establish that the model solves the equations governing galactic dynamics.

In particular, the current visualisation should not be interpreted as a quantitatively accurate model of stellar velocities, gravitational equilibrium, or long-term galaxy evolution without additional physical modelling and validation.

This distinction is intentional: procedural visualisation can be useful for demonstrating geometry, producing educational material, and creating astronomical-style graphics.

## Potential Improvements

- Add a configuration file for the main visual parameters.
- Separate particle generation from animation and rendering.
- Support reproducible configurations and command-line arguments.
- Add tests for generated coordinates and parameter validation.
- Document runtime and memory use at different particle counts.
- Compare any future physical model against appropriate analytical or numerical benchmarks.

## Licence

Check the repository's current licence before reusing or distributing the project. If no licence is present, add one only after confirming the ownership of all contributions.

## Author

[@LuceilIsRight](https://github.com/LuceilIsRight)
