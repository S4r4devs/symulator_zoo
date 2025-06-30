import json
from django.http import HttpResponseNotFound, JsonResponse, HttpResponseBadRequest

from zoo.models.animals import EuropeanHamster, Lion, Elephant, Monkey, Giraffe, Parrot
from zoo.models.department import Department
from zoo.models.exceptions import AnimalNotFoundException
from zoo.models.feeding import CarnivoreFeedingTemplate, HerbivoreFeedingTemplate
from zoo.models.supply import Supply, Water
from zoo.models.maintenance import BigAnimalMaintenanceTemplate, SmallAnimalMaintenanceTemplate
from zoo.models.zookeepers import Zookeeper


class ZooService:

    _zookeepers = [
        Zookeeper("Alex"),
        Zookeeper("Justyna"),
        Zookeeper("Sara"),
    ]

    _water_reservoir = [ Water(10000) ]

    _food_inventory = [
        _water_reservoir[0],
        Supply("Carrots", 50),
        Supply("Meat", 30),
        Supply("Bananas", 20),
        Supply("Tree foliage", 75),
        Supply("Seeds", 578)
    ]


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
    def water(name):
        department = ZooService._departments[name]
        if not department:
            return HttpResponseNotFound(str(AnimalNotFoundException(name)))
        return department.maintenance.refill_water(department.animal, ZooService._water_reservoir)

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

    def get_animals(request):
        """Fetch all animals and their details."""
        return JsonResponse(
            [{
                "name": ZooService._departments[key].animal.name,
                "species": ZooService._departments[key].animal.species,
                "age": ZooService._departments[key].animal.age,
                "status": ZooService._departments[key].animal.status,
                "status_bar": ZooService._departments[key].animal.status_bar
            } for key in ZooService._departments],
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

