import pygame


class Coin(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)

        self._is_eaten = False
        self._sprite = pygame.image.load("resources/images/Coins/Coin.png").convert()  # будет спрайт
        self._price = 50
        rect = self._sprite.get_rect()
        center = rect.center
        rect.w //= 4
        rect.h //= 4
        rect.center = center
        self._collider = rect  # будет рект от спрайта
        self._coords = (0, 0)
        self._screen = screen

    def render(self, coords):
        self._coords = coords
        self._collider.topleft = self._coords
        self.update()

    def get_price(self):
        return self._price

    def get_rect(self):
        return self._collider

    def got_eaten(self):
        self._is_eaten = True

    def get_if_eaten(self):
        return self._is_eaten

    def update(self):
        self._screen.blit(self._sprite, self._collider)


class SpecialCoin(Coin):  # монетки, от которых приведения и пакман свайпаются ролями
    def __init__(self, screen):
        super().__init__(screen)
        self._price = 200
        self._sprite = pygame.image.load("resources/images/Coins/SpecialCoin.png").convert()  # будет спрайт
        self._collider = self._sprite.get_rect()  # рект от спрайта


class Fruit(Coin):
    FRUITS_CHARACTERISTICS = {}  # спрайты, скорости, цены и т.д. для каждого фрукта

    def __init__(self, fruit_level, screen):
        super().__init__(screen)
        self._tag = ""  # будет тег фрукта
        self._price = 50 * fruit_level
        self._sprite = None  # будет спрайт
        self._collider = None  # рект от спрайта
        self._speed = 5 * fruit_level

    def move(self, delta_coords):
        pass  # нужен интерфейс
