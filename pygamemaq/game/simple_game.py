import pygame

from pygamemaq.game import BaseGame
from pygamemaq.event import BaseEvent
from pygamemaq.event.controllers import EventController

class SimpleGame(BaseGame):
    """docstring for SimpleGame."""
    def __init__(self, width, height, flags=0):
        super(SimpleGame, self).__init__(width, height, flags=flags)

        self.event_controllers["main"] = EventController()
        self.event_controllers["main"].add_event(BaseEvent(pygame.QUIT), self.exit)


    def exit(self, event):
        self.quit = True
