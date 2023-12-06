# Para instalar depencias: pip install -r requirements.txt
import pygame
import sys
import src

# Inicializamos el pygame
pygame.init()

#Creamos una varible que tenga la ruta de la imagenes
ruta = "./assets/"

# Le damos dimensiones a la pantalla 
screen = pygame.display.set_mode((890,720))

# Le damos nombre a nuestro juego
pygame.display.set_caption("Space Invaders")

# Guaradamos el fondo principal en una varible
backgroun_main = pygame.image.load("./assets/background_main.png").convert()

# Redimensionamos el fondo para que este igual a la dimension de la pantalla
backgroun_main_redimension = pygame.transform.scale(backgroun_main,(890,720)).convert()

# Lo mismo que arriba pero en este caso guardamos el icono del juego
icon = pygame.image.load(ruta+"GameIcon.png")

# Creamos la varible clock para determinar en un rato a cuantos fps va ir el juego
clock = pygame.time.Clock()

# Esta varible la inicializamos con true para comezar el loop jugable
running = True 

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.blit(backgroun_main_redimension,(0,0))
    pygame.display.set_icon(icon)

    pygame.display.flip()

    clock.tick(60)


pygame.quit()