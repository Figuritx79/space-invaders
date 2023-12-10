# Para instalar depencias: pip install -r requirements.txt
import pygame
import pygame_gui as pgi
import sys
sys.path.append('./src')
from button import create_buton
from text import create_text

WIDTH, HEIGTH = 890,720

# Inicializamos el pygame
pygame.init()

#Creamos una varible que tenga la ruta de la imagenes
ruta = "./assets/"

# Le damos dimensiones a la pantalla 
screen = pygame.display.set_mode((WIDTH,HEIGTH))

# Le damos nombre a nuestro juego
pygame.display.set_caption("Space Invaders")

# Guaradamos el fondo principal en una varible
backgroun_main = pygame.image.load("./assets/background_main.png").convert()

# Redimensionamos el fondo para que este igual a la dimension de la pantalla
backgroun_main_redimension = pygame.transform.scale(backgroun_main,(890,720)).convert()

# Lo mismo que arriba pero en este caso guardamos el icono del juego
icon = pygame.image.load(ruta+"GameIcon.png")


manager = pgi.UIManager((WIDTH,HEIGTH))
# Creamos la varible clock para determinar en un rato a cuantos fps va ir el juego
clock = pygame.time.Clock()


create_buton(manager,'Start',340,230)   
create_buton(manager,'Credits',340,330)   
create_buton(manager,'Exit',340,430)  

screen.blit(backgroun_main_redimension,(0,0))   
create_text("Space Invaders",screen)
# Esta varible la inicializamos con true para comezar el loop jugable
running = True 

while running: 

    time_delta = clock.tick(60) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

 

    pygame.display.set_icon(icon)

    manager.process_events(event)

    manager.update(time_delta)

    manager.draw_ui(screen)
    
    pygame.display.flip()


pygame.quit()