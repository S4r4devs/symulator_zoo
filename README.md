# Symulator Zoo

Zrealizowane wymagania na tą chwilę:

Użycie klas:
  - animals.py
  - commands.py
  - exceptions.py
  - feeding.py
  - food.py
  - zookeepers.py

Użycie dziedziczenia (konkretne klasy):
  - Lion i Elephant po klasie Animal
  - FeedCommand po klasie Command
  - HerbivoreFeedingTemplate po klasie FeedingTemplate
  - HerbivoreFeeding i CarnivoreFeeding po klasie Feeder

Użycie atrybutów w klasach; pokazanie nadpisywania atrybutów w klasach potomnych:
  - animals.py
  - zookeepers.py (używa atrybutów, ale nie nadpisuje ich)

Użycie metod w klasach; pokazanie nadpisywania metod w klasach potomnych:
  - animals.py
  - commands.py
  - feeding.py
  - food.py (używa metod, ale nie nadpisuje ich)
  - zookeepers.py (używa metod, ale nie nadpisuje ich)

Użycie dekoratora @classmethod lub @staticmethod:
  - zookepers.py

Klasa zawierająca więcej niż jeden konstruktor:
  - zookeepers.py

Użycie enkapsulacji (settery i gettery):
  - animals.py
  - food.py

Polimorfizm:
  - animals.py
  - commands.py
  - feeding.py

Użycie implementacji z klasy rodzica: super():
  - animals.py
  - exceptions.py

Utworzenie i użycie swojego wyjątku (własna klasa dziedziąca z wbudowanej klasy Exception):
  - exceptions.py

Zastosowanie trzech wzorców projektowych
  - Jeden wybrany z:
    - Strategia (strategy) => to mamy
    - Polecenie (command) => to mamy
    - Metoda szablonowa (template method) => to mamy
  - Dwa dowolne (zrealizowane jako command i template method)
Zrealizowane:
  - Jeden wybrany:
    - np. strategy
  - Dwa dowolne:
    - command
    - template method
    - +static factory method (do implementacji wielu konstruktorów w pliku zookeepers.py)

