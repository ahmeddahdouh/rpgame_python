class Item:
    """object class"""

    nbr = 0

    def __init__(self, targs, stat):
        self._name = targs["name"]
        self._type = targs["type"]
        self._space = targs["space"]
        self._stat = stat
        Item.nbr += 1

    def __str__(self):
        return str(self._name)
