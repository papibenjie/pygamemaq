import pygamemaq

from pygamemaq.game import CompleteGame
from pygamemaq.event.events import RenderEvent, UpdateEvent


class TestGame(CompleteGame):
    """docstring for TestGame."""
    def __init__(self, glo, render_speed=60, update_speed=100):
        super(TestGame, self).__init__(600, 400, render_speed=render_speed, update_speed=update_speed)
        if "draw" in glo:
            self.event_controllers["render"].add_event(RenderEvent(), glo["draw"])
        if "update" in glo:
            self.event_controllers["update"].add_event(UpdateEvent(), glo["update"])
