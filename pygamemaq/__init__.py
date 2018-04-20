import logging
import os

from colorlog import ColoredFormatter
from colorama import Fore, Back, Style

from .utils import OnlyLevelFileHandler

from .game import logger as gameLogger
from .event import logger as eventLogger
from .event.controllers import logger as controllersLogger
from .event.events import logger as eventsLogger
from .shape import logger as shapeLogger
from .utils import logger as utilsLogger


name = "%(name)-30s"
time = "%(asctime)-8s"
level =  "%(levelname)8s(%(levelno)-2s)"
module = "%(module)-20s"
filename = "%(filename)s"
funcname = "%(funcName)12s"
lineno = "%(lineno)d"
message = "%(message)-73s"


formatter = ColoredFormatter('{0} :: {1} :: {2} -> {3}() :: {4} [{5}:{6}]'.format(time, level, name, funcname, message, filename, lineno), datefmt="%H:%M:%S")
colformatter = ColoredFormatter('{0} :: %(log_color)s{1}%(reset)s :: {2} -> {3}() :: {4} %(log_color)s[{5}:{6}]%(reset)s'.format(time, Style.BRIGHT + level + Style.RESET_ALL, Fore.BLUE + Style.BRIGHT + name + Style.RESET_ALL, funcname, message, Style.BRIGHT + filename, lineno), datefmt="%H:%M:%S")
cleanformatter = logging.Formatter()

mainLogger = logging.getLogger(__name__)
mainLogger.setLevel(logging.DEBUG)

loggers = [mainLogger, gameLogger, eventLogger, controllersLogger, eventsLogger, shapeLogger, utilsLogger]
categories = {"debug": [logging.DEBUG],
              "info": [logging.INFO],
              "other": [logging.WARNING, logging.ERROR, logging.CRITICAL]}

for i, logger in enumerate(loggers):
    path = logger.name.split(".")
    directory = "/".join(logger.name.split(".")[:len(path) - 1])
    path = "/".join(path)

    if not os.path.exists("logs/{0}".format(directory)):
        os.makedirs("logs/{0}".format(directory))

    file_handler = logging.FileHandler("logs/{0}.log".format(path), mode="w")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)


for k in categories:
    if not os.path.exists("logs/filtered/"+k):
        os.makedirs("logs/filtered/"+k)
    file_handler = OnlyLevelFileHandler(categories[k], "logs/filtered/"+k+"/main.log", mode="w")
    file_handler.setFormatter(cleanformatter)
    mainLogger.addHandler(file_handler)
    mainLogger.log(categories[k][0], Fore.CYAN + Back.MAGENTA + Style.BRIGHT + "{0} :: {1} :: {2} -> {3} :: {4} [{5}]".format("time".ljust(8), "level".rjust(12), "name".ljust(30), "function".rjust(14), "message".ljust(73), "error location") + Style.RESET_ALL)
    file_handler.setFormatter(colformatter)



for name in dir():
    if not name.startswith('_'):
        del globals()[name]


import logging
logger = logging.getLogger(__name__)
del logging

import game
import event
import shape
import utils
