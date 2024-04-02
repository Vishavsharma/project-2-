import pygame
import sys
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CENTER_X, CENTER_Y = WIDTH // 2, HEIGHT // 2
SUN_RADIUS = 50
ORBIT_RADIUS_MULTIPLIER = 30  # Adjust this multiplier to increase/decrease the distance of planets from the Sun

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Solar System")

# Load planet images
planet_images = {
    "mercury": pygame.image.load("mercury.png").convert_alpha(),
    "venus": pygame.image.load("venus.png").convert_alpha(),
    "earth": pygame.image.load("earth.png").convert_alpha(),
    "mars": pygame.image.load("mars.png").convert_alpha(),
    "jupiter": pygame.image.load("jupiter.png").convert_alpha(),
    "saturn": pygame.image.load("saturn.png").convert_alpha(),
    "uranus": pygame.image.load("uranus.png").convert_alpha(),
    "neptune": pygame.image.load("neptune.png").convert_alpha()
}

# Define planet data (name, distance from Sun in AU, image)
planet_data = [
    ("mercury", 0.39, 15),   # Mercury: 0.39 AU from Sun
    ("venus", 0.72, 20),     # Venus: 0.72 AU from Sun
    ("earth", 1.0, 25),      # Earth: 1.0 AU from Sun
    ("mars", 1.52, 20),      # Mars: 1.52 AU from Sun
    ("jupiter", 5.20, 40),   # Jupiter: 5.20 AU from Sun
    ("saturn", 9.58, 35),    # Saturn: 9.58 AU from Sun
    ("uranus", 19.22, 30),   # Uranus: 19.22 AU from Sun
    ("neptune", 30.05, 30)   # Neptune: 30.05 AU from Sun
]

# Function to draw the sun and planets
def draw_objects():
    # Draw Sun
    pygame.draw.circle(screen, (255, 255, 0), (CENTER_X, CENTER_Y), SUN_RADIUS)

    # Draw planets
    for name, distance, planet_radius in planet_data:
        planet_pos = calculate_position(distance)
        planet_img = pygame.transform.scale(planet_images[name], (planet_radius*2, planet_radius*2))
        screen.blit(planet_img, (planet_pos[0]-planet_radius, planet_pos[1]-planet_radius))

# Function to calculate position of planets
def calculate_position(distance):
    angle = pygame.time.get_ticks() / 1000 * 0.1  # Set the angular speed for orbit simulation
    x = CENTER_X + math.cos(angle) * distance * ORBIT_RADIUS_MULTIPLIER
    y = CENTER_Y + math.sin(angle) * distance * ORBIT_RADIUS_MULTIPLIER
    return round(x), round(y)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))
    draw_objects()
    pygame.display.flip()
    pygame.time.delay(10)
