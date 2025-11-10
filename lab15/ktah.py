from dataclasses import dataclass
import math
import pygame
import pygame.freetype
# it is considered goof pracrtice to import basic python libraries first,
# then third party libraries like pygame, then your own modules

# the pygame.init(), draw_scene(), and while True loops are the functions that run the game window and keep it open - necessary for any pygame program
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("K'tah Game")
clock = pygame.time.Clock()
font = pygame.freetype.SysFont('sans', 100)
font_health = pygame.freetype.SysFont('sans', 20)

# part of superpowers
frozen = False
UNFREEZE = pygame.USEREVENT + 1
scarecrow = None
REMOVE_SCARECROW = pygame.USEREVENT + 2


@dataclass
class Agent:
    x: int
    y: int
    radius: int
    speed: int
    color: tuple

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move_towards(self, target):
        dx = target[0] - self.x
        dy = target[1] - self.y
        # ^ target[0] means target 0 and target[1] means target 1, so basically x and y coordinates of target
        distance = math.hypot(dx, dy)
        if distance > 3.0:
            # allow 3 pixels of leeway so they don't jitter when close
            self.x += (dx / distance) * self.speed
            self.y += (dy / distance) * self.speed

    def is_collided_with(self, other):
        distance = math.hypot(self.x - other.x, self.y - other.y)
        return distance < (self.radius + other.radius)


@dataclass
# when you put agent in parentheses, it means that Player is a subtype of Agent,
# meaning that every attribute or method an agent has, a player also has (including default values)
class Player(Agent):
    x: int = WIDTH // 2
    y: int = HEIGHT // 2
    radius: int = 20
    speed: int = 5
    color: tuple = (200, 200, 255)
    health: int = 100

    def teleport(self, pos):
        self.x, self.y = pos

    def is_caught_by_zombie(self, zombies):
        for zombie in zombies:
            if self.is_collided_with(zombie):
                self.health -= 5
        if self.health > 0:
            return False
        else:
            return True

# a subtype inherits everything from its supertype, but can also have its own unique attributes or methods
# if an attiribute is not defined in the subtype, it uses the one from the supertype


@dataclass
class Zombie(Agent):
    # no x and y defined here, but defined in agent, meaning we must specify them when creating a zombie object
    speed: int = 2
    radius: int = 20
    color: tuple = (80, 255, 0)


def draw_scene():
    if player.is_caught_by_zombie(zombies) and player.health <= 0:
        font_health.render_to(screen, (WIDTH-150, 20),
                              "HEALTH:0", (255, 0, 0))
        font.render_to(screen, (20, 20), "GAME OVER", (255, 0, 0))
        pygame.display.flip()
        return
    player.move_towards(pygame.mouse.get_pos())
    if not frozen:
        for zombie in zombies:
            '''if scarecrow:
                zombie.move_towards(scarecrow)
            else:
                zombie.move_towards((player.x, player.y))'''
            # another way to do it ^ (more advanced)
            target = scarecrow or (player.x, player.y)
            zombie.move_towards(target)
    # helps you update your world before you apply a drawing to it
    screen.fill((0, 100, 0))  # Fill the screen with black
    # Here you would add code to draw the game elements
    player.draw()
    for zombie in zombies:
        zombie.draw()
    font_health.render_to(screen, (WIDTH-150, 20),
                          "HEALTH:" + str(player.health), (255, 0, 0))
    if scarecrow is not None:
        pygame.draw.circle(screen, (255, 200, 0), scarecrow, 20)
    pygame.display.flip()


player = Player()
zombies = [
    Zombie(x=20, y=20, speed=0.9, color=(0, 200, 200)),
    Zombie(x=WIDTH-20, y=20),
    Zombie(x=20, y=HEIGHT-20, speed=2.5),
    Zombie(x=WIDTH-20, y=HEIGHT-20, speed=0.9, color=(0, 200, 0)),
    Zombie(x=WIDTH // 2, y=20, speed=1.5, radius=30),
    Zombie(x=WIDTH // 2, y=HEIGHT-20, speed=1.5, radius=10),]


# game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONDOWN:
            player.teleport(event.pos)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if not frozen:
                    frozen = True
                    pygame.time.set_timer(UNFREEZE, 5000, loops=1)
            elif event.key == pygame.K_s:
                if not scarecrow:
                    scarecrow = (player.x, player.y)
                    pygame.time.set_timer(REMOVE_SCARECROW, 5000, loops=1)

        elif event.type == UNFREEZE:
            frozen = False
        elif event.type == REMOVE_SCARECROW:
            scarecrow = None
    clock.tick(60)
    draw_scene()
