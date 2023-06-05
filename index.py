"""Index"""
from animals import Llama
from animals import Turtle
from attractions import PettingZoo

varmint_village = PettingZoo("The Varmint Village", "critters that love to be pet!")

# remember, some animals may require more arguments than others; e.g. shift
dolly = Llama("Dolly", "miniature llama", "morning", "hay", 1033)
snappy = Turtle("Snappy", "American Snapping turtle", "fish", 1044)

varmint_village.add_animal_pythonic(dolly)
varmint_village.add_animal_pythonic(snappy)


for animal in varmint_village.animals:
    print(animal)
