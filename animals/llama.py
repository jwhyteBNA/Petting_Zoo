"""Model"""
from datetime import date
from movements import Walking
from .animal import Animal

class Llama(Animal, Walking):
    """Defines animal class"""
    def __init__(self, name, species, shift, food, chip_num):
        """Initializes model"""
        Animal.__init__(self, name, species, food, chip_num)
        Walking.__init__(self)
        self.shift = shift

    def feed_llama(self):
        """To feed animal"""
        print(f'on {date.today()}, {self.name} had "Rockytop" sung to it and ate its {self.food}')
