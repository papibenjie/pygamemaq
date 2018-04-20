import pygame

from pygamemaq.event import BaseEvent

from pygamemaq.utils import variables

class UpdateEvent(BaseEvent):
    """docstring for RenderEvent."""
    def __init__(self):
        super(UpdateEvent, self).__init__(variables.UPDATE_EVENT_ID)

    def test(self, event):
        if super().test(event):
            return True
        return False
