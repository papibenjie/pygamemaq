from . import logger

class BaseEvent(object):
    """docstring for BaseEvent."""
    def __init__(self, event_types):
        super(BaseEvent, self).__init__()
        if type(event_types) == int:
            event_types = [event_types]
        self.event_types = event_types
        logger.debug("BaseEvent({0}) created".format(event_types))

    def test(self, event):
        if event.type in self.event_types:
            return True
        return False

    def __str__(self):
        return "{0}({1})".format(self.__class__.__name__, self.event_types)
