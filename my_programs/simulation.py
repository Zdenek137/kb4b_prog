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

#---statistics---
field_red = 0
field_blue = 0
field_yellow = 0
field_green = 0

forest_red = 0
forest_blue = 0
forest_yellow = 0
forest_green = 0

desert_red = 0
desert_blue = 0
desert_yellow = 0
desert_green = 0

tundra_red = 0
tundra_blue = 0
tundra_yellow = 0
tundra_green = 0

for i in range(mice_count):
    
    match(mice[i].biome):
        case "field":
            match(mice[i].color):
                case "red":
                    field_red += 1
                case "blue":
                    field_blue += 1
                case "yellow":
                    field_yellow += 1
                case "green":
                    field_green += 1
        case "forest":
            match(mice[i].color):
                case "red":
                    forest_red += 1
                case "blue":
                    forest_blue += 1
                case "yellow":
                    forest_yellow += 1
                case "green":
                    forest_green += 1
        case "desert":
            match(mice[i].color):
                case "red":
                    desert_red += 1
                case "blue":
                    desert_blue += 1
                case "yellow":
                    desert_yellow += 1
                case "green":
                    desert_green += 1
        case "tundra":
            match(mice[i].color):
                case "red":
                    tundra_red += 1
                case "blue":
                    tundra_blue += 1
                case "yellow":
                    tundra_yellow += 1
                case "green":
                    tundra_green += 1

print("============")
print("RED MICE: ", field_red + forest_red + desert_red + tundra_red)
print("BLUE MICE: ", field_blue + forest_blue + desert_blue + tundra_blue)
print("YELLOW MICE: ", field_yellow + forest_yellow + desert_yellow + tundra_yellow)
print("GREEN MICE: ", field_green + forest_green + desert_green)
print("============")

print("FIELD RED MICE: ", field_red)
print("FIELD BLUE MICE: ", field_blue)
print("FIELD YELLOW MICE: ", field_yellow)
print("FIELD GREEN MICE: ", field_green)
print("----")

print("FOREST RED MICE: ", forest_red)
print("FOREST BLUE MICE: ", forest_blue)
print("FOREST YELLOW MICE: ", forest_yellow)
print("FOREST GREEN MICE: ", forest_green)
print("----")

print("DESERT RED MICE: ", desert_red)
print("DESERT BLUE MICE: ", desert_blue)
print("DESERT YELLOW MICE: ", desert_yellow)
print("DESERT GREEN MICE: ", desert_green)
print("----")

print("TUNDRA RED MICE: ", tundra_red)
print("TUNDRA BLUE MICE: ", tundra_blue)
print("TUNDRA YELLOW MICE: ", tundra_yellow)
print("TUNDRA GREEN MICE: ", tundra_green)
