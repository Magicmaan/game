# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:15:22 2023

@author: theob
"""
import pygame
import spritesheet

class gunClass(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y,initiateClass):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.initiateClass = initiateClass

        self.position = (x,y)
        
        ss = spritesheet.spritesheet('textures/player/portal gun.png',self.surface)
        self.gunsprites = (ss.images_at((0, 0, 11, 6),2))
        self.image = self.gunsprites[0]
        self.rect = self.image.get_rect()

        self.spritemultiplier = 4
        self.spritesizemod = (self.surface.get_size())

        x = self.spritesizemod[0] / self.image.get_width()
        y = self.spritesizemod[1] / self.image.get_height()

        x = round(self.spritesizemod[0] / x) * self.spritemultiplier
        y = round(self.spritesizemod[1] / y) * self.spritemultiplier

        # if sprite moving left, flips sprite

        self.image = pygame.transform.scale(self.image, (x, y))

    def update(self):
        self.position = self.initiateClass.player.position
        self.position = (self.position[0]+5,self.position[1]+35)


        self.rect = pygame.Rect(self.position[0], self.position[1], self.image.get_width(), self.image.get_height())

    def imageupdate(self,direction,flip,spritestate):
        self.image = pygame.transform.flip(self.image, flip, 0)

    def draw(self):
        self.surface.blit(self.image, self.position)