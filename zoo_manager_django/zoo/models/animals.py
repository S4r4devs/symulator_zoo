import time
from .state_calculator import MoodStateCalculator, StatusBarStateCalculator
from zoo.models.moving_strategy import Big_Animal_Moving, Jumping_Animal_Moving, \
    Flying_Animal_Moving, Small_Animal_Moving


class Animal:
    """Base class for all animals."""
    def __init__(self, name, species, age, moving_strategy, carnivore=False):
        self._name = name
        self._species = species
        self._age = age
        self._moving_strategy = moving_strategy
        self._last_fed = 0
        self._last_watered = 0
        self._carnivore = carnivore

    @property
    def name(self):
        return self._name

    def move(self):
        return self._moving_strategy.moving(self)


    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def species(self):
        return self._species

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value >= 0:
            self._age = value

    @property
    def status(self):
        return MoodStateCalculator().calculate(self._last_fed, self._last_watered)

    @property
    def status_bar(self):
        return StatusBarStateCalculator().calculate(self._last_fed, self._last_watered)

    def feed(self):
        self._last_fed = time.time()

    def water(self):
        self._last_watered = time.time()

    def is_carnivore(self):
        """Check if the animal is a carnivore."""
        return self._carnivore

class Lion(Animal):
    def __init__(self, name, age, roar_volume=80):
        super().__init__(name,species="Lion", age=age, moving_strategy=Big_Animal_Moving(), carnivore=True)
        self.roar_volume = roar_volume

class Elephant(Animal):
    def __init__(self, name, age, trunk_length=200):
        super().__init__(name, species="Elephant", age=age, moving_strategy=Big_Animal_Moving())
        self.trunk_length = trunk_length

class Monkey(Animal):
    def __init__(self, name, age):
        super().__init__(name, species="Monkey", age=age, moving_strategy=Jumping_Animal_Moving())

class Giraffe(Animal):
    def __init__(self, name, age):
        super().__init__(name, species="Giraffe", age=age, moving_strategy=Big_Animal_Moving())

class Parrot(Animal):
    def __init__(self, name, age):
        super().__init__(name, species="Parrot", age=age, moving_strategy=Flying_Animal_Moving())

class EuropeanHamster(Animal):
    def __init__(self, name, age):
        super().__init__(name, species="EuropeanHamster", age=age, moving_strategy=Small_Animal_Moving())