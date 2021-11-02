""" alien.py

In the Alien file, the alien is created as a Sprite. There are 
additional functions such as checking the edges of the game, to update
the aliens, and to draw the alien. 

Name: Antonio Jimenez
Version: 1
"""
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet.
    
    The sprite class is inherited and the initialization of a 
    single alien is executed. Initialize the alien and set its 
    starting position.

    Attributes
    -----------
    ai_settings: obj
        ai_settings holds all the values used to define the games parameters.
        
    screen: obj
        screen is an object that holds all the properties of the game screen.

    Methods
    --------
    check_edges()
        checks if the aliens have reached the edge of the screen.
    
    update()
        changes the position of the alien.
    
    blitme()
        draws the alien on the screen at its current position. 

    """

    def __init__(self, ai_settings, screen):
        """
        Parameters
        -----------
        ai_settings: obj
            ai_settings holds all the values used to define the games parameters.

        screen: obj
            screen is an object that holds all the properties of the game screen.
        """
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # load the alien image and set its rect attribute.
        self.image = pygame.image.load('image/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact positon.
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return true if alien is at edge of the screen.
        
        Parameters
        -----------
        None
        """
        # get the screen object and place it in a variable.
        screen_rect = self.screen.get_rect()
        # if the right side of the alien is beyond the boundary of the screen then return true.
        if self.rect.right >= screen_rect.right:
            return True
        # if the left side of the alien is beyond the boundaries of the alien then return true.
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left.

        Parameters
        -----------
        None
        """
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x

    def blitme(self):
        """Draw the alien at its current location.

        Parameters
        -----------
        None
        """
        self.screen.blit(self.image, self.rect)
