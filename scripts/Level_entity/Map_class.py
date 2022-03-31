class Map:
    MAP_OBJECTS = {}  # Словарь кодов спрайтов объектов

    def __init__(self):
        self._pattern = None  # будет закодированный паттерн карты
        self._objects = []

    def render(self, screen):
        pass  # нужен интерфейс

    def get_object_rect(self, coords):
        x, y = coords
        for obj in self._objects:
            pass  # проверка координат каждого объекта, нужен интерфейс
