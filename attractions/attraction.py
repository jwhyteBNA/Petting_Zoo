"""Base attraction model"""

class Attraction:
    """Attraction"""
    def __init__(self, name, description):
        """Initializer"""
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add_animal(self, animal):
        """Add animal"""
        self.animals.append(animal)

    def remove_animal(self, animal):
        """Remove animal"""
        self.animals.remove(animal)

    @property
    def last_critter_added(self):
        """Getter for last animal added to list"""
        return self.animals[-1]

    def __str__(self):
        """Print string"""
        return f'{self.attraction_name} ({len(self)} animals)'

    def __len__(self):
        """Length"""
        return len(self.animals)
