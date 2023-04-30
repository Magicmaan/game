# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 21:33:58 2023

@author: theob
"""

import pygame
#from initiategame import initiateClass
#from playercontrol import Player as Playerclass
#initiate = initiateClass()
colliding = False

surface = pygame.display.get_surface()



class collision:
   
    def collidecheck(subject,subject2):
        gravity = subject.surface.get_height() / 27
        gravitymax = subject.surface.get_height() / 22
        
        subject.velocity = (subject.velocity[0],subject.velocity[1]+gravity)
        if subject.velocity[1] > gravitymax:
            subject.velocity = (subject.velocity[0],gravitymax)
        
        hit = False
        global colliding
        colliding = 0



        if pygame.sprite.spritecollideany(subject,subject2) != None:
            for x in subject2:  

                #if subject.rect.colliderect(x.rect):


                    
                   
                    if subject.rect.clipline(x.rect.left,x.rect.top,x.rect.right,x.rect.top):
                        
                        pygame.draw.line(subject.surface,'green',(x.rect.left,x.rect.top),(x.rect.right,x.rect.top))

                        colliding += 1
                        if subject.velocity[1] > 0:
                            subject.velocity = (subject.velocity[0],0)
                        if subject.position[1] < x.rect.top+2:
                            subject.position = (subject.position[0],x.rect.top-subject.image.get_height()+1)
                        subject.onground = True
                    else:
                    
                        if subject.rect.clipline(x.rect.left-1,x.rect.top+3,x.rect.left-1,x.rect.bottom):
                            pygame.draw.line(subject.surface,'green',(x.rect.left-1,x.rect.top+3),(x.rect.left-1,x.rect.bottom))
                            if subject.velocity[0] > 0:
                                subject.velocity = (0,subject.velocity[1])
                            if subject.position[0]+subject.image.get_width() > x.rect.left:
                                subject.position = (subject.position[0]-(subject.rect.right-x.rect.left),subject.position[1])
                                #subject.velocity = (subject.velocity[0]-2,subject.velocity[1])
                        
    
                        if subject.rect.clipline(x.rect.right,x.rect.top+3,x.rect.right,x.rect.bottom):
                            pygame.draw.line(subject.surface,'green',(x.rect.right,x.rect.top+3),(x.rect.right,x.rect.bottom))
                            if subject.velocity[0] < 0:
                                subject.velocity = (0,subject.velocity[1])


        if colliding > 0:
            subject.onground = True
        else:
            subject.onground = False



        return subject.position,subject.velocity,subject.onground

    