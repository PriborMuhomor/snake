import pygame

class Settings:
    def __init__(self):
        self.__colors = {
            "BLACK":(0,0,0),
            "WHITE": (255,255,255),
            "RED": (255,0,0),
            "GREEN": (0,255,0),
            "BLUE": (0,140,255),
            "CYAN": (100,250,255),
        } 
        self.__screen_size = {
            "w": 800,
            "h": 600
        }
        self.__snake_settings = {
            "snake_block_width": 10,
            "snake_speed": 15
        }
        self.__fonts = {
            "message_font": pygame.font.SysFont("comicsansms", 20),
            "score_font": pygame.font.SysFont("comicsansms", 35)
        }
    def get_colors(self):
        return self.__colors

    def get_screen_size(self):
        return self.__screen_size
    
    def get_snake_settings(self):
        return self.__snake_settings
    
    def get_fonts(self):
        return self.__fonts


    
        
        