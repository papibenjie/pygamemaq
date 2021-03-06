import math
import pygame

from . import logger

class Vector2D(object):
    """docstring for Vector2D."""
    def __init__(self, x, y):
        super(Vector2D, self).__init__()
        self.x = x
        self.y = y
        logger.debug("{0} initialized".format(str(self)))


    def draw(self, screen, pos, color=(255,0,0)):
        pos_final = (pos[0] + self.x, pos[1] + self.y)
        pygame.draw.line(screen, color, pos, pos_final)
        pygame.draw.rect(screen, color, (pos_final[0] - 3, pos_final[1] - 3, 6, 6))


    def normalize(self):
        norm = self.get_normalized()
        self.x = norm.x
        self.y = norm.y

    def get_normalized(self):
        v = Vector2D(self.x/self.length(), self.y/self.length())
        logger.debug("'{0}' normalized vector of {1} returned".format(str(v), str(self)))
        return v

    def reverse(self):
        rev = self.get_reversed()
        self.x = rev.x
        self.y = rev.y

    def get_reversed(self):
        v = Vector2D(self.x * -1, self.y * -1)
        logger.debug("'{0}' reversed vector of {1} returned".format(str(v), str(self)))
        return v

    def length(self):
        l = math.sqrt(self.x ** 2 + self.y ** 2)
        return l

    def copy(self):
        return Vector2D(self.x, self.y)

    def __add__(self, value):
        if type(value) == Vector2D:
            return Vector2D(self.x + value.x, self.y + value.y)
        if type(value) in [float, int]:
            return Vector2D(self.x + value, self.y + value)

    def __sub__(self, value):
        if type(value) == Vector2D:
            return Vector2D(self.x - value.x, self.y - value.y)
        if type(value) in [float, int]:
            return Vector2D(self.x - value, self.y - value)

    def __mul__(self, value):
        if type(value) == Vector2D:
            return Vector2D(self.x * value.x, self.y * value.y)
        if type(value) in [float, int]:
            return Vector2D(self.x * value, self.y * value)

    def __str__(self):
        return "Vector2D({0}, {1})".format(self.x, self.y)
