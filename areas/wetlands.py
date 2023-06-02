"""Wetlands"""

class Wetlands:
    """Defines park area"""

    def __init__(self, name, description):
        """Initializes model"""
        self.attraction_name = name
        self.description = description
        self.animals = list()

    @property
    def last_critter_added(self):
        """Getter for last animal added to list"""
        return self.animals[-1]

    def add_animal(self, animal):
        """A method to add animals to petting zoo"""
        self.animals.append(animal)

    def __str__(self):
        """Print a string"""
        animal_list = "\n   * ".join(str(animal) for animal in self.animals)
        return f"{self.attraction_name} is where you'll find {self.description}, like:\n   * {animal_list}"
