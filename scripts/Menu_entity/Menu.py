import sys
import os
import pygame

class Menu():
	def __init__(self):
		self._all_sprites_list = pygame.sprite.Group()
		self._quit = Button(200, 400, 'quit1.png', 'quit2.png', self._all_sprites_list, 'quit')
		self._play = Button(200, 250, 'play1.png', 'play2.png', self._all_sprites_list, 'play')
		self._screen = pygame.Surface((800, 800))
		self._window = pygame.display.set_mode((800, 800))
		pygame.display.set_caption('Pacman')
		pygame.mixer.music.load("shivers.wav")
	def show(self):
		pygame.mixer.music.play(-1)
		while True:
			pygame.mouse.set_visible(True)
			self._screen.fill((0, 0, 0))
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					sys.exit()
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_ESCAPE:
						sys.exit()
			self._screen.blit(self._quit._image, (self._quit._rect[0], self._quit._rect[1]))
			self._screen.blit(self._play._image, (self._play._rect[0], self._play._rect[1]))
			self._quit.update(455, 65, self._screen)
			self._play.update(455, 65, self._screen)
			self._window.blit(self._screen, (0, 0))
			pygame.display.flip()


class Button(pygame.sprite.Sprite):
	def __init__(self, x, y, filename1, filename2, all_sprites_list, name):
		pygame.sprite.Sprite.__init__(self)
		self._image = pygame.image.load(filename1)
		self._changeim = pygame.image.load(filename2)
		self._name = name
		self._rect = self._image.get_rect()
		self._rect[0] = x
		self._rect[1] = y
		all_sprites_list.add(self)
	def update(self, w, h, screen):
		click = pygame.mouse.get_pressed()
		mouse = pygame.mouse.get_pos()
		if self._rect[0] + w > mouse[0] > self._rect[0] and self._rect[1] + h > mouse[1] > self._rect[1]:
			screen.blit(self._changeim, (self._rect[0], self._rect[1]))
			if click[0] == 1:
				if self._name == 'quit':
					sys.exit()
				if self._name == 'play':
					pass
