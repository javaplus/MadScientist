from basegame import BaseGame
from laser import Laser
from motor_class import MotorController


## WTF Mode - "Whatever the fantastic" idea is you have for a game mode can go here!


class WTFGame(BaseGame):

    ## Implement Setup
    def setup(self):
        # set color to violet
        self.rgb.color = (127, 0, 255)
        self.laser.turnOn()

    ## implement on Hit.
    def onHit(self):
        #Put whatever you want to happen in here when you get hit in your game mode

        print("WTF Mode - you've been hit!!")
        # Let's flash our eyes
        # go red
        self.rgb.color = (255, 0, 0)
        self.motor_controller.spin_lock()
        self.laser.turnOff()
    

    