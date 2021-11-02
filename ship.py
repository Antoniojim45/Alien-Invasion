"""ship.py

The ship.py file contains the Ship class. Ship has an __init__() method, an
update() method to manage the ship’s position, and a blitme() method
to draw the ship to the screen. The actual image of the ship is stored in
ship.bmp, which is in the images folder.

Author: Antonio Jimenez
Version: 1

"""
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """
    
    
    """
    # In the initialization section of the ship, the screen object is passed
    # and is placed in self.screen. the ship image is loaded and turned to
    # a rectangle. Get the screen rectangle and get rect. then center the
    # ship relative to the screen.
    def __init__(self, screen, ai_settings):
        """Initialize the ship and set its starting position."""
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
        """Update the ship's position based on the movement flag."""
        # if the flag is true and the right part of the ship rect, is less than
        # the right edge of the screen.update the ships center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor

        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        #update the rect object from self.center.
        self.rect.centerx = self.center

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx


    # draw the image
    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)
