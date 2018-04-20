import logging

class OnlyLevelFileHandler(logging.FileHandler):
    def __init__(self, levels, filename, mode='a', encoding=None, delay=False):
        logging.FileHandler.__init__(self, filename, mode, encoding, delay)
        self._levels = levels


    def emit(self, record):
        if record.levelno not in self._levels:
            return

        logging.FileHandler.emit(self, record)
