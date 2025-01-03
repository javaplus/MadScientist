from motor_class import MotorController

class BaseGame:
    # Constructor gets motor_controller and rgb
    def __init__(self, motor_controller, rgb):
        self.motor_controller = motor_controller
        self.rgb = rgb


    ## Implement Setup (initialize rgbs and motor status)
    def setup(self):
        pass

    ## implement on Hit.
    def onHit(self):
       pass
    

    