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
            new_row = [None] * COLS
            for col in range((row + 1) % 2, ROWS, 2):
                new_row[col] = Piece(row, col, WHITE)
            board.append(new_row)

        # empty space
        for row in range(3, ROWS - 3):
            board.append([None] * COLS)

        # second team
        for row in range(ROWS - 3, ROWS):
            new_row = [None] * COLS
            for col in range((row + 1) % 2, ROWS, 2):
                new_row[col] = Piece(row, col, COOL_RED)
            board.append(new_row)
        return board

    def draw_possible_movs(self, win):
        if self.selected_piece is not None:
            pos_movs = self.selected_piece.possible_movs(self.board)
            if pos_movs:
                for dot in pos_movs:
                    dot.draw(win)

    def draw_pieces(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != None:
                    piece.draw(win)
                    if piece == self.selected_piece:
                        piece.draw_selected(win)
                        piece.draw_possible_movs(self.board, win)

    def select_piece(self, row, col):
        self.selected_piece = self.board[row][col]
        if self.selected_piece is not None:
            print(self.selected_piece.row, self.selected_piece.col)
            pos_movs = self.selected_piece.possible_movs(self.board)
        else:
            pos_movs = None
        return self.selected_piece, pos_movs

