"""Animals"""

from slithering import Arachnid, Lizard, Monitor, Scorpion, Snake
from swimming import Duck, Fish, Frog, Gecko, Turtle
from walking import Donkey, Goat, Llama, Pony, Rabbit
from areas import PettingZoo, Wetlands, SnakePit

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
varmint_village.add_animal(lefty)
varmint_village.add_animal(lebron)
varmint_village.add_animal(miss_fuzz)
varmint_village.add_animal(peter)
varmint_village.add_animal(lil)
last_animal = varmint_village.last_critter_added
# print(varmint_village)
print(last_animal)

slither_inn = SnakePit("Slither Inn", "creepy crawlies run this scareBNB")
slither_inn.add_animal(charlotte)
slither_inn.add_animal(sparks)
slither_inn.add_animal(mortimor)
slither_inn.add_animal(spike)
slither_inn.add_animal(sir_hugs_a_lot)
print(slither_inn)

critter_cove = Wetlands("Critter Cove", "creatures galore - floating, swimming, and more")
critter_cove.add_animal(quackers)
critter_cove.add_animal(bubbles)
critter_cove.add_animal(tinkerbell)
critter_cove.add_animal(gordon)
critter_cove.add_animal(donatello)
# print(critter_cove)

# for animal in varmint_village.animals:
#     print(f"{varmint_village.attraction_name} is where you'll find {varmint_village.description}, like {animal.name} the {animal.species}")

# for animal in varmint_village.animals:
#     print(f'You can find {animal.name} the {animal.species} in {varmint_village.attraction_name}')

# print(f'{lebron.name} the {lebron.species} is available to pet during the {lebron.shift} shift.')
# print(miss_fuzz.feed())
# print(lil)
