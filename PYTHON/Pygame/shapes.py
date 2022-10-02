import sys

import pygame
from pygame.locals import *

pygame.init()  # Imports all needed pygame modules
DISPLAYSURF = pygame.display.set_mode(
    (500, 400), 0, 32
)  # Sets the height and width of the display
pygame.display.set_caption("Drawing")  # Sets the caption
# Its best practice to set constants for each color
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

DISPLAYSURF.fill(WHITE)  # fills out the surface with color

# Args : surface, color, pointlist, width
pygame.draw.polygon(
    DISPLAYSURF,
    GREEN,
    (
        (146, 0),
        (291, 106),
        (236, 277),
        (56, 277),
        (0, 106),
    ),
)
# Args : surface, color, startpoint, endpoint, width
pygame.draw.line(DISPLAYSURF, BLUE, (60, 60), (120, 60), 4)
pygame.draw.line(DISPLAYSURF, BLUE, (120, 60), (60, 120))
pygame.draw.line(DISPLAYSURF, BLUE, (60, 120), (120, 120), 4)

# Args: surface, color, center_point, radius, width
pygame.draw.circle(DISPLAYSURF, BLUE, (300, 50), 20, 0)

# Args: surface, color, bounding_rectangle, width
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)

# surface, color, rectangle_tuple, width
pygame.draw.rect(DISPLAYSURF, RED, (200, 150, 100, 50))


# Create a pixelarray and now affect color of invidual pixels
# Until i del pixelarray obj the surface will be locked (and error wil be raised if i try to blit something o screen)
pixObj = pygame.PixelArray(DISPLAYSURF)
pixObj[480][380] = BLACK
pixObj[482][382] = BLACK
pixObj[484][384] = BLACK
pixObj[486][386] = BLACK
pixObj[488][388] = BLACK
del pixObj


# Main game loop
while True:
    for event in pygame.event.get():  # All events
        if event.type == QUIT:  # if the cross is clicked pygame will do these actions
            pygame.quit()
            sys.exit()
    pygame.display.update()  # updates the screen
