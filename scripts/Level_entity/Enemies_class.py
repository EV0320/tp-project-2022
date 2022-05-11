class Enemy:
    SPRITES = {}  # словарь спрайтой для каждого номера

    def __init__(self, number):
        self._sprite = None  # из словаря
        self._collider = None  # рект от спрайта
        self._coords = (0, 0)
        self._hunt_mode = True

    def _eat(self, object):
        pass  # пока непонятна реализация, будет вызываться из move

    def render(self, screen, coords):
        pass  # нужен интерфейс

    def get_rect(self):
        return self._collider

    def move(self, delta_coords):
        pass  # нужен интерфейс

    def change_mode(self):
        self._hunt_mode = not self._hunt_mode

        if self._hunt_mode:
            self._sprite = None  # замена спрайта
        else:
            self._sprite = None  # замена спрайта

    def die(self):
        pass  # когда его ест Пакман, без интерфеса реализация пока непонятна
