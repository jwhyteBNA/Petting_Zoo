"""Model"""

from animal import Animal

class Rabbit(Animal):
    """Defines animal class"""
    def __init__(self, name, species, shift, food, chip_num):
        """Establish animal properties"""
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
