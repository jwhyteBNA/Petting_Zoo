"""Frog"""
from movements import Swimming
from .animal import Animal

class Frog(Animal, Swimming):
    """Defines animal class"""
    def __init__(self, name, species, food, chip_num):
        """# Establish the properties of each animal
        # with a default value"""
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
