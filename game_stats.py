class GameStats():
    """Track statistics for Alien Invasion
    
    Parameters
    ----------
    ai_settings: obj
        ai_settings holds all the values used to define the games parameters.

    Methods
    --------
    reset_stats():
        resets the statistics for the game, the ship limit, scoreboard, ect. 
    """

    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()

        # Start Alien Invasion in an inactive state.
        self.game_active = False

        # High score should never be reset.
        self.high_score = 0

    def reset_stats(self):
        """Initialize statistics that can change during the game.
        
        Parameters
        ----------
        None
        """
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
