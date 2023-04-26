# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:23:01 2023

@author: theob
"""
import pygame

from playercontrol import Player as Playerclass
from floorcontrol import Floor


class initiateClass:
    def __init__(self):
        surface = pygame.display.get_surface()
        self.playergroup = pygame.sprite.Group()

        
        self.player = Playerclass(0,0,0,0,surface)
        self.playergroup.add(self.player)
        
        
        
        self.floorgroup = pygame.sprite.Group()
        for x in range(0,10):
            temp = Floor(0,300)
            temp.position = (x*80,510)
            self.floorgroup.add(temp)
        
    

        