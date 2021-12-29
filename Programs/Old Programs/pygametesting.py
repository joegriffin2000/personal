import pygame
import abc

pygame.init()
width = 400
height = 300
surface = pygame.display.set_mode((width,height))
pygame.display.set_caption('Hello World!')

while True:
    for event in pygame.event.get():
        pygame.draw.line(surface,(255,255,255),(0,0),(width,height),6)
        if (event.type == pygame.QUIT) or (event.type ==
            pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
    pygame.display.update()

class Drawable(metaclass = abc.ABCMeta):
    def __init__(self,x=0,y=0):
        self.__x = x
        self.__y = y
        
    def getLocation(self):
        return (self.__x,self.__y)
    
    def setLocation(self,x=0,y=0):
        self.__x = x
        self.__y = y
    
    