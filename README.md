# Stable-Galaxy

A Python visualisation project for generating animated, three-dimensional spiral-galaxy-style scenes.

The project uses numerical arrays and plotting tools to create a particle-based representation of a galaxy. It explores spiral geometry, colour, perspective, and animation through computational graphics.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Visualisation-Matplotlib-11557C?style=flat&logo=plotly&logoColor=white)

> **Project type:** Scientific-style visualisation. Do not interpret the generated scene as a self-consistent galactic dynamics simulation unless the underlying physics has been implemented and validated accordingly.

---

## Contents

- [Overview](#overview)
- [Preview](#preview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [Installation](#installation)
- [Running the Animations](#running-the-animations)
- [Customisation](#customisation)
- [Scientific Interpretation](#scientific-interpretation)
- [Roadmap](#roadmap)
- [Licence](#licence)

---

## Overview

Spiral galaxies have distinctive structures that can be explored through computational visualisation.

Stable-Galaxy uses Python-based graphics to create an animated representation of a spiral-galaxy-like distribution. Its focus is on visual structure and presentation rather than claiming to reproduce the complete physical evolution of a real galaxy.

## Preview

Add an actual rendered frame or animation from the repository here.

<!-- Replace the placeholder below with a committed image or GIF. -->
<!-- Example: ![Stable-Galaxy preview](docs/images/stable-galaxy.gif) -->

**Suggested preview:** one still image showing the spiral structure and one short animation demonstrating the available camera perspective.

## Features

The repository has been described as containing separate scripts for different viewing perspectives. Confirm the filenames and available options against the current source.

- Spiral-galaxy-style particle visualisation.
- Three-dimensional rendering, where supported by the script.
- Animated output.
- Customisable visual parameters, where exposed by the implementation.
- Optional MP4 output, if configured and supported by the local rendering environment.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| NumPy | Numerical array operations |
| Matplotlib | Plotting and animation |
| FFmpeg | MP4 encoding, if used by the output pipeline |

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/LuceilIsRight/Stable-Galaxy.git
cd Stable-Galaxy
```

### 2. Create a virtual environment

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

### 3. Install dependencies

For scripts that use NumPy and Matplotlib:

```bash
python -m pip install --upgrade pip
python -m pip install numpy matplotlib
```

If the source imports additional packages, install them too. If MP4 export is supported, make sure FFmpeg is installed and accessible from your terminal.

## Running the Animations

Use the actual script names present in the repository.

For example, if the repository contains `galaxytop.py` and `galaxyangled.py`, run:

```bash
python galaxytop.py
```

and:

```bash
python galaxyangled.py
```

These commands are examples based on the documented script names; confirm that they match the current repository before publishing this section.

## Customisation

Inspect the source code for the parameters supported by the current implementation. Common visualisation controls may include:

- Number of rendered particles.
- Spiral-arm geometry.
- Particle colour and apparent size.
- Camera angle and viewing perspective.
- Animation duration and frame rate.
- Output resolution.

Only document parameters that are actually configurable in the code.

## Scientific Interpretation

A spiral-galaxy-style image does not, by itself, establish that the system is gravitationally stable or that it accurately reproduces a real galaxy.

A physically predictive galaxy simulation would require a defined dynamical model, appropriate initial conditions, numerical integration, and validation. If the current project uses prescribed particle positions or visual motion, describe it as a procedural or phenomenological visualisation.

This distinction makes the project's scope clear and helps viewers understand what the output demonstrates.

## Roadmap

Potential future improvements — **not yet claimed as implemented**:

- [ ] Add a committed example image and short animation.
- [ ] Document the available visualisation parameters.
- [ ] Add a reproducible configuration.
- [ ] Separate particle generation from rendering.
- [ ] Add command-line arguments for common settings.
- [ ] Document runtime and memory requirements.
- [ ] Add tests for generated coordinates and input parameters.
- [ ] Investigate a physically motivated dynamical model as a separate development goal.

## Licence

Check the repository's current licence before reusing or redistributing the code. If no licence is present, reuse permissions should not be assumed.

## Author

[ @LuceilIsRight ](https://github.com/LuceilIsRight)

