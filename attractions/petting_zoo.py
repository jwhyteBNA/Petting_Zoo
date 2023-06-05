"""Petting Zoo"""
from movements import Walking
from . import Attraction

class PettingZoo(Attraction):
    """Defines park area"""

    def __init__(self, name, description):
        """Initializes model"""
        super().__init__(name, description)
        self.animals = list()

    def add_animal_pythonic(self, animal):
        """Number 1: Duck typing check"""
        try:
            if animal.walk_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal} doesn\'t like to be petted, so please do not put it in the {self.attraction_name} attraction.')

    def add_animal_type_check(self, animal):
        """Number 2: Actual typing check"""
        if isinstance(animal, Walking):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(f'{animal} doesn\'t like to be petted, so please do not try to put it in the {self.attraction_name} attraction.')


    # def __str__(self):
    #     """Print a string"""
    #     animal_list = "\n   * ".join(str(animal) for animal in self.animals)
    #     return f"{self.attraction_name} is where you'll find {self.description}, like:\n   * {animal_list}"
