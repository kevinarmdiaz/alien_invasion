# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:52:50 2019
    Creating a empty pygame 
@author: kevin.armando.diaz
"""

import game_functions as gfu
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship


def run_game():
    # Initialize game a create a empty screen object
    pygame.init()

    # Getting Settings with an instance of class Settings
    ai_settings = Settings()
    # Make a group to store bullets in.
    bullets = Group()
    # Make a group of aliens
    aliens = Group()

    # Applying screen settings
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Getting Ship drawing a ship at the bottom center of the screen
    ship = Ship(screen, ai_settings)
    # Create the fleet of aliens.
    gfu.create_fleet(ai_settings, screen, ship, aliens)
    # Start the main loop for the game.
    while True:
        # Watch for keyboard and mouse events.
        gfu.check_events(ai_settings, screen, ship, bullets)
        # Updating ship's position
        ship.update()
        gfu.update_bullets(aliens, bullets)
        gfu.update_aliens(ai_settings, aliens)
        # Updating the screen in each loop
        gfu.update_screen(ai_settings, screen, aliens, ship, bullets)


run_game()
