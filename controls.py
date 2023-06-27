import pygame
import sys

def events(gun):
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
        elif event.type == pygame.KEYUP:
            #right button
            if event.key == pygame.K_RIGHT:
                gun.mright = False
                #left button
            elif event.key == pygame.K_LEFT:
                gun.mleft = False
