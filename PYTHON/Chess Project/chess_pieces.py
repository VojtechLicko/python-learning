import os

import pygame


class Pieces:
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
    BLACK_ROOK = pygame.transform.scale(BLACK_ROOK, (85, 85))
    WHITE_ROOK = pygame.image.load(os.path.join("Assets", "white_rook.png"))
