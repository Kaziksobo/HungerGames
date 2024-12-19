import matplotlib.pyplot as plt
import numpy as np
import random
import opensimplex

class Arena:
    def __init__(self, size: int = 21, water_size: float = 0.25, sand_size: float = 0.05, grass_size: float = 0.45, rock_size: float = 0.25):
        '''Creates an arena.
        This arena is circular and has a grid of cells, each with a value representing the elevation of the terrain.
        The terrain is divided into four types: water, sand, grass, and rock, which are dependent on the value of the cell.
        The values are generated using OpenSimplex noise.

        Args:
            size (int, optional): The size of the arena grid. Defaults to 21.
            water_size (float, optional): Determines the amount of water in comparison to the other terrain options. Defaults to 0.25.
            sand_size (float, optional): Determines the amount of sand in comparison to the other terrain options. Defaults to 0.05.
            grass_size (float, optional): Determines the amount of grass in comparison to the other terrain options. Defaults to 0.45.
            rock_size (float, optional): Determines the amount of rock in comparison to the other terrain options. Defaults to 0.25.

        Raises:
            ValueError: The sizes of the water, sand, grass, and rock areas must add up to 1
            ValueError: The grid must be square
        '''
        # Ensure the sizes of the water, sand, grass, and rock areas add up to 1
        if water_size + sand_size + grass_size + rock_size != 1:
            raise ValueError('The sizes of the water, sand, grass, and rock areas must add up to 1')
        
        # Set the size of the water, sand, grass, and rock areas
        self.water_size = water_size
        self.sand_size = sand_size
        self.grass_size = grass_size
        self.rock_size = rock_size
        
        # Set the size of the grid
        self.size = size
        
        # Create a 16x16 grid of random values between 0 and 1 to represent the elevation of the terrain using OpenSimplex noise
        self.noise = opensimplex.OpenSimplex(seed=random.randint(0, 100))
        self.grid = [[(self.noise.noise2(x / 10, y / 10) + 1) / 2 for y in range(self.size)] for x in range(self.size)]
        
        # Apply circular mask to the grid
        mask = self._create_circular_mask(self.size)
        self.grid = [[self.grid[x][y] if mask[x][y] else None for y in range(self.size)] for x in range(self.size)]
        
        # Width for displaying plots
        self.fig_width = 11
    
    def _value_to_terrain(self, value: float) -> str:
        '''Converts a value to a terrain type based on the size of the water, sand, grass, and rock areas

        Args:
            value (float): The value to convert

        Returns:
            str: The terrain type
        '''
        if value is None: 
            return 'black'
        if 0 <= value < self.water_size:
            return 'blue'
        elif self.water_size <= value < self.water_size + self.sand_size:
            return 'yellow'
        elif self.water_size + self.sand_size <= value < self.water_size + self.sand_size + self.grass_size:
            return 'green'
        else:
            return 'gray'
    
    def _create_circular_mask(self, size: int) -> np.ndarray:
        '''Creates a circular mask for the grid

        Args:
            size (int): The size of the grid

        Returns:
            np.ndarray: The circular mask
        '''
        # Calculate the center of the grid
        center = size // 2, size // 2
        # Calculate the radius of the circular mask
        radius = min(center[0], center[1], size-center[0], size-center[1])
        # Create a grid of distances from the center
        Y, X = np.ogrid[:size, :size]
        dist_from_center = np.sqrt((X - center[1])**2 + (Y - center[0])**2)
        return dist_from_center <= radius

    def _3d_data(self):
        '''Creates the data for a 3D bar chart

        Returns:
            x (int): The x coordinates of each cell in the grid
            y (int): The y coordinates of each cell in the grid
            top (float): The elevation values from the grid
            bottom (float): The bottom values for the 3D bar chart
            width (int): The width of the 3D bar chart
            depth (int): The depth of the 3D bar chart
        '''
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
        top = [self.grid[i][j] if self.grid[i][j] is not None else 0 for i, j in zip(x, y)]
        bottom = np.zeros_like(top)
        width = depth = 1
        return x, y, top, bottom, width, depth
        
        
    def display_3d(self):
        '''Displays grid as a 3D bar chart using matplotlib, with the x and y axis representing the grid coordinates and the z axis representing the elevation
        '''
        # Set up figure, with figsize based on a 16:9 aspect ratio
        aspect_ratio = 16 / 9
        fig_height = self.fig_width / aspect_ratio
        fig = plt.figure(figsize=(self.fig_width, fig_height))
        # Create 3D plot
        ax = fig.add_subplot(projection='3d')
        
        # Get the data for the 3D bar chart
        x, y, top, bottom, width, depth = self._3d_data()
        # Get the colors for the 3D bar chart based on the value of the cell
        colors = [self._value_to_terrain(self.grid[i][j]) if self.grid[i][j] is not None else 'white' for i, j in zip(x, y)]
        
        # Create the 3D bar chart
        ax.bar3d(x, y, bottom, width, depth, top, shade=True, color=colors)
        
        # Set the aspect ratio of the plot, mainly to reduce the vertical exaggeration
        ax.set_box_aspect(aspect=(2, 2, 0.6))
        
        # Hide grid lines
        ax.grid(False)

        # Hide axes ticks
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_zticks([])
        
        # Hide axes
        ax.xaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.yaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        ax.zaxis.line.set_color((1.0, 1.0, 1.0, 0.0))
        
        plt.show()
    
    def display_2d(self):
        '''Displays grid as a 2D plot with values in each cell
        '''
        # Set up figure, with figsize based on a square aspect ratio
        fig = plt.figure(figsize=(self.fig_width, self.fig_width))
        # Create 2D plot
        ax = fig.add_subplot()
        
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                if self.grid[i][j]:
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