from Map_class import Map
from Coins_class import Coin, SpecialCoin, Fruit
from Enemies_class import Enemy
from PacMan_class import PacMan


class Level:
    LEVEL_ITEMS = {}  # Словарь плюшек для каждого уровня

    def __init__(self, number):
        self.number = number
        self._coins = [Coin() for _ in range(240)]
        self._special_coins = [SpecialCoin() for _ in range(4)]
        self._map = Map()
        self._player = PacMan()
        self._enemies = [Enemy(i) for i in range(4)]

    def render(self, screen):
        pass  # нужен интерфейс

    def check_coins(self):
        new_coins = []
        for i in range(len(self._coins)):
            if not self._coins[i].get_if_eaten():
                new_coins.append(self._coins[i])

        del self._coins
        self._coins = new_coins.copy()

    def _change_enemies_mode(self):
        for enemy in self._enemies:
            enemy.change_mode()

    def finish_level(self, winning: bool):
        if winning:
            pass  # вывести UI победы
        elif self._player.get_lives():
            pass  # Начать новый уровень
        else:
            pass  # Вывести UI поражения
        del self
