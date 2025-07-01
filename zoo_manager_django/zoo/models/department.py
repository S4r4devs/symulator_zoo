from zoo.models.feeding import CarnivoreFeedingTemplate, HerbivoreFeedingTemplate

class Department:

    def __init__(self, animal, maintenance):
        self._animal = animal
        self._feed = CarnivoreFeedingTemplate() if animal.is_carnivore() else HerbivoreFeedingTemplate()
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


