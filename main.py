# Para instalar depencias: pip install -r requirements.txt
import pygame
import sys
sys.path.append('./src')
from button import create_buton
from text import create_text
# Screen dimensions
WIDTH, HEIGTH = 890,720

# Inicializamos el pygame
pygame.init()
ruta = "./assets/"
screen = pygame.display.set_mode((WIDTH,HEIGTH))
pygame.display.set_caption("Space Invaders")

# Load Media
backgroun_main = pygame.image.load("./assets/background_main.png").convert()
background_second = pygame.image.load('./assets/background_game.png').convert()
backgroun_main_redimension = pygame.transform.scale(backgroun_main,(890,720)).convert()
background_second_redimension = pygame.transform.scale(background_second,(WIDTH,HEIGTH)).convert()
icon = pygame.image.load(ruta+"GameIcon.png")

# Creamos la varible clock para determinar en un rato a cuantos fps va ir el juego
clock = pygame.time.Clock()

# Scenes mannager
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

            #Credit state    
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if credit.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'credit'

            # Exit scene
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if exit_button.collidepoint(pygame.mouse.get_pos()):
                    pygame.quit()
                    sys.exit()
            # Questions scenes
            if event.type == pygame.MOUSEBUTTONDOWN  and event.button ==1:
                if start.collidepoint(pygame.mouse.get_pos()):
                    state_random = ["one"]
                    self.state = state_random[0]


        pygame.display.set_icon(icon)
    
        pygame.display.flip()

    def clear_screen(self):
        screen.fill((0,0,0))


    def game_background(self):
        screen.blit(background_second_redimension,(0,0))    

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
                if back.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'main'
        pygame.display.set_icon(icon)
        pygame.display.flip()

    def question_one(self):
        self.game_background()
        create_text('Si quieres un powerup, contesta',screen,422,50,30)
        create_text('Dime que numero es 10101',screen,220,180,25)
        one = create_buton(50,310,screen,150,50)
        two = create_buton(50,410,screen,150,50)
        three = create_buton(50,510,screen,150,50)
        create_text('A) 21',screen,85,335,25)
        create_text('B) 25',screen,85,435,25)
        create_text('C) 18',screen,85,535,25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if two.collidepoint(pygame.mouse.get_pos()):
                    self.game_background()
                    self.state = 'game'

        pygame.display.set_icon(icon)
        pygame.display.flip()
    
    def game_state(self):
        create_text('HOla',screen,422,360,30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.set_icon(icon)
        pygame.display.flip()

    def change_state(self):
        if self.state == 'main':
            self.clear_screen()
            self.main_state()
        if self.state == 'credit':
            self.clear_screen()
            self.credits_state()
        if self.state == 'one':
            self.question_one()    




state_manager = manager_states()
while True: 

    state_manager.change_state()

    clock.tick(60)/100.0
