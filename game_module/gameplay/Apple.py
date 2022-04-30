"""Apple.py: File that handle the apple display and collision"""

import pygame
import random

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Apple:
    position = (0, 0)
    sprite_size = 25.0

    def __init__(self, screen, screen_size, position_save=None):
        self._sprite = pygame.image.load("game_module/assets/elements/apple.png")
        self._screen_size = screen_size
        self._screen = screen
        if position_save is not None:
            self.position = position_save

    def is_occupied(self, body_part, head, x, y):
        if x == head[0] and y == head[1]:
            return True
        for part in body_part:
            if part.x == x and part.y == y:
                return True
        return False

    def generate(self, body_part, head):
        x = round(random.randrange(0, round(self._screen_size[0] / self.sprite_size - 1))) * self.sprite_size
        y = round(random.randrange(0, round(self._screen_size[1] / self.sprite_size - 1))) * self.sprite_size

        while self.is_occupied(body_part, head, x, y):
            x = round(random.randrange(0, round(self._screen_size[0] / self.sprite_size - 1))) * self.sprite_size
            y = round(random.randrange(0, round(self._screen_size[1] / self.sprite_size - 1))) * self.sprite_size
        self.position = (x, y)

    def display(self):
        self._screen.blit(self._sprite, self.position)
