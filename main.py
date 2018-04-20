import logging

from examples.circlega import CircleGAGame

from pygamemaq import logger

game = CircleGAGame(600, 400, 50)

game.loop()
