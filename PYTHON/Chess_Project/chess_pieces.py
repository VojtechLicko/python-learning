import os

import pygame


class Pieces:
    def __init__(self) -> None:
        pass

    BLACK_BISHOP = pygame.image.load(os.path.join("Assets", "black_bishop.png"))

    WHITE_BISHOP = pygame.image.load(os.path.join("Assets", "white_bishop.png"))

    BLACK_KING = pygame.image.load(os.path.join("Assets", "black_king.png"))
    WHITE_KING = pygame.image.load(os.path.join("Assets", "white_king.png"))
    BLACK_KNIGHT = pygame.image.load(os.path.join("Assets", "black_knight.png"))
    WHITE_KNIGHT = pygame.image.load(os.path.join("Assets", "white_knight.png"))
    BLACK_PAWN = pygame.image.load(os.path.join("Assets", "black_pawn.png"))
    WHITE_PAWN = pygame.image.load(os.path.join("Assets", "white_pawn.png"))
    BLACK_QUEEN = pygame.image.load(os.path.join("Assets", "black_queen.png"))
    WHITE_QUEEN = pygame.image.load(os.path.join("Assets", "white_queen.png"))
    BLACK_ROOK = pygame.image.load(os.path.join("Assets", "black_rook.png"))
    WHITE_ROOK = pygame.image.load(os.path.join("Assets", "white_rook.png"))

    BLACK_PIECES = [
        BLACK_ROOK,
        BLACK_KNIGHT,
        BLACK_BISHOP,
        BLACK_QUEEN,
        BLACK_KING,
        BLACK_BISHOP,
        BLACK_KNIGHT,
        BLACK_ROOK,
    ]
    WHITE_PIECES = [
        WHITE_ROOK,
        WHITE_KNIGHT,
        WHITE_BISHOP,
        WHITE_QUEEN,
        WHITE_KING,
        WHITE_BISHOP,
        WHITE_KNIGHT,
        WHITE_ROOK,
    ]

    def place_pieces(self, WINDOW):
        def black_side():
            x = 0
            y = 0
            for piece in Pieces.BLACK_PIECES:
                piece = pygame.transform.scale(piece, (95, 95))
                WINDOW.blit(piece, (x, y))
                x += 100

            x = 0
            y += 100
            for _ in range(8):
                BLACK_PAWN = pygame.transform.scale(Pieces.BLACK_PAWN, (95, 95))
                WINDOW.blit(BLACK_PAWN, (x, y))
                x += 100

        def white_side():

            y = 700
            x = 0
            for piece in Pieces.WHITE_PIECES[::-1]:
                # white_piece = Pieces(piece, x, y)
                # for image, name in piece.values():
                #   new_dict[name] = white_piece.rect
                piece = pygame.transform.scale(piece, (95, 95))

                # print(white_piece.rect)

                WINDOW.blit(piece, (x, y))
                x += 100
            x = 0
            y -= 100
            for _ in range(8):
                WHITE_PAWN = pygame.transform.scale(Pieces.WHITE_PAWN, (95, 95))
                WINDOW.blit(WHITE_PAWN, (x, y))
                x += 100

        white_side()
        black_side()
