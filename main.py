# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:39:06 2023

@author: theob
"""

import pygame
import random
from playercontrol import Player as Playerclass
from floorcontrol import Floor
from game import gameClass
from initiategame import initiateClass
from collision import collision


pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.display.set_caption("Space invaders but its horizontal with Portal assets :| turn sound on")




WindowX = 800
WindowY = round(WindowX / 1.333)
print(WindowY)
# Set the window size
window_size = (WindowX, WindowY)
window = pygame.display.set_mode(window_size)
tick = 0


    
initiate = initiateClass()
    

player = initiate.player
floorgroup = initiate.floorgroup
playergroup = initiate.playergroup




while True:
    window.fill("white")
    
    # Handle events
    
   
    
    
    #key inputs of player, passes in velocity multiply amount
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
        player.playervelocity(1,0)   
    if keys[pygame.K_a]:
        player.playervelocity(-1,0)
    if keys[pygame.K_SPACE]:
        player.playervelocity(0,-1)
    if keys[pygame.K_LCTRL]:
        player.playervelocity(0,1)

    #updates floor and player
    
    floorgroup.update()
    floorgroup.draw(window)
    
    
    
    playergroup.update()
    playergroup.draw(window)
    

    
    
    
    #updates and displays monitor
    pygame.display.update()
    pygame.display.flip()
    #game.refresh()
    tick = gameClass.gametime()

    
    
    