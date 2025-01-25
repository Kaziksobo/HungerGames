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
        self.grid = [
            [(None, None, None) for _ in range(self.size)]
            for _ in range(self.size)
        ]
        # apply circular mask to the grid
        mask = self._create_circular_mask(self.size)
        self.grid = [[self.grid[x][y] if mask[x][y] else None for y in range(self.size)] for x in range(self.size)]
        # create the resources grid
        self._create_resources_grid()

        # Width for displaying plots
        self.fig_width = 11
    
    def _create_resources_grid(self) -> list:
        """Creates the resource grid.

        Resources are represented as tuples: (quantity, type, quality).
        - Quantity: Higher at the edges, lower towards the center.
        - Type: Randomly chosen from 'weapons', 'food', 'medicine'.
        - Quality: Lower at the edges, higher towards the center.
        """

        center_x = self.size // 2
        center_y = self.size // 2
        max_distance_squared = center_x**2  # Maximum squared distance from the center

        for i in range(self.size):
            for j in range(self.size):
                # Make sure the cell isn't masked out
                if self.grid[i][j]:
                    # Calculate the squared distance from the center
                    distance_squared = (i - center_x)**2 + (j - center_y)**2
                    
                    # Ensure the distance is within the circular mask
                    if distance_squared <= max_distance_squared:
                        # Calculate normalized distance from the center (0.0 at center, 1.0 at edge)
                        normalized_distance = (distance_squared**0.5) / center_x
                        
                        # Calculate quantity and quality based on distance
                        quantity = 0.2 + 0.6 * normalized_distance
                        quality = 0.8 - 0.6 * normalized_distance
                        
                        # Randomly assign a resource type
                        resource_type = random.choice(['weapons', 'food', 'medicine'])
                        
                        # Assign the resource tuple to the grid cell
                        self.grid[i][j] = (quantity, resource_type, quality)
    
    def display_2d(self):
        """Displays the 2D resource grid.

        The grid is visualized using matplotlib, with each cell colored
        according to its resource quality.  Quantities are displayed
        as text within each cell.
        """
        fig = plt.figure(figsize=(self.fig_width, self.fig_width))
        ax = fig.add_subplot(111)
        
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j]:
                    quantity, resource_type, quality = self.grid[i][j]
                    rect = plt.Rectangle([j, self.size - i - 1], 1, 1, fc=plt.cm.viridis(quality))
                    ax.add_patch(rect)
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