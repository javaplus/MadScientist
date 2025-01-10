from basegame import BaseGame
from motor_class import MotorController
from buzzer import Buzzer

## Sharkbyte or Virus game mode
# A contagious frenzy takes over the arena! 
# One player starts infected with the Sharkbyte virus, glowing a sickly green. 
# Their mission? Spread the infection! Every shark they tag joins the horde, turning green and 
# helping to spread the virus. Uninfected players (glowing blue) must use their agility and 
# cunning to avoid the infected and survive until the timer runs out.

# Optional Twist: To increase the challenge, infected players could be slowed down, making it 
# harder for them to catch their prey and spread the virus. This adds an extra layer of 
# strategy and suspense to the game!

class VirusGame(BaseGame):
    
    ## Implement Setup
    def setup(self):
        # set color to blue
        # Default all to blue... get hit to turn green
        self.rgb.color = (0, 0, 255)
        # Start out not infected... get hit to be infected
        self.infected = False   # Could be used to react different if infected and hit.
        # Non infected can move at max speed.
        self.motor_controller.setMaxSpeed(MotorController.MAX_SPEED)
        # Make sure lazer is off
        self.laser.turnOff()

    ## implement on Hit.
    def onHit(self):
        print("Virus Game been hit!!")
        self.infected = True # not used now, but could be used to behave differently if already infected.
        # turn green... yous infected now!
        self.rgb.color = (0, 255, 0)
        self.buzzer.buzzLow()
        # turn yourself about
        self.motor_controller.spin_lock()    
        self.buzzer.stop()
        # You slow zombie now bro!
        self.motor_controller.setMaxSpeed(45000)

    ## Implement on Fire
    def onFire(self):
        ## Turn on laser for 5 seconds
        self.laser.fire(5)
        ## Play a beep sound
        self.buzzer.buzzTimeNFreq(.25,50)