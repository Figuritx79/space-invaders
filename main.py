# Para instalar depencias: pip install -r requirements.txt
import pygame
from pygame import mixer
from pygame.locals import *
import random
import sys
sys.path.append('./src')
from button import create_buton
from text import create_text
# Screen dimensions
WIDTH, HEIGTH = 890,720

# Inicializamos el pygame
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
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

#load sounds
explosion_fx = pygame.mixer.Sound("./assets/explosion.wav")
explosion_fx.set_volume(0.25)
explosion2_fx = pygame.mixer.Sound("./assets/explosion2.wav")
explosion2_fx.set_volume(0.25)
laser_fx = pygame.mixer.Sound("./assets/laser.wav")
laser_fx.set_volume(0.25)


#define game variables
rows = 5
cols = 5
alien_cooldown = 1000#bullet cooldown in milliseconds
last_alien_shot = pygame.time.get_ticks()
countdown = 3
last_count = pygame.time.get_ticks()
game_over = 0#0 is no game over, 1 means player has won, -1 means player has lost

#define colours
red = (255, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)

#create spaceship class
class Spaceship(pygame.sprite.Sprite):
	def __init__(self, x, y, health):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./assets/spaceship.png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.health_start = health
		self.health_remaining = health
		self.last_shot = pygame.time.get_ticks()


	def update(self):
		#set movement speed
		speed = 8
		#set a cooldown variable
		cooldown = 500 #milliseconds
		game_over = 0


		#get key press
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] and self.rect.left > 0:
			self.rect.x -= speed
		if key[pygame.K_RIGHT] and self.rect.right < WIDTH:
			self.rect.x += speed

		#record current time
		time_now = pygame.time.get_ticks()
		#shoot
		if key[pygame.K_SPACE] and time_now - self.last_shot > cooldown:
			laser_fx.play()
			bullet = Bullets(self.rect.centerx, self.rect.top)
			bullet_group.add(bullet)
			self.last_shot = time_now


		#update mask
		self.mask = pygame.mask.from_surface(self.image)


		#draw health bar
		pygame.draw.rect(screen, red, (self.rect.x, (self.rect.bottom + 10), self.rect.width, 15))
		if self.health_remaining > 0:
			pygame.draw.rect(screen, green, (self.rect.x, (self.rect.bottom + 10), int(self.rect.width * (self.health_remaining / self.health_start)), 15))
		elif self.health_remaining <= 0:
			explosion = Explosion(self.rect.centerx, self.rect.centery, 3)
			explosion_group.add(explosion)
			self.kill()
			game_over = -1
		return game_over
#create Bullets class
class Bullets(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./assets/bullet.png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		self.rect.y -= 5
		if self.rect.bottom < 0:
			self.kill()
		if pygame.sprite.spritecollide(self, alien_group, True):
			self.kill()
			explosion_fx.play()
			explosion = Explosion(self.rect.centerx, self.rect.centery, 2)
			explosion_group.add(explosion)
               
#create Aliens class
class Aliens(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./assets/alien" + str(random.randint(1, 5)) + ".png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.move_counter = 0
		self.move_direction = 1

	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		if abs(self.move_counter) > 75:
			self.move_direction *= -1
			self.move_counter *= self.move_direction

class Alien_Bullets(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load("./assets/alien_bullet.png")
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]

	def update(self):
		self.rect.y += 2
		if self.rect.top > HEIGTH:
			self.kill()
		if pygame.sprite.spritecollide(self, spaceship_group, False, pygame.sprite.collide_mask):
			self.kill()
			explosion2_fx.play()
			#reduce spaceship health
			spaceship.health_remaining -= 1
			explosion = Explosion(self.rect.centerx, self.rect.centery, 1)
			explosion_group.add(explosion)  

#create Explosion class
#create Explosion class
class Explosion(pygame.sprite.Sprite):
	def __init__(self, x, y, size):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		for num in range(1, 6):
			img = pygame.image.load(f"./assets/exp{num}.png")
			if size == 1:
				img = pygame.transform.scale(img, (20, 20))
			if size == 2:
				img = pygame.transform.scale(img, (40, 40))
			if size == 3:
				img = pygame.transform.scale(img, (160, 160))
			# add the image to the list
			self.images.append(img)
		self.index = 0
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.counter = 0


	def update(self):
		explosion_speed = 3
		#update explosion animation
		self.counter += 1

		if self.counter >= explosion_speed and self.index < len(self.images) - 1:
			self.counter = 0
			self.index += 1
			self.image = self.images[self.index]

		#if the animation is complete, delete explosion
		if self.index >= len(self.images) - 1 and self.counter >= explosion_speed:
			self.kill()


#create sprite groups
spaceship_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()
alien_group = pygame.sprite.Group()
alien_bullet_group = pygame.sprite.Group()
explosion_group = pygame.sprite.Group()

def create_aliens():
	#generate alienslast_count = pygame.time.get_ticks()
	for row in range(rows):
		for item in range(cols):
			alien = Aliens(100 + item * 100, 100 + row * 70)
			alien_group.add(alien)
         
create_aliens()
#create player
spaceship = Spaceship(int(WIDTH / 2), HEIGTH - 100, 3)
spaceship_group.add(spaceship)

def game():
    countdown = 0
    last_alien_shot = pygame.time.get_ticks()
    game_over = 0
    alien_cooldown = 1000
    if countdown == 0 :
        time_now = pygame.time.get_ticks()
        if time_now - last_alien_shot > alien_cooldown and len(alien_bullet_group) < 5 and len(alien_group) > 0: 
            attacking_alien = random.choice(alien_group.sprites())
            alien_bullet = Alien_Bullets(attacking_alien.rect.centerx, attacking_alien.rect.bottom)
            alien_bullet_group.add(alien_bullet)
            last_alien_shot = time_now
        if len(alien_group) == 0:
            game_over = 1
        if game_over == 0:
            game_over = spaceship.update()
            bullet_group.update()
            alien_bullet_group.update()
            alien_group.update()
        else:
            if game_over == -1:
                create_text('GAME OVER',screen,int(WIDTH / 2 - 100),int(HEIGTH /2 + 50),40)
            if game_over == 1:
                create_text('YOU WIN',screen,int(WIDTH / 2 - 100),int(HEIGTH /2 + 50),40)
    if countdown > 0:
        create_text('GET READY',screen,int(WIDTH / 2 - 100),int(HEIGTH /2 + 50),40)
        create_text(str(countdown),screen,int(WIDTH / 2 - 100),int(HEIGTH /2 + 50),40)
        count_timer = pygame.time.get_ticks()
        if count_timer > 1000:
            countdown -= 1
            last_count = count_timer
    explosion_group.update()
    spaceship_group.draw(screen)
    alien_group.draw(screen)
    alien_bullet_group.draw(screen)
    explosion_group.draw(screen)
                 
            

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
                    state_random = ["one","two","three","four"]
                    random_scene = random.randint(0,3)
                    self.state = state_random[random_scene]


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
                    self.state = 'game'
                    self.clear_screen

        pygame.display.set_icon(icon)
        pygame.display.flip()

    def question_two(self):
        create_text('Si quieres un powerup, contesta',screen,422,50,30)
        create_text('Dime que numero es 1000 en hexa',screen,280,180,25)
        one = create_buton(50,310,screen,150,50)
        two = create_buton(50,410,screen,150,50)
        three = create_buton(50,510,screen,150,50)
        create_text('A) 21EFA',screen,105,335,25)
        create_text('B) 3E8',screen,105,435,25)
        create_text('C) 18AF',screen,105,535,25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if two.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'game'
                    self.clear_screen

        pygame.display.set_icon(icon)
        pygame.display.flip()

    def question_three(self):
        create_text('Si quieres un powerup, contesta',screen,422,50,30)
        create_text('Salida de V con el operador NOT',screen,280,180,25)
        one = create_buton(50,310,screen,150,50)
        two = create_buton(50,410,screen,150,50)
        three = create_buton(50,510,screen,150,50)
        create_text('A) V',screen,105,335,25)
        create_text('B) F',screen,105,435,25)
        create_text('C) OLO',screen,105,535,25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if two.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'game'
                    self.clear_screen

        pygame.display.set_icon(icon)
        pygame.display.flip()
        
    def question_four(self):
        create_text('Si quieres un powerup, contesta',screen,422,50,30)
        create_text('Cual es el operador <=>',screen,280,180,25)
        one = create_buton(50,310,screen,150,50)
        two = create_buton(50,410,screen,150,50)
        three = create_buton(50,510,screen,150,50)
        create_text('A) Tampo',screen,105,335,25)
        create_text('B) No se',screen,105,435,25)
        create_text('C) AND',screen,105,535,25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 :
                if two.collidepoint(pygame.mouse.get_pos()):
                    self.state = 'game'
                    self.clear_screen

        pygame.display.set_icon(icon)
        pygame.display.flip()
    
    def game_state(self):
        game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.set_icon(icon)
        pygame.display.update()

    def change_state(self):
        if self.state == 'main':
            self.clear_screen()
            self.main_state()
        if self.state == 'credit':
            self.clear_screen()
            self.credits_state()
        if self.state == 'one':
            self.game_background()
            self.question_one()
        if self.state == 'two':
            self.game_background()
            self.question_two()
        if self.state == 'three':
            self.game_background()
            self.question_three()
        if self.state == 'four':
            self.game_background()
            self.question_four()
        if self.state == 'game':
            self.clear_screen()
            self.game_state()    




state_manager = manager_states()
while True: 
    

    clock.tick(60)/100.0
    state_manager.change_state()
