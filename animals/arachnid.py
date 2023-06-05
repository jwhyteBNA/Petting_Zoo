"""Arachnid"""
from datetime import date
from movements import Slithering
from .animal import Animal

class Arachnid(Animal, Slithering):
    """Defines animal class"""
    def __init__(self, name, species, food, chip_num):
        """# Establish the properties of each animal
        # with a default value"""
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)

    def feed(self):
        """To feed animal"""
        print(f'on {date.today()}, {self.name} had "The Itsy Bitsy Spider" sung to it so it would eat its {self.food}')
