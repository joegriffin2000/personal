from Drawable import *
import pygame

class Block(Drawable):
    def __init__(self,x,y,visible=True):
        super().__init__(x,y,visible)
        self.__width = 20
        self.__height = 20
        
    def draw(self,surface):
        pygame.draw.rect(surface,(0,0,255),(self.getX()-self.__width,self.getY()-self.__height,self.__width,self.__height))
    
    def get_rect(self):
        pass
    
