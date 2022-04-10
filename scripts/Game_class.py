import pygame
import time

from scripts.Level_entity.Level_class import Level

WIDTH, HEIGTH = 800, 800


class Game:
    def __init__(self):
        pygame.init()

        self.level_num = 1
        self.screen = pygame.display.set_mode((WIDTH, HEIGTH))
        self.level = Level(self.level_num, self.screen)
        self.opened_UI = None  # Для меню/уровня/...

        self._set_screen()

    def _set_screen(self):
        pygame.display.set_caption("PacMan Game")
        self.screen.fill(pygame.Color("black"))

    def run(self):
        while True:
            self.level.render()
            pygame.display.flip()
            time.sleep(3)
            self.level.process()

