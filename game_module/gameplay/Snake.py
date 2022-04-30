"""Snake.py: File that handle the snake display and movement"""

import pygame
from game_module.gameplay.SnakeHead import SnakeHead
from game_module.gameplay.Apple import Apple
from game_module.gameplay.SnakeBody import SnakeBody
from game_module.gameplay.Enumerations import CollideType
from menu.MenuRedirection import MenuRedirection

__author__ = "Magalie Vandenbriele"
__credits__ = ["Magalie Vandenbriele", "Pierre Ghyzel", "Irama Chaouch"]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Magalie Vandenbriele"
__email__ = "magalie.vandenbriele@epitech.eu"


class Snake:
    corners = []
    snake_head = None
    snake_body = None
    apple = None

    def __init__(self, window, window_size, snake_head_save=None, snake_body_save=None, corner_save=None, apple_save=None):
        self._window = window
        self._window_size = window_size
        if snake_head_save is None:
            self.snake_head = SnakeHead(window, window_size)
            self.snake_body = SnakeBody(window, window_size)
            self.apple = Apple(window, window_size)
            self.apple.generate(self.snake_body.body_part, self.snake_head.head_position)
        else:
            self.snake_head = snake_head_save
            self.snake_body = snake_body_save
            self.corners = corner_save
            self.apple = apple_save

    def score(self):
        return len(self.snake_body.body_part) - 1

    def display(self):
        self.snake_head.display()
        self.snake_body.display()

    def event_trigger(self, evnt):
        self.snake_head.event_trigger(evnt)

    def collide(self, apple):
        collide_type = self.snake_head.collide(apple)
        if collide_type == CollideType.APPLE:
            self.apple.generate(self.snake_body.body_part, self.snake_head.head_position)
            self.snake_body.add_body()
        for part in self.snake_body.body_part:
            if part.collide(self.snake_head.head_position):
                return CollideType.BORDER
        return collide_type

    def update(self):
        new_corner = self.snake_head.update()
        if new_corner is not None:
            self.corners.append(new_corner)
        self.corners = self.snake_body.update(self.corners)

    def run_snake_game(self):
        for event in pygame.event.get():
            self.event_trigger(event)
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return MenuRedirection.QUIT
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return MenuRedirection.PAUSE
        self.update()
        state = self.collide(self.apple)
        self._window.fill((0, 0, 0))
        self.apple.display()
        self.display()
        if state is CollideType.BORDER:
            return MenuRedirection.OVER
        return MenuRedirection.PLAY