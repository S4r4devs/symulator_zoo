class AnimalNotFoundException(Exception):
    def __init__(self, animal_name):
        super().__init__(f"Animal '{animal_name}' not found in the system.")
