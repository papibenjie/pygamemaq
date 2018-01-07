import pygame

from .event_controller import EventController
from ...utils import variables

from . import logger

class RenderController(EventController):
    """docstring for EventController."""
    def __init__(self, screen, bg_color=(255,255,255)):
        super(RenderController, self).__init__()
        self._screen = screen
        self._bg_color = bg_color



    def run(self, event):
        if event.type == variables.RENDER_EVENT_ID:
            self._screen.fill(self._bg_color)
            super().run(event)
            pygame.display.flip()
