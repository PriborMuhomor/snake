class Score:
    def __init__(self, score_font, font_color):
        self.score = 0
        self.score_font = score_font
        self.font_color = font_color

    def score_draw(self, display):
        value = self.score_font.render("Your score: "+str(self.score), True, self.font_color)
        display.blit(value, (0, 0))
    
    def score_add(self):
        self.score += 1

        