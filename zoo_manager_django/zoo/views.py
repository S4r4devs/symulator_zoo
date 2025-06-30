from django.http import JsonResponse
import json
import time

from zoo_manager_django.zoo.models.zoo_service import ZooService


def get_animals(request):
    return ZooService.get_animals(request)

def feed_animal(request, animal_name):
    return ZooService.feeding(request, animal_name)

def maintenance(request, animal_name):
    return ZooService.maintenance(animal_name)

def move(request, animal_name):
    return ZooService.move(animal_name)

def get_zookeepers(request):
    """Fetch all zookeepers."""
    return ZooService.get_zookeepers(request)


def get_food_inventory(request):
    """Fetch food inventory."""
    return ZooService.get_food_inventory(request)

def login(request):
    """Authenticate a zookeeper."""
    return ZooService.login(request)
