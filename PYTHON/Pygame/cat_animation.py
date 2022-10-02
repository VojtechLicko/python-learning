import os
import sys

import pygame
from pygame.locals import *

pygame.init()

FPS = 60  # frames per second constant
fpsClock = pygame.time.Clock()

# set up the window

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption("Animation")

WHITE = (255, 255, 255)
catImg = pygame.image.load(os.path.join("assets", "cat.png"))  # Load Image
catx = 10  # x coord of cat Img
caty = 10  # y coord of cat IMg
direction = "right"

while True:  # the main game loop
    DISPLAYSURF.fill(WHITE)
    # x coord and y coord of the cat image will change based on the direction variable
    if direction == "right":
        catx += 5
        if catx == 280:
            direction == "down"
    elif direction == "down":
        caty += 5
        if caty == 220:
            direction = "left"
    elif direction == "left":
        catx -= 5
        if catx == 10:
            direction = "up"
    elif direction == "up":
        caty -= 5
        if caty == 10:
            direction = "right"

    DISPLAYSURF.blit(catImg, (catx, caty))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(
        FPS
    )  # sets the refresh rate and the pause between ticks (refreshes of the screen)
