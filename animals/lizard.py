"""Lizard"""
from movements import Slithering, Walking
from .animal import Animal

class Lizard(Animal, Slithering, Walking):
    """Defines animal class"""
    def __init__(self, name, species, food, chip_num):
        """# Establish the properties of each animal
        # with a default value"""
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        Walking.__init__(self)


# After adding more than one super class, can no longer use super__init__ like super().__init__(name, species, food, chip_num)