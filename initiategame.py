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
        self.allsprite = pygame.sprite.Group()
        self.allsprite.add(self.player)
        
        
        self.playergroup.add(self.player)
        self.playergroup = self.player.image.get_rect()
        
        
        floor = Floor()
        self.floorgroup = floor.floorgroupsetup()
        
        return
    
    def update(self):
        self.playergroup = self.player.image.get_rect()
        self.floorgroup = self.floorgroup.image.get_rect()
        