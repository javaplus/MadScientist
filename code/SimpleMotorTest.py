from machine import Pin, PWM
import utime

print("Hello")

in1 = Pin(27, Pin.OUT)
in2 = Pin(26, Pin.OUT)

def forwardFull():
    print("in foward full")
    in1.low()
    in2.high()
    
def stop():
    print("in stop")
    in1.low()
    in2.low()

while True:
    forwardFull()
    utime.sleep_ms(3000)
    stop()
    utime.sleep_ms(3000)
