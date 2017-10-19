'''
David Fuller

Food class - Handles the Food object.

10-15-2017
'''

import random
import math

from .Constants import pink, grid_scale
from .Node import Node

class Food(object):
    '''
    Sets up a Food class
    '''
    
    def __init__(self, screen):
        '''
        Game's init method.

        Stores screen object and Snake color. Initializes Food object. Calls
        method to decide where Food should be located
 
        Args:
            screen (pygame.display): Screen object to draw Food on.
        '''
        
        self.screen = screen
        self.node = Node(screen, pink)

        self.pick_location()

    def pick_location(self):
        '''
        Decides Food's position, based on the number of columns and rows according
        to the screen's resolution and grid_size.
        '''
        
        screen_width, screen_height = self.screen.get_size()

        column_count = math.floor(screen_width / grid_scale)
        row_count = math.floor(screen_height / grid_scale)

        x = math.floor(random.randint(0, column_count)) * grid_scale
        y = math.floor(random.randint(0, row_count)) * grid_scale

        self.node.set_position(x, y)
        self.node.constrain()

    def show(self):
        '''
        Shows the food Node.
        '''
        
        self.node.show()
