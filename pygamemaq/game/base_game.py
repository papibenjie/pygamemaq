
import pygame
import sys

from . import logger

class BaseGame(object):
    """docstring for BaseGame."""
    def __init__(self, width, height, flags=0):
        super(BaseGame, self).__init__()

        self.event_controllers = {}
        self.quit = False

        pygame.init()
        self.screen = pygame.display.set_mode((width, height), flags)

        logger.info("{0} created".format(str(self)))

    def loop(self):

        logger.info("Main loop starting, event_controllers={0}".format(str(self.event_controllers.keys())))
        while self.quit == False:
            for event in pygame.event.get():
                for controller in self.event_controllers.values():
                    controller.run(event)
        logger.info("Main loop finished")
        pygame.quit()
        sys.exit()

    def __str__(self):
        return "{0}".format(self.__class__.__name__)
