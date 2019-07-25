# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:35:33 2019
    Class Settings contains the configuration params needed for the alien invasion game
@author: kevin.armando.diaz
"""


class Settings:
    """A class that stores all settings for alien invasion"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen settings
        self.screen_width = 800
        self.screen_height = 500
        self.bg_color = (211, 211, 211)
        # ship's speed
        self.ship_speed_factor = 1.5
        # Bullet settings
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        # Alien settings
        self.alien_speed_factor = 1
        # Alien settings
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
