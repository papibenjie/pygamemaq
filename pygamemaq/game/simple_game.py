import pygame

from .base_game import BaseGame
from ..event import BaseEvent, EventController


class SimpleGame(BaseGame):
    """docstring for SimpleGame."""
    def __init__(self, width, height, flags=0):
        super(SimpleGame, self).__init__(width, height, flags=flags)

        self.event_controllers["main"] = EventController()
        self.event_controllers["main"].add_event(BaseEvent(pygame.QUIT), self.exit)


    def exit(self, event):
        self.quit = True
