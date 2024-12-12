import random
import time

import pygame

pygame.init()
w = 800
h = 600
dis=pygame.display.set_mode((w, h))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (100, 250, 255)

snake_block_width = 10

snake_speed = 15


font_style = pygame.font.SysFont(None, 20)

score_font = pygame.font.SysFont("comicsansms", 35)

pygame.display.update()

pygame.display.set_caption("Snake")


clock = pygame.time.Clock()

def draw_snake(snake_block, snake_list):
    for node in snake_list:
        pygame.draw.rect(dis, BLACK, (node[0], node[1], snake_block, snake_block))

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, (dis.get_size()[0]//3, dis.get_size()[1]//2))
def score_draw(score):
    value = score_font.render("Your score: "+str(score), True, CYAN)
    dis.blit(value, (0, 0))

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis.get_size()[0] // 2
    y1 = dis.get_size()[1] // 2

    dx1 = 0
    dy1 = 0
    snake_nodes_list = []
    snake_length = 1

    food_x = round(random.randrange(0, w - snake_block_width) / 10.0) * 10.0
    food_y = round(random.randrange(0, h - snake_block_width) / 10.0) * 10.0

    while not game_over:
        while game_close:


            dis.fill(WHITE)
            message("You lose. Play again (C) or Quit (Q)?", RED)
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    dx1 = -snake_block_width
                    dy1 = 0
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    dx1 = snake_block_width
                    dy1 = 0
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    dx1 = 0
                    dy1 = -snake_block_width
                if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    dx1 = 0
                    dy1 = snake_block_width

        if x1 >= dis.get_size()[0] or x1 < 0 or y1 >= dis.get_size()[1] or y1 < 0:
            game_close = True
        x1 += dx1
        y1 += dy1
        

        dis.fill(WHITE)



        # pygame.draw.rect(dis, (0, 30, 255), (x1, y1, snake_block_width, snake_block_width))

        pygame.draw.rect(dis, RED, (food_x, food_y, snake_block_width, snake_block_width))

        snake_head = []

        snake_head.append(x1)
        snake_head.append(y1)
        snake_nodes_list.append(snake_head)
        if len(snake_nodes_list) > snake_length:
            del snake_nodes_list[0]
        for node in snake_nodes_list[:-1]:
            if node == snake_head:
                game_close = True



        draw_snake(snake_block_width, snake_nodes_list)
        score_draw(snake_length-1)
        pygame.display.update()




        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, w - snake_block_width) / 10.0) * 10.0
            food_y = round(random.randrange(0, h - snake_block_width) / 10.0) * 10.0
            snake_length += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()

gameLoop()