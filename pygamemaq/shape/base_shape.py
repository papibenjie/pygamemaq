class BaseShape(object):
    """docstring for BaseShape."""
    def __init__(self, x, y):
        super(BaseShape, self).__init__()
        self.x = x
        self.y = y

    def get_middle(self):
        raise NotImplementedError("{0} Must implement 'get_middle()' function".format(self))

    def draw(self):
        raise NotImplementedError("{0} Must implement 'draw()' function".format(self))

    def __str__(self):
        return "{0}({1})".format(self.__class__.__name__, (self.x, self.y))
