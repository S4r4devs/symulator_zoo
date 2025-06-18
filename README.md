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
   
## Plan dalszego rozwoju projektu

Dodatkowe aktywności oprócz karmienia:
  - pojenie
  - sprzątanie wybiegu
  - wyprowadzanie zwierząt
  - dawanie zwierzętom różnych rzeczy typu: słoń-piłka, małpa grzechotka.

Może być też abstrakcyjnie (aktywności) tak aby było to ciekawe np. wyprowadzanie pingwinów na spacer po zoo.

Jeśli chodzi o zwierzęta to np na początek można tylko dodawać lwy, słonie, małpy lub pingwiny, każde zwierze może jeść tylko okresloną żywność czyli małpe nakarmimy tylko bananem, Iwa tylko mięsem itd. I np. powinien wystąpić komunikat typu "Nakarmiłeś zwierzę niewłaściwym jedzeniem".

Można zrobić paski, które by pokazywały np. poziom najedzenia się zwierzeka lub że trzeba posprzątać bo ma brudno albo że zwierzę jest nieszczęśliwe bo nie poszło na spacer lub nie dostało zabawki. Jak wszystkie paski lub część z nich (do dogadania i ustalenia) będą na zerowym poziomie to zwierze umiera/znika.

Obrazki zrobione za pomocą AI:
Czyli np. szczęśliwy lew, nieszczęśliwy, bawiący się np piłką, jedzący.
Obrazek by się pojawiał na stronie w momencie jakiejś aktywności np karmimy lwa i pojawia się obrazek z lwem, który je.

Odnośnie zapasów jedzenia jest to kwestia do ustalenia (musimy ustalić jak to będzie działać i czy zapasy będą ubywać z każdym nakarmieniem itp)

Odnośnie Zookeepers jest to kwestia do ustalenia (musimy ustalić po co są, jakie pełnią funkcje, czy np. my jesteśmy tymi zookeepers itp.)

