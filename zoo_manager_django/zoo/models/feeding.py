from abc import ABC, abstractmethod
import json
from django.http import JsonResponse


class FeedingTemplate(ABC):

    def feed(self, request,  animal, food_inventory):
        data = json.loads(request.body) if request.method == "POST" else {}
        food_name = data.get("food", None)
        if not food_name:
            return JsonResponse({"error": "No food specified"}, status=400)
        food = next((f for f in food_inventory if f.name == food_name), None)
        if not food or food.quantity <= 0:
            return JsonResponse({"error": "Food not available"}, status=400)

        prepare_food = self.prepare_food(animal)
        provide_food = self.provide_food(animal)
        self.feed_animal(food_name, food_inventory, animal)

        return JsonResponse({
            "message": f"{animal.name} has been given {food_name}.",
            "provide_food" : provide_food,
            "prepare_food" : prepare_food,
            "status_bar": animal.status_bar,
            "status": animal.status
        })

    def feed_animal(self, food_name, food_inventory, animal):
        food = next((f for f in food_inventory if f.name == food_name), None)
        food.quantity -= 1
        animal.feed()


    @abstractmethod
    def prepare_food(self, animal):
        pass

    @abstractmethod
    def provide_food(self, animal):
        pass

class HerbivoreFeedingTemplate(FeedingTemplate):
    def prepare_food(self, animal):
        return f"Preparing vegetables for {animal.name}"

    def provide_food(self, animal):
        return f"Feeding {animal.name} with vegetables"

class CarnivoreFeedingTemplate(FeedingTemplate):
    def prepare_food(self, animal):
        return f"Preparing meat for {animal.name}"

    def provide_food(self, animal):
        return f"Feeding {animal.name} with meat"


