from motor_class import MotorController

class BasicGame:
    def __init__(self, motor_controller, rgb):
        self.motor_controller = motor_controller
        self.rgb = rgb

    ## implement on Hit.
    def onHit(self):
        print("Basic Game been hit!!")
        # Let's flash our eyes
        # go red
        self.rgb.color = (255, 0, 0)
        self.motor_controller.spin_lock()
    

    