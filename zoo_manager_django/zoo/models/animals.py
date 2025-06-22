import time

class Animal:
    """Base class for all animals."""
    def __init__(self, name, species, age):
        self._name = name
        self._species = species
        self._age = age
        self._last_fed = 0
        self._last_watered = 0

    @property
    def name(self):
        return self._name

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
        now = time.time()
        fed_ok = now - self._last_fed < 3600
        watered_ok = now - self._last_watered < 3600
        if fed_ok and watered_ok:
            return "happy"
        elif fed_ok or watered_ok:
            return "neutral"
        else:
            return "sad"

    @property
    def status_bar(self):
        now = time.time()
        fed_ok = now - self._last_fed < 3600
        watered_ok = now - self._last_watered < 3600
        if fed_ok and watered_ok:
            return "green"
        elif fed_ok or watered_ok:
            return "yellow"
        else:
            return "red"

    def feed(self):
        self._last_fed = time.time()

    def water(self):
        self._last_watered = time.time()

class Lion(Animal):
    """Lion class inheriting from Animal."""
    def __init__(self, name, age, roar_volume=80):
        super().__init__(name, species="Lion", age=age)
        self.roar_volume = roar_volume

class Elephant(Animal):
    """Elephant class inheriting from Animal."""
    def __init__(self, name, age, trunk_length=200):
        super().__init__(name, species="Elephant", age=age)
        self.trunk_length = trunk_length

class Monkey(Animal):
    """Elephant class inheriting from Animal."""
    def __init__(self, name, age):
        super().__init__(name, species="Monkey", age=age)

class Giraffe(Animal):
    """Elephant class inheriting from Animal."""
    def __init__(self, name, age):
        super().__init__(name, species="Giraffe", age=age)

class Parrot(Animal):
    """Elephant class inheriting from Animal."""
    def __init__(self, name, age):
        super().__init__(name, species="Parrot", age=age)