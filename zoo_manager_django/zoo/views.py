from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
import json
from zoo.models.animals import Lion, Elephant
from zoo.models.exceptions import AnimalNotFoundException
from zoo.models.feeding import HerbivoreFeedingTemplate, CarnivoreFeedingTemplate
from zoo.models.zookeepers import Zookeeper

# Sample data
animals = [
    Lion("Simba", 80),
    Elephant("Dumbo", 200)
]

zookeepers = [
    Zookeeper("Alice"),
    Zookeeper("Bob"),
]

# Sample food inventory data
food_inventory = [
    {"name": "Carrots", "quantity": 50},
    {"name": "Meat", "quantity": 30},
    {"name": "Bananas", "quantity": 20},
]

def get_animals(request):
    """Fetch all animals and their details."""
    return JsonResponse(
        [{"name": a.name, "species": a.species, "sound": a.speak()} for a in animals],
        safe=False
    )

def feed_animal(request, animal_name):
    """Feed an animal based on its species."""
    animal = next((a for a in animals if a.name == animal_name), None)
    if not animal:
        return HttpResponseNotFound(str(AnimalNotFoundException(animal_name)))

    # Strategy pattern for feeding
    strategy = CarnivoreFeedingTemplate() if animal.species == "Lion" else HerbivoreFeedingTemplate()
    preparation = strategy.prepare_food(animal)
    feeding = strategy.provide_food(animal)

    return JsonResponse({"preparation": preparation, "feeding": feeding})

def get_zookeepers(request):
    """Fetch all zookeepers."""
    return JsonResponse(
        [{"name": zk.name} for zk in zookeepers],
        safe=False
    )

def add_zookeeper(request):
    """Add a new zookeeper."""
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid HTTP method. Use POST.")

    try:
        data = json.loads(request.body)
        name = data.get("name", "").strip()  # Ensure name is not empty
        if not name:
            return JsonResponse({"error": "Name cannot be empty!"}, status=400)

        if Zookeeper.validate_name(name):
            new_zookeeper = Zookeeper(name)
            zookeepers.append(new_zookeeper)
            return JsonResponse({"message": f"Zookeeper {name} added successfully!"})
        else:
            return JsonResponse({"error": "Invalid zookeeper name!"}, status=400)
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON data!"}, status=400)

def get_food_inventory(request):
    """Fetch food inventory."""
    return JsonResponse(food_inventory, safe=False)
