import pygame

# Always begin with initialization, sizing, and captioning
pygame.init()
# a tuple that shows width and height
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Just a Simple Rectangle')

# Not strictly necessary, but good practice for readability
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)


# A best practice is to do the drawing in its own function
def draw_scene():
    screen.fill(WHITE)  # "Clear the screen"
    the_rectangle = (300, 225, 200, 150)  # (x, y, width, height)
    pygame.draw.rect(screen, RED, the_rectangle)  # filled
    pygame.draw.rect(screen, BLACK, the_rectangle, 3)  # outlined
    pygame.display.flip()  # Put the drawing on the screen


# Draw the scene then wait for the QUIT event to come in
draw_scene()
while True:
    # pygame.event.get() gets all the events that have happened since the last time it was called - reads the actions the user has taken
    for event in pygame.event.get():
        # use a for loop to go through each event in the list of events
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

# ^ this code above pretty much occurs in every program you will write in pygame
