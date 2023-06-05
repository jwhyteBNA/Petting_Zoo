"""Animal Class - inheritance and polymorphism"""

from datetime import date

class Animal:
    """Main Animal Class"""
    def __init__(self, name, species, food, chip_number):
        """To create animal"""
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()
        if isinstance(chip_number, int):
            self.__chip_number = chip_number
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
    def chip_number(self, chip_number):
        """Setter function that will not change chip number"""
        print("Error: Chip Number Cannot Be Edited.")
