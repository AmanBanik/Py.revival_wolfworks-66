import pygame
import math
import colorsys
import numpy as np

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
hue = 0

WIDTH = 1920
HEIGHT = 1080

x_start, y_start = 0, 0
x_separator = 8
y_separator = 16

rows = HEIGHT // y_separator
columns = WIDTH // x_separator
screen_size = rows * columns

x_offset = columns / 2
y_offset = rows / 2

A, B = 0, 0  # rotating animation

# Black hole specific parameters
disk_inner_radius = 2.5  # Event horizon area
disk_outer_radius = 8.0  # Accretion disk outer edge
schwarzschild_radius = 2.0  # Event horizon size

# Character sets for different regions
event_chars = " "  # Event horizon - pure black
disk_chars = ".,-~:;=!*#$@%&"  # Accretion disk - increasing brightness
lensing_chars = ".,;*#@"  # Gravitationally lensed light

screen = pygame.display.set_mode((WIDTH, HEIGHT))
display_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gargantua - Black Hole Simulation')
font = pygame.font.SysFont('Arial', 14, bold=True)

def hsv2rgb(h, s, v):
    return tuple(round(i * 255) for i in colorsys.hsv_to_rgb(h, s, v))

def get_black_hole_color(distance, velocity, luminance):
    """Generate colors for different parts of the black hole"""
    if distance < schwarzschild_radius:
        return (0, 0, 0)  # Event horizon - pure black
    
    # Accretion disk coloring
    base_hue = 0.1  # Orange-yellow base
    temp_factor = max(0, (disk_outer_radius - distance) / (disk_outer_radius - disk_inner_radius))
    
    # Doppler effect - approaching side brighter, receding side dimmer
    doppler_factor = 1.0 + velocity * 0.3
    
    # Temperature-based coloring (hotter = bluer, cooler = redder)
    hue_shift = base_hue - temp_factor * 0.05
    saturation = min(1.0, 0.8 + temp_factor * 0.2)
    brightness = min(1.0, luminance * doppler_factor * temp_factor)
    
    return hsv2rgb(hue_shift, saturation, brightness)

def text_display(letter, x_pos, y_pos, color):
    text = font.render(str(letter), True, color)
    display_surface.blit(text, (x_pos, y_pos))

def calculate_black_hole_geometry(phi, theta, A, B):
    """Calculate the 3D geometry of the black hole accretion disk"""
    
    # Accretion disk coordinates (flat disk in x-z plane)
    radius = disk_inner_radius + (disk_outer_radius - disk_inner_radius) * (phi / 628.0)
    
    # Disk position
    x = radius * math.cos(theta)
    y = 0.2 * math.sin(theta * 3) * math.sin(phi * 2)  # Slight disk warping
    z = radius * math.sin(theta)
    
    # Apply rotations
    # Rotation around Y-axis (A)
    cos_A, sin_A = math.cos(A), math.sin(A)
    new_x = x * cos_A - z * sin_A
    new_z = x * sin_A + z * cos_A
    x, z = new_x, new_z
    
    # Rotation around X-axis (B)
    cos_B, sin_B = math.cos(B), math.sin(B)
    new_y = y * cos_B - z * sin_B
    new_z = y * sin_B + z * cos_B
    y, z = new_y, new_z
    
    return x, y, z, radius

run = True
clock = pygame.time.Clock()

while run:
    screen.fill(black)
    
    z_buffer = [0] * screen_size  # Depth buffer
    char_buffer = [' '] * screen_size  # Character buffer
    color_buffer = [(0, 0, 0)] * screen_size  # Color buffer
    
    # Render accretion disk
    for phi in range(0, 628, 4):  # Radial sampling
        for theta in range(0, 628, 2):  # Angular sampling
            
            x, y, z, radius = calculate_black_hole_geometry(phi, theta, A, B)
            
            # Distance from viewer
            distance_from_viewer = z + 6
            
            if distance_from_viewer > 0:  # Only render visible points
                # Perspective projection
                D = 1 / distance_from_viewer
                
                # Screen coordinates
                screen_x = int(x_offset + 30 * D * x)
                screen_y = int(y_offset + 20 * D * y)
                
                # Check bounds
                if 0 <= screen_x < columns and 0 <= screen_y < rows:
                    buffer_index = screen_x + columns * screen_y
                    
                    # Check if this point is closer than previous points
                    if D > z_buffer[buffer_index]:
                        z_buffer[buffer_index] = D
                        
                        # Calculate luminance and effects
                        distance_from_center = math.sqrt(x*x + y*y + z*z)
                        
                        # Gravitational lensing effect
                        lensing_factor = schwarzschild_radius / max(distance_from_center, 0.1)
                        
                        # Velocity for Doppler effect (approximated)
                        velocity = math.sin(theta) * math.cos(A)
                        
                        # Event horizon check
                        if distance_from_center < schwarzschild_radius * 1.2:
                            char_buffer[buffer_index] = ' '
                            color_buffer[buffer_index] = (0, 0, 0)
                        else:
                            # Luminance calculation
                            base_luminance = max(0, 1.0 - (distance_from_center - disk_inner_radius) / (disk_outer_radius - disk_inner_radius))
                            
                            # Add gravitational lensing brightness
                            luminance = min(1.0, base_luminance + lensing_factor * 0.3)
                            
                            # Doppler and temperature effects
                            temp_factor = max(0, (disk_outer_radius - distance_from_center) / (disk_outer_radius - disk_inner_radius))
                            doppler_brightness = 1.0 + velocity * 0.4
                            
                            final_luminance = luminance * doppler_brightness * (0.3 + temp_factor * 0.7)
                            
                            # Choose character based on luminance
                            char_index = min(len(disk_chars) - 1, int(final_luminance * len(disk_chars)))
                            char_buffer[buffer_index] = disk_chars[char_index]
                            
                            # Generate color
                            color_buffer[buffer_index] = get_black_hole_color(distance_from_center, velocity, final_luminance)
    
    # Add gravitational lensing ring effect
    for angle in range(0, 628, 3):
        # Einstein ring approximation
        ring_x = schwarzschild_radius * 1.8 * math.cos(angle)
        ring_y = schwarzschild_radius * 0.3 * math.sin(angle * 2)
        ring_z = schwarzschild_radius * 1.8 * math.sin(angle)
        
        # Apply rotations
        cos_A, sin_A = math.cos(A), math.sin(A)
        new_ring_x = ring_x * cos_A - ring_z * sin_A
        ring_z = ring_x * sin_A + ring_z * cos_A
        ring_x = new_ring_x
        
        distance_from_viewer = ring_z + 6
        if distance_from_viewer > 0:
            D = 1 / distance_from_viewer
            screen_x = int(x_offset + 30 * D * ring_x)
            screen_y = int(y_offset + 20 * D * ring_y)
            
            if 0 <= screen_x < columns and 0 <= screen_y < rows:
                buffer_index = screen_x + columns * screen_y
                if D > z_buffer[buffer_index]:
                    char_buffer[buffer_index] = lensing_chars[min(len(lensing_chars)-1, int(D * len(lensing_chars)))]
                    color_buffer[buffer_index] = hsv2rgb(0.15, 0.8, min(1.0, D * 2))
    
    # Render to screen
    y_pos = 0
    for i in range(len(char_buffer)):
        if i != 0 and i % columns == 0:
            y_pos += y_separator
            x_pos = 0
        else:
            x_pos = (i % columns) * x_separator
            
        text_display(char_buffer[i], x_pos, y_pos, color_buffer[i])
    
    # Update rotation angles
    A += 0.008  # Horizontal rotation (360° in ~15 seconds)
    B += 0.0008  # Vertical rotation (much slower z-axis)
    
    pygame.display.update()
    clock.tick(30)  # 30 FPS for smooth animation
    
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False

pygame.quit()