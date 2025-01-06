from machine import Pin, PWM
import utime

print("Running Simple Motor Test")

in1 = Pin(16, Pin.OUT)
in2 = Pin(17, Pin.OUT)

def forwardFull():
    print("in foward full")
    in1.low()
    in2.high()
    
def backwardFull():
    print("in backward full")
    in2.low()
    in1.high()

def stop():
    print("in stop")
    in1.low()
    in2.low()

while True:
    forwardFull()
    utime.sleep_ms(3000)
    stop()
    utime.sleep_ms(3000)
    backwardFull();
    utime.sleep_ms(3000)
    stop()
    utime.sleep_ms(3000)
