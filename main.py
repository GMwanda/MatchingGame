import pygame

import Game_Functions as game_def

pygame.init()

# GAME VARIABLES
WIDTH = 600
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (10, 200, 10)
GREY = (150, 150, 150)
BLUE = (30, 50, 200)
FPS = 60
timer = pygame.time.Clock()
title_font = pygame.font.Font("freesansbold.ttf", 45)
small_font = pygame.font.Font("freesansbold.ttf", 25)
rows = 6
columns = 8
CORRECT = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
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
best_score = 0
game_over = False

# GAME SCREEN
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption("Matching Game")


def game_loop():
    global new_board, first_guess, second_guess, first_guess_num, second_guess_num, spaces_list, CORRECT, options_list, used, score, matches, game_over, best_score
    running = True
    while running:
        timer.tick(FPS)
        screen.fill(WHITE)

        if new_board:
            game_def.generate_board(rows, columns, options_list, spaces_list, used)
            new_board = False

        restart = game_def.draw_backgrounds(screen, BLACK, GREY, WHITE, WIDTH, HEIGHT, title_font, score, best_score)
        board_list = game_def.draw_boards(rows, columns, screen, WHITE, GREY, BLACK, GREEN, small_font, spaces_list,
                                          CORRECT)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(board_list)):
                    button = board_list[i]
                    if not game_over:
                        if button.collidepoint(event.pos) and not first_guess:
                            first_guess = True
                            first_guess_num = i

                        if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_num:
                            second_guess = True
                            second_guess_num = i

                if restart.collidepoint(event.pos):
                    options_list = []
                    used = []
                    spaces_list = []
                    new_board = True
                    score = 0
                    matches = 0
                    CORRECT = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                               [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]
                    first_guess = False
                    second_guess = False
                    first_guess_num = 0
                    second_guess_num = 0
                    game_over = False

        # WHEN FIRST GUESS IS MADE CHANGE COLOR TO BLUE
        if first_guess:
            piece_text = small_font.render(f'{spaces_list[first_guess_num]}', True, BLUE)
            location = (
                first_guess_num // rows * 75 + 18,
                (first_guess_num - (first_guess_num // rows * rows)) * 65 + 120)
            screen.blit(piece_text, (location))

        if second_guess:
            piece_text = small_font.render(f'{spaces_list[second_guess_num]}', True, (BLUE))
            location = (
                second_guess_num // rows * 75 + 18,
                (second_guess_num - (second_guess_num // rows * rows)) * 65 + 120)
            screen.blit(piece_text, (location))
            pygame.display.update()

        # IF BOTH GUESSES ARE MADE
        if first_guess and second_guess:
            pygame.time.delay(1000)
            score, matches = game_def.check_guess(first_guess_num, second_guess_num, spaces_list, CORRECT, rows, score,
                                                  matches)
            first_guess = False
            second_guess = False

        if matches == rows * columns // 2:
            game_over = True
            winner = pygame.draw.rect(screen, GREY, [10, HEIGHT - 300, WIDTH - 20, 80], 0, 10)
            winner_text = title_font.render(f'You won in {score} moves!', True, WHITE)
            screen.blit(winner_text, (10, HEIGHT - 290))
            if best_score > score or best_score == 0:
                best_score = score

        pygame.display.flip()
    pygame.quit()


game_loop()
