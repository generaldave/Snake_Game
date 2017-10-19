'''
David Fuller

Constants file - File contains application constants.

10-15-2017
'''

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
vector = namedtuple('vector', ['x', 'y'])
color = namedtuple('color', ['red', 'green', 'blue'])
resolution = namedtuple('resolution', ['width', 'height'])

white = color(red = 255, green = 255, blue = 255)
black = color(red = 0, green = 0, blue = 0)
pink = color(red = 255, green = 0, blue = 100)

grid_scale = 20

class Key(object):
    up = 273
    down = 274
    left = 276
    right = 275
