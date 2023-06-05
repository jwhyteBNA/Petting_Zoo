"""Model"""
from movements import Walking
from .animal import Animal

class Rabbit(Animal, Walking):
    """Defines animal class"""
    def __init__(self, name, species, shift, food, chip_num):
        """Establish animal properties"""
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift
