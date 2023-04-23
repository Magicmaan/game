# -*- coding: utf-8 -*-
import pygame
import math
from gravity import Gravity












idle = ['player/idle/1.png','player/idle/2.png']
forward = ['player/playerforward.png','player/playerforward.png']
up = ['player/playerup.png','player/playerforward.png']
down = ['player/playerdown.png','player/playerforward.png']




class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, velocity_x, velocity_y, surface):
        super().__init__()
        self.position = (x, y)
        self.velocity = (velocity_x, velocity_y)
        #loads player image and scales
        self.image = pygame.image.load(idle[0])
        self.rect = self.image.get_rect()
        self.onground = True
        self.surface = surface
        self.Gravity = Gravity(self.surface)
        self.flip = 0
        self.moving = False
        
        self.movedecayaccelX = self.surface.get_height()/24
        self.movedecayaccelY = self.surface.get_height()/24
        
        self.movedecaymaxX = self.movedecayaccelX * 10
        self.movedecaymaxY = self.movedecayaccelX * 10
        
        self.movedecayeaseX = self.movedecayaccelX / 13
        
        self.spritestate = 0        
        
    
    def image_update(self):
        if self.spritestate+1 > len(self.direction): 
            self.spritestate = 0
        print(self.spritestate)
        print(self.direction[self.spritestate])
        self.image = pygame.image.load(self.direction[self.spritestate])
        self.image = pygame.transform.flip(self.image,self.flip,0)
        self.image = pygame.transform.scale(self.image,(51,75))

        print(self.spritestate)
        self.spritestate = self.spritestate + 1
        
            
    
    def image_get(self):
        return self.imageraw
    
    def update(self): 
        #updates position and collision
        self.rect = self.image.get_rect()
        
        
        #movementX decay logic, divides by half per frame then updates image to correct one
        print(self.velocity)
        if self.velocity[0] > self.movedecaymaxX: 
            self.velocity = (self.movedecaymaxX, self.velocity[1])
        

        self.velocity = (self.velocity[0]/self.movedecayeaseX, self.velocity[1])
        
        if math.isclose(self.velocity[0],0,abs_tol = 1.0): 
            self.velocity = (0,self.velocity[1])
        print(self.velocity)
        
        if self.velocity == (0,0): #idle
            self.direction = idle
        if self.velocity[0] > 0: #right
            self.direction = forward
            self.flip = 0
        if self.velocity[0] < 0: #left flipped
            self.direction = forward
            self.flip = 1
        if self.velocity[1] < 0: #up
            self.direction = up
        if self.velocity[1] > 0: #down
            self.direction = down
        

        Player.image_update(self)
        
        self.Gravity.gravitytick(self)
        self.position = (self.position[0] + self.velocity[0], self.position[1] + self.velocity[1])        
        

        

    def draw(self):
        self.surface.blit(self.image, self.position)
        
    
    def playervelocity(self,movedecayX, movedecayY):
        

        
        self.velocity = (self.velocity[0] + movedecayX*self.movedecayaccelX, self.velocity[1])
        
        if movedecayY != 0 and self.onground == True:
            self.velocity = (self.velocity[0], self.velocity[1] + movedecayY*self.movedecayaccelY)   
        
        
        
        
        
        
        
        
        
        
        
        
        
        
