from entity import Entity
import pygame

class Snake(Entity):
    def __init__(self, color):
        super().__init__(color)
        self.snake_nodes_list = []
        self.snake_length = 1
        
    def set_position(self,x,y):
        self.x = x
        self.y = y

    def draw(self, dis):
        for node in self.snake_nodes_list:
            pygame.draw.rect(dis, self.color, (node[0], node[1], self.size, self.size))


    # def move(self, dx, dy):
    #     snake_head = []

    #     snake_head.append(self.x+dx)
    #     snake_head.append(self.y+dy)
    #     self.snake_nodes_list.append(snake_head)
    #     if len(self.snake_nodes_list) > self.snake_length:
    #         del self.snake_nodes_list[0]
        
    # def check_collision(self, snake_head):
    #     for node in self.snake_nodes_list[:-1]:
    #         if node == snake_head:
    #             return True
    #     return False