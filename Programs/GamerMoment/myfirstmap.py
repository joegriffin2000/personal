# Map Creation
#
#
#ground = Voxel(position = self.position + mouse.normal)
from ursina import *

#Default Block
class Ground(Entity):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            scale= (100,1,100),
            model = 'plane',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.color(0,0,1),
            texture_scale=(100,100),
            collider='box')     
        

#World Generation Code
def createWorld():
    world = Ground()