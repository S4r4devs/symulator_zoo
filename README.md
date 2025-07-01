# Zoo Manager

1. Use of classes

    All model files:
    zoo/models/animals.py (Animal, Lion, Elephant, Monkey, Giraffe, Parrot)
    zoo/models/zookeepers.py (Zookeeper)
    zoo/models/food.py (Food)
    zoo/models/commands.py (Command, FeedCommand)
    zoo/models/feeding.py (FeedingTemplate, HerbivoreFeedingTemplate, CarnivoreFeedingTemplate, Feeder, HerbivoreFeeding, CarnivoreFeeding)
    zoo/models/exceptions.py (AnimalNotFoundException)

2. Use of inheritance

    zoo/models/animals.py:
    Lion, Elephant, Monkey, Giraffe, Parrot inherit from Animal
    zoo/models/commands.py:
    FeedCommand inherits from Command
    zoo/models/feeding.py:
    HerbivoreFeedingTemplate, CarnivoreFeedingTemplate inherit from FeedingTemplate
    HerbivoreFeeding, CarnivoreFeeding inherit from Feeder
    zoo/models/exceptions.py:
    AnimalNotFoundException inherits from Exception
    zoo/models/food.py:
    Water inherits from Food
    zoo/models/state_calculator.py:
    MoodStateCalculator, StatusBarStateCalculator inherit from StateCalculatorTemplate

3. Use of attributes in classes; demonstration of overriding attributes in child classes

    zoo/models/animals.py:
    Animal defines _name, _species, _age, _last_fed, _last_watered
    Lion adds roar_volume
    Elephant adds trunk_length

4. Use of methods in classes; demonstration of overriding methods in child classes

    zoo/models/animals.py:
    Child classes override the constructor (__init__)
    zoo/models/feeding.py:
    HerbivoreFeedingTemplate and CarnivoreFeedingTemplate override prepare_food and provide_food from FeedingTemplate
    HerbivoreFeeding and CarnivoreFeeding override feed from Feeder
    zoo/models/commands.py:
    FeedCommand overrides execute from Command

5. Use of the @classmethod and @staticmethod decorators

    zoo/models/zookeepers.py:
    from_dict, from_string (@classmethod)
    validate_name, authenticate (@staticmethod)

6. Class containing more than one constructor

    zoo/models/zookeepers.py:
    __init__, from_dict, from_string

7. Use of encapsulation (setters and getters)

    zoo/models/animals.py:
    name, age properties with setters/getters
    is_carnivore
    zoo/models/supply.py:
    quantity property with setter/getter

8. Polymorphism

    zoo/models/animals.py:
    All animal subclasses can be used as Animal
    zoo/models/feeding.py:
    All feeders/templates can be used as their parent type
    zoo/models/commands.py:
    FeedCommand command can be used as Command

9. Use of parent class implementation: super()

    zoo/models/animals.py:
    All animal subclasses call super().__init__ in their constructors
    zoo/models/exceptions.py:
    AnimalNotFoundException calls super().__init__

10. Creating and using a custom exception (a custom class inheriting from the built-in Exception class)

    zoo/models/exceptions.py:
    AnimalNotFoundException
    Usage:
    zoo/zoo_service.py: used in feeding, water, maintenance, move

11. Use of the design pattern: Strategy

    zoo/models/feeding.py:
    FeedingTemplate, HerbivoreFeedingTemplate, CarnivoreFeedingTemplate
    Usage:
    zoo/department.py:
    CarnivoreFeedingTemplate() if animal.is_carnivore() else HerbivoreFeedingTemplate()

12. Use of the design pattern: Command

    zoo/models/commands.py:
    Command, FeedCommand, WaterCommand, MaintainCommand

13. Use of the design pattern: Template Method

    zoo/models/feeding.py:
    FeedingTemplate defines the template method feed, which calls prepare_food and provide_food (overridden in subclasses)
    zoo/models/state_calculator.py:
    StateCalculatorTemplate defines the template method calculate_state, which calls low, mid and high (overridden in subclasses)
