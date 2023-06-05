"""Goose"""
from movements import Walking, Swimming
from .animal import Animal

class Goose(Animal, Walking, Swimming):
    """Goose"""
    def __init__(self, name, species, food, chip_number):
        """Initialize Goose"""
        # No more super() when initializing multiple base classes
        Animal.__init__(self, name, species, food, chip_number)
        Swimming.__init__(self)
        Walking.__init__(self)
        # no more self.swimming = True

    def honk(self):
        """Print noise"""
        print("The goose honks. A lot")

    def run(self):
        """Overriding parent behavior of Walking model"""
        print(f'{self} waddles')

    def __str__(self):
        """String for name"""
        return f'{self.name} the Goose'
