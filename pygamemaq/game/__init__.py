import logging
logger = logging.getLogger(__name__)
del logging

from .test_game import TestGame
from .game import Game
from .simple_game import SimpleGame
from .base_game import BaseGame
