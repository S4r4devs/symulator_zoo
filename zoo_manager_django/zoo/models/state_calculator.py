import time
from abc import abstractmethod

class StateCalculatorTemplate:
    """Class to calculate the state of an animal based on its last fed and watered times.
    Uses the Template Method pattern to define the skeleton of the calculation algorithm.
    """

    def calculate(self, last_fed, last_watered):
        now = time.time()
        fed_ok = now - last_fed < 3600
        watered_ok = now - last_watered < 3600
        if fed_ok and watered_ok:
            return self.low()
        elif fed_ok or watered_ok:
            return self.mid()
        else:
            return self.high()

    @abstractmethod
    def low(self):
        pass

    @abstractmethod
    def mid(self):
        pass

    @abstractmethod
    def high(self):
        pass

class MoodStateCalculator(StateCalculatorTemplate):
    """Mood state calculator for animals."""

    def low(self):
        return "happy"

    def mid(self):
        return "neutral"

    def high(self):
        return "sad"

class StatusBarStateCalculator(StateCalculatorTemplate):
    """Status bar state calculator for animals."""

    def low(self):
        return "green"

    def mid(self):
        return "yellow"

    def high(self):
        return "red"
