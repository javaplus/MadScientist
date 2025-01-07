from basegame import BaseGame
from motor_class import MotorController
from buzzer import Buzzer
from random import randint, randrange
import utime

## Saturday Bite Fever (Disco mode)
#
# Get ready to boogie! In this high-energy mode, getting tagged triggers a dazzling disco fever. 
# Your shark will go into a spinning frenzy while your RGB lights erupt in a vibrant rave show. 
# It's a party in the laser tag arena, even if you're temporarily out of the action. 
#
# This mode adds a fun and exciting element to the game, encouraging players to embrace the chaos and enjoy the light show!


class DiscoGame(BaseGame):
    
    ## Implement Setup
    def setup(self):
        # set color to pink
        self.rgb.color = (255, 192, 203)
       
        self.motor_controller.setMaxSpeed(MotorController.MAX_SPEED)
        # Make sure lazer is off
        self.laser.turnOff()

    ## implement on Hit.
    def onHit(self):
        print("GET DOWN AND BOOGIE YOUVE BEEN HIT BY THE DISCO!!")

        for count in range(10):
            self.rgb.color = (randint(1, 255), randint(1, 255), randint(1, 255))
            utime.sleep_ms(500)    

        self.buzzer.buzzDisco()

        # potential dance moves to code
        #front a little bit
        #back a little bit
        #left shimmy
        #right shimmy
        #turn around 360 degrees

        self.buzzer.stop()

    ## Implement on Fire
    def onFire(self):
        ## Turn on laser for 5 seconds
        self.laser.fire(5)