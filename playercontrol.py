# -*- coding: utf-8 -*-
import spritesheet
import pygame
import math
from game import gameClass
#from gravity import Gravity
from collision import collision



class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y,initiateClass):
        super().__init__()
        self.surface = pygame.display.get_surface()
        self.initiateClass = initiateClass
        
        
        #sprite assignment
        ss = spritesheet.spritesheet('textures/player/playersprites.png',self.surface)
        self.idlesprites = (ss.images_at((0, 0, 11, 19),3))
        self.forwardsprites = (ss.images_at((11, 0, 11, 19),3))
        self.jumpsprites = (ss.images_at((22, 0, 11, 21),2))
        self.idlecrouchsprites = (ss.image_at((34, 0, 11, 15)))
        self.forwardcrouchsprites = (ss.image_at((34, 15, 11, 15)))
        self.spritemultiplier = 4
        self.spritesizemod = (self.surface.get_size())
        
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        #loads player image and scales
        
        self.image = self.idlesprites[0]
        self.direction = self.idlesprites
        self.spritestate = 0   
        self.onground = True
        self.crouching = False

        #self.Gravity = Gravity()
        #self.collision = collision()
        self.flip = 0
        
        #acceleration values
        self.movedecayaccelX = round(self.surface.get_width()/60)
        self.movedecayaccelY = round(self.surface.get_height()/10)
        #12
        self.movedecaymaxX = self.movedecayaccelX * 3
        self.movedecaymaxY = self.movedecayaccelX * 10
        
        self.movedecayeaseX = self.movedecayaccelX / 9
        
        
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)

    
    def image_update(self):
        
        #sets which sprite to use
        if self.velocity == (0,0): #idle
            self.direction = self.idlesprites
        if self.velocity[0] > 0: #right
            self.direction = self.forwardsprites
            self.flip = 0
        if self.velocity[0] < 0: #left flipped
            self.direction = self.forwardsprites
            self.flip = 1
        if self.velocity[1] < 0: #jump
            self.direction = self.jumpsprites
        if self.crouching == True: #crouch
            self.direction = self.idlecrouchsprites
        
        #animation tick
        if type(self.direction) == list:
            if self.spritestate+1 > len(self.direction): 
                self.spritestate = 0
            self.image = self.direction[self.spritestate]
        else:
            self.image = self.direction
        
        
        #sets scale of sprite, so its consistent across resolutions
        x = self.spritesizemod[0]/self.image.get_width()
        y = self.spritesizemod[1]/self.image.get_height()

        x = round(self.spritesizemod[0]/x)*self.spritemultiplier
        y = round(self.spritesizemod[1]/y)*self.spritemultiplier


        #if sprite moving left, flips sprite
        self.image = pygame.transform.flip(self.image,self.flip,0)
        self.image = pygame.transform.scale(self.image,(x,y))
        
        
        
        #animation control, sets when to change sprite every frame
        if self.direction == self.idlesprites:
            if (self.tick % 5) == 0:
                self.spritestate += 1
        elif self.direction == self.forwardsprites:
            if (self.tick % 2) == 0:
                self.spritestate += 1
        else:
            self.spritestate += 1
        
        #updates rect to match sprite
        self.rect = pygame.Rect(self.position[0], self.position[1], self.image.get_width(),self.image.get_height())
        #self.rect.bottom = self.position[1]+self.image.get_height()
        

        
        
        
        
            
    
    def image_get(self):
        return self.imageraw
    
    def update(self): 
        global collideoutput
        #updates position and collision
        self.tick = gameClass.gettick()
        
        
        
        Player.velocitylogic(self)
        Player.image_update(self)
        #gravity check
        
        #self.collision.collidecheck()
        
        
        #collideoutput = collision.collidecheck(self,self.initiateClass.floorgroup)
        #self.velocity,self.position,self.onground = self.Gravity.gravityticknew(self,collideoutput)
        
        
        
        #print(self.velocity)
        
        
        #sets position
        
        
        
        self.crouching = False
        
        self.mask = pygame.mask.from_surface(self.image)
        
        self.gravity =  self.surface.get_height()/27
        subject2 = self.initiateClass.floorgroup

        
        
        self.velocity = (self.velocity[0],self.velocity[1]+self.gravity)
        if self.velocity[1] > self.gravity:
            self.velocity = (self.velocity[0],self.gravity)
        
        """hit = False
        
        
        for x in subject2:  
            if self.rect.colliderect(x.rect) == True:
                hit = True
                bean = x    
                
        if hit == True:
            
            #self.velocity = (0,self.velocity[1])
            
            if self.jumping == False:
                if self.velocity[1] > 0:
                    self.onground = True
                    self.velocity = (self.velocity[0],self.velocity[1]-self.gravity)
                    if self.rect.bottom >= bean.rect.top+1:
                        self.position = (self.position[0], self.position[1] - (self.rect.bottom-bean.rect.top)+1)
                        self.velocity = (self.velocity[0],0)
            
            

        else:
            self.onground = False"""
                        #self.position = (self.position[0],x.rect.top-(self.rect.bottom-x.rect.top))
        
        collision.collidecheck(self,self.initiateClass.floorgroup)


        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1]) 
        self.jumping = False
        
                
        
        
        
        
        
        
        
        
        #print(self.position)
       #print(self.velocity)
        
        
        
        

        

    def draw(self):
        #blits image to screen
        self.surface.blit(self.image, self.position)
        
    
    def playervelocity(self,movedecayX, movedecayY):
        #jump movement, only if on ground
        if movedecayY != 0 and self.onground == True:
            self.velocity = (self.velocity[0], self.velocity[1] + movedecayY*self.movedecayaccelY)   
            self.jumping == True
        else:
            self.jumping == False
            
        #crouching check
        if movedecayY > 0:
            self.crouching = True
        else:
            self.crouching = False
        
        #if on ground, max acceleration, less if in air
        if self.onground == True:
            self.velocity = (self.velocity[0] + movedecayX*self.movedecayaccelX, self.velocity[1])
        else:
            self.velocity = (self.velocity[0] + movedecayX*(self.movedecayaccelX/1.5), self.velocity[1])
        
    def velocitylogic(self):
        #movementX decay logic
        #rounds to max speed if exceeds
        if self.velocity[0] > self.movedecaymaxX: 
            self.velocity = (self.movedecaymaxX, self.velocity[1])
        if self.velocity[0] < -abs(self.movedecaymaxX):
            self.velocity = (-abs(self.movedecaymaxX), self.velocity[1])
            
        #decay movement rate, seperate value for air time
        if self.onground == True:
            
            self.velocity = (self.velocity[0]/self.movedecayeaseX, self.velocity[1])
        else:
            self.velocity = (self.velocity[0]/(self.movedecayeaseX/1.2), self.velocity[1])


        #prevents X movement if crouching
        if self.crouching == True:
            if self.onground == True:
                self.velocity = (0,self.velocity[1])
            else:
                self.velocity = (self.velocity[0]/2,self.velocity[1])
        
        #floors value if near 1
        if math.isclose(self.velocity[0],0,abs_tol = 1.0): 
            self.velocity = (0,self.velocity[1])
        
        
        
