import sys
import os
import pygame
pygame.init()

window = pygame.display.set_mode((800, 800))
pygame.display.set_caption('Pacman')
info_string = pygame.Surface((600, 30))
screen = pygame.Surface((800, 800))
pygame.font.init()
all_sprites_list = pygame.sprite.Group()
pygame.mixer.music.load("shivers.wav")
def menu(QUIT, PLAY):
	done = True
	pygame.mixer.music.play(-1)
	
	while done:
		pygame.mouse.set_visible(True)
		screen.fill((0, 0, 0))
		for e in pygame.event.get():
			if e.type == pygame.QUIT:
				sys.exit()
			if e.type == pygame.KEYDOWN:
				if e.key == pygame.K_ESCAPE:
					sys.exit()
		screen.blit(QUIT.image, (QUIT.rect[0], QUIT.rect[1]))
		screen.blit(PLAY.image, (PLAY.rect[0], PLAY.rect[1]))
		QUIT.update(455, 65)
		PLAY.update(455, 65)
		window.blit(screen, (0, 0))
		pygame.display.flip()
		

class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, filename1, filename2):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(filename1)
		self.changeim = pygame.image.load(filename2)
		self.rect = self.image.get_rect()
		self.rect[0] = x
		self.rect[1] = y
		all_sprites_list.add(self)
	def update(self, w, h):
		click = pygame.mouse.get_pressed()
		mouse = pygame.mouse.get_pos()
		if self.rect[0] + w > mouse[0] > self.rect[0] and self.rect[1] + h > mouse[1] > self.rect[1]:
			screen.blit(self.changeim, (self.rect[0], self.rect[1]))
			if click[0] == 1:
				if self == QUIT:
					sys.exit()
				if self == PLAY:
					print("PLAY")

QUIT = Button(200, 400, 'quit1.png', 'quit2.png')
PLAY = Button(200, 250, 'play1.png', 'play2.png')

menu(QUIT, PLAY)
