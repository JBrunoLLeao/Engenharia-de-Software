import pygame
from sys import exit
from random import randint, choice



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
		if keys[pygame.K_SPACE] and self.rect.bottom >= 623:
			self.gravity = -16
			self.jump_sound.play()

	def apply_gravity(self):
		self.gravity += 1.2
		self.rect.y += self.gravity
		if self.rect.bottom >= 623:
			self.rect.bottom = 623

	def animation_state(self):
		if self.rect.bottom < 623: 
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
			fly_1 = pygame.image.load('graphics/Fly/ghost-1.png').convert_alpha()
			fly_2 = pygame.image.load('graphics/Fly/ghost-2.png').convert_alpha()
			fly_3 = pygame.image.load('graphics/Fly/ghost-3.png').convert_alpha()
			fly_4 = pygame.image.load('graphics/Fly/ghost-4.png').convert_alpha()
			self.frames = [fly_1,fly_2,fly_3,fly_4]
			y_pos = 550
		else:
			Hound1 = pygame.image.load('graphics/Hound/hell-gato-1.png').convert_alpha()
			Hound2 = pygame.image.load('graphics/Hound/hell-gato-2.png').convert_alpha()
			Hound3 = pygame.image.load('graphics/Hound/hell-gato-3.png').convert_alpha()
			Hound4 = pygame.image.load('graphics/Hound/hell-gato-4.png').convert_alpha()
			self.frames = [Hound1,Hound2,Hound3,Hound4]
			y_pos  = 623

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		speed = int(pygame.time.get_ticks() / 1000) - start_time
		self.animation_state()
		self.rect.x -= speed
		self.destroy()

	def destroy(self):
		if self.rect.x <= 0: 
			self.kill()



def display_score():
	current_time = int(pygame.time.get_ticks() / 1000) - start_time
	score_surf = test_font.render(f'Tempo: {current_time}',False,(64,64,64))
	score_rect = score_surf.get_rect(center = ((464,50)))
	screen.blit(score_surf,score_rect)
	return current_time

def Victory():
	if display_score() == 30:
		bg_music.stop()
		victory_music = pygame.mixer.Sound('audio/music.wav')
		victory_music.play(loops = -1)
		return False
	else: return True

def collision_sprite():
	if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
		obstacle_group.empty()
		return False
	else: return True


class ParallaxBackground:
    def __init__(self, screen_size, layers):
        self.screen_size = screen_size
        self.layers = layers  # List of tuples: (image_path, speed)

        self.images = []
        for layer in self.layers:
            image = pygame.image.load(layer[0]).convert_alpha()
            image = pygame.transform.scale(image, screen_size)
            self.images.append(image)

        self.num_layers = len(self.layers)
        self.layer_positions = [0] * self.num_layers

    def update(self):
        for i in range(self.num_layers):
            self.layer_positions[i] -= self.layers[i][1]
            if self.layer_positions[i] < -self.screen_size[0]:
                self.layer_positions[i] = 0

    def draw(self, screen):
        for i in range(self.num_layers):
            screen.blit(self.images[i], (self.layer_positions[i], 0))
            screen.blit(self.images[i], (self.layer_positions[i] + self.screen_size[0], 0))

pygame.init()
screen = pygame.display.set_mode((928,678))
pygame.display.set_caption('Arturo decide andar na floresta - The Game')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/somepx.ttf', 50)
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
	("graphics/Layers/layer12.png", 1),
    ("graphics/Layers/layer10.png", 2),
    ("graphics/Layers/layer7.png", 3),
    ("graphics/Layers/layer4.png", 4),
    ("graphics/Layers/layer2.png", 4),
    ("graphics/Layers/layer3.png", 4),
    ("graphics/Layers/layer1.png", 4)
]

background = ParallaxBackground((928,678), layers)

game_name = test_font.render('Arturo decide andar na floresta - The Game',False,(144,238,144))
game_name_rect = game_name.get_rect(center = (464,139))

game_message = test_font.render('Sobreviva por 30 segundos!',False,(144,238,144))
game_message_rect = game_message.get_rect(center = (464,360))

game_message2 = test_font.render('Sobreviveu!',False,(144,238,144))
game_message2_rect = game_message2.get_rect(center = (464,360))

# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,1500)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			exit()

		if game_active:
			if event.type == obstacle_timer:
				obstacle_group.add(Obstacle(choice(['fly','snail'])))
		
		else:
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)


	if game_active:

		score = display_score()

		background.update()
		background.draw(screen)

		player.draw(screen)
		player.update()
		obstacle_group.update()
		obstacle_group.draw(screen)

		game_active = Victory()
		if game_active == True:
			game_active = collision_sprite()
		
		
	else:

		screen.fill((255,255,255))
		if score == 0:
			screen.blit(game_name,game_name_rect)
			screen.blit(game_message,game_message_rect)
		elif score == 30:
			game_message = test_font.render(f'YOU WIN',False,(144,248,144))
			game_message_rect = game_message.get_rect(center = (464,360))
			screen.blit(game_message2,game_message2_rect)
		else:
			screen.fill((0,0,0))
			bg_music.stop()
			game_message = test_font.render(f'YOU DIED',False,(255,0,0))
			game_message_rect = game_message.get_rect(center = (464,360))
			screen.blit(game_message,game_message_rect)

	pygame.display.update()
	clock.tick(60)
