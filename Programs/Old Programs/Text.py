from Drawable import *
import pygame

class Text(Drawable):
    def __init__(self,x,y,visible=True,color=(0,0,0)):
        super().__init__(x,y,visible)
        
    def draw(self,surface):
        if self.getVisible() == True:
            pass
    
    def get_rect(self):
        pass