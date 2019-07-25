# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 21:03:58 2019
    Class will manage the behavior of the player ship!
@author: kevin.armando.diaz
"""
import pygame


class Ship:

    def __init__(self, screen, ai_settings):
        """init method of the class"""
        self.screen = screen
        self.ai_settings = ai_settings
        # Loading ship image and gets its rectangle
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Each ship will start at the bottom center of the screen
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Attrib to Moving the ship to the right
        self.moving_right = False
        # Attrib to Moving the ship to the left
        self.moving_left = False
        self.center = float(self.rect.centerx)

    def blitme(self):
        """Draw the ship in the current location"""
        self.screen.blit(self.image, self.rect)

    def update(self) -> object:
        """Update the ship's position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Update the rect center
        self.rect.centerx = self.center
