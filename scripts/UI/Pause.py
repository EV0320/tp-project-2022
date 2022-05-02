import pygame

from scripts.UI.Button import Button


class Pause:
	def __init__(self, screen):
		self._all_sprites_list = pygame.sprite.Group()
		self._pause = pygame.image.load('resources/images/UI/pause.png')
		self._menu = Button(172.5, 500, 'resources/images/UI/quit1.png', 'resources/images/UI/quit2.png', self._all_sprites_list, 'quit')
		self._resume = Button(self._menu.get_rect()[0], self._menu.get_rect()[1] - 150,
								'resources/images/UI/resume1.png', 'resources/images/UI/resume2.png', self._all_sprites_list, 'resume')
		self.startover = False
		self._screen = pygame.Surface((800, 800))
		self._window = screen
		pygame.mixer.music.load("resources/audio/shivers.wav")

	def show(self):
		run = True
		pygame.mixer.music.play(-1)
		while run:
			pygame.mouse.set_visible(True)
			self._screen.fill((0, 0, 0))
			for e in pygame.event.get():
				if e.type == pygame.QUIT:
					exit(0)
				if e.type == pygame.KEYDOWN:
					if e.key == pygame.K_ESCAPE:
						exit(0)

			self._screen.blit(self._pause, (self._resume.get_rect()[0], self._resume.get_rect()[1] - 150))
			self._resume.show(self._screen)
			self._menu.show(self._screen)
			resume_pressed = self._resume.handle_pressed_button(self._screen)
			menu_pressed = self._menu.handle_pressed_button(self._screen)

			if resume_pressed:
				run = False
			elif menu_pressed:
				self.startover = True
				run = False

			self._window.blit(self._screen, (0, 0))
			pygame.display.flip()
