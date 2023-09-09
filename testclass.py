import pygame
from sys import exit
from random import randint, choice

'''class IntroEnter(pygame.sprite.Sprite)
	def __init___(self):
		super().__init__()
		game_enter = pygame.image.load('graphics/Intro/enter.png')
		game_enter_zoom = pygame.transform.rotozoom(game_enter,0,2)
		game_enter_position = game_enter_zoom.get_rect(center = (510,380))'''



class IntroPlayer(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_idle_1 = pygame.image.load('graphics/Intro/hat-man-idle-1.png').convert_alpha()
		player_idle_2 = pygame.image.load('graphics/Intro/hat-man-idle-2.png').convert_alpha()
		player_idle_3 = pygame.image.load('graphics/Intro/hat-man-idle-3.png').convert_alpha()
		player_idle_4 = pygame.image.load('graphics/Intro/hat-man-idle-4.png').convert_alpha()
		player_stand_1 = pygame.transform.rotozoom(player_idle_1,0,2)
		player_stand_2 = pygame.transform.rotozoom(player_idle_2,0,2)
		player_stand_3 = pygame.transform.rotozoom(player_idle_3,0,2)
		player_stand_4 = pygame.transform.rotozoom(player_idle_4,0,2)
		self.player_idle = [player_stand_1, player_stand_2, player_stand_3, player_stand_4]
		self.player_index = 0

		self.image = self.player_idle[self.player_index]
		self.rect = self.image.get_rect(midbottom = (464,340))

	def update(self):
		self.player_index += 0.12
		if self.player_index >= len(self.player_idle):self.player_index = 0
		self.image = self.player_idle[int(self.player_index)]

class Player(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_walk_1 = pygame.image.load('graphics/player/hat-man-walk-1.png').convert_alpha()
		player_walk_2 = pygame.image.load('graphics/player/hat-man-walk-2.png').convert_alpha()
		player_walk_3 = pygame.image.load('graphics/player/hat-man-walk-3.png').convert_alpha()
		player_walk_4 = pygame.image.load('graphics/player/hat-man-walk-4.png').convert_alpha()
		player_walk_5 = pygame.image.load('graphics/player/hat-man-walk-5.png').convert_alpha()
		player_walk_6 = pygame.image.load('graphics/player/hat-man-walk-6.png').convert_alpha()
		self.player_walk = [player_walk_1,player_walk_2,player_walk_3,player_walk_4,player_walk_5,player_walk_6]
		self.player_index = 0
		self.player_jump = pygame.image.load('graphics/player/hat-man-walk-1.png').convert_alpha()

		self.image = self.player_walk[self.player_index]
		self.rect = self.image.get_rect(midbottom = (80,623))
		self.gravity = 0

		self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
		self.jump_sound.set_volume(0.5)

	def player_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_SPACE] and self.rect.bottom >= 640:
			self.gravity = -16
			self.jump_sound.play()

	def apply_gravity(self):
		self.gravity += 1.3
		self.rect.y += self.gravity
		if self.rect.bottom >= 640:
			self.rect.bottom = 640

	def animation_state(self):
		if self.rect.bottom < 640: 
			self.image = self.player_jump
		else:
			self.player_index += 0.1
			if self.player_index >= len(self.player_walk):self.player_index = 0
			self.image = self.player_walk[int(self.player_index)]

	def update(self):
		self.player_input()
		self.apply_gravity()
		self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'fly':
			bee1 = pygame.image.load('graphics/aseprite/bee1.png').convert_alpha()
			bee2 = pygame.image.load('graphics/aseprite/bee2.png').convert_alpha()
			self.frames = [bee1,bee2]
			y_pos = 560
		else:
			k1 = pygame.image.load('graphics/aseprite/knight1.png').convert_alpha()
			k2 = pygame.image.load('graphics/aseprite/knight2.png').convert_alpha()
			k3 = pygame.image.load('graphics/aseprite/knight3.png').convert_alpha()
			k4 = pygame.image.load('graphics/aseprite/knight4.png').convert_alpha()
			k5 = pygame.image.load('graphics/aseprite/knight5.png').convert_alpha()
			k6 = pygame.image.load('graphics/aseprite/knight6.png').convert_alpha()
			self.frames = [k1,k2,k3,k4,k5,k6]
			y_pos  = 640

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 15
		self.destroy()

	def destroy(self):
		if self.rect.x <= 0: 
			self.kill()



def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True

class ParallaxLayer:
	def __init__(self,image,speed):
		self.image = pygame.image.load(image).convert_alpha()
		self.speed = speed
		self.image = pygame.transform.scale(pygame.image.load(image).convert_alpha(),(928,678))
		self.position = 0
	
	def update(self):
		self.position -= self.speed
		if self.position < - 928:
			self.position = 0
	
	def draw(self,surface):
		surface.blit(self.image, (self.position, 0))
		surface.blit(self.image, (self.position + 928, 0))
	

pygame.init()
screen = pygame.display.set_mode((928,678))
pygame.display.set_caption('Arturo Jones')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/upheaval.ttf', 35)
game_active = False
start_time = 0
score = 0
bg_music = pygame.mixer.Sound('audio/music2.mp3')
bg_music.play(loops = -1)



#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())
obstacle_group = pygame.sprite.Group()

layers = [
	("graphics/aseprite/layer1.png",0),
	("graphics/aseprite/layer2new.png",1),
	("graphics/aseprite/layer3new.png",2),
	("graphics/aseprite/layer4new.png",3),
	("graphics/aseprite/terrain.png",3),

]


background = [ParallaxLayer(image,speed) for image,speed in layers]

game_intro = pygame.transform.scale(pygame.image.load('graphics/aseprite/Intro.png').convert_alpha(),(928,678))
game_intro_position = game_intro.get_rect(center = (464,339))

game_message = test_font.render('Sobreviva por 30 segundos!',False,(0,0,0))
game_message_rect = game_message.get_rect(center = (464,360))

game_message2 = test_font.render('Morreu!',False,(144,238,144))
game_message2_rect = game_message2.get_rect(center = (464,360))

game_message3 = test_font.render('Sobreviveu!',False,(144,238,144))
game_message3_rect = game_message2.get_rect(center = (464,360))

game_enter = pygame.image.load('graphics/Intro/enter.png')
game_enter_zoom = pygame.transform.rotozoom(game_enter,0,2)
game_enter_position = game_enter_zoom.get_rect(center = (510,380))

player2 = pygame.sprite.GroupSingle()
player2.add(IntroPlayer())

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,500)

font_fade = pygame.USEREVENT + 1
show_text = True

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()
		if event.type == font_fade:
			show_text = not show_text

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly','hound'])))
		
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)
				obstacle_group.empty()


	if game_active:

		for layers in background:
			layers.update()
			layers.draw(screen)

		player.draw(screen)
		player.update()

		obstacle_group.draw(screen)
		obstacle_group.update()

		current_time = int(pygame.time.get_ticks() / 1000) - start_time
		score_surf = test_font.render(f'Tempo: {current_time}',1,(64,64,64))
		score_rect = score_surf.get_rect(center = ((464,50)))
		screen.blit(score_surf,score_rect)

		score = current_time
		if score == 30:
			game_active = False

		if game_active:
			game_active = collision_sprite()

		
		
	else:

		screen.fill((255,255,255))
		if score == 0:
			screen.blit(game_intro,game_intro_position)
			if show_text:
				screen.blit(game_enter,game_enter_position)
			player2.draw(screen)
			player2.update()
			pygame.display.flip()

		elif score == 30:
			screen.fill((255,255,255))
			screen.blit(game_message3,game_message3_rect)
		else:
			screen.fill((0,0,0))
			screen.blit(game_message2,game_message2_rect)


	pygame.display.update()
	clock.tick(60)
