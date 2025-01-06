from basegame import BaseGame
from laser import Laser
from motor_class import MotorController

class BasicGame(BaseGame):

    ## Implement Setup
    def setup(self):
        # set color to green
        self.rgb.color = (0, 255, 0)
        self.laser.turnOn()

    ## implement on Hit.
    def onHit(self):
        print("Basic Game been hit!!")
        # Let's flash our eyes
        # go red
        self.rgb.color = (255, 0, 0)
        self.motor_controller.spin_lock()
        self.laser.turnOff()
    

    