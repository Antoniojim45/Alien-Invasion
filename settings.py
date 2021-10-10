##############################
# Project: Alien invasion
# File Name: setting.py
# Name: Antonio Jimenez
# Version: 1
#
# Description: The settings.py file contains the Settings class. This class only has an
# __init__() method, which initializes attributes controlling the game’s
# appearance and the ship’s speed.
##############################

class Settings():
    """A class to store all the setting for Alien Invasion."""

    # When the settings class is used, the __init__ function is automatically
    # executed with everything in the function.
    def __init__(self):
        """intitalize the game's static settings."""
        #Screen setting
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # ship setting
        self.ship_limit = 3

        # Bullets settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Alien Settings
        self.fleet_drop_speed = 5

        # How quickly the game speeds up
        self.speedup_scale = 1.1

        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initalize_dynamic_settings()

    def initalize_dynamic_settings(self):
        """Initialize speed settings that change thorughout the game."""
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.5

        # fleet_direction of 1 represent right; -1 represents left.
        self.fleet_direction = 1

        # Scoring, every hit of an alien is worth 50 points.
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        # the new alien points would be multiplied by the score scale.
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
