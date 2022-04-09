import sys
import os
import pygame

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
				if self._name == 'resume':
					pass
				if self._name == 'menu':
					pass
				if self._name == 'play':
					pass
				if self._name == 'quit':
					sys.exit()
				
