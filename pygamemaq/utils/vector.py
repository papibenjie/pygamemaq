import math
import pygame

from . import logger

class Vector2D(object):
    """docstring for Vector2D."""
    def __init__(self, x, y):
        super(Vector2D, self).__init__()
        self.x = x
        self.y = y

        logger.info("{0} created".format(str(self)))


    def draw(self, screen, pos, color=(255,0,0)):
        logger.info("{0} drew at {1}".format(str(self), pos))
        pos_final = (pos[0] + self.x, pos[1] + self.y)
        pygame.draw.line(screen, color, pos, pos_final)
        pygame.draw.rect(screen, color, (*pos_final, 5, 5))



    def normalize(self):
        norm = self.get_normalized()
        self.x = norm.x
        self.y = norm.y
        logger.info("{0} drew".format(str(self)))

    def get_normalized(self):
        v = Vector2D(self.x/self.length(), self.y/self.length())
        logger.info("{0} normalized returned".format(str(v)))
        return v

    def length(self):
        l = math.sqrt(self.x ** 2 + self.y ** 2)
        logger.info("lenght {0} of {1} drew".format(l, str(self)))
        return l

    def copy(self):
        logger.info("{1} copie returned".format(l, str(self)))
        return Vector2D(self.x, self.y)

    def __add__(self, value):
        logger.info("{0} + {1} vector returned".format(str(self), value))
        if type(value) == Vector2D:
            return Vector2D(self.x + value.x, self.y + value.y)
        if type(value) in [float, int]:
            return Vector2D(self.x + value, self.y + value)

    def __sub__(self, value):
        logger.info("{0} - {1} vector returned".format(str(self), value))
        if type(value) == Vector2D:
            return Vector2D(self.x - value.x, self.y - value.y)
        if type(value) in [float, int]:
            return Vector2D(self.x - value, self.y - value)

    def __mul__(self, value):
        logger.info("{0} * {1} vector returned".format(str(self), value))
        if type(value) == Vector2D:
            return Vector2D(self.x * value.x, self.y * value.y)
        if type(value) in [float, int]:
            return Vector2D(self.x * value, self.y * value)

    def __str__(self):
        return "Vector2D({0}, {1})".format(self.x, self.y)
