from Drawable import *
import pygame
import math

class Ball(Drawable):
    def __init__(self,x,y,visible=True):
        super().__init__(x,y,visible)
        self.__xv = 0
        self.__yv = 0 
        
    def draw(self,surface):
        if self.getVisible() == True:
            pygame.draw.circle(surface,(255,0,0),(int(self.getX()-10),int(self.getY()-10)),10)
    
    def get_rect(self):
        pass
    
    def getxv(self):
        return self.__xy
    def getyv(self):
        return self.__yv
    def setxv(self,xv):
        self.__xy = xv
    def setyv(self,yv):
        self.__yv = yv
    
    def fly(self,dt=0.1,g=6.67,R=0.7,eta=0.5):
        x = self.getX() + dt * self.__xv
        y = self.getY() - dt * self.__yv
        
        self.setX(x)
        self.setY(y)
        
        if y > 400:
            self.__yv = -R * self.__yv
            self.__xv = eta * self.__xv
        else:
            yv = self.__yv - g * dt
        
        
        