from pygamemaq.event import BaseEvent

from pygamemaq.utils import variables

class RenderEvent(BaseEvent):
    """docstring for RenderEvent."""
    def __init__(self):
        super(RenderEvent, self).__init__(variables.RENDER_EVENT_ID)

    def test(self, event):
        if super().test(event):
            return True
        return False
