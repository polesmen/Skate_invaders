import pygame
import sys
from bullet import Bullet
from ino import Ino

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

def update(bg_color, screen, gun, inos, bullets):
    screen.fill(bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.gun_output()
    inos.draw(screen)
    pygame.display.flip()

def update_bullets(bullets):
    """bulet position update """
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullet.remove(bullets)

def update_inos(inos):
    """update position of inos"""
    inos.update()

def create_army(screen, inos):
    """army creating"""
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)
    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 4):
        """здесь можно добавить уровень сложности увеличивая или уменьшая списо к"""
        for ino_number in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + (ino_width * ino_number)
            ino.y = ino_height + (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)