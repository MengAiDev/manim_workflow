# Manim Video Renderer Action

[![GitHub Marketplace](https://img.shields.io/badge/Marketplace-Manim%20Video%20Renderer-blue.svg?logo=github)](https://github.com/marketplace/actions/manim-video-renderer)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A GitHub Action that automatically installs [Manim](https://www.manim.community/) (Mathematical Animation Engine), renders a video from your scene, and uploads it as a downloadable artifact. Perfect for automating animation renders in your CI/CD pipeline.

## 🎥 What It Does

- Installs all system dependencies (Cairo, TeXLive, Pango, etc.)
- Sets up Python and installs Manim
- Renders your Manim scene with specified quality
- Uploads the generated video as a workflow artifact
- Caches pip packages for faster subsequent runs

## 📋 Prerequisites

- A GitHub repository containing your Manim scene file(s)
- Basic understanding of GitHub Actions

## 🚀 Usage

### Basic Example

```yaml
name: Render Animation
on: [push]

jobs:
  render:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: MengAiDev/manim-video-renderer@v1
        with:
          file: 'scene.py'
          scene: 'MyScene'
```

### Advanced Example with All Options

```yaml
name: Render High-Quality Animation
on:
  push:
    branches: [main]
  workflow_dispatch:  # Allow manual triggers

jobs:
  render:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: MengAiDev/manim-video-renderer@v1
        with:
          file: 'my_animation.py'      # Your scene file
          scene: 'ComplexScene'        # Scene class name
          quality: '-h'                 # High quality
          output_dir: 'rendered/videos' # Custom output path
          python-version: '3.11'        # Python 3.11
```

## ⚙️ Inputs

| Input | Description | Required | Default |
|-------|-------------|----------|---------|
| `file` | Python file containing the scene (relative to repository root) | ✅ Yes | `scene.py` |
| `scene` | Name of the scene class to render | ✅ Yes | `MyScene` |
| `quality` | Rendering quality: `-l` (low), `-m` (medium), `-h` (high), `-k` (4K) | ❌ No | `-m` |
| `output_dir` | Output directory where videos are saved | ❌ No | `media/videos` |
| `python-version` | Python version to use | ❌ No | `3.10` |

## 📤 Outputs

This action uploads the rendered video as a GitHub Actions artifact named `manim-video`. You can download it from the workflow run page.

## 💡 Examples

### Example 1: Simple Scene

**`scene.py`**
```python
from manim import *

class MyScene(Scene):
    def construct(self):
        circle = Circle(color=BLUE)
        square = Square(color=RED)
        
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.wait(1)
```

### Example 2: Mathematical Animation

**`math_scene.py`**
```python
from manim import *

class MathScene(Scene):
    def construct(self):
        formula = MathTex("E = mc^2", color=YELLOW)
        self.play(Write(formula))
        self.wait(2)
```

### Example 3: Multiple Scenes

You can render different scenes by running the action multiple times:

```yaml
jobs:
  render-all:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      
      - name: Render first scene
        uses: your-username/manim-video-renderer@v1
        with:
          file: 'scenes.py'
          scene: 'FirstScene'
          
      - name: Render second scene
        uses: your-username/manim-video-renderer@v1
        with:
          file: 'scenes.py'
          scene: 'SecondScene'
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Manim Community](https://www.manim.community/) for the amazing animation engine
- GitHub Actions team for the composite actions feature
