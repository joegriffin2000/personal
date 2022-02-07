from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from myfirstmap import *
from makeup import *

ursina = Ursina()

#Currently my only way to close the program          
def update():
    if held_keys['escape']:
        application.quit()
        
#Gatewayto running the code only in source code 
if __name__ == '__main__':
    createWorld()
    player = Player()
    
    ursina.run()
