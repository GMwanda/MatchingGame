import random

import pygame

pygame.init()


def draw_backgrounds(screen, BLACK, GREY, WHITE, WIDTH, HEIGHT, title_font):
    top_menu = pygame.draw.rect(screen, BLACK, [0, 0, WIDTH, 100], 0)
    title_text = title_font.render("Josiah's Matching Game", True, WHITE)
    screen.blit(title_text, (20, 20))
    board_space = pygame.draw.rect(screen, GREY, [0, 100, WIDTH, HEIGHT - 200], 0)
    bottom_menu = pygame.draw.rect(screen, BLACK, [0, HEIGHT - 100, WIDTH, 100], 0)


def draw_boards(rows, columns, screen, WHITE, GREY, small_font, spaces_list):
    board_list = []
    for i in range(columns):
        for j in range(rows):
            piece = pygame.draw.rect(screen, WHITE, [i * 75 + 12, j * 65 + 112, 50, 50], 0, 4)
            board_list.append(piece)
            piece_text = small_font.render(f'{spaces_list[i * rows + j]}', True, GREY)
            screen.blit(piece_text, (i * 75 + 18, j * 65 + 120))

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


def check_guess(first_guess_num, second_guess_num, spaces_list, correct, rows, score, matches):
    if spaces_list[first_guess_num] == spaces_list[second_guess_num]:
        col1 = first_guess_num // rows
        col2 = second_guess_num // rows
        row1 = first_guess_num - (col1 * rows)
        row2 = second_guess_num - (col2 * rows)

        if correct[row1][col1] == 0 and correct[row2][col2] == 0:
            correct[row1][col1] = 1
            correct[row2][col2] = 1
            score += 1
            matches += 1
            print(correct)

    else:
        score += 1
