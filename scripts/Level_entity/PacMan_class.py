import pygame
from pygame.math import Vector2
from resources.images.AnimatedSprite_class import AnimatedSprite


class PacMan(pygame.sprite.Sprite):
    def __init__(self, screen, start_pos):
        self._screen = screen
        pygame.sprite.Sprite.__init__(self)
        self._speed = 0.45
        self._coords = Vector2(*start_pos)

        self._DELTA = {pygame.K_a: (Vector2(-self._speed, 0), (-9, 0)),
                       pygame.K_s: (Vector2(0, self._speed), (0, 9)),
                       pygame.K_d: (Vector2(self._speed, 0), (9, 0)),
                       pygame.K_w: (Vector2(0, -self._speed), (0, -9)),
                       pygame.K_LEFT: (Vector2(-self._speed, 0), (-9, 0)),
                       pygame.K_DOWN: (Vector2(0, self._speed), (0, 9)),
                       pygame.K_RIGHT: (Vector2(self._speed, 0), (9, 0)),
                       pygame.K_UP: (Vector2(0, -self._speed), (0, -9))}

        self._sprite = AnimatedSprite(pygame.image.load("resources/images/Pacman/PacMan.png"))
        self._collider = self._sprite.get_rect()
        center = self._collider.center
        self._collider.w //= 3
        self._collider.h //= 3
        self._collider.center = center
        self._lives = 3
        self._score = 0
        self._direction = [(0, 0), (0, 0)]
        self._start_pos = Vector2(*start_pos).copy()

    def eat(self, objects):
        rects = list(map(lambda x: x.get_rect(), objects))
        indexes = self._collider.collidelistall(rects)
        for ind in indexes:
            objects[ind].got_eaten()
            self._score += objects[ind].get_price()

    def move(self, map_object):
        map_coords = map_object.get_coords()
        map_size = map_object.size
        object = map_object.get_object_rect((self._collider.x + self._direction[1][0], self._collider.y + self._direction[1][1]))

        if object not in "WGH":
            self._coords += self._direction[0]

            self._collider.topleft = self._coords
            if self._collider.bottomright[0] <= map_coords[0]:
                self._collider.topleft = (map_coords[0] + 18 * 27, self._collider.y)
                self._coords = (map_coords[0] + 18 * 27, self._collider.y)
            elif self._collider.bottomleft[0] >= map_coords[0] + map_size[0]:
                self._collider.topleft = (map_coords[0], self._collider.y)
                self._coords = (map_coords[0], self._collider.y)

    def change_direction(self, direction):
        self._direction = self._DELTA[direction]

    def get_lives(self):
        return self._lives

    def damaged(self):
        self._lives -= 1

    def get_score(self):
        return self._score

    def get_rect(self):
        return self._collider

    def render(self):
        self._collider.topleft = self._coords
        self.update()

    def update(self):
        self._screen.blit(self._sprite.image, self._collider)

    def reset(self):
        print(self._start_pos)
        self._coords = self._start_pos.copy()
        self._collider.topleft = self._coords
        self.update()
