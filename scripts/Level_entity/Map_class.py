import pygame
WIDTH, HEIGHT = 800, 800


class Map(pygame.sprite.Sprite):
    MAP_OBJECTS = {}  # Словарь кодов спрайтов объектов

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        with open("resources/images/Map/map.txt", 'r') as fin:
            self._pattern = list(map(lambda x: x.split(), fin.readlines()))

        image = pygame.image.load("resources/images/Map/map.png")
        mult_y = HEIGHT * 0.7 / image.get_size()[1]
        x = int(28 * round((image.get_size()[0] * mult_y) / 28.))
        y = int(31 * round((image.get_size()[1] * mult_y) / 31.))

        self._sprite = pygame.transform.scale(image, (x, y)).convert()

        self._coords = (WIDTH // 2 - self._sprite.get_size()[0] // 2,
                        HEIGHT // 2 - self._sprite.get_size()[1] // 2)

        self.size = (x, y)

    def render(self, screen):
        screen.blit(self._sprite, self._coords)

    def get_object_rect(self, coords):
        return self._pattern[(coords[1] - self._coords[1] - 5) // 18 + 1][(coords[0] - self._coords[0] - 2) // 18 + 1]

    def get_text_map(self):
        return self._pattern

    def get_coords(self):
        return self._coords
