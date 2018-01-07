import pygame
import sys

from .simple_game import SimpleGame
from ..event import BaseEvent, EventController, RenderController
from ..utils import variables


class CompleteGame(SimpleGame):
    """docstring for Game."""
    def __init__(self, width, height, bg_color=(255,255,255), render_speed=60, update_speed=100, flags=0):
        super(CompleteGame, self).__init__(width, height, flags=flags)
        self.RENDER_EVENT = variables.RENDER_EVENT_ID
        self.UPDATE_EVENT = variables.UPDATE_EVENT_ID

        self.bg_color = bg_color

        self.event_controllers["render"] = RenderController(self.screen, bg_color)
        self.event_controllers["update"] = EventController()


        pygame.time.set_timer(self.RENDER_EVENT, int(1000/render_speed))
        pygame.time.set_timer(self.UPDATE_EVENT, int(1000/update_speed))
