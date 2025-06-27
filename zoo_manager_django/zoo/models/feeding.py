from abc import ABC, abstractmethod

class FeedingTemplate(ABC):
    def feed(self, animal):
        self.prepare_food(animal)
        return self.provide_food(animal)

    @abstractmethod
    def prepare_food(self, animal):
        pass

    def provide_food(self, animal):
        """Default implementation for providing food."""
        animal.feed()


class HerbivoreFeedingTemplate(FeedingTemplate):
    def prepare_food(self, animal):
        return f"Preparing vegetables for {animal.name}"

    def provide_food(self, animal):
        super().provide_food(animal)
        return f"Feeding {animal.name} with vegetables"

class CarnivoreFeedingTemplate(FeedingTemplate):
    def prepare_food(self, animal):
        return f"Preparing meat for {animal.name}"

    def provide_food(self, animal):
        super().provide_food(animal)
        return f"Feeding {animal.name} with meat"

class Feeder:
    def feed(self, animal):
        raise NotImplementedError("This method should be overridden in subclasses")

class HerbivoreFeeding(Feeder):
    def feed(self, animal):
        return f"Feeding {animal.name} with plants"

class CarnivoreFeeding(Feeder):
    def feed(self, animal):
        return f"Feeding {animal.name} with meat"
