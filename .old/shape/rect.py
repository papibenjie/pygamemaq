import pygame

from .base_shape import BaseShape

class Rect(BaseShape):
    """docstring for Rect."""
    def __init__(self, x, y, w, h):
        super(Rect, self).__init__(x, y)
        self.w = w
        self.h = h

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.w, self.h))
