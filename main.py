import pygame

import Game_Functions as game_def

pygame.init()

# GAME VARIABLES
WIDTH = 600
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (150, 150, 150)
FPS = 60
timer = pygame.time.Clock()
title_font = pygame.font.Font("freesansbold.ttf", 35)
small_font = pygame.font.Font("freesansbold.ttf", 25)
rows = 6
columns = 8
correct = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
new_board = True
options_list = []
spaces_list = []
used = []
first_guess = False
second_guess = False
first_guess_num = 0
second_guess_num = 0
score = 0
matches = 0

# GAME SCREEN
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Matching Game")


def game_loop():
    global new_board, first_guess, second_guess, first_guess_num, second_guess_num
    running = True
    while running:
        timer.tick(FPS)
        screen.fill(WHITE)

        if new_board:
            game_def.generate_board(rows, columns, options_list, spaces_list, used)
            new_board = False

        game_def.draw_backgrounds(screen, BLACK, GREY, WHITE, WIDTH, HEIGHT, title_font)
        board_list = game_def.draw_boards(rows, columns, screen, WHITE, GREY, small_font, spaces_list)

        if first_guess and second_guess:
            game_def.check_guess(first_guess_num, second_guess_num, spaces_list, correct, rows, score, matches)
            first_guess = False
            second_guess = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(board_list)):
                    button = board_list[i]
                    if button.collidepoint(event.pos) and not first_guess:
                        first_guess = True
                        first_guess_num = i

                    if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                        second_guess = True
                        second_guess_num = i

        if first_guess and second_guess:
            first_guess = False
            second_guess = False

        pygame.display.flip()
    pygame.quit()


game_loop()
