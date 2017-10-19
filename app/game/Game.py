'''
David Fuller

Game class - Handles the Snake game.

10-15-2017
'''

import math

from .Constants import Key
from .Snake import Snake
from .Food import Food


class Game(object):
    '''
    Sets up a Game class
    '''
    
    def __init__(self, screen):
        '''
        Game's init method.

        Initializes a Snake and Food object.

        Args:
            screen (pygame.display): Screen object to draw Snake and Food on.
        '''
        
        self.snake = Snake(screen)
        self.food = Food(screen)
        self.playing = True
        self.frame_one = True

    def update(self, key):
        '''
        Changes direction of Snake according to which key was pressed.
        '''
        
        if key == Key.up:
            self.snake.set_direction(0, -1)
        elif key == Key.down:
            self.snake.set_direction(0, 1)
        elif key == Key.left:
            self.snake.set_direction(-1, 0)
        elif key == Key.right:
            self.snake.set_direction(1, 0)

    def find_distance(self, x_one, y_one, x_two, y_two):
        '''
        Finds the distance between two points on a graph.

        Args:
            x_one (int): x coordinate of first point
            y_one (int): y coordinate of first point
            x_two (int): x coordinate of second point
            y_two (int): yx coordinate of second point

        Returns:
            Float: math.sqrt((x_two - x_one)^2 + (y_two - y_one)^2)
        '''
        
        operand_one = math.pow(x_two - x_one, 2)
        operand_two = math.pow(y_two - y_one, 2)
        
        return math.sqrt(operand_one + operand_two)

    def game_over(self):
        '''
        Decides whether the Snake has died or not. Sets self.playing to False
        if so. Otherwise, do nothing.
        '''

        head = self.snake.head
        tail = self.snake.tail
        for node in tail:
            distance = self.find_distance(head.position.x, head.position.y,
                                          node.position.x, node.position.y)
            if distance < 20:
                self.snake.length = 0
                self.snake.tail = []

    def show(self):
        '''
        Updates the Snake's tail and shows Snake and Food objects.
        '''

        if not self.frame_one:
            self.game_over()
        if self.frame_one:
            self.frame_one = False
        self.snake.update()
        self.snake.show()
        if self.snake.eat(self.food) == True:
            self.frame_one = True
            self.food.pick_location()
        self.food.show()
