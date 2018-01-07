from ..wrapped_event import WrappedEvent

from . import logger

class EventController(object):
    """docstring for EventController."""
    def __init__(self, activated=True):
        super(EventController, self).__init__()
        self._wrapped_events = []

        self.activated = activated

        logger.info("{0} created".format(str(self)))


    def add_event(self, event, func, **kwargs):
        self._wrapped_events.append(WrappedEvent(event, func, **kwargs))
        logger.info("{0} with {1}() added to {2}".format(str(event), func.__name__, str(self)))

    def run(self, event):
        if self.activated:
            for wevent in self._wrapped_events:
                wevent.run(event)

    def __str__(self):
        return "{0}".format(self.__class__.__name__)
