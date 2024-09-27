import pygame as py
from pygame.locals import *
import random

py.init()

# Define colors
red = (255, 0, 0)
blue = (51, 153, 255)
grey = (192, 192, 192)
green = (51, 102, 0)
yellow = (255, 255, 0)

# Window dimensions
win_width = 600
win_height = 400

window = py.display.set_mode((win_width, win_height))
py.display.set_caption("Snake Game")

snake_block = 10
snake_speed = 15

clock = py.time.Clock()

font_style = py.font.SysFont("msreference Sans Serif", 24)
score_font = py.font.SysFont("goudyoldstyle", 32)

def user_score(score):
    score_display = score_font.render("Score: " + str(score), True, blue)
    window.blit(score_display, [0, 0])

def game_snake(snake_block, snake_list):
    for x in snake_list:
        py.draw.rect(window, green, [x[0], x[1], snake_block, snake_block])

def message(msg):
    msg_rendered = font_style.render(msg, True, red)
    window.blit(msg_rendered, [win_width / 9, win_height / 9])

def game_loop():
    game_over = False
    game_close = False

    x1 = win_width / 2
    y1 = win_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    snake_length = 1

    foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0

    while not game_over:
        while game_close:
            window.fill(green)
            message("You Lose! Press P to Play Again or Q to Quit.")
            user_score(snake_length - 1)
            py.display.update()

            for event in py.event.get():
                if event.type == py.KEYDOWN:
                    if event.key == py.K_q:
                        game_over = True
                        game_close = False
                    if event.key == py.K_p:
                        game_loop()

        for event in py.event.get():
            if event.type == py.QUIT:
                game_over = True
            if event.type == py.KEYDOWN:
                if event.key == K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == K_UP:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == K_DOWN:
                    x1_change = 0
                    y1_change = snake_block

        if x1 >= win_width or x1 < 0 or y1 >= win_height or y1 < 0:
            print("Game Over: Out of bounds")  # Debug print
            game_close = True

        x1 += x1_change
        y1 += y1_change
        window.fill(grey)

        py.draw.rect(window, yellow, [foodx, foody, snake_block, snake_block])

        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        game_snake(snake_block, snake_list)
        user_score(snake_length - 1)

        py.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, win_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, win_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    py.quit()
    quit()

game_loop()