class Animal:
    """Base class for all animals."""
    def __init__(self, name, species):
        self._name = name
        self._species = species

    @property
    def name(self):
        """Getter for the name attribute."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for the name attribute."""
        if isinstance(value, str) and len(value) > 0:
            self._name = value

    @property
    def species(self):
        return self._species

    def speak(self):
        return f"{self.name} makes a sound"

class Lion(Animal):
    """Lion class inheriting from Animal."""
    def __init__(self, name, roar_volume):
        super().__init__(name, species="Lion")  # Use of parent class implementation: super()
        self.roar_volume = roar_volume  # Attribute overriding in child class

    def speak(self):
        """Override the speak method to provide Lion-specific behavior."""
        return f"{self.name} roars at {self.roar_volume} dB"

class Elephant(Animal):
    """Elephant class inheriting from Animal."""
    def __init__(self, name, trunk_length):
        super().__init__(name, species="Elephant")  # Use of parent class implementation: super()
        self.trunk_length = trunk_length

    def speak(self):
        return f"{self.name} trumpets with trunk length {self.trunk_length} cm"
