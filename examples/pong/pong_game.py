import pygame

from pygamemaq.game import CompleteGame
from pygamemaq.event.events import RenderEvent, UpdateEvent

from .player import Player

class PongGame(CompleteGame):
    """docstring for PongGame."""
    def __init__(self, width, height):
        super(PongGame, self).__init__(width, height)

        self.event_controllers["render"].add_event(RenderEvent(), self.draw)
        self.event_controllers["update"].add_event(UpdateEvent(), self.update)

        #self._player1 = Player(pygame.K_w, pygame.K_s)
        #self._player2 = Player(pygame.K_w, pygame.K_s)


    def draw(self, event):
        pass

    def update(self, event):
        pass
