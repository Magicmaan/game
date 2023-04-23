# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:39:06 2023

@author: theob
"""
import pygame



class Gravity:
    def __init__ (self,surface):
        self.surface = surface
        self.gravity = self.surface.get_height()/24
        print(self.surface.get_height()/24)
    
    def gravitytick(self,subject):
        subject.velocity = (subject.velocity[0],subject.velocity[1]+self.gravity)
        if subject.velocity[1] > self.gravity:
            subject.velocity = (subject.velocity[0],self.gravity)
        
        
        if subject.onground == True:
            subject.velocity = (subject.velocity[0],subject.velocity[1]-self.gravity)
            
        if subject.position[1] <= 380:
            subject.onground = False
        else:
            subject.onground = True
        
        return subject.velocity, subject.onground
    
    
    