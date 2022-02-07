import pygame
from Drawable import Drawable
import random

class Rectangle(Drawable):
    def __init__(self,x=0,y=0,width=0,height=0,color=(0,0,0)):
        super().__init__(x,y)
        self.__width = width
        self.__height = height
        self.__color = color
        
    def draw(self,surface):
        location = self.getLoc()
        pygame.draw.rect(surface, self.__color, [location[0], location[1], self.__width, self.__height])

class Snowflake(Drawable):
    def __init__(self,x=0,y=0):
        super().__init__(x,y)
    
    def draw(self,surface):
        location = self.getLoc()
        pygame.draw.line(surface, (255,255,255), (location[0]-5,location[1]),(location[0]+5,location[1]))
        pygame.draw.line(surface, (255,255,255), (location[0],location[1]-5),(location[0],location[1]+5))
        pygame.draw.line(surface, (255,255,255), (location[0]-5,location[1]-5),(location[0]+5,location[1]+5))
        pygame.draw.line(surface, (255,255,255), (location[0]-5,location[1]+5),(location[0]+5,location[1]-5))
    
    
width = 800
height = 600

pygame.init()
surface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Hello World!')
drawings = []
snowflakes = []

Grass = Rectangle(0,height/2,width,height/2,(0,255,0))
Sky =  Rectangle(0,0,width,height,(0,0,245))

drawings.append(Sky)
drawings.append(Grass)

fpsClock = pygame.time.Clock()

def paused():
    paused = True
    while paused:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type ==
                pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
                pygame.quit()
                exit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False
                    
        pygame.display.update()
        print('Hello')
        fpsClock.tick(0)
        
while True:
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type ==
            pygame.KEYDOWN and event.__dict__['key'] == pygame.K_q):
            pygame.quit()
            exit()
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN and event.__dict__['key'] == pygame.K_c:
            print("Hello")
            
    
    surface.fill((255, 255, 255))
    for items in drawings:
        items.draw(surface)
    
    p = random.randint(0,width)
    s1 = Snowflake(p,0)
    snowflakes.append(s1)
    
    for snowflake in snowflakes:
        location = snowflake.getLoc()
        xint = location[0]
        yint = location[1]
        snowflake.setLoc((xint,yint+1))
        snowflake.draw(surface)

    pygame.display.update()
    