# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:33:58 2023

@author: theob
"""

import pygame
#from initiategame import initiateClass
#from playercontrol import Player as Playerclass
#initiate = initiateClass()



class collision:
   
    def collidecheck(subject,subject2):
        gravity =  subject.surface.get_height()/27
        
        hit = False
        

        for x in subject2:  
            if subject.rect.colliderect(x.rect) == True:
                hit = True
                subject3 = x    
                
        if hit == True:
            
            if subject.jumping == False:
                if subject.velocity[1] > 0:
                    subject.onground = True
                    subject.velocity = (subject.velocity[0],subject.velocity[1]-gravity)
                    if subject.rect.bottom >= subject3.rect.top:
                        subject.position = (subject.position[0], subject.position[1] - (subject.rect.bottom-subject3.rect.top)+5)
                        subject.velocity = (subject.velocity[0],0)
        else:
            subject.onground = False
        
            

        return subject.position,subject.velocity,subject.onground

    