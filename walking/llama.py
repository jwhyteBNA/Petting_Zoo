"""Model"""

from walking import Animal

class Llama(Animal):
    """Defines animal class"""
    def __init__(self, name, species, shift, food, chip_num):
        """Initializes model"""
        super().__init__(name, species, food, chip_num)
        self.shift = shift
        self.walking = True
