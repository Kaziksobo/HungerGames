from arena import Arena
import matplotlib.pyplot as plt
import random

class Resources(Arena):
    def __init__(self, arena: Arena):
        '''Creates a resource grid for the given arena.
        Args:
            arena (Arena): The arena to create the resources on
        '''
        # Set the size of the grid
        self.size = arena.size
        # create empty grid
        self.grid = [[(None, None, None) for y in range(self.size)] for x in range(self.size)]
        # apply circular mask to the grid
        mask = self._create_circular_mask(self.size)
        self.grid = [[self.grid[x][y] if mask[x][y] else None for y in range(self.size)] for x in range(self.size)]
        # create the resources grid
        self.grid = self._create_resources_grid()
        
        # Width for displaying plots
        self.fig_width = 11
    
    def _create_resources_grid(self):
        '''Creates the resource grid.
        Each resource has 3 values: quantity, quality and type (quality and quantity are measured from 0 to 1).
        The design will consist of a ring of high quantity, low quality resources around the edge of the arena. The closer to the centre of the arena,
        the lower the quantity and the higher the quality of the resources. Then in the centre, there are a high quantity of high quality weapons.
        The types of resources are: weapons, food and medicine. The resources are randomly distributed within the rings.'''
        # use self.grid and add the outside ring of resources
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j]:
                    # If the cell is in the outermost ring, give a quantity of 0.8 and a quality of 0.2, and randomly assign a resource type
                    if (i > 0 and self.grid[i-1][j] is None) or (i < self.size - 1 and self.grid[i+1][j] is None) or \
                       (j > 0 and self.grid[i][j-1] is None) or (j < self.size - 1 and self.grid[i][j+1] is None):
                        self.grid[i][j] = (0.8, random.choice(['weapons', 'food', 'medicine']), 0.2)
                        current_ring = 2
                    # Repeat this process, reducing the quantity and increasing the quality as we move towards the centre of the arena.
                    # The rate of reduction and increase should be based on the size of the arena.
                    # CURRENTLY DOES NOT WORK
                    rate_of_reduction = 0.8 / (self.size // 2)
                    rate_of_increase = 0.2 / (self.size // 2)
                    quantity = 0.8 - rate_of_reduction * current_ring
                    quality = 0.2 + rate_of_increase * current_ring
                    if self.grid[i][j] == (None, None, None):
                        self.grid[i][j] = (quantity, random.choice(['weapons', 'food', 'medicine']), quality)
                        current_ring += 1
        return self.grid
    
    def display_2d(self):
        fig = plt.figure(figsize=(self.fig_width, self.fig_width))
        ax = fig.add_subplot(111)
        
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j]:
                    rect = plt.Rectangle([j, self.size - i - 1], 1, 1)
                    ax.add_patch(rect)
                    quantity, resource_type, quality = self.grid[i][j]
                    if resource_type:
                        ax.text(j + 0.5, self.size - i - 0.5, f'{quantity:.2f}', ha='center', va='center', color='white')
        
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