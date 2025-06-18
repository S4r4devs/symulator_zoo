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
        return f"Feeding {self.animal.name} with {self.food.name}"
