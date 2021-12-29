class Settings:
    """A class to store all settings for game."""

    def __init__(self):
        """Initialise game's static settings"""
        #screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_colour = (0, 0, 0)

        #ship settings
        self.ship_limit = 3

        #Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colour = (255, 255, 255)
        self.bullets_allowed = 10

        #Alien settings
        self.fleet_drop_speed = 50

        #How quickly the game speeds up
        self.speedup_scale = 1.1

        #How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialise settings that change throughout the game."""
        self.ship_speed = 8.0
        self.bullet_speed = 8
        self.alien_speed = 3.0

        #fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)