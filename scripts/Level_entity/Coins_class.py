
class Coin:
    def __init__(self):
        self._is_eaten = False
        self._sprite = None  # будет спрайт
        self._price = 50
        self._collider = None  # будет рект от спрайта
        self._coords = (0, 0)

    def render(self, screen, coords):
        pass  # нужен интерфейс

    def get_price(self):
        return self._price

    def get_rect(self):
        return self._collider

    def got_eaten(self):
        self._is_eaten = True

    def get_if_eaten(self):
        return self._is_eaten


class SpecialCoin(Coin):  # монетки, от которых приведения и пакман свайпаются ролями
    def __init__(self):
        super().__init__()
        self._price = 200
        self._sprite = None  # будет спрайт
        self._collider = None  # рект от спрайта


class Fruit(Coin):
    FRUITS_CHARACTERISTICS = {}  # спрайты, скорости, цены и т.д. для каждого фрукта

    def __init__(self, fruit_level):
        super().__init__()
        self._tag = ""  # будет тег фрукта
        self._price = 50 * fruit_level
        self._sprite = None  # будет спрайт
        self._collider = None  # рект от спрайта
        self._speed = 5 * fruit_level

    def move(self, delta_coords):
        pass  # нужен интерфейс
