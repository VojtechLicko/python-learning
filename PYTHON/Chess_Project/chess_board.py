import pygame


def create_chessboard(window_width, window_height, surface):

    rect_width = window_width / 8  # width of one
    rect_height = window_height / 8
    x = y = 0
    white = (232, 235, 239)
    blue = (125, 135, 150)

    def create_horizontal_rects(x, y, color, color2):  # draws the squares horizontally
        for i in range(8):

            rects = pygame.Rect(x, y, rect_width, rect_height)

            if i % 2 == 0:
                pygame.draw.rect(surface, color, rects)
                x += rect_width

            else:
                pygame.draw.rect(surface, color2, rects)
                x += rect_width

    x = 0

    for i in range(8):  # draws the squares horizontaly 8 times

        if i % 2 == 0:  # check if the square should be blue or white
            create_horizontal_rects(x, y, white, blue)
            y += rect_height

        if i % 2 == 1:  # check if the square should be blue or white
            create_horizontal_rects(x, y, blue, white)
            y += rect_height
