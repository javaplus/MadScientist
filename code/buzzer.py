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
        
    def buzzDisco(self):
        self.buzzer.freq(400)
        self.buzzer.duty_u16(1000)

        frequencies = [3830, 3400, 3038, 2864, 2550, 2272, 2028, 1915, 1700, 1519, 1430, 1275, 1136, 1014]
 
        for freq in frequencies:
            utime.sleep_ms(500)
            self.buzzer.freq(freq)
        self.buzzer.duty_u16(0)
        
