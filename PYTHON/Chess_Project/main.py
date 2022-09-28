import pygame

from chess_board import create_chessboard
from chess_pieces import Pieces

# Sub problems:
# Create board
# Be able to know coords of squares on board
# Place pieces on the board (initial position)
# Be able to move the pieces around to squares
# Check what kind of piece it is on click eg. queen pawn king
# Check if the piece is left clicked and select it >> chage the color
# Create Logic for pieces
# If dont move the piece dont count it as move
# Highlight squares the piece can move to from their current position
# Change turns
# Keep track of current pieces on the board or the captured pieces
# Cant move something that if i move gets me in check
# See if i am checked
# Check for winner
# Menu > be able to reset board

WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
WHITE = (255, 255, 255)
FPS = 60

COORDS = []


def draw_window():
    # WIN.blit(CHESS_BOARD_IMAGE, (0, 0))
    pieces = Pieces()
    create_chessboard(WIDTH, HEIGHT, WINDOW)
    pieces.place_pieces(WINDOW)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                pass
        draw_window()

    pygame.quit()


if __name__ == "__main__":
    main()
