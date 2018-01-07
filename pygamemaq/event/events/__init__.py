import logging
logger = logging.getLogger(__name__)
del logging

from .base_event import BaseEvent

from .key_events.button_event import ButtonEvent
from .game_events.render_event import RenderEvent
from .game_events.update_event import UpdateEvent
from .key_events.key_pressed_event import KeyPressedEvent
