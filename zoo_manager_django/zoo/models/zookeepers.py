class Zookeeper:
    def __init__(self, name):
        self.name = name

    @classmethod
    def from_dict(cls, data):
        """Create a Zookeeper instance from a dictionary."""
        return cls(name=data["name"])

    @classmethod
    def from_string(cls, name_string):
        """Create a Zookeeper instance from a string."""
        return cls(name=name_string.strip())

    @staticmethod
    def validate_name(name):
        """Validate the name of a zookeeper."""
        return isinstance(name, str) and len(name) > 2
