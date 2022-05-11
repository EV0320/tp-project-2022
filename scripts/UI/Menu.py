import pygame

from scripts.UI.Button import Button


class Menu:
	def __init__(self, screen):
		self._all_sprites_list = pygame.sprite.Group()
		self._menu = pygame.image.load('resources/images/UI/menu.png')
		self._quit = Button(172.5, 500, 'resources/images/UI/quit1.png', 'resources/images/UI/quit2.png', self._all_sprites_list, 'quit')
		self._play = Button(172.5, self._quit.get_rect()[1] - 150, 'resources/images/UI/play1.png', 'resources/images/UI/play2.png', self._all_sprites_list, 'play')
		self._screen = pygame.Surface((800, 800))
		self._window = screen
		pygame.mixer.music.load("resources/audio/shivers.wav")

	def run(self):
		do = True
		pygame.mixer.music.play(-1)
		while do:
			pygame.mouse.set_visible(True)
			self._screen.fill((0, 0, 0))
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					exit(0)
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_ESCAPE:
						exit(0)

			self._screen.blit(self._menu, (self._play.get_rect()[0], self._play.get_rect()[1] - 150))
			self._quit.show(self._screen)
			self._play.show(self._screen)

			quit_pressed = self._quit.handle_pressed_button(self._screen)
			play_pressed = self._play.handle_pressed_button(self._screen)

			if play_pressed:
				do = False
			elif quit_pressed:
				exit(0)

			self._window.blit(self._screen, (0, 0))
			pygame.display.flip()

		self._screen.fill(pygame.Color("black"))
		pygame.display.flip()