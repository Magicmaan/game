# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 19:39:06 2023

@author: theob
"""
import pygame

height = 300

class Gravity:
    def __init__ (self):
        self.surface = pygame.display.get_surface()
        #sets gravity value, consistent across resolution
        self.gravity =  self.surface.get_height()/27
    
        
        #temporary placeholder variable
        self.collisionbox = [self.surface.get_height(),0,0,self.surface.get_width()]
        
        
    
    
    def gravityticknew(self,subject,collideoutput):
        pygame.draw.rect(subject.surface,'green',(0,520,800,2))
        #pygame.draw.rect(subject.surface,'green',(0,height,800,2))
        #applies gravity value each tick
        subject.velocity = (subject.velocity[0],subject.velocity[1]+self.gravity)
        
        #caps gravity speed for subject
        if subject.velocity[1] > self.gravity:
            subject.velocity = (subject.velocity[0],self.gravity)
        
        
        #checks if meeting floor
        if collideoutput:
            subject.onground = True 
            #print(subject.rect.right)
            #print(collideoutput[0].rect.left)
            #look i don't know how this shit works, it just does ok
            if subject.velocity[1] == self.gravity:
                subject.velocity = (subject.velocity[0],0)
            if subject.rect.bottom >= collideoutput[0].rect.top-1:
                subject.position = (subject.position[0],(collideoutput[0].position[1]-subject.image.get_height())+1)
                #print("Top")
                #print("other")
            else:
                if subject.rect[0]+subject.rect[3] == collideoutput[0].rect[0]:
                    print("hit side")
                #subject.velocity = (0,subject.velocity[1])
        else:
            self.collisionbox = [self.surface.get_height(),0,0,self.surface.get_width()]
            subject.onground = False
        
        if subject.position[1] > self.surface.get_height():
            #print("hit")
            subject.position = (10,300)
        subject.position = (subject.position[0] + subject.velocity[0], subject.position[1] + subject.velocity[1]) 
        

        return subject.velocity, subject.position, subject.onground
    
    
    