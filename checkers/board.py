import pygame
from .constants import (
    BLACK,
    ROWS,
    COLS,
    COOL_RED,
    SQUARE_SIZE,
    GREEN,
    WHITE,
    COOL_GRAY,
    COOL_BLACK,
)
from checkers.piece import Piece


class Board:
    def __init__(self):
        self.board = self.create_board()
        self.selected_piece = None
        self.red_left = self.white_left = 12
        self.red_kings = self.white_kings = 0

    def draw_squares(self, win):
        win.fill(COOL_BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(
                    win,
                    COOL_GRAY,
                    (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                )

    def create_board(self):
        board = []
        # first team
        for row in range(3):
            new_row = [0] * COLS
            for col in range((row + 1) % 2, ROWS, 2):
                new_row[col] = Piece(row, col, WHITE)
            board.append(new_row)

        # empty space
        for row in range(3, ROWS - 3):
            board.append([0] * COLS)

        # second team
        for row in range(ROWS - 3, ROWS):
            new_row = [0] * COLS
            for col in range((row + 1) % 2, ROWS, 2):
                new_row[col] = Piece(row, col, COOL_RED)
            board.append(new_row)
        return board

    def draw_pieces(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(win)

