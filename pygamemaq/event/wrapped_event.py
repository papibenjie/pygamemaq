from . import logger

class WrappedEvent(object):
    """docstring for WrappedEvent."""
    def __init__(self, event, func, **kwargs):
        super(WrappedEvent, self).__init__()
        self._func = func
        self._event = event
        self._kwargs = kwargs
        logger.debug("{0} created".format(str(self)))

    def run(self, event):
        if self._event.test(event):
            event.kwargs = self._kwargs
            self._func(event)

    def __str__(self):
        return "{0}: ({1} --> {2}())".format(self.__class__.__name__, str(self._event), self._func.__name__)
