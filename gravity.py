# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:39:06 2023

@author: theob
"""
import pygame



class Gravity:
    def __init__ (self):
        self.surface = pygame.display.get_surface()
        #sets gravity value, consistent across resolution
        self.gravity =  self.surface.get_height()/27
        #27
        
        #temporary
        global height
        height = 620
    
    def gravitytick(self,subject):
        #pygame.draw.rect(subject.surface,'green',(0,height,800,2))
        #applies gravity value each tick
        subject.velocity = (subject.velocity[0],subject.velocity[1]+self.gravity)
        
        #caps gravity speed for subject
        if subject.velocity[1] > self.gravity:
            subject.velocity = (subject.velocity[0],self.gravity)
        
        
        #checks if meeting floor
        #position is set to top-left, corrects this to be at the bottom of sprite
        if subject.position[1]+subject.image.get_height() < height:
            subject.onground = False
        else:
            subject.onground = True
            #honestly don't know why this is needed but it works
            subject.velocity = (subject.velocity[0],subject.velocity[1]-self.gravity)
            #snaps player position to be ontop of floor
            subject.position = (subject.position[0],height-subject.image.get_height())

        return subject.velocity, subject.onground
    
    
    