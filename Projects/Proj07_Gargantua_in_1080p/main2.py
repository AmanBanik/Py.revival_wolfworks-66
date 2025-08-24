# main2.py
import pygame
import math
import colorsys
import platform
import subprocess
import time

pygame.init()

# -----------------------------
# SYSTEM REFRESH RATE DETECTION
# -----------------------------
def get_system_refresh_rate():
    """Detect actual system refresh rate using OS-specific methods."""
    refresh_rate = 60  # default fallback
    system = platform.system()
    print(f"Detecting refresh rate on {system}...")

    try:
        if system == "Windows":
            try:
                import win32api, win32con
                device = win32api.EnumDisplayDevices()
                settings = win32api.EnumDisplaySettings(device.DeviceName, win32con.ENUM_CURRENT_SETTINGS)
                if settings.DisplayFrequency > 0:
                    refresh_rate = settings.DisplayFrequency
                    print(f"pywin32 detected: {refresh_rate}Hz")
            except ImportError:
                print("pywin32 not installed, using PowerShell...")
                try:
                    result = subprocess.run(
                        ['powershell', '-Command',
                         '(Get-CimInstance Win32_VideoController | Select-Object -First 1).CurrentRefreshRate'],
                        capture_output=True, text=True, timeout=3
                    )
                    if result.returncode == 0 and result.stdout.strip().isdigit():
                        refresh_rate = int(result.stdout.strip())
                        print(f"PowerShell detected: {refresh_rate}Hz")
                except Exception as e:
                    print(f"PowerShell detection failed: {e}")
        elif system == "Darwin":  # macOS
            try:
                result = subprocess.run(['system_profiler', 'SPDisplaysDataType'],
                                        capture_output=True, text=True, timeout=3)
                for line in result.stdout.splitlines():
                    if "Hz" in line and "@" in line:
                        hz_value = line.split("@")[1].split("Hz")[0].strip()
                        if hz_value.replace(".", "").isdigit():
                            refresh_rate = int(float(hz_value))
                            print(f"macOS detected: {refresh_rate}Hz")
                            break
            except Exception as e:
                print(f"macOS detection failed: {e}")
        elif system == "Linux":
            try:
                result = subprocess.run(['xrandr', '--current'],
                                        capture_output=True, text=True, timeout=3)
                for line in result.stdout.splitlines():
                    if "*" in line:
                        hz_str = line.split()[1].replace("*", "").replace("+", "")
                        if hz_str.replace(".", "").isdigit():
                            refresh_rate = int(float(hz_str))
                            print(f"xrandr detected: {refresh_rate}Hz")
                            break
            except Exception as e:
                print(f"Linux detection failed: {e}")
    except Exception as e:
        print(f"Refresh rate detection failed: {e}")

    if refresh_rate < 24 or refresh_rate > 240:
        refresh_rate = 60
    print(f"Final detected refresh rate: {refresh_rate}Hz")
    return refresh_rate

# -----------------------------
# FPS OPTIMIZATION
# -----------------------------
def optimize_fps(system_refresh_rate):
    if system_refresh_rate >= 120:
        return 120
    elif system_refresh_rate >= 90:
        return 90
    elif system_refresh_rate >= 75:
        return 75
    elif system_refresh_rate >= 60:
        return 60
    elif system_refresh_rate >= 48:
        return 48
    else:
        return 30

SYSTEM_REFRESH_RATE = get_system_refresh_rate()
TARGET_FPS = optimize_fps(SYSTEM_REFRESH_RATE)
print(f"Running at {TARGET_FPS} FPS\n")

# -----------------------------
# SIMULATION PARAMETERS
# -----------------------------
WIDTH, HEIGHT = 1920, 1080
theta_spacing, phi_spacing = 2, 4
font_size = 14

disk_inner_radius = 2.5
disk_outer_radius = 8.0
schwarzschild_radius = 2.0

event_chars = " "
disk_chars = ".,-~:;=!*#$@%&"
lensing_chars = ".,;*#@"

x_separator, y_separator = 8, 16
rows, columns = HEIGHT // y_separator, WIDTH // x_separator
screen_size = rows * columns
x_offset, y_offset = columns / 2, rows / 2

A, B = 0, 0
fps_factor = TARGET_FPS / 30.0
horizontal_speed = 0.008 * fps_factor
vertical_speed = 0.0008 * fps_factor

# -----------------------------
# INITIALIZE PYGAME
# -----------------------------
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(f'Gargantua - Black Hole Simulation ({TARGET_FPS} FPS)')
font = pygame.font.SysFont('Arial', font_size, bold=True)

# -----------------------------
# HELPER FUNCTIONS
# -----------------------------
def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def get_black_hole_color(distance, velocity, luminance):
    if distance < schwarzschild_radius:
        return (0, 0, 0)
    base_hue = 0.1
    temp_factor = max(0, (disk_outer_radius - distance) / (disk_outer_radius - disk_inner_radius))
    doppler_factor = 1.0 + velocity * 0.3
    hue_shift = base_hue - temp_factor * 0.05
    saturation = min(1.0, 0.8 + temp_factor * 0.2)
    brightness = min(1.0, luminance * doppler_factor * temp_factor)
    return hsv2rgb(hue_shift, saturation, brightness)

def text_display(letter, x_pos, y_pos, color):
    text = font.render(str(letter), True, color)
    screen.blit(text, (x_pos, y_pos))

def calculate_black_hole_geometry(phi, theta, A, B):
    radius = disk_inner_radius + (disk_outer_radius - disk_inner_radius) * (phi / 628.0)
    x = radius * math.cos(theta)
    y = 0.2 * math.sin(theta * 3) * math.sin(phi * 2)
    z = radius * math.sin(theta)
    cos_A, sin_A = math.cos(A), math.sin(A)
    x, z = x * cos_A - z * sin_A, x * sin_A + z * cos_A
    cos_B, sin_B = math.cos(B), math.sin(B)
    y, z = y * cos_B - z * sin_B, y * sin_B + z * cos_B
    return x, y, z, radius

# -----------------------------
# MAIN LOOP
# -----------------------------
clock = pygame.time.Clock()
frame_count = 0
run = True

while run:
    screen.fill((0, 0, 0))
    z_buffer = [0] * screen_size
    char_buffer = [' '] * screen_size
    color_buffer = [(0, 0, 0)] * screen_size

    for phi in range(0, 628, phi_spacing):
        for theta in range(0, 628, theta_spacing):
            x, y, z, radius = calculate_black_hole_geometry(phi, theta, A, B)
            dist = z + 6
            if dist > 0:
                D = 1 / dist
                sx = int(x_offset + 30 * D * x)
                sy = int(y_offset + 20 * D * y)
                if 0 <= sx < columns and 0 <= sy < rows:
                    idx = sx + columns * sy
                    if D > z_buffer[idx]:
                        z_buffer[idx] = D
                        dist_center = math.sqrt(x*x + y*y + z*z)
                        lensing_factor = schwarzschild_radius / max(dist_center, 0.1)
                        velocity = math.sin(theta) * math.cos(A)
                        if dist_center < schwarzschild_radius * 1.2:
                            char_buffer[idx] = ' '
                            color_buffer[idx] = (0, 0, 0)
                        else:
                            base_lum = max(0, 1.0 - (dist_center - disk_inner_radius) / (disk_outer_radius - disk_inner_radius))
                            lum = min(1.0, base_lum + lensing_factor * 0.3)
                            temp_factor = max(0, (disk_outer_radius - dist_center) / (disk_outer_radius - disk_inner_radius))
                            doppler_brightness = 1.0 + velocity * 0.4
                            final_lum = lum * doppler_brightness * (0.3 + temp_factor * 0.7)
                            char_index = min(len(disk_chars) - 1, int(final_lum * len(disk_chars)))
                            char_buffer[idx] = disk_chars[char_index]
                            color_buffer[idx] = get_black_hole_color(dist_center, velocity, final_lum)

    # Lensing ring
    for angle in range(0, 628, 3):
        ring_x = schwarzschild_radius * 1.8 * math.cos(angle)
        ring_y = schwarzschild_radius * 0.3 * math.sin(angle * 2)
        ring_z = schwarzschild_radius * 1.8 * math.sin(angle)
        cos_A, sin_A = math.cos(A), math.sin(A)
        ring_x, ring_z = ring_x * cos_A - ring_z * sin_A, ring_x * sin_A + ring_z * cos_A
        dist = ring_z + 6
        if dist > 0:
            D = 1 / dist
            sx = int(x_offset + 30 * D * ring_x)
            sy = int(y_offset + 20 * D * ring_y)
            if 0 <= sx < columns and 0 <= sy < rows:
                idx = sx + columns * sy
                if D > z_buffer[idx]:
                    char_buffer[idx] = lensing_chars[min(len(lensing_chars)-1, int(D * len(lensing_chars)))]
                    color_buffer[idx] = hsv2rgb(0.15, 0.8, min(1.0, D * 2))

    # Draw
    y_pos = 0
    for i in range(len(char_buffer)):
        if i != 0 and i % columns == 0:
            y_pos += y_separator
            x_pos = 0
        else:
            x_pos = (i % columns) * x_separator
        text_display(char_buffer[i], x_pos, y_pos, color_buffer[i])

    A += horizontal_speed
    B += vertical_speed
    pygame.display.update()
    clock.tick(TARGET_FPS)

    # FPS counter
    frame_count += 1
    if frame_count % 60 == 0:
        actual_fps = clock.get_fps()
        if abs(actual_fps - TARGET_FPS) > 5:
            print(f"Performance Warning: Target {TARGET_FPS} FPS, Actual: {actual_fps:.1f} FPS")

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            run = False

pygame.quit()
