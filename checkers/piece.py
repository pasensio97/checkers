import os
import pygame
from .constants import COOL_RED, SQUARE_SIZE, BLACK, COOL_GOLD, ROWS, COLS, GREEN


class Piece:
    PADDING = 10
    OUTLINE = 2
    CROWN_FILE = os.path.join("imgs", "crown.png")

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = True

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

    def draw_king(self, win):
        rect = self.img.get_rect()
        rect = rect.move(self.x - SQUARE_SIZE // 4, self.y - SQUARE_SIZE // 4)
        win.blit(self.img, rect)

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        # pygame.draw.circle(win, BLACK, (self.x, self.y), radius + self.OUTLINE)
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            self.draw_king(win)

    def possible_movs(self, board):
        pos_movs = []
        if not self.king:
            # Up team
            if self.direction == 1:
                potential_movs = [
                    (self.row + 1, self.col + 1),
                    (self.row + 1, self.col - 1),
                ]
            # Down team
            else:
                potential_movs = [
                    (self.row - 1, self.col + 1),
                    (self.row - 1, self.col - 1),
                ]

            for mov in potential_movs:
                if mov[0] >= 0 and mov[1] >= 0 and mov[0] < ROWS and mov[1] < COLS:
                    if board[mov[0]][mov[1]] is None:
                        pos_movs.append(Dot(mov[0], mov[1]))

        else:
            pass  # print("I'm a king")

        return pos_movs

    def draw_selected(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, COOL_GOLD, (self.x, self.y), radius - radius // 8)
        if self.king:
            self.draw_king(win)

    def draw_possible_movs(self, board, win):
        pos_movs = self.possible_movs(board)
        if pos_movs:
            for dot in pos_movs:
                dot.draw(win)

    def __repr__(self):
        return str(self.color)


class Dot:
    PADDING = 10

    def __init__(self, row, col, color=GREEN):
        self.row = row
        self.col = col
        self.color = color

        self.x = 0
        self.y = 0
        self.calc_pos()

    def calc_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, win):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, self.color, (self.x, self.y), radius // 2)

    def __repr__(self):
        return "Dot: [" + str(self.row) + " " + str(self.col) + "]"
