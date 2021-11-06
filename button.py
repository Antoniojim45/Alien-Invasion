import pygame.font

class Button():
    """
    The button class holds basic methods and parameters of the start button.
    the button will show up in the start of the game. 

    Parameters
    -----------
    ai_settings: obj
        ai_settings holds all the values used to define the games parameters.

    screen: obj
        screen is an object that holds all the properties of the game screen.

    msg: str
        A string that will be placed on the button, "Play".

    Methods
    --------
    prep_msg(msg):
        places the string on the center of the button.
    
    draw_button():
        colors the button and blits the button into the game.

    """

    def __init__(self, ai_settings, screen, msg):
        """Initialize button attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Set the dimentions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)

        # the fot.SysFont allows us to create a fontt for the words used.
        # the None argument tells us that we will be using the default font
        # and 48 will be the size of the words
        self.font = pygame.font.SysFont(None, 48)


        # Build the buttons rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be preped only once.
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button.

        Parameters
        -----------
        msg: str
            A string that will be placed on the button, "Play".
        """
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        """Draw blank button and then draw the message
        
        Parameters
        -----------
        None
        """
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
