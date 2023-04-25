# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 13:57:33 2023

@author: theob
"""

import pygame

class spritesheet(object):
    def __init__(self,filename,surface):
        self.sheet = pygame.image.load(filename).convert()
    # Load a specific image from a specific rectangle
    def image_at(self, rectangle):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        image.set_colorkey((0,0,0), pygame.RLEACCEL)
        return image
    
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, numberofpos):
        "Loads multiple images, supply a list of coordinates" 
        rects = list(rects)
        if numberofpos > 1:
            rects = [rects]
            for x in range(0,numberofpos-1):
                print(rects[0][1]+(rects[0][3]*(x+1)))
                rects.append([rects[x-1][0],rects[x-1][1]+(rects[x-1][3]*(x+1)),rects[x-1][2],rects[x-1][3]])
                

        
        #print(rects)
        #print(numberofpos)
        table = []
        for x in rects:
            table.append(self.image_at(x))
        return table
            
    # Load a whole strip of images
    
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
