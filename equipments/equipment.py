from equipments.item import Item


class Equipment(Item):
    def __init__(self, targs, stat):
        Item.__init__(self, targs, stat)
        self._lClasses = targs["classList"]
        self._place = targs["place"]
