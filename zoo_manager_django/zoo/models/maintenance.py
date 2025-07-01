from abc import ABC, abstractmethod

from django.http import JsonResponse


class MaintenanceTemplate(ABC):
    def maintain_enclosure(self, animal, water_reservoir):
        waste = self.clean_waste(animal)
        self.refill_water(animal, water_reservoir)
        enclosure = self.check_enclosure_security(animal)
        inspect = self.inspect_animals_health(animal)
        return JsonResponse({
            "message": f"{animal.name} has its enclosure maintained.",
            "status": animal.status,
            "maintenance": waste,
            "status_bar": animal.status_bar,
            "enclosure": enclosure,
            "inspect": inspect,

        })

    def clean_waste(self, animal):
        return f"Cleaning {animal.name} enclosure"

    def refill_water(request, animal, water_reservoir):
        if water_reservoir[0].quantity <= 0:
            return JsonResponse({"error": "No water available"}, status=400)
        water_reservoir[0].quantity -= 1
        animal.water()
        return JsonResponse({
            "message": f"{animal.name} has been given water.",
            "status": animal.status,
            "status_bar": animal.status_bar,

        })

    @abstractmethod
    def check_enclosure_security(self, animal):
        pass

    @abstractmethod
    def inspect_animals_health(self, animal):
        pass

class BigAnimalMaintenanceTemplate(MaintenanceTemplate):
    def check_enclosure_security(self, animal):
        return f"Direct the {animal.species} to the resting areas. Checking enclosure"

    def inspect_animals_health(self,animal):
        return f"Direct the {animal.species} to the medical area. Chcecking health"

class SmallAnimalMaintenanceTemplate(MaintenanceTemplate):
    def check_enclosure_security(self, animal):
        return f"Direct the {animal.species} to the resting areas. Checking enclosure"

    def inspect_animals_health(self,animal):
        return f"Check if he {animal.species} is healthy"




