from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

ursina = Ursina()

class Voxel(Button):
    def __init__(self, position = (0,0,0)):
        super().__init__(
            parent = scene,
            position = position,
            model = 'cube',
            origin_y = 0.5,
            texture = 'white_cube',
            color = color.color(0,0,random.uniform(0.9,1)),
            highlight_color = color.lime)
    
    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                voxel = Voxel(position = self.position + mouse.normal)
            elif key == 'right mouse down':
                destroy(self)

def createWorld():
    for z in range(20):
        for x in range(20):
            voxel = Voxel((x,0,z))
            
def update():
    if held_keys['escape']:
        application.quit()
        

if __name__ == '__main__':
    createWorld()
    player = FirstPersonController()
    ursina.run()