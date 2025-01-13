from basegame import BaseGame
from laser import Laser
from motor_class import MotorController
import asyncio

class DriveGame(BaseGame):

    ## Implement Setup
    def setup(self):
        # set color to green
        self.rgb.color = (0, 255, 0)
        self.laser.turnOff()

    ## implement on Hit.
    def onHit(self):
        print("Drive Game been hit!!")
        # Let's flash our eyes
        asyncio.create_task(self.flashRGB())
        
        
    async def flashRGB(self):
        # go red, then blue back and forth
        for x in range(10):
            self.rgb.color = (255, 0, 0)
            await asyncio.sleep(.5)
            self.rgb.color = (0, 0, 255)
            await asyncio.sleep(.5)
        
    ## Implement on Fire
    def onFire(self):
        ## Turn on laser for 5 seconds
        self.laser.fire(5)
        ## Play a beep sound
        self.buzzer.buzzTimeNFreq(.25,50)
    

    