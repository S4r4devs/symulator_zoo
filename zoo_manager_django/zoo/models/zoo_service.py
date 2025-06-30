import json
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseBadRequest

from zoo_manager_django.zoo.models.animals import EuropeanHamster, Lion, Elephant, Monkey, Giraffe, Parrot
from zoo_manager_django.zoo.models.department import Department
from zoo_manager_django.zoo.models.exceptions import AnimalNotFoundException
from zoo_manager_django.zoo.models.feeding import CarnivoreFeedingTemplate, \
    HerbivoreFeedingTemplate
from zoo_manager_django.zoo.models.supply import Supply
from zoo_manager_django.zoo.models.maintenance import BigAnimalMaintenanceTemplate, \
    SmallAnimalMaintenanceTemplate
from zoo_manager_django.zoo.models.zookeepers import Zookeeper


class ZooService:

    animals = [
        Lion("Simba", 5),
        Elephant("Dumbo", 10),
        Monkey("George", 3),
        Giraffe("Melman", 7),
        Parrot("Polly", 2),
        EuropeanHamster("Borubar", 1000),

    ]

    _zookeepers = [
        Zookeeper("Alex"),
        Zookeeper("Justyna"),
        Zookeeper("Sara"),
    ]

    _food_inventory = [
        Supply("Carrots", 50),
        Supply("Meat", 30),
        Supply("Bananas", 20),
        Supply("Tree foliage", 75),
        Supply("Seeds", 578),
        Supply("Test", 0),

    ]

    _water_reservoir = Supply("Water", 10000),

    _departments = {
        "Simba": Department(Lion("Simba", 5), CarnivoreFeedingTemplate(), BigAnimalMaintenanceTemplate()),
        "Dumbo": Department(Elephant("Dumbo", 10), HerbivoreFeedingTemplate(), BigAnimalMaintenanceTemplate()),
        "George": Department(Monkey("George", 3), HerbivoreFeedingTemplate(), BigAnimalMaintenanceTemplate()),
        "Melman": Department(Giraffe("Melman", 7), HerbivoreFeedingTemplate(), BigAnimalMaintenanceTemplate()),
        "Polly": Department(Parrot("Polly", 2), HerbivoreFeedingTemplate(), SmallAnimalMaintenanceTemplate()),
        "Borubar": Department(EuropeanHamster("Borubar", 1000), HerbivoreFeedingTemplate(), SmallAnimalMaintenanceTemplate()),
    }

    @staticmethod
    def feeding(request, name):
        department = ZooService._departments[name]
        if not department:
            return HttpResponseNotFound(str(AnimalNotFoundException(name)))
        return department.feed.feed(request, department.animal, ZooService._food_inventory)

    @staticmethod
    def maintenance(name):
        department = ZooService._departments[name]
        if not department:
            return HttpResponseNotFound(str(AnimalNotFoundException(name)))
        return department.maintenance.maintain_enclosure(department.animal, ZooService._water_reservoir)

    @staticmethod
    def move(name):
        department = ZooService._departments[name]
        if not department:
            return HttpResponseNotFound(str(AnimalNotFoundException(name)))
        return JsonResponse({
            "move": department.animal.move()
        })

    def get_food_inventory(request):
        """Fetch food inventory."""
        return JsonResponse(
            [{"name": f.name, "quantity": f.quantity} for f in ZooService._food_inventory],
            safe=False
        )

    def get_zookeepers(request):
        """Fetch all zookeepers."""
        return JsonResponse(
            [{"name": zk.name} for zk in ZooService._zookeepers],
            safe=False
        )

    def login(request):
        """Authenticate a zookeeper."""
        if request.method != "POST":
            return HttpResponseBadRequest("Invalid HTTP method. Use POST.")
        try:
            data = json.loads(request.body)
            name = data.get("name", "").strip()
            password = data.get("password", "")
            if Zookeeper.authenticate(name, password):
                return JsonResponse({"message": "Login successful", "zookeeper": name})
            else:
                return JsonResponse({"error": "Invalid credentials"}, status=401)
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON data!"}, status=400)

