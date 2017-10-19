'''
David Fuller

App class: Initializes application

10-15-2017
'''

import pygame

from .Constants import background_color, screen_resolution, app_title, fps
from .game import Game

class App(object):
    '''
    Sets up and runs a Pygame application.
    '''
    
    def __init__(self, app_directory):
        '''
        App's init method.

        Stores application directory. Sets up the graphical user interface.
        Runs the applicaiton.

        Args:
            app_directory (str): Representation of application directory.
        '''
        
        self.app_directory = app_directory

        self.setup_GUI()

        self.run_app()

    def setup_GUI(self):
        '''
        Method sets up the graphical user interface.

        Initializes Pygame. Sets up the window size and title. Stores Pygame
        clock variable for setting frames per second.
        '''
        
        pygame.init()
        self.screen = pygame.display.set_mode(screen_resolution)
        pygame.display.set_caption(app_title)
        self.clock = pygame.time.Clock()

        self.game = Game(self.screen)

    def run_app(self):
        '''
        Runs Pygame application.
        '''
        
        running = True
        while running:
            for event in pygame.event.get():
                
                # Handle quit event
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    self.game.update(event.key)

            self.screen.fill(background_color)

            self.game.show()

            # Update Screen
            pygame.display.update()
            self.clock.tick(fps)            

        # Close app cleanly
        pygame.quit()
