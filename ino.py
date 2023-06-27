import pygame

class Ino(pygame.sprite.Sprite):
    """one invader class"""

    def __init__(self, screen):
        """initialising and start position"""
        super(Ino, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/ino.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """imaging ino on the screen"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ino movements"""
        self.y += 0.1
        self.rect.y = self.y