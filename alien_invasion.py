""" Alien Invasion.py

This is the main file of the game. The only function in this file is run_game()
where the program creates the screen for the game with the specified parameters in
the settings. before the function is ran there are multiple functions that are imported.
There are a number of objects created so that the functions within them are utilized.
The main loop consist of different functions where the game is updated.the last command
is the run_game() command which tells pygame to run.

Project: Alien Invasion
Name: Antonio Jimenez
Version 1
"""
import pygame
import game_functions as gf
from settings import Settings
from pygame.sprite import Group
from ship import Ship
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():
    """
    The main function of alien invasion. pygame is initialized and the screen is
    created. There are multiple objects created which play specific roles in the game.
    The main loop updates the game for any changes made while playing.

    Parameters
    ------------
    none
    """
    # Initailize game and create a screen object.
    pygame.init()
    ai_settings = Settings() # Creates the settings object

    # create a window with the tuple param
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a Play Button by creating the play object.
    play_button = Button(ai_settings, screen, "Play")

    # make a ship object.
    ship = Ship(screen, ai_settings)

    # Make a group to store bullets in.
    bullets = Group()

    # Set the background colors (R, G, B).
    bg_colors = (230, 230, 230)

    # Make an alien group.
    aliens = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # Create an instance to store statistics.
    stats = GameStats(ai_settings)

    # Create an instance to store game statistics and create a scoreboard
    sb = Scoreboard(ai_settings, screen, stats)

    # Start the main loop of the game.
    while True:

        # from gf get check events and execute
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # run the ship update function so that the movement of the ship can
            # occur.
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, sb, ship, aliens, bullets)

        # from the gf execute update screen with the parameters.
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

# run the game
run_game()
