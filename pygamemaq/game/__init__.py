import logging
logger = logging.getLogger(__name__)
del logging

from .base_game import BaseGame
from .simple_game import SimpleGame
from .complete_game import CompleteGame
from .test_game import TestGame
