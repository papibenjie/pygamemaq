import pygame

from pygamemaq.event.events import ButtonEvent

from . import logger

class KeyPressedEvent(ButtonEvent):
    """docstring for KeyPressedEvent."""
    def __init__(self, key_codes, on_not=False):
        super(KeyPressedEvent, self).__init__([pygame.KEYUP, pygame.KEYDOWN], key_codes)
        self._keys_pressed = []
        self._on_not = on_not

    def test(self, event):
        if super().test(event):
            if event.type == pygame.KEYUP:
                if event.key in self._keys_pressed:
                    logger.info("Key '{0}' released".format(event.key))

                    self._keys_pressed.remove(event.key)
            elif event.type == pygame.KEYDOWN:
                logger.info("Key '{0}' pressed".format(event.key))
                self._keys_pressed.append(event.key)
        event.keyspressed = self._keys_pressed
        return (len(self._keys_pressed) > 0) != self._on_not
