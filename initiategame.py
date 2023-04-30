# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:23:01 2023

@author: theob
"""
import pygame

from playercontrol import Player as Playerclass

from floorcontrol import Floor
from guncontrol import gunClass
from collision import collision





class initiateClass:
    def __init__(self):
        self.surface = pygame.display.get_surface()
        
        self.playergroup = pygame.sprite.Group()
        
        self.player = Playerclass(30,0,0,0,self)

        self.gun = gunClass(0,0,0,0,self)
        
        self.playergroup.add(self.player)
        self.playergroup.add(self.gun)

        
        self.floorgroup = pygame.sprite.Group()
        """for x in range(0,10):
            temp = Floor(0,0)
            temp.position = (x*80,self.surface.get_height()-temp.image.get_height()-60)
            self.floorgroup.add(temp)
            if x == 5:
                temp.kill()"""
        f1 = Floor(0,0)
        f1.position = (0,self.surface.get_height()-f1.image.get_height()-60)
        
        f2 = Floor(0,0)
        f2.position = (200,self.surface.get_height()-f1.image.get_height()-156)
        self.floorgroup.add(f1)
        self.floorgroup.add(f2)
    def spritelist(self):
        return self.floorgroup
        
    

        