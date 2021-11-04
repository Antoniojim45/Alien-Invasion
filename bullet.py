# Import pygame for basic functions.
# Import sprites for group objects.
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """A class to manage bullets fired from the ship

    the bullets initilizes at the current positon the ship is in.
    
    Parameters
    -----------
    ai_settings: obj
        ai_settings holds all the values used to define the games parameters.

    screen: obj
        screen is an object that holds all the properties of the game screen.

    ship: obj
        ship is the main object in controll and features moving left, right, and 
        shooting.
    
    Methods
    --------
    update():
        move the bullets in the y direction.
    
    draw_bullets():
        draw the bullets on the screen. 

    """

    def __init__(self, ai_settings, screen, ship):
        """
        Parameters
        -----------
        ai_settings: obj

        screen: obj

        ship: obj

        """
        # the super method calls Sprite.__init__()
        super(Bullet, self).__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # store the bullet's postion as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """move the bullet up the screen"""
        # Update the decimal position of the bullets
        self.y -= self.speed_factor
        # Update the bullet to the screen.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet on the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
