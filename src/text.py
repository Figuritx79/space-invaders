import pygame
import os 
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(current_dir, '..', 'assets')
font_path = os.path.join(assets_path, '04B03.ttf')



def create_text(text,screen,x,y,font_size):
    GREEN = (82, 214, 141)# Color verde en RGB
    font = pygame.font.Font(font_path, font_size)  # Fuente y tamaño del texto
    text_surface = font.render(text, True, GREEN)  # Renderizar el texto
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)  # Centrar el texto en la pantalla
    screen.blit(text_surface, text_rect)  # Dibujar el texto en la pantalla

# 445 y 100