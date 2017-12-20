import pygame
import logging

from pygamemaq.game import TestGame
from pygamemaq.shape import Rect
from pygamemaq.utils import Vector2D
from pygamemaq.event import ButtonEvent, KeyPressedEvent


r = Rect(10,10, 100 ,100)
r2 = Rect(200,100, 100 ,100)
v = Vector2D(3,4)


game = None

def draw(event):
    r.draw(game.screen, (100,0,0))
    r2.draw(game.screen, (100,0,100))
    v.draw(game.screen, (100,100))

def update(event):
    r.x += v.x
    r.y += v.y

def move(event):
    v.x = 0
    v.y = 0
    if pygame.K_a in event.keyspressed:
        v.x = -1
    if pygame.K_s in event.keyspressed:
        v.y = 1
    if pygame.K_d in event.keyspressed:
        v.x = 1
    if pygame.K_w in event.keyspressed:
        v.y = -1

def change(event):
    if game.event_controllers["render"].activated:
        game.event_controllers["render"].activated = False
        game.event_controllers["update"].activated = False

    else:
        game.event_controllers["render"].activated = True
        game.event_controllers["update"].activated = True


game = TestGame(globals())

game.event_controllers["main"].add_event(KeyPressedEvent([pygame.K_a,pygame.K_s,pygame.K_d,pygame.K_w]), move)
game.event_controllers["main"].add_event(ButtonEvent(pygame.KEYDOWN, pygame.K_SPACE), change)


game.loop()
