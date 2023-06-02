"""Animal Class - inheritance and polymorphism"""

from datetime import date

class Animal:
    """Main Animal Class"""
    def __init__(self, name, species, food, chip_num):
        """To create animal"""
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        if isinstance(chip_num, int):
            self.__chip_number = chip_num
        else:
            raise ValueError("Chip number is integer only.")

    def feed(self):
        """To feed animal"""
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        """Print a string"""
        return f"{self.name} the {self.species}"

    @property
    def chip_number(self):
        """To get chip"""
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, num):
        """Setter function that will not change chip number"""
        print("Error: Chip Number Cannot Be Edited.")
