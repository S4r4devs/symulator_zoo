from django.http import JsonResponse, HttpResponseNotFound, HttpResponseBadRequest
import json
import time
from zoo.models.animals import Lion, Elephant, Monkey, Giraffe, Parrot
from zoo.models.exceptions import AnimalNotFoundException
from zoo.models.feeding import HerbivoreFeedingTemplate, CarnivoreFeedingTemplate
from zoo.models.zookeepers import Zookeeper
from zoo.models.food import Food, Water

# Sample data
animals = [
    Lion("Simba", 5),
    Elephant("Dumbo", 10),
    Monkey("George", 3),
    Giraffe("Melman", 7),
    Parrot("Polly", 2)
]

zookeepers = [
    Zookeeper("Alex"),
    Zookeeper("Justyna"),
    Zookeeper("Sara"),
]

food_inventory = [
    Food("Carrots", 50),
    Food("Meat", 30),
    Food("Bananas", 20),
    Water(100)
]

def get_animals(request):
    """Fetch all animals and their details."""
    return JsonResponse(
        [{
            "name": a.name,
            "species": a.species,
            "age": a.age,
            "status": a.status,
            "status_bar": a.status_bar
        } for a in animals],
        safe=False
    )

def feed_animal(request, animal_name):
    """Feed an animal based on its species."""
    animal = next((a for a in animals if a.name == animal_name), None)
    if not animal:
        return HttpResponseNotFound(str(AnimalNotFoundException(animal_name)))
    data = json.loads(request.body) if request.method == "POST" else {}
    food_name = data.get("food", None)
    if not food_name:
        return JsonResponse({"error": "No food specified"}, status=400)
    food = next((f for f in food_inventory if f.name == food_name and f.name.lower() != "water"), None)
    if not food or food.quantity <= 0:
        return JsonResponse({"error": "Food not available"}, status=400)
    # Decrement food
    food.quantity -= 1
    animal.feed()
    # Strategy pattern for feeding
    strategy = CarnivoreFeedingTemplate() if animal.species == "Lion" else HerbivoreFeedingTemplate()
    preparation = strategy.prepare_food(animal)
    feeding = strategy.provide_food(animal)
    return JsonResponse({
        "preparation": preparation,
        "feeding": feeding,
        "status": animal.status,
        "status_bar": animal.status_bar
    })

def water_animal(request, animal_name):
    """Give water to an animal."""
    animal = next((a for a in animals if a.name == animal_name), None)
    if not animal:
        return HttpResponseNotFound(str(AnimalNotFoundException(animal_name)))
    water = next((f for f in food_inventory if f.name.lower() == "water"), None)
    if not water or water.quantity <= 0:
        return JsonResponse({"error": "No water available"}, status=400)
    water.quantity -= 1
    animal.water()
    return JsonResponse({
        "message": f"{animal.name} has been given water.",
        "status": animal.status,
        "status_bar": animal.status_bar
    })

def get_zookeepers(request):
    """Fetch all zookeepers."""
    return JsonResponse(
        [{"name": zk.name} for zk in zookeepers],
        safe=False
    )


def get_food_inventory(request):
    """Fetch food inventory."""
    return JsonResponse(
        [{"name": f.name, "quantity": f.quantity} for f in food_inventory if f.name.lower() != "water"],
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
