# Simulating Hunger Games to find the best way to design the game.
# Starting with designing the arena.
# The arena will be a 16x16 grid
# A value between 0 and 1 will determine the elevation of each cell

import matplotlib.pyplot as plt
import numpy as np
import random
import opensimplex
from matplotlib.colors import LinearSegmentedColormap

class Arena:
    def __init__(self, water_size: float = 0.25, sand_size: float = 0.05, grass_size: float = 0.45, rock_size: float = 0.25):
        # Ensure the sizes of the water, sand, grass, and rock areas add up to 1
        if water_size + sand_size + grass_size + rock_size != 1:
            raise ValueError('The sizes of the water, sand, grass, and rock areas must add up to 1')
        
        # Set the size of the water, sand, grass, and rock areas
        self.water_size = water_size
        self.sand_size = sand_size
        self.grass_size = grass_size
        self.rock_size = rock_size
        
        # Create a 16x16 grid of random values between 0 and 1 to represent the elevation of the terrain using OpenSimplex noise
        self.noise = opensimplex.OpenSimplex(seed=random.randint(0, 100))
        self.grid = [[(self.noise.noise2(x / 10, y / 10) + 1) / 2 for y in range(16)] for x in range(16)]
        
        # Width for displaying plots
        self.fig_width = 12
    
    def _value_to_terrain(self, value: float) -> str:
        if 0 <= value < self.water_size:
            return 'blue'
        elif self.water_size <= value < self.water_size + self.sand_size:
            return 'yellow'
        elif self.water_size + self.sand_size <= value < self.water_size + self.sand_size + self.grass_size:
            return 'green'
        else:
            return 'gray'
    
    def display_3d_grid(self):
        '''Displays grid as a 3D bar chart using matplotlib, with the x and y axis representing the grid coordinates and the z axis representing the elevation
        '''
        # Set up figure, with figsize based on a 16:9 aspect ratio
        aspect_ratio = 16 / 9
        fig_height = self.fig_width / aspect_ratio
        fig = plt.figure(figsize=(self.fig_width, fig_height))
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
        colors = [self._value_to_terrain(self.grid[i][j]) for i, j in zip(x, y)]
        
        # Create the 3D bar chart
        ax.bar3d(x, y, bottom, width, depth, top, shade=True, color=colors)
        plt.show()
    
    def display_2d_grid(self):
        '''Displays grid as a 2D plot with values in each cell
        '''
        # Set up figure, with figsize based on a square aspect ratio
        fig_height = self.fig_width
        fig = plt.figure(figsize=(self.fig_width, fig_height))
        # Create 2D plot
        ax = fig.add_subplot(111)
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                # Finds correct colour to use based on the value of the cell
                color = self._value_to_terrain(self.grid[i][j])
                # Create a rectangle for each cell in the grid
                rect = plt.Rectangle([j, len(self.grid) - i - 1], 1, 1, color=color)
                ax.add_patch(rect)
                # Add text to each cell with the value of the cell
                ax.text(j + 0.5, len(self.grid) - i - 0.5, f'{self.grid[i][j]:.2f}', ha='center', va='center', color='black')
        
        # Draw grid lines
        for i in range(len(self.grid) + 1):
            ax.axhline(i, color='black', lw=2)
            ax.axvline(i, color='black', lw=2)
        
        # Remove axis labels and ticks
        ax.set_xlim(0, len(self.grid[0]))
        ax.set_ylim(0, len(self.grid))
        ax.set_aspect('equal')
        ax.set_xticks([])
        ax.set_yticks([])
        
        plt.show()

# print the grid
arena = Arena()
arena.display_3d_grid()
