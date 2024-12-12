from entity import Entity
import random
import pygame
class Fruit(Entity):
    def __init__(self, color):
        super().__init__(color)

    def set_random_position(self, w, h):
        self.x = round(random.randrange(0, w - self.size) / 10.0) * 10.0
        self.y = round(random.randrange(0, h - self.size) / 10.0) * 10.0
    def draw(self, dis):
        pygame.draw.rect(dis, self.color, (self.x, self.y, self.size, self.size))