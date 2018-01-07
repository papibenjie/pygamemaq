from .game import *
from .event import *
from .shape import *
from .utils import *

from .game import logger as gameLogger
from .event import logger as eventLogger
from .event.controllers import logger as controllersLogger
from .event.events import logger as eventsLogger
from .shape import logger as shapeLogger
from .utils import logger as utilsLogger

import logging
import os
mainLogger = logging.getLogger(__name__)
loggers = [mainLogger, gameLogger, eventLogger, controllersLogger, eventsLogger, shapeLogger, utilsLogger]

time = "%(asctime)s.%(msecs)03d"
level = "%(levelname)s"
module = "%(module)s"
func = "%(funcName)s()"
message = "%(message)s"
formatter = logging.Formatter('{0} :: {1} :: {2} -> {3} :: {4}'.format(time, level, module, func, message), datefmt="%H:%M:%S")


for logger in loggers:
    path = logger.name.split(".")
    directory = "/".join(logger.name.split(".")[:len(path) - 1])
    path = "/".join(path)

    if not os.path.exists("logs/{0}".format(directory)):
        os.makedirs("logs/{0}".format(directory))

    file_handler = logging.FileHandler("logs/{0}.log".format(path), mode="w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

out_handler = logging.StreamHandler()
out_handler.setFormatter(formatter)
mainLogger.addHandler(out_handler)

eventLogger.setLevel(logging.INFO)

del logging
del os
