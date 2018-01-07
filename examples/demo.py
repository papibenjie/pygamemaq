import sys
sys.path.insert(0, '..')

import pygame
import logging

from pygamemaq.game import CompleteGame
from pygamemaq.event import RenderEvent, UpdateEvent
from pygamemaq.shape import Rect
from pygamemaq.utils import Vector2D
from pygamemaq import mainLogger, utilsLogger


mainLogger.setLevel(logging.DEBUG)
utilsLogger.setLevel(logging.INFO)

game = CompleteGame(600, 400)
screen_width, screen_height = game.screen.get_size()
rect = Rect(10, 10, 100, 100)
direction = Vector2D(1, 2)

def draw(event):
    rect.draw(game.screen, (100, 100, 255))
    (direction * 15).draw(game.screen, rect.get_middle())

def update(event):
    rect.x += direction.x
    rect.y += direction.y

    if(rect.x < 0 or rect.x > screen_width or
        rect.y < 0 or rect.y > screen_height):

        direction.reverse()


game.event_controllers["render"].add_event(RenderEvent(), draw)
game.event_controllers["update"].add_event(UpdateEvent(), update)


game.loop()
