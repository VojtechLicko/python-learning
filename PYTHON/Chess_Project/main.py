import pygame

from chess_board import create_chessboard
from chess_pieces import Pieces

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
