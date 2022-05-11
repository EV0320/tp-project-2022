import pygame
import time

from scripts.Level_entity.Coins_class import Coin, SpecialCoin, Fruit
from scripts.Level_entity.Map_class import Map, WIDTH, HEIGHT
from scripts.Level_entity.Enemies_class import Enemy
from scripts.Level_entity.PacMan_class import PacMan
from scripts.UI.Button import Button
from scripts.UI.Pause import Pause


class Level:
	def __init__(self, number, screen):
		self._all_sprites_list = pygame.sprite.Group()
		self.number = number
		self._screen = screen
		self._coins = []
		self._special_coins = []
		self._map = Map()
		self._player = None
		self._enemies = []
		self._pause_UI = None
		self._hearts_image = pygame.image.load("resources/images/Pacman/heart.png").convert()
		self._score_label = pygame.font.Font("resources/fonts/color basic.ttf", 30).render("0", True, pygame.Color("white"))
		self._pause = Button(338, 700, "resources/images/UI/menub1.png", "resources/images/UI/menub2.png",
							 self._all_sprites_list, "pause")

	def render(self):
		self._map.render(self._screen)

		x, y = self._map.get_coords()
		x -= 6
		y -= 5
		elem_x, elem_y = self._map.size[0] / 28, self._map.size[1] / 31
		coin_count = 0
		sp_coin = 0
		enemy_count = 0
		text_map = self._map.get_text_map()
		for i in range(len(text_map)):
			row = text_map[i]
			for j in range(len(row) - 2):
				if row[j] == 'C':
					self._coins.append(Coin(self._screen))
					self._coins[coin_count].render((x + j * elem_x, y + i * elem_y))
					coin_count += 1
				elif row[j] == 'S':
					self._special_coins.append(SpecialCoin(self._screen))
					self._special_coins[sp_coin].render((x + j * elem_x, y + i * elem_y))
					sp_coin += 1
				elif row[j] == 'B':
					self._player = PacMan(self._screen, (x + j * elem_x + 8, y + i * elem_y))
					self._player.render()
				elif row[j] == 'V':
					self._enemies.append(Enemy(enemy_count, self._screen, (x + j * elem_x + 8, y + i * elem_y)))
					self._enemies[enemy_count].render()
					enemy_count += 1
		x, y = self._map.get_coords()[0] + 50, self._map.get_coords()[1] - 50
		self._screen.blit(self._score_label, (x, y))

		pygame.draw.rect(self._screen, pygame.Color("black"),
							pygame.Rect((self._map.get_coords()[0] + self._map.size[0],
										 self._map.get_coords()[1] + self._map.size[1]),
										(50, self._map.size[1])))
		pygame.draw.rect(self._screen, pygame.Color("black"),
						pygame.Rect((self._map.get_coords()[0] - 50, self._map.get_coords()[1]),
									 (50, self._map.size[1])))

		self._render_hearts()

	def _render_hearts(self):
		heart_size = self._hearts_image.get_size()
		heart_start_coords = self._map.get_coords()[0] + self._map.size[0], self._map.get_coords()[1] - heart_size[1] - 10

		for i in range(1, self._player.get_lives() + 1):
			self._screen.blit(self._hearts_image, (heart_start_coords[0] - heart_size[0] * i, heart_start_coords[1]))

	def _check_coins(self):
		new_coins = []
		for coin in self._coins:
			if not coin.get_if_eaten():
				new_coins.append(coin)

		del self._coins
		self._coins = new_coins.copy()

		new_special_coins = []
		for coin in self._special_coins:
			if not coin.get_if_eaten():
				new_special_coins.append(coin)
			else:
				self._change_enemies_mode()
				pygame.time.set_timer(pygame.USEREVENT, 7000)

		del self._special_coins
		self._special_coins = new_special_coins.copy()

		if not len(self._coins) and not len(self._special_coins):
			self.finish_level(True)

	def _change_enemies_mode(self):
		for enemy in self._enemies:
			enemy.change_mode()

	def finish_level(self, winning: bool):
		if winning:
			rect = pygame.image.load("resources/images/UI/win.png").get_rect()
			rect.center = (400, 400)
			self._screen.blit(pygame.image.load("resources/images/UI/win.png"), rect)
			pygame.display.flip()
			time.sleep(3)
			exit(0)
		elif self._player.get_lives() > 1:
			self._player.damaged()
			self._player.reset()
			for enemy in self._enemies:
				enemy.reset()
			return True
		else:
			rect = pygame.image.load("resources/images/UI/gameover.png").get_rect()
			rect.center = (400, 400)
			self._screen.blit(pygame.image.load("resources/images/UI/gameover.png"), rect)
			pygame.display.flip()
			time.sleep(3)
			exit(0)

	def process(self):
		run = True

		while run:
			
			self._player.eat(self._coins + self._special_coins)
			self._check_coins()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit(0)
				elif event.type == pygame.KEYDOWN:
					self._player.change_direction(event.key, self._map)
				elif event.type == pygame.USEREVENT:
					for enemy in self._enemies:
						enemy.change_mode()
					pygame.time.set_timer(pygame.USEREVENT, 0)
			self._player.move(self._map)
			self._screen.fill(pygame.Color("black"))
			self._map.render(self._screen)
			for coin in self._coins + self._special_coins:
				coin.update()

			self._player.update()
			for enemy in self._enemies:
				if enemy.eat(self._player) == 1:
					run = self.finish_level(False)
				elif enemy.eat(self._player) == 2:
					enemy.reset()
					self._player.eat_ghost(enemy)
				enemy.move(self._map)
				enemy.update()

			pygame.draw.rect(self._screen, pygame.Color("black"),
							 pygame.Rect((self._map.get_coords()[0] - 50, self._map.get_coords()[1]),
										 (50, self._map.size[1])))
			pygame.draw.rect(self._screen, pygame.Color("black"),
							 pygame.Rect((self._map.get_coords()[0] + self._map.size[0], self._map.get_coords()[1]),
										 (50, self._map.size[1])))

			x, y = self._map.get_coords()[0] + 20, self._map.get_coords()[1] - 50
			self._score_label = pygame.font.Font("resources/fonts/color basic.ttf", 20).\
				render(str(self._player.get_score()), True, pygame.Color("white"))
			self._screen.blit(self._score_label, (x, y))
			self._pause.show(self._screen)
			pause_pressed = self._pause.handle_pressed_button(self._screen)
			if pause_pressed:
				pause = Pause(self._screen)
				pause.show()
				if pause.startover:
					run = False

			self._render_hearts()
			pygame.display.flip()

		self._screen.fill(pygame.Color("black"))
