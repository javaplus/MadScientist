from machine import Pin,PWM
import utime


class Buzzer:

    # Constructor gets motor_controller and rgb
    def __init__(self, pin_number):
        self.buzzer = PWM(Pin(pin_number))
        self.stop()
        
    ## Implement Setup
    def buzzLow(self):
        self.buzzer.freq(100)
        self.buzzer.duty_u16(45000)
        
    def stop(self):
        self.buzzer.duty_u16(0)
        

    
