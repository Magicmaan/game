# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:15:22 2023

@author: theob
"""
import pygame
import spritesheet

class gunClass(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.position = (x,y)
        
        ss = spritesheet.spritesheet('textures/player/playersprites.png',self.surface)
        self.gunsprite = ss.image_at