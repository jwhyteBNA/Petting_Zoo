"""Turtle"""
from movements import Swimming, Walking
from .animal import Animal

class Turtle(Animal, Swimming, Walking):
    """Defines animal class"""
    def __init__(self, name, species, food, chip_num):
        """# Establish the properties of each animal
        # with a default value"""
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)
