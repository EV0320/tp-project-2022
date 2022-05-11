class PacMan:
    def __init__(self):
        self._sprite = None
        self._collider = None
        self._coords = None
        self._lives = 3
        self._score = 0

    def _eat(self, object):
        object.got_eaten()
        self._score += object.get_price()

    def move(self, delta_coords):
        pass  # нужен интерфейс

    def get_lives(self):
        return self._lives

    def get_score(self):
        return self._score
