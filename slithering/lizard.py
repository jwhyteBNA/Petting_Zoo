"""Lizard"""
from animal import Animal

class Lizard(Animal):
    """Defines animal class"""
    def __init__(self, name, species, food, chip_num):
        """# Establish the properties of each animal
        # with a default value"""
        super().__init__(name, species, food, chip_num)
        self.slithering = True
