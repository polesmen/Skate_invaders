import pygame

class Bullet(pygame.sprite.Sprite):

    def __init__(self, screen, gun):
        """bullet initialisation in gun position"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 4, 12)
        self.color = 43, 237, 211
        self.speed = 1
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)


    def update(self):
        """bullet moving"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """bullet drawing"""
        pygame.draw.rect(self.screen, self.color, self.rect)