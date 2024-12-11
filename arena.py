# Simulating Hunger Games to find the best way to design the game.
# Starting with designing the arena.
# The arena will be a 16x16 grid
# A value between 0 and 1 will determine the elevation of each cell

import matplotlib.pyplot as plt
import numpy as np
import random

class Arena:
    def __init__(self):
        self.grid = [[round(random.random(), 2) for i in range(16)] for j in range(16)]
    
    def print_grid(self):
        '''Prints grid in grid format to console
        '''
        for row in self.grid:
            print(row)
    
    def display_3d_grid(self):
        '''Displays grid as a 3D bar chart using matplotlib, with the x and y axis representing the grid coordinates and the z axis representing the elevation
        '''
        # Set up figure, with figsize based on a 16:9 aspect ratio
        aspect_ratio = 16 / 9
        fig_width = 8
        fig_height = fig_width / aspect_ratio
        fig = plt.figure(figsize=(fig_width, fig_height))
        
        # Create 3D plot
        ax = fig.add_subplot(111, projection='3d')
        # Create data for a 3D bar chart
        # For the x values we need to create a list of the x coordinates of each cell in the grid, by using the length of the grid array as the x values
        # For the y values we use the length of one of the rows nested in the grid array. This approach assumes the grid is a rectangle, with the same number of columns in each row
        x = np.arange(len(self.grid))
        y = np.arange(len(self.grid[0]))
        # Create a meshgrid from the x and y values
        _xx, _yy = np.meshgrid(x, y)
        # Flatten the meshgrid arrays
        x, y = _xx.ravel(), _yy.ravel()
        # Create the top and bottom values for the 3D bar chart
        # The top values are the elevation values from the grid
        # The bottom values are all zeros
        top = [self.grid[i][j] for i, j in zip(x, y)]
        bottom = np.zeros_like(top)
        width = depth = 1
        # Create the 3D bar chart
        ax.bar3d(x, y, bottom, width, depth, top, shade=True)
        plt.show()
        

# print the grid
arena = Arena()
arena.display_3d_grid()
