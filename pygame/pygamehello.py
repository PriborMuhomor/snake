import pygame
from pygame.locals import*

pygame.init()
display = pygame.display.set_mode((1000,1000))
pygame.display.set_caption("hello PyGame!")
x, y = [100,200]

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,140,255)
CYAN = (100,250,255)
KIRPICH = (169,0,0)


display.fill(BLUE)

pygame.draw.polygon(display, BLACK, ((300,200),(500,100),(700,200)))
pygame.draw.rect(display, KIRPICH,(350,200,290,500))
pygame.draw.rect(display,CYAN,(400,250,50,50))
pygame.draw.rect(display,CYAN,(400,350,50,50))
pygame.draw.rect(display,CYAN,(530,350,50,50))
pygame.draw.rect(display,CYAN,(400,450,50,50))
pygame.draw.rect(display,CYAN,(530,250,50,50))
pygame.draw.rect(display,CYAN,(530,450,50,50))
pygame.draw.rect(display,CYAN,(530,550,50,50))
pygame.draw.rect(display,CYAN,(400,550,50,50))
pygame.draw.rect(display,BLACK,(530,620,60,90))



pygame.draw.rect(display, GREEN, (0,700,1000,300))

#pygame.draw.line(display, GREEN, (450,250),(400,350),4)
#pygame.draw.circle(display, BLUE,(450,300),100,0)
#pix_object = pygame.PixelArray(display)
#pix_object[480][380] = CYAN
#pix_object[479][380] = CYAN
#pix_object[478][380] = CYAN
#pix_object[477][380] = CYAN
#pix_object[476][380] = CYAN

#del pix_object

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            break
    
    pygame.display.update()