import pygame

class Gun():

    def __init__(self, screen):
        """Gun initialisation"""

        self.screen = screen
        self.image = pygame.image.load('images/skate_invader_gun.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def gun_output(self):
        """Gun -maging"""
        self.screen.blit(self.image,self.rect)
