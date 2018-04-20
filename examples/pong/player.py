class Player(object):
    """docstring for Player."""
    def __init__(self, up_key, down_key, x, y, w, h):
        super(Player, self).__init__()
        self._up_key = up_key
        self._down_key = down_key
