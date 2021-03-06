import pygame

from .base_shape import BaseShape

class Rect(BaseShape):
    """docstring for Rect."""
    def __init__(self, x, y, w, h):
        super(Rect, self).__init__(x, y)
        self.w = w
        self.h = h

    def get_middle(self):
        return (self.x + self.w/2, self.y + self.h/2)

    def draw(self, screen, color):
        pygame.draw.rect(screen, color, (self.x, self.y, self.w, self.h))
