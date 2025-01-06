from machine import Pin,PWM
import asyncio

class Laser:
    
    # sets pin for laser
    def __init__(self, pin_number):
        self.laser = PWM(Pin(pin_number))
        self.laser.freq(100)
        self.stop()
    
    def fire(self, seconds):
        asyncio.create_task(self.fire_task(seconds))
        
    def turnOn(self):
        self.laser.duty_u16(65535)
        
    def turnOff(self):
        self.stop()
        
    async def fire_task(self, seconds):
        self.laser.duty_u16(65535) 
        await asyncio.sleep(seconds)
        self.stop()
    
    def stop(self):
        self.laser.duty_u16(0)
    