from machine import Pin, PWM
import utime

print("Hello")
MAX_SPEED = 45000
MIN_SPEED = 5000

GO_FORWARD_MS = 1000
SLEEP_TIME_MS = 1

in1 = PWM(Pin(27))
in2 = PWM(Pin(26))

in1.freq(1000)
in2.freq(1000)

in3 = PWM(Pin(16))
in4 = PWM(Pin(17))

in3.freq(1000)
in4.freq(1000)



def forwardFull():
    print("in foward full")
    in1.duty_u16(0)
    in2.duty_u16(65000)
    
def accelerate():
    print("Accelerating")
    for speed in range(MIN_SPEED,MAX_SPEED,10):
        in1.duty_u16(0)
        in2.duty_u16(speed)
        in3.duty_u16(0)
        in4.duty_u16(speed)
        utime.sleep_ms(SLEEP_TIME_MS)
        
def accel_backwards():
    print("backwards")
    for speed in range(MIN_SPEED,MAX_SPEED,10):
        in1.duty_u16(speed)
        in2.duty_u16(0)
        in3.duty_u16(speed)
        in4.duty_u16(0)
        utime.sleep_ms(SLEEP_TIME_MS)
        
def decelerate():
    for speed in range(MAX_SPEED,0,-10):
        in1.duty_u16(0)
        in2.duty_u16(speed)
        in3.duty_u16(0)
        in4.duty_u16(speed)
        utime.sleep_ms(SLEEP_TIME_MS)
        
def decelerate_reverse():
    for speed in range(MAX_SPEED,0,-10):
        in1.duty_u16(speed)
        in2.duty_u16(0)
        in3.duty_u16(speed)
        in4.duty_u16(0)
        utime.sleep_ms(SLEEP_TIME_MS)
def stop():
    print("in stop")
    in1.duty_u16(0)
    in2.duty_u16(0)
    in3.duty_u16(0)
    in4.duty_u16(0)

while True:
    accelerate()
    #utime.sleep_ms(GO_FORWARD_MS)
    decelerate()
    accel_backwards()
    decelerate_reverse()
    #utime.sleep_ms(GO_FORWARD_MS)
    stop()
    utime.sleep_ms(3000)

