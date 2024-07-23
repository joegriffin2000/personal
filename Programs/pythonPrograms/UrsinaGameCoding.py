from ursina import *

#Global Init_____
WindowName = "Joe's Game"
XBorder = 6.96
YBorder = 3.83
#____________________

class Player(Entity):
    def __init__(self):
        super().__init__(
            model = 'sphere',
            color = color.salmon,
            scale = (.5,.5),
            position = (0,0)
            )
        self.PlayerSpeed = 3
        self.SprintMult = 2
    
    #getters
    def getPlayerSpeed(self):
        return self.PlayerSpeed
    def getSprintMult(self):
        return self.SprintMult
    
    #setters
    def setPlayerSpeed(self,speed):
        self.PlayerSpeed = speed
    def setSprintMult(self,mult):
        self.SprintMult = mult

def update():
    if held_keys['a']:
        if held_keys['left shift'] or held_keys['right shift']:
            player.x -= player.getPlayerSpeed() * time.dt * player.getSprintMult()
        else:
            player.x -= player.getPlayerSpeed() * time.dt
    if held_keys['w']:
        if held_keys['left shift'] or held_keys['right shift']:
            player.y += player.getPlayerSpeed() * time.dt * player.getSprintMult()
        else:
            player.y += player.getPlayerSpeed() * time.dt
    if held_keys['s']:
        if held_keys['left shift'] or held_keys['right shift']:
            player.y -= player.getPlayerSpeed() * time.dt * player.getSprintMult()
        else:
            player.y -= player.getPlayerSpeed() * time.dt
    if held_keys['d']:
        if held_keys['left shift'] or held_keys['right shift']:
            player.x += player.getPlayerSpeed() * time.dt * player.getSprintMult()
        else:
            player.x += player.getPlayerSpeed() * time.dt
            
    StopAtBorder(player)
        
def StopAtBorder(p):
    if (p.x < -1 * XBorder):
        p.x = -1 * XBorder
    elif (p.x > XBorder):
        p.x = XBorder
    if (p.y < -1*YBorder):
        p.y = -1*YBorder
    elif (p.y > YBorder):
        p.y = YBorder
      

if __name__ == '__main__':
    app = Ursina()
    window.show_ursina_splash = True
    player = Player()
    app.run()
