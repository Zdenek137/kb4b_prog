import random
import os

mice_colors = ["red", "yellow", "blue", "green"]
biomes = ["field", "forest", "desert", "tundra"]

mice = []
mice_count = 30

class Mouse:
    def __init__(self, color, age, biome):
        self.color = color
        self.age = age
        self.biome = biome

    def show(self):
        print("Mouse")
        print("color: ", self.color)
        print("age: ", self.age)
        print("biome: ", self.biome)

#---mice creation---
for i in range(mice_count):
    mice.append(Mouse(random.choice(mice_colors), random.randint(1, 12),random.choice(biomes)))
