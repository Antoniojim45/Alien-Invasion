# Import pygame for basic functions.
# Import sprites for group objects.
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """ A class that represents the ship. 

    The ship is the main object that the player controlls. sprite is inhereted 
    for the score board to keep track of. starts by setting the ship at the bottom
    center.

    Parameters
    -----------
    screen: obj
        screen is an object that holds all the properties of the game screen.

    ai_settings: obj
        ai_settings holds all the values used to define the games parameters.
    
    Methods
    --------
    update():
        moves the ship from left to right. 
    
    center_ship():
        center the ship to the bottom center of the screen. 
    
    blitme():
        draws the ship in the current location. 
    
    """
    def __init__(self, screen, ai_settings):
        """
        Parameters:
            screen: obj
                screen is an object that holds all the properties of the game screen.
        
            ai_settings: obj
                ai_settings holds all the values used to define the games parameters.

        """
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('image/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # store a decimal value for the ships center
        self.center = float(self.rect.centerx)

        # Movement Flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ship's position based on the movement flag.

        if the flag is true and the right part of the ship rect, is less than
        the right edge of the screen.update the ships center value, not the rect.

        Parameters:
            None
        
        """
        # if the flag is true and the right part of the ship rect, is less than
        # the right edge of the screen.update the ships center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update the rect object from self.center.
        self.rect.centerx = self.center

    def center_ship(self):
        """Center the ship on the screen.

        Parameters:
            None
        """
        self.center = self.screen_rect.centerx

    def blitme(self):
        """Draw the ship at its current location
        
        Parameters:
            None
        """
        self.screen.blit(self.image, self.rect)
