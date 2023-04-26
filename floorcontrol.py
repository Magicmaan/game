# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 20:45:34 2023

@author: theob
"""

import spritesheet
import pygame
from game import gameClass
spritesizemod = 10


class Floor(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.x = x
        self.y = y
        
        self.surface = pygame.display.get_surface()
        
        ss = spritesheet.spritesheet('textures/tiles/floor.png',self.surface)
        self.image = ss.image_at((0,0,288,96))
        #sets scale to be consistent no matter resolution
        #self.image = pygame.transform.scale(self.image,((self.surface.get_width()/10),(self.surface.get_width()/10)))
        
        #sets rectangle for collision
        self.rect = self.image.get_rect()
        
        self.rect.center = (x,y)

        #floorgroup init
        #self.floorgroup = pygame.sprite.Group()
        self.position = (x,y)
    
    """def floorgroupsetup(self):
        #gets width of screen, creates enough sprites to cover screen
        for x in range(0,round(self.surface.get_width()/self.image.get_width())):
            y = Floor(0,0) 
            #sets height to be bottom of screen, iterates for every new sprite
            #y.rect ORIGINAL = (abs(y.rect[0])*(x*2),self.surface.get_height()+(y.rect[1]*2))
            #y.position = (50,50)
            
            #y.rect = (abs(y.rect[0])*(x*2),self.surface.get_height()+(y.rect[1]*2))
            y.mask = pygame.mask.from_surface(y.image)
            self.floorgroup.add(y)
        return self.floorgroup"""
    
    def update(self):
        self.rect = pygame.Rect(self.position[0], self.position[1], self.image.get_width(),self.image.get_height())
        
        

