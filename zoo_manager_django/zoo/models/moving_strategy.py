from abc import ABC, abstractmethod

class Moving_strategy (ABC):

    @abstractmethod
    def moving (self, animal):
        pass

class Small_Animal_Moving(Moving_strategy):
    def moving (self, animal):
        return f"Moving {animal.name} with small steps"

class Big_Animal_Moving(Moving_strategy):
    def moving (self, animal):
        return f"Moving {animal.name} with big steps"

class Jumping_Animal_Moving(Moving_strategy):
    def moving (self, animal):
        return f" {animal.name} jumping "

class Flying_Animal_Moving(Moving_strategy):
    def moving (self, animal):
        return f" {animal.name} is flying"




