'''
David Fuller

Snake class - Handles snake object.

10-15-2017
'''

from .Constants import grid_scale, point, vector, black
from .processing import Processing

class Node(object):
    '''
    Sets up a Node class
    '''
    
    def __init__(self, screen, color):
        '''
        Node's init method.

        Stores screen object and Node attributes. Initializes a processing type
        package for drawing shapes.

        Args:
            screen (pygame.display): Screen object to draw Node on.
            color (namedtuple): Stores RGB values of a color.
        '''
        
        self.screen = screen
        self.color = color
        
        self.position = point(x = 0, y = 0)
        self.direction = vector(x = 0, y = 0)

        self.width = grid_scale
        self.height = grid_scale

        self.processing = Processing(screen)

    def set_position(self, x, y):
        '''
        Sets position of a Node object.

        Arg:
            x (int): x coordinate.
            y (int): y coordinate.
        '''
        
        self.position = point(x = x, y = y)

    def set_direction(self, x, y):
        '''
        Sets direction of a Node object.

        Arg:
            x (int): x direction.
            y (int): y direction.
        '''
        
        self.direction = vector(x = x, y = y)

    def constrain(self):
        '''
        Keeps Node object within the screen.
        '''
        
        screen_width, screen_height = self.screen.get_size()
        x = self.position.x
        y = self.position.y
        
        if self.position.x < 0:
            x = 0
        elif self.position.x > screen_width - grid_scale:
            x = screen_width - grid_scale
        elif self.position.y < 0:
            y = 0
        elif self.position.y > screen_height - grid_scale:
            y = screen_height - grid_scale

        self.position = point(x = x, y = y)

    def update(self):
        '''
        Moves Node one block up, down, left, or right according to the direction
        it is heading.
        '''
        self.position = point(x = self.position.x + self.direction.x * grid_scale,
                              y = self.position.y + self.direction.y * grid_scale
                              )

        self.constrain()

    def show(self):
        '''
        Shows the Node on screen with a black border.
        '''
        
        self.processing.fill(self.color)
        self.processing.stroke(black)
        self.processing.rect(self.position.x, self.position.y, self.width,
                             self.height
                             )

    def __repr__(self):
        '''
        Returns:
            String representation of a Node object in the format (x, y).
        '''
        
        return '({}, {})'.format(self.position.x, self.position.y)
