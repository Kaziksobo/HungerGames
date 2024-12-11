# Simulating Hunger Games to find the best way to design the game.
# Starting with designing the arena.
# The arena will be a 16x16 grid
# A value between 0 and 1 will determine the elevation of each cell

import matplotlib.pyplot as plt

class Arena:
    def __init__(self):
        self.grid = [[0 for i in range(16)] for j in range(16)]
    
    def print_grid(self):
        '''Prints grid in grid format to console
        '''
        for row in self.grid:
            print(row)
    
    def display_3d_grid(self):
        '''Displays grid in 3D format using matplotlib
        '''
        

# print the grid
arena = Arena()
arena.print_grid()