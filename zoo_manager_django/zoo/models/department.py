class Department:

    def __init__(self,animal, feed, maintenance):
        self._animal = animal
        self._feed = feed
        self._maintenance = maintenance

    @property
    def animal(self):
        return self._animal

    @property
    def feed(self):
        return self._feed

    @property
    def maintenance(self):
        return self._maintenance


