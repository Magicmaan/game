# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:39:06 2023

@author: theob
"""

import pygame
import random
import time
from playercontrol import Player as Playerclass


pygame.init()
pygame.font.init()
pygame.mixer.init()
random.seed(1111)
pygame.display.set_caption("Space invaders but its horizontal with Portal assets :| turn sound on")
clock = pygame.time.Clock()

class game:
    def refresh():
        pygame.display.flip()
        pygame.display.update()
    
# Set the window size
window_size = (1000, 600)
window = pygame.display.set_mode(window_size)
window.fill("white")

print(window.get_height())
player = Playerclass(50,50,0,0,window)

while True:
    # Handle events
    window.fill("white")
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.playervelocity(1,0)   
    if keys[pygame.K_a]:
        player.playervelocity(-1,0)
    if keys[pygame.K_SPACE]:
        player.playervelocity(0,-0.7)

    
    #player.update()
    player.update()
    player.draw()
    
    clockfps = 18
    #sets framerate
    ft = clock.tick(clockfps) / 1000
    
    
    pygame.display.flip()
    
    
    #game.refresh()
    
    
    
    
    