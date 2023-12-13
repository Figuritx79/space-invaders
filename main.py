# Para instalar depencias: pip install -r requirements.txt
import pygame
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
backgroun_button = pygame.image.load("./assets/button.png").convert()

# Redimensionamos el fondo para que este igual a la dimension de la pantalla
backgroun_main_redimension = pygame.transform.scale(backgroun_main,(890,720)).convert()
backgroun_button_redimension = pygame.transform.scale(backgroun_button,(150,50)).convert()

# Lo mismo que arriba pero en este caso guardamos el icono del juego
icon = pygame.image.load(ruta+"GameIcon.png")


# Creamos la varible clock para determinar en un rato a cuantos fps va ir el juego
clock = pygame.time.Clock()

class  manager_states():
    def __init__(self):
        self.state = 'main'
    def main_state(self):
        screen.blit(backgroun_main_redimension,(0,0)) 
        start = create_buton(340,250,screen,150,50)
        credit = create_buton(340,350,screen,150,50)
        exit_button = create_buton(340,450,screen,150,50)
        create_text("Space Invaders",screen,445,100,50)
        create_text('Start',screen,410,280,32)
        create_text('Credits',screen,420,380,32)
        create_text('Exit',screen,415,475   ,32)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if credit.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'credit'
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if exit_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()

        pygame.display.set_icon(icon)
    
        pygame.display.flip()

    def clear_screen(self):
        screen.fill((0,0,0))
    def credits_state(self):
        create_text("Juan Enrique",screen,422,150,50)
        create_text("Antonio",screen,422,250,50)
        create_text("Luis Eduardo",screen,422,350,50)
        create_text("Angel Ivan",screen,422,450,50)
        back = create_buton(222,550,screen,450,50)
        create_text('BACK TO THE MENU',screen,445,575,35)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if   back.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'main'
        pygame.display.set_icon(icon)
    
        pygame.display.flip()
       

    def change_state(self):
        if self.state == 'main':
            self.clear_screen()
            self.main_state()
        if self.state == 'credit':
            self.clear_screen()
            self.credits_state()




state_manager = manager_states()
while True: 

    state_manager.change_state()

    clock.tick(60)/100.0
