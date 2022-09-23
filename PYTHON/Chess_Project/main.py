import pygame

from chess_board import create_chessboard
from chess_pieces import Pieces

WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess Game")
WHITE = (255, 255, 255)
FPS = 60
# CHESS_BOARD_IMAGE = pygame.image.load(os.path.join("Assets", "Chessboard.png"))
# CHESS_BOARD_IMAGE = pygame.transform.scale(CHESS_BOARD_IMAGE, (800, 800))
COORDS = []


def draw_window():
    # WIN.blit(CHESS_BOARD_IMAGE, (0, 0))
    create_chessboard(WIDTH, HEIGHT, WINDOW)
    WINDOW.blit(Pieces.BLACK_ROOK, (0, 0))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()


if __name__ == "__main__":
    main()
