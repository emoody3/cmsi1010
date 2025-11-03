import pygame
from dataclasses import dataclass
import random

# my own initializers
WIDTH, HEIGHT = 800, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Invasion")
clock = pygame.time.Clock()


SKY_COLOR = (25, 25, 112)
GRASS_HEIGHT = 100
GRASS_TOP = HEIGHT - GRASS_HEIGHT
GRASS_RECTANGLE = pygame.Rect(0, GRASS_TOP, WIDTH, GRASS_HEIGHT)
GRASS_COLOR = (0, 128, 0)
SUN_COLOR = (255, 255, 0)
SUN_RADIUS = 150
SUN_POSITION = (WIDTH, 0)


@dataclass
class UFO:
    x: int
    y: int
    width: int = 100
    height: int = 30
    color: tuple = (128, 128, 128)
    speed: int = 1

    # we want this draw method to happen within the ufo class
    def draw(self):  # remember methods in classes always take self as first parameter
        pygame.draw.ellipse(screen, self.color,
                            pygame.Rect(self.x, self.y, self.width, self.height))
        pygame.draw.ellipse(screen,
                            self.color,
                            pygame.Rect(
                                self.x + self.width // 4,
                                self.y - self.height // 3,
                                self.width // 2,
                                self.height)
                            )

    def move(self):
        self.x += self.speed
        if self.x > WIDTH:
            self.x = -self.width  # reset to left side off screen so it can come back in smoothly


# creating ufo instances
ufos = [
    UFO(x=0, y=50),
    UFO(x=200, y=100, speed=3.5, width=80, height=20),
    UFO(x=400, y=150, color=(160, 160, 160), width=120, speed=3),
    UFO(x=600, y=200, speed=4),
    UFO(x=400, y=400, speed=.9, width=200, height=60, color=(255, 111, 97))
]

# must draw in order, the first one is in the back, newer ones are in front


def draw_star():
    for _ in range(50):
        x = random.randint(0, WIDTH)
        y = random.randint(0, GRASS_TOP)
        radius = random.randint(1, 3)
        pygame.draw.circle(screen, (255, 255, 255), (x, y), radius)


def draw_scene():
    screen.fill(SKY_COLOR)  # Fill the screen with a color (cyan)
    pygame.draw.circle(screen, SUN_COLOR, SUN_POSITION, SUN_RADIUS)  # Draw sun
    pygame.draw.rect(screen, GRASS_COLOR, GRASS_RECTANGLE)  # Draw grass
    draw_star()  # Draw stars in the sky
    for ufo in ufos:
        ufo.draw()  # Draw each UFO
        ufo.move()  # Move each UFO
    clock.tick(60)  # Limit to 60 frames per second
    pygame.display.flip()  # Update the full display Surface to the screen


while True:
    # theres two things running here: the program and pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    draw_scene()
