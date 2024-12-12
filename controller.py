from settings import Settings
from score import Score
from snake import Snake
from fruit import Fruit
from view import View
import pygame


class Controller:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.score = Score(self.settings.get_fonts()["score_font"], self.settings.get_colors()["CYAN"])
        self.entities = []
        self.view = View(self.settings)
        self.game_over = False
        self.game_close = False


    def init_game(self):
        self.entities.clear()
        pygame.display.update()
        snake = Snake(self.settings.get_colors()["BLACK"])
        snake.set_position(self.view.dis.get_size()[0] // 2, self.view.dis.get_size()[1] // 2)
        snake.snake_nodes_list.append([snake.x, snake.y])
        self.entities.append(snake)

        fruit = Fruit(self.settings.get_colors()["RED"])
        fruit.set_random_position(self.settings.get_screen_size()["w"], self.settings.get_screen_size()["h"])
        self.entities.append(fruit)

        self.game_loop()


    def game_loop(self):
        clock = pygame.time.Clock()
        dx = 0
        dy = 0
        while not self.game_over:
            while self.game_close:
                self.view.game_end_draw("You lose. Play again (C) or Quit (Q)?")
                self.end_game()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

                if event.type == pygame.KEYDOWN:
                    snake_block_width = self.settings.get_snake_settings()["snake_block_width"]
                    if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        dx = -snake_block_width
                        dy = 0
                    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        dx = snake_block_width
                        dy = 0
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        dx = 0
                        dy = -snake_block_width
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        dx = 0
                        dy = snake_block_width
            new_coords = [self.entities[0].x + dx, self.entities[0].y + dy]
            if self.check_collision(new_coords):
                self.game_close = True
            if self.check_self_eating(new_coords):
                self.game_close = True
            self.check_fruit_eating(new_coords)

            self.view.main_draw(self.entities, self.score)

            clock.tick(self.settings.get_snake_settings()["snake_speed"])
        pygame.quit()
        quit()


    def check_collision(self, new_coords):
        if new_coords[0] >= self.view.dis.get_size()[0] or new_coords[0] < 0 or new_coords[1] >= self.view.dis.get_size()[
            1] or new_coords[1] < 0:
            return True
        return False


    # def player_move(self, event, dx, dy):
    #     if event.type == pygame.KEYDOWN:
    #         snake_block_width = self.settings.get_snake_settings()["snake_block_width"]
    #         if event.key == pygame.K_LEFT or event.key == pygame.K_a:
    #             dx = -snake_block_width
    #             dy = 0
    #         if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
    #             dx = snake_block_width
    #             dy = 0
    #         if event.key == pygame.K_UP or event.key == pygame.K_w:
    #             dx = 0
    #             dy = -snake_block_width
    #         if event.key == pygame.K_DOWN or event.key == pygame.K_s:
    #             dx = 0
    #             dy = snake_block_width
    #
    #     return [self.entities[0].x + dx, self.entities[0].y + dy], [dx, dy]


    def check_self_eating(self, new_coords):
        snake_head = [new_coords[0], new_coords[1]]
        self.entities[0].snake_nodes_list.append(snake_head)
        self.entities[0].set_position(snake_head[0], snake_head[1])
        if len(self.entities[0].snake_nodes_list) > self.entities[0].snake_length:
            del self.entities[0].snake_nodes_list[0]
        for node in self.entities[0].snake_nodes_list[:-1]:
            if node == snake_head:
                return True
        return False


    def check_fruit_eating(self, new_coords):
        for fruit in self.entities[1:]:
            if fruit.x == new_coords[0] and fruit.y == new_coords[1]:
                fruit.set_random_position(self.settings.get_screen_size()["w"], self.settings.get_screen_size()["h"])
                self.entities[0].snake_length += 1
                self.score.score_add()
                break


    def end_game(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    self.game_over = True
                    self.game_close = False
                if event.key == pygame.K_c:
                    self.game_close = False
                    self.init_game()