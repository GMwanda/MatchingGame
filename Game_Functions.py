import random

import pygame

pygame.init()


def draw_backgrounds(screen, BLACK, GREY, WHITE, WIDTH, HEIGHT, title_font, score, best_score):
    top_menu = pygame.draw.rect(screen, BLACK, [0, 0, WIDTH, 100], 0)
    title_text = title_font.render("Josiah's Matching Game", True, WHITE)
    screen.blit(title_text, (20, 20))
    board_space = pygame.draw.rect(screen, GREY, [0, 100, WIDTH, HEIGHT - 200], 0)
    bottom_menu = pygame.draw.rect(screen, BLACK, [0, HEIGHT - 100, WIDTH, 100], 0)
    restart_button = pygame.draw.rect(screen, GREY, [10, HEIGHT - 85, 80, 30], 0, 20, )
    small_font = pygame.font.Font("freesansbold.ttf", 18)
    restart_text = small_font.render("Restart", True, WHITE)
    screen.blit(restart_text, (18, 520))
    score_text = small_font.render(f"Number of Turns: {score}", True, WHITE)
    screen.blit(score_text, (350, 520))
    best_score_text = small_font.render(f"Best Score: {best_score}", True, WHITE)
    screen.blit(best_score_text, (350, 555))

    return restart_button


def draw_boards(rows, columns, screen, WHITE, GREY, BLACK, GREEN, small_font, spaces_list, correct):
    board_list = []
    for i in range(columns):
        for j in range(rows):
            piece = pygame.draw.rect(screen, WHITE, [i * 75 + 12, j * 65 + 112, 50, 50], 0, 4)
            board_list.append(piece)
            # piece_text = small_font.render(f'{spaces_list[i * rows + j]}', True, GREY)
            # screen.blit(piece_text, (i * 75 + 18, j * 65 + 120))

    for r in range(rows):
        for c in range(columns):
            if correct[r][c] == 1:
                pygame.draw.rect(screen, GREEN, [c * 75 + 10, r * 65 + 110, 54, 54], 3, 4)
                piece_text = small_font.render(f'{spaces_list[c * rows + r]}', True, BLACK)
                screen.blit(piece_text, (c * 75 + 18, r * 65 + 120))

    return board_list


def generate_board(rows, columns, options_list, spaces_list, used):
    for item in range(rows * columns // 2):
        options_list.append(item)

    for item in range(rows * columns):
        piece = options_list[random.randint(0, len(options_list) - 1)]
        spaces_list.append(piece)

        if piece in used:
            used.remove(piece)
            options_list.remove(piece)
        else:
            used.append(piece)
    print(spaces_list)


def check_guess(first_guess_num, second_guess_num, spaces_list, correct, rows, score, matches):
    if spaces_list[first_guess_num] == spaces_list[second_guess_num]:
        col1 = first_guess_num // rows
        col2 = second_guess_num // rows
        row1 = first_guess_num - (first_guess_num // rows * rows)
        row2 = second_guess_num - (second_guess_num // rows * rows)

        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            score += 1
            matches += 1
    else:
        score += 1

    return score, matches
