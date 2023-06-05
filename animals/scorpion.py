"""Scorpion"""
from movements import Slithering
from .animal import Animal

class Scorpion(Animal, Slithering):
    """Defines animal class"""
    def __init__(self, name, species, food, chip_num):
        """# Establish the properties of each animal
        # with a default value"""
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
