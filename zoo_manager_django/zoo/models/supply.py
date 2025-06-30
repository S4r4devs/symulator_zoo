class Supply:
    def __init__(self, name, quantity):
        self.name = name
        self._quantity = quantity

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value >= 0:
            self._quantity = value
