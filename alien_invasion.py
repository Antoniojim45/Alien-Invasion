""" Alien Invasion.py

This is the main file of the game. 

"""
###################
# Project: Alien invasion
# File Name: alien_invasion.py
# Name: Antonio Jimenez
# Version: 1
#
# Description:
# The main file, alien_invasion.py, creates a number of important objects used throughout the game:
# the settings are stored in ai_settings, the main display surface is stored in screen, and a ship
# instance is created in this file as well. Also stored in alien_invasion.py is the main loop of
# the game, which is a while loop that calls check_events(), ship.update(), and update_screen().
# alien_invasion.py is the only file you need to run when you want to play Alien Invasion.
# The other files —settings.py, game_functions.py, ship.py— contain code that is imported,
# directly or indirectly, into this file.
###################
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
    # Initailize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    # create a window with the tuple param
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make a Play Button.
    play_button = Button(ai_settings, screen, "Play")

    # make a ship object
    ship = Ship(screen, ai_settings)

    # Make a group to store bullets in.
    bullets = Group()

    # Set the background colors (R, G, B).
    bg_colors = (230, 230, 230)

    # Make an alien group
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
