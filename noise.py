# Creating a noise based function for generating the values for the terrain in the arena from game.py

# Examnple grid for testing
grid = [[0 for i in range(16)] for j in range(16)]

# Heres if we just used random
import random
grid = [[round(random.random(), 2) for i in range(16)] for j in range(16)]
for row in grid:
    print(row)