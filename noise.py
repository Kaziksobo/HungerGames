# Creating a noise based function for generating the values for the terrain in the arena from game.py

import matplotlib.pyplot as plt
import numpy as np
import random

class PerlinNoise:
    '''Class for generating Perlin noise for an arbitrary point in an arbitrary number of dimensions.
    '''
    def __init__(self, dimensions: int, octaves: int = 1):
        '''Creates a PerlinNoise object.

        Args:
            dimensions (int): Given number of dimensions, which should be greater than 1.
            octaves (int, optional): More octaves create more detailed noise. Defaults to 1.
        '''
        self.dimensions = dimensions
        self.octaves = octaves
        
        # For n dimensions, the range of Perlin noise is ±sqrt(n)/2
        self.scale_factor = (dimensions ** 0.5) / 2
        
        self.gradient = {}
    
    def _generate_gradient(self):
        # Generate a random unit vector for each point in the grid
        # This is the gradient vector, so the grid tile slopes in this direction
        
        # For 1 dimension, the gradient is a scalar, so we just use a slope between -1 and 1
        if self.dimensions == 1:
            return random.uniform(-1, 1)
        
        # Generate a random point on the surface of the unit n-sphere
        # This works the same as generating a random unit vector in n dimensions
        random_point = [random.gauss(0, 1) for _ in range(self.dimensions)]
        # Then we scale the result to a unit vector
        scale = sum(x ** 2 for x in random_point) ** 0.5
        
        return tuple(x / scale for x in random_point)