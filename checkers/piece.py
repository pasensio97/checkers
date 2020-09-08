import os
import pygame
from .constants import COOL_RED, SQUARE_SIZE, BLACK, COOL_GOLD


class Piece:
    PADDING = 10
    OUTLINE = 2
    CROWN_FILE = os.path.join("imgs", "crown.png")

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        try:
            self.img = pygame.image.load(self.CROWN_FILE)
            self.img = pygame.transform.scale(
                self.img, (SQUARE_SIZE // 2, SQUARE_SIZE // 2)
            )
        except:
            print(
                "An error has occurred while the game was loading the image [%s]"
                % (self.CROWN_FILE)
            )
            input("Press [ENTER] to exit")
            exit(0)

        if self.color == COOL_RED:
            self.direction = -1
        else:
            self.direction = 1

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        # pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            rect = self.img.get_rect()
            rect = rect.move(self.x - SQUARE_SIZE // 4, self.y - SQUARE_SIZE // 4)
            win.blit(self.img, rect)
            # pygame.draw.circle(win, COOL_GOLD, (self.x, self.y), radius // 2)

    def __repr__(self):
        return str(self.color)

