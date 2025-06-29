#import necessary modules from same package

from zoo.models.feeding import HerbivoreFeedingTemplate, CarnivoreFeedingTemplate

class Command:
    """Base class for all commands."""
    def execute(self):
        """Abstract method to execute a command."""
        raise NotImplementedError("Subclasses must implement the execute method.")

class FeedCommand(Command):
    """Command to feed an animal."""
    def __init__(self, animal, food):
        self.animal = animal
        self.food = food

    def execute(self):
        # Strategy pattern for feeding
        strategy = CarnivoreFeedingTemplate() if self.animal.is_carnivore() else HerbivoreFeedingTemplate()
        preparation = strategy.prepare_food(self.animal)
        feeding = strategy.provide_food(self.animal)

        self.food.quantity = self.food.quantity - 1

        return preparation, feeding