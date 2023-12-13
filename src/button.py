import pygame
import os
def create_buton(x,y,screen,width,height):
    GREEN = (82, 214, 141)
    button = pygame.Rect(x,y,width,height)
    return pygame.draw.rect(screen,('#725ea4'),button,0,10)
# 150 y 50 