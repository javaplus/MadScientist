from machine import Pin, PWM
import utime

print("Hello")
MAX_SPEED = 45000
MIN_SPEED = 5000

GO_FORWARD_MS = 1000
SLEEP_TIME_MS = 1

left_motor_forward = PWM(Pin(27))
left_motor_backward = PWM(Pin(26))

left_motor_forward.freq(1000)
left_motor_backward.freq(1000)

right_motor_forward = PWM(Pin(16))
right_motor_backward = PWM(Pin(17))

right_motor_forward.freq(1000)
right_motor_backward.freq(1000)



def forwardFull():
    print("in foward full")
    left_motor_forward.duty_u16(0)
    left_motor_backward.duty_u16(65000)
    
def accelerate():
    print("Accelerating")
    for speed in range(MIN_SPEED,MAX_SPEED,10):
        left_motor_forward.duty_u16(0)
        left_motor_backward.duty_u16(speed)
        right_motor_forward.duty_u16(0)
        right_motor_backward.duty_u16(speed)
        utime.sleep_ms(SLEEP_TIME_MS)
        
def accel_backwards():
    print("backwards")
    for speed in range(MIN_SPEED,MAX_SPEED,10):
        left_motor_forward.duty_u16(speed)
        left_motor_backward.duty_u16(0)
        right_motor_forward.duty_u16(speed)
        right_motor_backward.duty_u16(0)
        utime.sleep_ms(SLEEP_TIME_MS)
        
def decelerate():
    for speed in range(MAX_SPEED,0,-10):
        left_motor_forward.duty_u16(0)
        left_motor_backward.duty_u16(speed)
        right_motor_forward.duty_u16(0)
        right_motor_backward.duty_u16(speed)
        utime.sleep_ms(SLEEP_TIME_MS)
        
def decelerate_reverse():
    for speed in range(MAX_SPEED,0,-10):
        left_motor_forward.duty_u16(speed)
        left_motor_backward.duty_u16(0)
        right_motor_forward.duty_u16(speed)
        right_motor_backward.duty_u16(0)
        utime.sleep_ms(SLEEP_TIME_MS)
def stop():
    print("in stop")
    left_motor_forward.duty_u16(0)
    left_motor_backward.duty_u16(0)
    right_motor_forward.duty_u16(0)
    right_motor_backward.duty_u16(0)

while True:
    accelerate()
    #utime.sleep_ms(GO_FORWARD_MS)
    decelerate()
    accel_backwards()
    decelerate_reverse()
    #utime.sleep_ms(GO_FORWARD_MS)
    stop()
    utime.sleep_ms(3000)

