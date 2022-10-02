import os
import sys

import pygame
from pygame.locals import *

pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Hello World!")

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)
# Playing sounds

# It does not for the sound to finish before next line of code

# Playing background music

# There can be only one background sound, but there can be multiple sound effects
# load the file
pygame.mixer.music.load(os.path.join("assets", "Photograph.mp3"))
# to set the volume of the sound on scale 0.0 to 1.0
pygame.mixer.music.set_volume(0.6)

# -1 sets forever loop, and 0 sets where to start in the file
# Args: loops, start
pygame.mixer.music.play(-1, 0)

# to stop the music:
# pygame.mixer.music.stop()


# Sound effects
soundObj = pygame.mixer.Sound(os.path.join("assets", "transition.wav"))
soundObj.play(2, 0)  # plays the sound effect 3 times from start


# font object with size and font
fontObj = pygame.font.Font("freesansbold.ttf", 32)

# Args : text, antialiasing, text color, background color
textSurfaceObj = fontObj.render("Hello World!", True, GREEN, BLUE)

# Antialiasing makes graphics less blocky with adding little of blur to their edges
# There is a pygame.draw.aaline() function

# Creates rect with heigh and width set for the text
textRectObj = textSurfaceObj.get_rect()

# Set the position of the rect
textRectObj.center = (200, 150)


while True:
    DISPLAYSURF.fill(WHITE)
    DISPLAYSURF.blit(textSurfaceObj, textRectObj)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
