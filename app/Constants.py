'''
David Fuller

Constants file - File contains application constants.

10-15-2017
'''

from collections import namedtuple

point = namedtuple('point', ['x', 'y'])
color = namedtuple('color', ['red', 'green', 'blue'])
resolution = namedtuple('resolution', ['width', 'height'])

background_color = color(red = 127, green = 127, blue = 127)
screen_resolution = resolution(width = 600, height = 600)

app_title = "Snake Classic"
fps = 10
