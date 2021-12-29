import pygame
import abc

class Drawable(metaclass = abc.ABCMeta):
    def __init__(self,x=0,y=0,visible=True):
        self.__x=x
        self.__y=y
        self.__visible=visible
        
    def getLoc(self):
        return (self.__x, self.__y)
        
    def setLoc(self,p):
        self.__x = p[0]
        self.__y = p[1]
    
    @abc.abstractmethod
    def draw(self,surface):
        pass

    @abc.abstractmethod
    def get_rect(self):
        pass
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def getVisible(self):
        return self.__visible
    
    def setX(self,x):
        self.__x = x
        
    def setY(self,y):
        self.__y = y
        
    def setVisible(self,bool):
        self.__visible