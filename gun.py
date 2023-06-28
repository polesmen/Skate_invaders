import pygame
from pygame.sprite import Sprite
from stats import Stats

class Gun(Sprite):

    def __init__(self, screen):
        """Gun initialisation"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/skate_invader_gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.center = float(self.rect.centerx)
        self.rect.bottom = self.screen_rect.bottom
        self.mright = False
        self.mleft = False


    def gun_output(self):
        """Gun imaging"""
        self.screen.blit(self.image, self.rect)

    def update_gun(self):
        """gun position update"""
        if self.mright and self.rect.right < self.screen_rect.right:
            self.center += 1.5
        if self.mleft and self.rect.left > 0:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        """placing gun at center of screen"""
        self.center = self.screen_rect.centerx

