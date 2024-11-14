class Bag:
    """Bag class to save Items"""

    def __init__(self, args):
        self._sizeMax = args["sizeMax"]
        self._lItems = args["items"]
        self._size = len(self._lItems)

    def addItem(self, i):
        if self._size < self._sizeMax:
            self._lItems.append(i)
            self._size += 1
        else:
            return False

    def delItem(self, i):
        self._lItems.pop(i)
        self._size -= 1

    def __str__(self):
        output = ""
        for i in self._lItems:
            output += str(i)
        return output
