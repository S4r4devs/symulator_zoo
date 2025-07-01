#import necessary modules from same package


class Command:
    """Base class for all commands."""
    def execute(self):
        """Abstract method to execute a command."""
        raise NotImplementedError("Subclasses must implement the execute method.")

class FeedCommand(Command):
    """Command to feed an animal."""
    def __init__(self, request, department, supplies):
        self.request = request
        self.department = department
        self.supplies = supplies

    def execute(self):
        """Feed the animal in the department."""
        return self.department.feed.feed(self.request, self.department.animal, self.supplies)

class WaterCommand(Command):
    """Command to water an animal."""
    def __init__(self, department, supplies):
        self.department = department
        self.supplies = supplies

    def execute(self):
        """Water the animal in the department."""
        return self.department.maintenance.refill_water(self.department.animal, self.supplies)

class MaintainCommand(Command):
    """Command to maintain an animal's enclosure."""
    def __init__(self, department, supplies):
        self.department = department
        self.supplies = supplies

    def execute(self):
        """Maintain the enclosure of the animal in the department."""
        return self.department.maintenance.maintain_enclosure(self.department.animal, self.supplies)
