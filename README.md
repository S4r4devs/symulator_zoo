# Zoo Manager

1. Use of classes

    All model files:
    zoo/models/animals.py (Animal, Lion, Elephant, Monkey, Giraffe, Parrot)
    zoo/models/zookeepers.py (Zookeeper)
    zoo/models/food.py (Food)
    zoo/models/commands.py (Command, FeedCommand)
    zoo/models/feeding.py (FeedingTemplate, HerbivoreFeedingTemplate, CarnivoreFeedingTemplate, Feeder, HerbivoreFeeding, CarnivoreFeeding)
    zoo/models/exceptions.py (AnimalNotFoundException)
    zoo/models/department.py (department)
    zoo/models/maintenance.py (MaintenanceTemplate)
    zoo/models/moving_strategy.py (Moving_strategy)
    
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
    zoo/models/supply.py:
    Water inherits from Supply
    zoo/models/state_calculator.py:
    MoodStateCalculator, StatusBarStateCalculator inherit from StateCalculatorTemplate
    zoo/models/maintenance.py:
    BigAnimalMaintenanceTemplate, SmallAnimalMaintenanceTemplate inherit from MaintenanceTemplate
    zoo/models/moving_strategy.py
    Small_Animal_Moving, Big_Animal_Moving,  Jumping_Animal_Moving, Flying_Animal_Moving inherit from  Moving_strategy
       


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
    zoo/models/moving_strategy.py:
    Concrete Moving Strategies (Child classes) Small_Animal_Moving overrides the moving method from Moving_strategy to implement small-step movement. 
    Big_Animal_Moving overrides the moving method from Moving_strategy to implement big-step movement. 
    Jumping_Animal_Moving overrides the moving method from Moving_strategy to implement jumping movement. 
    Flying_Animal_Moving overrides the moving method from Moving_strategy to implement flying movement.
    zoo/models/maintenance.py:
    Concrete MaintenanceTample (Child classes) BigAnimalMaintenanceTemplate overrides check_enclosure_security and inspect_animals_health from MaintenanceTemplate to provide specific procedures for large animals
    SmallAnimalMaintenanceTemplate overrides check_enclosure_security and inspect_animals_health from MaintenanceTemplate to provide specific procedures for small animals.
    
5. Use of the @classmethod and @staticmethod decorators

    zoo/models/zookeepers.py:
    from_dict, from_string (@classmethod)
    validate_name, authenticate (@staticmethod)
    zoo/models/zoo_service.py:
    feeding, water, maintenance, move (@staticmethod)
    

6. Class containing more than one constructor

    zoo/models/zookeepers.py:
    __init__, from_dict, from_string

7. Use of encapsulation (setters and getters)

    zoo/models/animals.py:
    name, age properties with setters/getters
    is_carnivore
    zoo/models/food.py:
    quantity property with setter/getter
    zoo/models/department.py:
    animal, feed, maintenance with setter/getter

8. Polymorphism

    zoo/models/animals.py:
    All animal subclasses can be used as Animal
    zoo/models/feeding.py:
    All feeders/templates can be used as their parent type
    zoo/models/commands.py:
    All commands can be used as Command

9. Use of parent class implementation: super()

    zoo/models/animals.py:
    All animal subclasses call super().__init__ in their constructors
    zoo/models/exceptions.py:
    AnimalNotFoundException calls super().__init__
    
    

10. Creating and using a custom exception (a custom class inheriting from the built-in Exception class)

    zoo/models/exceptions.py:
    AnimalNotFoundException
    Usage:
    zoo/views.py: used in feed_animal and water_animal

11. Use of the design pattern: Strategy

    zoo/models/feeding.py:
    FeedingTemplate, HerbivoreFeedingTemplate, CarnivoreFeedingTemplate
    Usage:
    zoo/commands.py:
    strategy = CarnivoreFeedingTemplate() if self.animal.is_carnivore() else HerbivoreFeedingTemplate()

12. Use of the design pattern: Command

    zoo/models/commands.py:
    Command, FeedCommand

13. Use of the design pattern: Template Method

    zoo/models/feeding.py:
    FeedingTemplate defines the template method feed, which calls prepare_food and provide_food (overridden in subclasses)
    zoo/models/state_calculator.py:
    StateCalculatorTemplate defines the template method calculate_state, which calls low, mid and high (overridden in subclasses)
    MaintenanceTemplate defines the template method  enclosure maintenance, which calls clean_waste and refill_water and check_enclosure_security and inspect_animals_health
    zoo/models/maintenance.py:
    MaintenanceTemplate defines the template method maintain_enclosure, which orchestrates steps like clean_waste, refill_water, and delegates abstract methods check_enclosure_security and inspect_animals_health to concrete child classes.
    zoo/models/moving_strategy.py:
    Moving_strategy defines the abstract interface for movement behaviors, with concrete strategies (e.g., Small_Animal_Moving, Big_Animal_Moving) overriding the 'moving' method to implement specific movements.

16. Use of the design pattern: strategy

    zoo/models/moving_strategy.py
    Strategy pattern to manage animal movement flexibly - Moving-strategy
    abstract Moving_strategy class, the made specific strategies like: Small_Animal_Moving, Big_Animal_Moving, Jumping_Animal_Moving,  Flying_Animal_Moving

15. Use of the design pattern: Facade
    zoo/models/zoo_service.py
    ZooService he does for facade

    
    