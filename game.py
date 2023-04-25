# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 17:09:41 2023

@author: theob
"""
import pygame

framerate = 24
clock = pygame.time.Clock()
global tick
tick = 0

class gameClass:
    def gametime():
        global tick
        clock.tick(framerate) / 1000
        tick += 1
        
        #checks if exit button is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        
        return tick
    
    def gettick():
        return tick