"""Animals"""

from animals import Arachnid, Lizard, Monitor, Scorpion, Snake
from animals import Duck, Fish, Frog, Gecko, Turtle
from animals import Donkey, Goat, Llama, Pony, Rabbit
from animals import Goose
from attractions import PettingZoo, Wetlands, SnakePit

charlotte = Arachnid("Charlotte", "Venezuelan Suntiger Tarantula", "bugs", 2001)
sparks = Lizard("Sparks", "Fire Skink", "bugs", 2002)
mortimor = Monitor("Mortimor", "Mangrove Monitor", "dragonflies", 2003)
spike = Scorpion("Spike", "Tailless Whip Scorpion", "mouse", 2004)
sir_hugs_a_lot = Snake("Sir Hugs-A-Lot", "Boa Constrictor", "mouse", 2005)

quackers = Duck("Quackers", "Mallard", "critter feed", 3001)
bubbles = Fish("Bubbles", "Peacock Bass", "critter feed", 3002)
tinkerbell = Frog("Tinkerbell", "Pixie Frog", "critter feed", 3003)
gordon = Gecko("Gordon", "Gargoyle Gecko", "critter feed", 3004)
donatello = Turtle("Donatello", "Leopard Tortoise", "critter feed", 3005)

lefty = Donkey("Donkey kick Dan", "Rare Donkey", "midday", "Donkey Chow", 1001)
lebron = Goat("Lebron", "G.O.A.T.", "morning", "Goat Chow", 1002)
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "afternoon", "Llama Chow", 1003)
lil = Pony("Lil Sebastian", "Miniature Shetland Pony", "afternoon", "Pony Chow", 1004)
peter = Rabbit("Peter Cottontail", "Flemish Giant Rabbit", "morning", "Salad", 1005)

varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
slither_inn = SnakePit("Slither Inn", "creepy crawlies run this scareBNB")
critter_cove = Wetlands("Critter Cove", "creatures galore - floating, swimming, and more")

varmint_village = PettingZoo("Varmint Village", "cute and fuzzy critters to cuddle")
varmint_village.add_animal_pythonic(lefty)
varmint_village.add_animal_pythonic(lebron)
varmint_village.add_animal_pythonic(miss_fuzz)
varmint_village.add_animal_pythonic(peter)
varmint_village.add_animal_pythonic(lil)
varmint_village.add_animal_pythonic(spike)
varmint_village.add_animal_pythonic(quackers)
last_animal = varmint_village.last_critter_added
print(varmint_village)
print(last_animal)
print (miss_fuzz.feed_llama())
print (miss_fuzz.feed())

slither_inn = SnakePit("Slither Inn", "creepy crawlies run this scareBNB")
slither_inn.add_animal_pythonic(charlotte)
slither_inn.add_animal_pythonic(sparks)
slither_inn.add_animal_pythonic(mortimor)
slither_inn.add_animal_pythonic(spike)
slither_inn.add_animal_pythonic(sir_hugs_a_lot)
print(slither_inn)

critter_cove = Wetlands("Critter Cove", "creatures galore - floating, swimming, and more")
critter_cove.add_animal_pythonic(quackers)
critter_cove.add_animal_pythonic(bubbles)
critter_cove.add_animal_pythonic(tinkerbell)
critter_cove.add_animal_pythonic(gordon)
critter_cove.add_animal_pythonic(donatello)
print(critter_cove)

# for animal in varmint_village.animals:
#     print(f"{varmint_village.attraction_name} is where you'll find {varmint_village.description}, like {animal.name} the {animal.species}")

# for animal in varmint_village.animals:
#     print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

# print(f'{lebron.name} the {lebron.species} is available to pet during the {lebron.shift} shift.')
# print(miss_fuzz.feed())
# print(lil)

bob = Goose("Bob", "Canada goose", "watercress sandwiches", 3006)
# bob.run()
# bob.swim()

# Create an attraction
varmint_village = PettingZoo("Varmint Village", "critters that like to dig and scurry")
varmint_village.add_animal(bob)

for animal in varmint_village.animals:
    print(animal)

for animal in slither_inn.animals:
    print(animal)

for animal in critter_cove.animals:
    print(animal)
