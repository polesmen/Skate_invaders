import pygame
import sys
from bullet import Bullet

def events(screen, gun, bullets):
    """event handling"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            #right button
            if event.key == pygame.K_RIGHT:
                gun.mright = True
                # left button
            elif event.key == pygame.K_LEFT:
                gun.mleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            #right button
            if event.key == pygame.K_RIGHT:
                gun.mright = False
                #left button
            elif event.key == pygame.K_LEFT:
                gun.mleft = False

def update(bg_color, screen, gun, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.gun_output()
    pygame.display.flip()

def update_bullets(bullets):
    """bulet position update """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullet.remove(bullets)
