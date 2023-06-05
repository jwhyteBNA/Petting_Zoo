"""Snake pit"""
from movements import Slithering
from .attraction import Attraction

class SnakePit(Attraction):
    """Defines park area"""

    def __init__(self, name, description):
        """Initializes model"""
        super().__init__(name, description)
        self.animals = list()

    def add_animal_pythonic(self, animal):
        """Number 1: Slithering typing check"""
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal} doesn\'t slither; it does not go in {self.attraction_name}.')

    # def __str__(self):
    #     """Print a string"""
    #     animal_list = "\n   * ".join(str(animal) for animal in self.animals)
    #     return f"{self.attraction_name} is where you'll find {self.description}, like:\n   * {animal_list}"
