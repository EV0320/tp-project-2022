import pygame
from pygame.math import Vector2
import random
from resources.images.AnimatedSprite_class import AnimatedSprite


class Enemy:
    def __init__(self, number, screen, start_pos):
        self._speed = 0.3
        self._DIRECTIONS = {(-self._speed, 0): ((-self._speed, 0), (0, -self._speed), (0, self._speed)),
                            (self._speed, 0): ((self._speed, 0), (0, -self._speed), (0, self._speed)),
                            (0, -self._speed): ((0, -self._speed), (-self._speed, 0), (self._speed, 0)),
                            (0, self._speed): ((0, self._speed), (-self._speed, 0), (self._speed, 0))}
        self._CHECK = {(-self._speed, 0): (-9, 0),
                       (self._speed, 0): (9, 0),
                       (0, -self._speed): (0, -9),
                       (0, self._speed): (0, 9)}

        self._sprite = AnimatedSprite(pygame.image.load(f"resources/images/Enemies/{number + 1}.png"), 2, 4)
        self._screen = screen
        self._collider = self._sprite.get_rect()
        center = self._collider.center
        self._collider.w //= 3
        self._collider.h //= 3
        self._collider.center = center
        self._coords = Vector2(*start_pos)
        self._hunt_mode = True
        self._direction = random.choice(((-self._speed, 0), (-self._speed, 0), (0, -self._speed)))
        self._start_pos = Vector2(*start_pos)

    def render(self):
        self._collider.topleft = self._coords
        self.update()

    def get_rect(self):
        return self._collider

    def move(self, map_object):
        map_coords = map_object.get_coords()
        map_size = map_object.size

        object = map_object.get_object_rect((self._collider.x + self._CHECK[self._direction][0],
                                             self._collider.y + self._CHECK[self._direction][1]))

        while object == 'W':
            self._direction = random.choice(self._DIRECTIONS[self._direction])
            object = map_object.get_object_rect((self._collider.x + self._CHECK[self._direction][0],
                                                 self._collider.y + self._CHECK[self._direction][1]))

        if object != 'W':
            self._coords += self._direction
            self._collider.topleft = self._coords
            if self._collider.bottomright[0] <= map_coords[0]:
                self._collider.topleft = (map_coords[0] + 18 * 27, self._collider.y)
                self._coords = (map_coords[0] + 18 * 27, self._collider.y)
            elif self._collider.bottomleft[0] >= map_coords[0] + map_size[0]:
                self._collider.topleft = (map_coords[0], self._collider.y)
                self._coords = (map_coords[0], self._collider.y)

    def change_mode(self):
        self._hunt_mode = not self._hunt_mode

        if self._hunt_mode:
            self._sprite = None  # замена спрайта
        else:
            self._sprite = None  # замена спрайта

    def reset(self):
        self._coords = self._start_pos.copy()
        self._collider.topleft = self._coords
        self.update()

    def update(self):
        self._screen.blit(self._sprite.image, self._collider)
