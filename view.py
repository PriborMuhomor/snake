import pygame
class View:
    def __init__(self, settings):
        self.settings = settings
        self.dis = pygame.display.set_mode((self.settings.get_screen_size()["w"], self.settings.get_screen_size()["h"]))
        pygame.display.update()
        pygame.display.set_caption("Snake")
        

    def main_draw(self, entities, score):
        self.dis.fill(self.settings.get_colors()["WHITE"])
        for element in entities:
            element.draw(self.dis)
        score.score_draw(self.dis)
        pygame.display.update()



    def game_end_draw(self, msg):
        self.dis.fill(self.settings.get_colors()["WHITE"])
        mesg = self.settings.get_fonts()["message_font"].render(msg, True, self.settings.get_colors()["RED"])
        self.dis.blit(mesg, (self.dis.get_size()[0]//3, self.dis.get_size()[1]//2))
        pygame.display.update()





