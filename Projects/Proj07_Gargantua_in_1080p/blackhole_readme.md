# 🌌 Gargantua Black Hole Simulation

A mesmerizing ASCII-based black hole visualization inspired by the iconic Gargantua from Christopher Nolan's *Interstellar*. This "cheap 1080p" simulation renders a scientifically-informed black hole complete with event horizon, accretion disk, and gravitational lensing effects using terminal characters and colors.

![Black Hole Demo](https://img.shields.io/badge/Demo-Black%20Hole-orange) ![Python](https://img.shields.io/badge/Python-3.7+-blue) ![Pygame](https://img.shields.io/badge/Pygame-2.0+-green) ![Auto-FPS](https://img.shields.io/badge/Auto--FPS-Adaptive-brightgreen)

## ✨ Features

### 🔭 Realistic Physics
- **Event Horizon**: Authentic black central region where light cannot escape
- **Accretion Disk**: Hot plasma spiraling around the black hole with proper orbital dynamics
- **Gravitational Lensing**: Einstein ring effects showing light bending around spacetime
- **Doppler Shift**: Approaching matter appears brighter, receding matter dimmer
- **Temperature Gradient**: Inner regions glow blue-white (hotter), outer regions red-orange (cooler)

### 🎬 Visual Effects
- **360° Horizontal Rotation**: Complete revolution every ~15 seconds
- **Z-axis Tilting**: Slow vertical rotation for dynamic perspective
- **Depth-based Rendering**: Character size and brightness based on distance
- **Color Coding**: Temperature and velocity-based coloring system
- **Smooth Animation**: Adaptive FPS based on display capability

### 🖥️ Intelligent Display Adaptation
- **Auto-Detection**: Automatically detects system refresh rate (30Hz-240Hz)
- **Smart FPS Mapping**: Optimizes target FPS to match display capability
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Performance Scaling**: Maintains smooth animation across all hardware
- **Fallback Protection**: Graceful degradation if detection fails

### 🎨 ASCII Art Rendering
- **Multi-tier Character Sets**: Different symbols for various regions and intensities
- **Dynamic Lighting**: Real-time luminance calculations
- **Perspective Projection**: 3D-to-2D conversion with proper depth handling

## 🚀 Quick Start

### Prerequisites
```bash
# Essential dependencies
pip install pygame

# For enhanced Windows refresh rate detection (optional)
pip install pywin32
```

### Running the Simulation
```bash
python main2.py
```

### Expected Output
```
Detecting refresh rate on Windows...
pywin32 detected: 60Hz
Final detected refresh rate: 60Hz
Running at 60 FPS

Gargantua - Black Hole Simulation (60 FPS)
```

### Controls
- **ESC**: Exit simulation
- **Close Window**: Standard window close

## 🛠️ Technical Details

### Dependencies
- **Python 3.7+**
- **Pygame 2.0+**
- **Built-in modules**: `math`, `colorsys`, `platform`, `subprocess`, `time`
- **Optional**: `pywin32` (Windows - for better refresh rate detection)

### Configuration
The simulation can be customized by modifying these parameters:

```python
# Display Settings
WIDTH, HEIGHT = 1920, 1080
theta_spacing, phi_spacing = 2, 4  # Rendering detail
font_size = 14

# Black Hole Physics
disk_inner_radius = 2.5   # Inner accretion disk boundary
disk_outer_radius = 8.0   # Outer accretion disk boundary
schwarzschild_radius = 2.0 # Event horizon size

# Character spacing
x_separator, y_separator = 8, 16
```

### Character Sets
```python
event_chars = " "                    # Event horizon (pure black)
disk_chars = ".,-~:;=!*#$@%&"      # Accretion disk (brightness levels)
lensing_chars = ".,;*#@"            # Gravitational lensing effects
```

### Adaptive FPS System
```python
def optimize_fps(system_refresh_rate):
    if system_refresh_rate >= 120: return 120
    elif system_refresh_rate >= 90: return 90
    elif system_refresh_rate >= 75: return 75
    elif system_refresh_rate >= 60: return 60
    elif system_refresh_rate >= 48: return 48
    else: return 30
```

## 📐 Mathematical Foundation

### Core Coordinate Systems

#### 1. Cylindrical Coordinates for Accretion Disk
The accretion disk is generated using cylindrical coordinates (r, θ, z):
```python
radius = disk_inner_radius + (disk_outer_radius - disk_inner_radius) * (phi / 628.0)
x = radius * math.cos(theta)
y = 0.2 * math.sin(theta * 3) * math.sin(phi * 2)  # Disk warping
z = radius * math.sin(theta)
```

#### 2. 3D Rotation Matrices
The simulation applies two sequential rotations with pre-calculated trigonometry:

**Y-axis Rotation (Horizontal spin):**
```python
cos_A, sin_A = math.cos(A), math.sin(A)  # Performance optimization
x, z = x * cos_A - z * sin_A, x * sin_A + z * cos_A
```

**X-axis Rotation (Vertical tilt):**
```python
cos_B, sin_B = math.cos(B), math.sin(B)
y, z = y * cos_B - z * sin_B, y * sin_B + z * cos_B
```

### Perspective Projection
3D-to-2D conversion using perspective division:
```python
dist = z + 6  # Distance factor (6 = viewer distance)
D = 1 / dist  # Perspective factor
sx = int(x_offset + 30 * D * x)  # Screen x coordinate
sy = int(y_offset + 20 * D * y)  # Screen y coordinate
```

### Black Hole Physics Approximations

#### 1. Schwarzschild Radius
The event horizon size is defined by:
```python
schwarzschild_radius = 2.0  # In simulation units
# Any point with distance < schwarzschild_radius is rendered as pure black
```

#### 2. Gravitational Lensing Factor
Light bending approximation:
```python
lensing_factor = schwarzschild_radius / max(dist_center, 0.1)
```
This creates the "Einstein ring" effect where light appears to bend around the black hole.

#### 3. Doppler Shift Calculation
Relativistic Doppler effect for approaching/receding matter:
```python
velocity = math.sin(theta) * math.cos(A)  # Orbital velocity component
doppler_brightness = 1.0 + velocity * 0.4
```
Positive velocity = approaching (brighter), negative = receding (dimmer).

#### 4. Temperature-Luminosity Relationship
Accretion disk temperature profile:
```python
temp_factor = max(0, (disk_outer_radius - dist_center) / (disk_outer_radius - disk_inner_radius))
base_lum = max(0, 1.0 - (dist_center - disk_inner_radius) / (disk_outer_radius - disk_inner_radius))
```

#### 5. Final Luminance Calculation
Combined brightness from multiple effects:
```python
final_lum = lum * doppler_brightness * (0.3 + temp_factor * 0.7)
```

### Color Mathematics

#### HSV Color Space Conversion
Temperature-based coloring using HSV:
```python
def get_black_hole_color(distance, velocity, luminance):
    base_hue = 0.1  # Orange-yellow baseline
    temp_factor = max(0, (disk_outer_radius - distance) / (disk_outer_radius - disk_inner_radius))
    doppler_factor = 1.0 + velocity * 0.3
    hue_shift = base_hue - temp_factor * 0.05
    saturation = min(1.0, 0.8 + temp_factor * 0.2)
    brightness = min(1.0, luminance * doppler_factor * temp_factor)
    return hsv2rgb(hue_shift, saturation, brightness)
```

Hot regions: hue → 0.05 (more blue-white)
Cool regions: hue → 0.1 (more orange-red)

### Character Mapping Algorithm
ASCII character selection based on luminance:
```python
char_index = min(len(disk_chars) - 1, int(final_lum * len(disk_chars)))
selected_char = disk_chars[char_index]
```

Character array: `".,-~:;=!*#$@%&"` (14 brightness levels)

### Einstein Ring Mathematics
Gravitational lensing creates bright rings at:
```python
ring_radius = schwarzschild_radius * 1.8  # Approximate Einstein radius
ring_x = ring_radius * math.cos(angle)
ring_y = ring_radius * 0.3 * math.sin(2 * angle)  # Elliptical distortion
ring_z = ring_radius * math.sin(angle)
```

### Z-Buffer Algorithm
Depth testing ensures proper occlusion:
```python
if D > z_buffer[idx]:  # Closer objects rendered
    z_buffer[idx] = D
    char_buffer[idx] = selected_char
    color_buffer[idx] = calculated_color
```

### Animation Timing (FPS-Independent)
Rotation angles increment per frame based on detected FPS:
```python
fps_factor = TARGET_FPS / 30.0  # Scaling factor
horizontal_speed = 0.008 * fps_factor  # ~15 seconds for 360°
vertical_speed = 0.0008 * fps_factor   # Proportional z-axis rotation

# Per frame updates:
A += horizontal_speed
B += vertical_speed
```

### Performance Optimizations

#### 1. Pre-calculated Trigonometry
```python
# Calculate once per frame, use multiple times
cos_A, sin_A = math.cos(A), math.sin(A)
cos_B, sin_B = math.cos(B), math.sin(B)
```

#### 2. Efficient Buffer Operations
```python
# Single index calculation
idx = sx + columns * sy

# Direct buffer updates
z_buffer[idx] = D
char_buffer[idx] = selected_char
color_buffer[idx] = calculated_color
```

#### 3. Smart Sampling
```python
theta_spacing, phi_spacing = 2, 4  # Balanced detail vs performance
# Total points ≈ (628/4) × (628/2) ≈ 49,298 per frame
```

## 🖥️ Display Detection System

### Cross-Platform Refresh Rate Detection

#### Windows Detection Methods
```python
# Method 1: pywin32 (Primary)
import win32api, win32con
device = win32api.EnumDisplayDevices()
settings = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
refresh_rate = settings.DisplayFrequency

# Method 2: PowerShell Fallback
'(Get-CimInstance Win32_VideoController | Select-Object -First 1).CurrentRefreshRate'
```

#### macOS Detection
```python
# Uses system_profiler to parse display information
system_profiler SPDisplaysDataType
# Parses output like: "Resolution: 2560 x 1440 @ 120 Hz"
```

#### Linux Detection
```python
# Uses xrandr to get current display mode
xrandr --current
# Parses output like: "1920x1080 60.00*+ 59.96"
```

### FPS Optimization Logic
```python
SYSTEM_REFRESH_RATE = get_system_refresh_rate()
TARGET_FPS = optimize_fps(SYSTEM_REFRESH_RATE)

# Examples:
# 240Hz Display → 120 FPS (performance optimized)
# 144Hz Display → 120 FPS (high refresh gaming)
# 60Hz Display  → 60 FPS  (standard displays)
# 30Hz Display  → 30 FPS  (minimum threshold)
```

## 🎯 How It Works

### 1. System Detection Phase
The simulation starts by detecting your display's capabilities:
1. **OS Detection**: Identifies Windows/macOS/Linux
2. **Hardware Query**: Uses platform-specific methods to get refresh rate
3. **FPS Optimization**: Maps detected rate to optimal target FPS
4. **Performance Scaling**: Adjusts animation speeds to maintain timing consistency

### 2. 3D Geometry Generation
Creates a 3D accretion disk using cylindrical coordinates, then applies rotational transformations to simulate the black hole's spin and our viewing angle.

### 3. Gravitational Effects
- **Event Horizon**: Points within the Schwarzschild radius are rendered as pure black
- **Lensing**: Light paths are bent around the black hole, creating the characteristic "ring of fire"
- **Redshift/Blueshift**: Doppler effects based on orbital velocity

### 4. Rendering Pipeline
1. **3D Coordinate Calculation**: Generate disk geometry with rotations
2. **Perspective Projection**: Convert 3D coordinates to 2D screen space
3. **Depth Testing**: Z-buffer ensures proper occlusion
4. **Luminance Calculation**: Physics-based brightness computation
5. **Character Selection**: Map luminance to appropriate ASCII characters
6. **Color Generation**: HSV-based coloring with temperature and velocity effects

### 5. Performance Monitoring
```python
# Real-time FPS monitoring with warnings
if abs(actual_fps - TARGET_FPS) > 5:
    print(f"Performance Warning: Target {TARGET_FPS} FPS, Actual: {actual_fps:.1f} FPS")
```

## 🎨 Visual Breakdown

### Regions
- **🖤 Event Horizon**: The point of no return - pure black void
- **🔥 Inner Accretion Disk**: Superheated plasma, blue-white glow
- **🌅 Outer Accretion Disk**: Cooler matter, orange-red emission
- **💫 Einstein Ring**: Gravitationally lensed light forming bright arcs
- **🌌 Background**: Deep space void

### Character Mapping
Characters represent different brightness levels:
```
Darkness:  [space]
Dim:       . , -
Medium:    ~ : ; =
Bright:    ! * # $
Intense:   @ % &
```

## 🔬 Scientific Accuracy

This simulation balances scientific authenticity with computational feasibility:

**✅ Accurate Elements:**
- Event horizon proportions (Schwarzschild radius)
- Accretion disk structure and temperature gradients
- Gravitational lensing geometry (Einstein rings)
- Doppler shift effects from orbital motion
- Temperature-color relationships (Wien's displacement law)
- Perspective projection and 3D rotations
- Frame-rate independent animation timing

**⚠️ Simplified Elements:**
- No full general relativity (uses Newtonian approximations)
- Simplified light ray tracing (no geodesic calculations)
- Basic orbital dynamics (circular orbits assumed)
- Linear temperature model (actual profile is more complex)
- No time dilation effects
- Simplified redshift calculations

## 🎮 Performance

### System Requirements
- **CPU**: Modern multi-core processor recommended
- **RAM**: 2GB minimum, 4GB recommended
- **Display**: Any resolution, auto-adapts to refresh rate
- **OS**: Windows 10/11, macOS 10.14+, or Linux

### Adaptive Performance Features
- **Smart FPS Detection**: Automatically matches display capability
- **Efficient Z-buffering**: Minimized overdraw with single-pass rendering
- **Pre-calculated Trigonometry**: Cached sin/cos values for performance
- **Optimized Buffer Operations**: Direct memory access patterns
- **Frame Rate Independence**: Consistent timing across all FPS targets

### Expected Performance
```
240Hz Gaming Monitor → 120 FPS (smooth, high detail)
144Hz Gaming Monitor → 120 FPS (excellent performance)
60Hz Standard Display → 60 FPS (optimal balance)
30Hz Basic Display → 30 FPS (minimum viable)
```

## 🌟 Inspiration

This project draws inspiration from:
- **Interstellar (2014)**: Christopher Nolan's scientifically-grounded visualization
- **Kip Thorne's Research**: Theoretical physics behind black hole imaging
- **Event Horizon Telescope**: Real black hole observations (M87*, Sagittarius A*)
- **Classic ASCII Art**: Terminal-based graphics tradition
- **Real-time Graphics**: Modern adaptive refresh rate technologies
- **[3D Rotating Donut by developerrahulofficial](https://github.com/developerrahulofficial/3D-rotating-Donut.git)**: Inspiration for 3D ASCII art rendering techniques and mathematical transformations

## 🤝 Contributing

Feel free to contribute improvements:
- Enhanced physics calculations
- Additional visual effects
- Performance optimizations
- Cross-platform compatibility
- Documentation improvements
- Bug fixes

## 📜 License

This project is open source. Feel free to use, modify, and distribute as needed.

## 🙏 Acknowledgments

- **Kip Thorne** - Scientific consultation for Interstellar
- **Christopher Nolan** - Visionary direction
- **Event Horizon Telescope Team** - Real black hole imaging
- **Pygame Community** - Excellent graphics framework
- **ASCII Art Community** - Creative text-based visualization techniques
- **Cross-platform developers** - Display detection methodologies

---

*"We are not meant to save the world. We are meant to leave it."* - Cooper, Interstellar

**Experience the majesty of a black hole with intelligent display adaptation.** 🚀✨