from ..base_event import BaseEvent

class ButtonEvent(BaseEvent):
    """docstring for ButtonEvent."""
    def __init__(self, event_type, key_codes):
        super(ButtonEvent, self).__init__(event_type)
        if type(key_codes) == int:
            key_codes = [key_codes]
        self.key_codes = key_codes

    def test(self, event):
        return super().test(event) and event.key in self.key_codes
