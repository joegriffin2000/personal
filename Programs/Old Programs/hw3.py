from Drawable import *
from Ball import Ball
from Block import Block
from Text import Text
import pygame
import math

#globals
framewidth = 1200
frameheight = 700

class baseLine(Drawable):
    def __init__(self,x=framewidth,y=400,visible=True):
        super().__init__(x,y,visible)
        
    def draw(self,surface):
        pygame.draw.line(surface,(0,0,0),(0,self.getY()),(self.getX(),self.getY()))
    
    def get_rect(self):
        pass
    
    def get_X(self):
        return self.getX()
    
    def get_Y(self):
        return self.getY()


pygame.init()
surface = pygame.display.set_mode((framewidth,frameheight))
pygame.display.set_caption('Ball Game')
surface.fill((255,255,255))
line = baseLine()
line.draw(surface)
drawables = []

#initializing all of the objects
Mainball = Ball(60,line.getY())
drawables.append(line)
drawables.append(Mainball)
drawables.append(Block(framewidth-120,line.getY()))
drawables.append(Block(framewidth-99,line.getY()))
drawables.append(Block(framewidth-78,line.getY()))
drawables.append(Block(framewidth-120,line.getY()-21))
drawables.append(Block(framewidth-99,line.getY()-21))
drawables.append(Block(framewidth-78,line.getY()-21))
drawables.append(Block(framewidth-120,line.getY()-42))
drawables.append(Block(framewidth-99,line.getY()-42))
drawables.append(Block(framewidth-78,line.getY()-42))
Mainball.draw(surface)
init = (0,0)
end = (0,0)
x=0
y=0

fpsClock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type ==
        pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
            
        surface.fill((255,255,255))
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            init = pygame.mouse.get_pos()
            
        elif event.type == pygame.MOUSEBUTTONUP:
            end = pygame.mouse.get_pos()
            Mainball.setxv(init[0]-end[0])
            Mainball.setyv(init[1]-end[1])

        if math.fabs(Mainball.getyv()) > 0.0001:
            Mainball.fly()
            
        for drawable in drawables:
            drawable.draw(surface)
        
    pygame.display.update()
    fpsClock.tick(30)
    
    
    
    