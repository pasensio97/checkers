import pygame
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE
from checkers.board import Board

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

board = Board()


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col, row = int(pos[0] / SQUARE_SIZE), int(pos[1] / SQUARE_SIZE)
                selected, pos_movs = board.select_piece(row, col)
                print(row, col, selected, "Possible movs:", pos_movs)

        board.draw_squares(WIN)
        board.draw_pieces(WIN)
        pygame.display.update()
        # input("Paused until Enter:")

    pygame.quit()


main()
