"""Monitor"""
from movements import Slithering, Swimming
from .animal import Animal

class Monitor(Animal, Slithering, Swimming):
    """Defines animal class"""
    def __init__(self, name, species, food, chip_num):
        """# Establish the properties of each animal
        # with a default value"""
        Animal.__init__(self, name, species, food, chip_num)
        Slithering.__init__(self)
        Swimming.__init__(self)
