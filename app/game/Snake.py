'''
David Fuller

Snake class - Handles snake object.

10-15-2017
'''

from .Constants import white, grid_scale
from .Node import Node

class Snake(object):
    '''
    Sets up a Snake class
    '''
    
    def __init__(self, screen):
        '''
        Snake's init method.

        Stores screen object and Snake color. Initializes Snake's head.

        Args:
            screen (pygame.display): Screen object to draw Snake on.
        '''
        
        self.screen = screen
        self.color = white
        
        self.head = Node(self.screen, self.color)

        self.length = 0
        self.tail = []

    def set_direction(self, x, y):
        '''
        Sets direction of Snake's head.

        Arg:
            x (int): x direction.
            y (int): y direction.
        '''
        
        self.head.set_direction(x, y)

    def eat(self, food):
        '''
        Decide whether or not the Snake ate the piece of food on screen. If so
        the Snake grows another Node on its tail.

        Args:
            food (object): Node object to handle food functionality.

        Returns:
            True (bool): Snake comes in contact with food.
            False (bool): Snake did not contact the food.
        '''
        
        if self.head.position.x >= food.node.position.x and \
           self.head.position.x < food.node.position.x + grid_scale and \
           self.head.position.y >= food.node.position.y and \
           self.head.position.y < food.node.position.y + grid_scale:
            self.tail.append(Node(self.screen, self.color))
            self.length = self.length + 1
            self.tail[len(self.tail) - 1].set_position(self.head.position.x,
                                                       self.head.position.y
                                                       )
            return True
        return False

    def update(self):
        '''
        Repositions Snakes tail nodes where applicable.
        '''

        length = len(self.tail)
        if self.length == length:
            for i in range(length - 1):
                self.tail[i].set_position(self.tail[i + 1].position.x,
                                          self.tail[i + 1].position.y
                                          )
        if length > 0:
            self.tail[self.length - 1].set_position(self.head.position.x,
                                                    self.head.position.y
                                                    )

    def show(self):
        '''
        Shows the Snake's head and tail nodes on screen.
        '''        
        
        self.head.update()
        for node in self.tail:
            node.show()
        self.head.show()
        

