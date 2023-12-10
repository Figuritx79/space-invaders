import pygame
import os 
current_dir = os.path.dirname(os.path.abspath(__file__))
assets_path = os.path.join(current_dir, '..', 'assets')
font_path = os.path.join(assets_path, '04B03.ttf')



def create_text(text,screen):
    GREEN = (82, 214, 141)# Color verde en RGB
    font = pygame.font.Font(font_path, 50)  # Fuente y tamaño del texto
    text_surface = font.render(text, True, GREEN)  # Renderizar el texto
    text_rect = text_surface.get_rect()
    text_rect.center = (screen.get_width() // 2, 100)  # Centrar el texto en la pantalla
    screen.blit(text_surface, text_rect)  # Dibujar el texto en la pantalla

