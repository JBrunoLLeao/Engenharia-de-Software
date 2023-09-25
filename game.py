import pygame
from sys import exit
from random import randint, choice

class WinPlayer(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_win_1 = pygame.image.load('graphics/aseprite/medal1.png').convert_alpha()
		player_win_2 = pygame.image.load('graphics/aseprite/medal2.png').convert_alpha()
		player_win_3 = pygame.image.load('graphics/aseprite/medal3.png').convert_alpha()
		player_win_4 = pygame.image.load('graphics/aseprite/medal4.png').convert_alpha()
		player_winscreen_1 = pygame.transform.scale(player_win_1,(100,100))
		player_winscreen_2 = pygame.transform.scale(player_win_2,(100,100))
		player_winscreen_3 = pygame.transform.scale(player_win_3,(100,100))
		player_winscreen_4 = pygame.transform.scale(player_win_4,(100,100))
		self.player_win = [player_winscreen_1, player_winscreen_2, player_winscreen_3, player_winscreen_4]
		self.player_index = 0

		self.image = self.player_win[self.player_index]
		self.image.set_colorkey((255,255,255), pygame.RLEACCEL)
		self.rect = self.image.get_rect(midbottom = (464,100))

	def update(self):
		self.player_index += 0.009
		if self.player_index >= len(self.player_win):self.player_index = 0
		self.image = self.player_win[int(self.player_index)]

class DeathPlayer(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		player_death_1 = pygame.image.load('graphics/aseprite/death-1.png').convert_alpha()
		player_death_2 = pygame.image.load('graphics/aseprite/death-2.png').convert_alpha()
		player_deathscreen_1 = pygame.transform.scale(player_death_1,(200,200))
		player_deathscreen_2 = pygame.transform.scale(player_death_2,(200,200))
		self.player_death = [player_deathscreen_1, player_deathscreen_2]
		self.player_index = 0

		self.image = self.player_death[self.player_index]
		self.image.set_colorkey((255,255,255), pygame.RLEACCEL)
		self.rect = self.image.get_rect(midbottom = (464,300))

	def update(self):
		self.player_index += 0.12
		if self.player_index >= len(self.player_death):self.player_index = 0
		self.image = self.player_death[int(self.player_index)]

class IntroBackground(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		intro_1 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro1.png').convert_alpha(),(928,678))
		intro_2 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro2.png').convert_alpha(),(928,678))
		intro_3 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro3.png').convert_alpha(),(928,678))
		intro_4 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro4.png').convert_alpha(),(928,678))
		intro_5 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro5.png').convert_alpha(),(928,678))
		intro_6 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro6.png').convert_alpha(),(928,678))
		intro_7 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro7.png').convert_alpha(),(928,678))
		intro_8 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro8.png').convert_alpha(),(928,678))
		intro_9 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro9.png').convert_alpha(),(928,678))
		intro_10 = pygame.transform.scale(pygame.image.load('graphics/aseprite/animatedintro10.png').convert_alpha(),(928,678))
		self.intro = [intro_1,intro_2,intro_3,intro_4,intro_5,intro_6,intro_7,intro_8,intro_9,intro_10]
		self.index = 0

		self.image = self.intro[self.index]
		self.image.set_colorkey((255,255,255), pygame.RLEACCEL)
		self.rect = self.image.get_rect(center = (464,340))

	def update(self):
		self.index += 0.05
		if self.index >= len(self.intro):
			self.image = self.intro[9]
		else:
			self.image = self.intro[int(self.index)]

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
		self.image.set_colorkey((255,255,255), pygame.RLEACCEL)
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
		self.image.set_colorkey((255,255,255), pygame.RLEACCEL)
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
		self.image.set_colorkey((255,255,255), pygame.RLEACCEL)
		self.position = 0
	
	def update(self):
		self.position -= self.speed
		if self.position < - 928:
			self.position = 0
	
	def draw(self,surface):
		surface.blit(self.image, (self.position, 0))
		surface.blit(self.image, (self.position + 928, 0))
	

leaderboard = [

]

class TextBox:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = ""
        self.font = pygame.font.Font(None, 36)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    if self.text != "": add_high_score(self.text,score)
                    self.text = ""
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode

    def draw(self, screen):
        text_surface = self.font.render(self.text, True, (0,0,0))
        width = max(self.rect.width, text_surface.get_width()+10)
        self.rect.w = width
        screen.blit(text_surface, (self.rect.x+5, self.rect.y+5))
        pygame.draw.rect(screen, (0,0,0), self.rect, 2)

def add_high_score(name, score):
    leaderboard.append({"name": name, "score": score})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    #leaderboard.pop()  # Remove the lowest score if the leaderboard exceeds a certain length


def get_player_name():
    player_name = input("Enter your name: ")
    return player_name


def render_leaderboard():

    font = pygame.font.Font('font/upheaval.ttf', 35)
    y = 120
    for entry in leaderboard:
        text = f"{entry['name']}: {entry['score']}"
        text_render = font.render(text, True, (0, 0, 0))
        screen.blit(text_render, (928 // 2 - text_render.get_width() // 2, y))
        y += 40

def reset_game():
    global game_active, score, run
    game_active = False
    run = True
    score = 0
    obstacle_group.empty()

pygame.init()
screen = pygame.display.set_mode((928,678))
pygame.display.set_caption('Arturo Jones')
clock = pygame.time.Clock()

#fonts
test_font = pygame.font.Font('font/upheaval.ttf', 35)
test_font2 = pygame.font.Font('font/RioGrande.ttf', 72)
test_font3 = pygame.font.Font('font/WildWestIcons.ttf',72)

game_active = False
start_time = 0
score = 0

#Music
bg_music = pygame.mixer.Sound('audio/music2.mp3')
bg_music.play(loops = -1)


#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()

playerDeath = pygame.sprite.GroupSingle()
playerDeath.add(DeathPlayer())

playerWin = pygame.sprite.GroupSingle()
playerWin.add(WinPlayer())

inback = pygame.sprite.GroupSingle()
inback.add(IntroBackground())

layers = [
	("graphics/aseprite/layer1.png",0),
	("graphics/aseprite/layer2new.png",1),
	("graphics/aseprite/layer3new.png",2),
	("graphics/aseprite/layer4new.png",3),
	("graphics/aseprite/terrain.png",3)
]

background = [ParallaxLayer(image,speed) for image,speed in layers]

#Intro
game_enter = pygame.image.load('graphics/Intro/enter.png')
game_enter_zoom = pygame.transform.rotozoom(game_enter,0,2)
game_enter_position = game_enter_zoom.get_rect(center = (510,380))





# Timer 
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,425)

font_fade = pygame.USEREVENT + 1
show_text = True

text_box = TextBox(370, 350, 200, 40)
run = True
flag = True
i = 0

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
			text_box.handle_event(event)
			if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
				game_active = True
				start_time = int(pygame.time.get_ticks() / 1000)
				obstacle_group.empty()


	if game_active and run:

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
		if game_active:
			game_active = collision_sprite()
			if (game_active == False): 
				obstacle_group.empty()
				flag = False
				run = False

		
		
	else:
		if score == 0:
			inback.draw(screen)
			inback.update()
			title = test_font2.render(f'Arturo Jones',1,(0,0,0))
			title_pos = title.get_rect(center = (464,210))
			title_img = test_font3.render(f'L',1,(0,0,0))
			title_img_pos = title.get_rect(center = (680,300))
			screen.blit(title,title_pos)
			screen.blit(title_img,title_img_pos)
			if show_text:
				screen.blit(game_enter,game_enter_position)

			pygame.display.flip()


		else:
			if flag == False:
				screen.fill((245,245,220))
				playerDeath.draw(screen)
				playerDeath.update()
				text_name =  test_font.render(f'Digite seu nome:',1,(0,0,0))
				text_name_pos = text_name.get_rect(center = (464,320))
				text_box.draw(screen)
				screen.blit(text_name, text_name_pos)
				pygame.display.update()
				key = pygame.key.get_pressed()
					
			
			if key[pygame.K_RETURN]:
				waiting_for_restart = True
				while waiting_for_restart:
					screen.fill((245,245,220))
					playerWin.draw(screen)
					playerWin.update()
					text_name =  test_font.render(f'Aperte espaço para voltar à tela de início',1,(0,0,0))
					text_name_pos = text_name.get_rect(center = (464,550))
					render_leaderboard()
					screen.blit(text_name, text_name_pos)
					pygame.display.update()
					for event in pygame.event.get():
						if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
							waiting_for_restart = False
				
				reset_game()


	pygame.display.update()
	clock.tick(60)
