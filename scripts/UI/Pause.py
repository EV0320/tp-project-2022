import sys
import os
import pygame

class Pause():
	def __init__(self):
		self._all_sprites_list = pygame.sprite.Group()
		self._pause = pygame.image.load('pause.png')
		self._menu = Button(172.5, 500, 'menu1.png', 'menu2.png', self._all_sprites_list, 'menu')
		self._resume = Button(self._menu._rect[0], self._menu._rect[0] - 150, 'resume1.png', 'resume2.png', self._all_sprites_list, 'resume')
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
			self._screen.blit(self._pause, (self._resume._rect[0], self._resume._rect[1] - 150))
			self._screen.blit(self._resume._image, (self._resume._rect[0], self._resume._rect[1]))
			self._screen.blit(self._menu._image, (self._menu._rect[0], self._menu._rect[1]))
			self._resume.update(455, 65, self._screen)
			self._menu.update(455, 65, self._screen)
			self._window.blit(self._screen, (0, 0))
			pygame.display.flip()
