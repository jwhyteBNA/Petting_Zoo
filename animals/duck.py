"""Duck"""
from datetime import date
from movements import Swimming, Walking
from .animal import Animal

class Duck(Animal, Swimming, Walking):
    """Defines animal class"""
    def __init__(self, name, species, food, chip_num):
        """# Establish the properties of each animal
        # with a default value"""
        Animal.__init__(self, name, species, food, chip_num)
        Swimming.__init__(self)
        Walking.__init__(self)

    def feed(self):
        """To feed animal"""
        print(f'on {date.today()}, {self.name} heard "Five Little Ducks" and ate its {self.food}')
