import pygame
import pygame_gui

def create_buton(manager,text,x,y):
     button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((x, y), (180, 40)),
                                             text=text,
                                             manager=manager)
