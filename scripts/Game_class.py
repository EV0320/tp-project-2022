import pygame
import time

from scripts.Level_entity.Level_class import Level
from scripts.UI.Menu import Menu
from scripts.UI.Button import Button

WIDTH, HEIGTH = 800, 800


class Game:
	def __init__(self):
		pygame.init()

		self.level_num = 1
		self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
		self.level = Level(self.level_num, self.screen)
		self._menu = Menu(self.screen)
		self._set_screen()

	def _set_screen(self):
		pygame.display.set_caption("PacMan Game")
		self.screen.fill(pygame.Color("black"))

	def run(self):
		while True:
			self._menu.run()
			self.level.render()
			pygame.display.flip()
			time.sleep(3)
			self.level.process()
			

