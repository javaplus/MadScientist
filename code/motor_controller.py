from machine import Pin, PWM
import utime

print("Hello")
MAX_SPEED = 45000
MIN_SPEED = 5000
SLEEP_TIME_MS = 1

# Define motor pins
left_motor_forward = PWM(Pin(27))
left_motor_backward = PWM(Pin(26))
right_motor_forward = PWM(Pin(16))
right_motor_backward = PWM(Pin(17))

# Set PWM frequency
left_motor_forward.freq(1000)
left_motor_backward.freq(1000)
right_motor_forward.freq(1000)
right_motor_backward.freq(1000)

def set_motor_direction(direction, speed):
    """Set the motors' direction based on the given command."""
    if direction == 'forward':
        left_motor_forward.duty_u16(speed)
        left_motor_backward.duty_u16(0)
        right_motor_forward.duty_u16(speed)
        right_motor_backward.duty_u16(0)
    elif direction == 'backward':
        left_motor_forward.duty_u16(0)
        left_motor_backward.duty_u16(speed)
        right_motor_forward.duty_u16(0)
        right_motor_backward.duty_u16(speed)
    elif direction == 'left':
        left_motor_forward.duty_u16(speed)
        left_motor_backward.duty_u16(0)
        right_motor_forward.duty_u16(0)
        right_motor_backward.duty_u16(0)
    elif direction == 'right':
        left_motor_forward.duty_u16(0)
        left_motor_backward.duty_u16(0)
        right_motor_forward.duty_u16(speed)
        right_motor_backward.duty_u16(0)
    else:
        stop()

def stop():
    """Stop all motors."""
    print("Stopping")
    left_motor_forward.duty_u16(0)
    left_motor_backward.duty_u16(0)
    right_motor_forward.duty_u16(0)
    right_motor_backward.duty_u16(0)

def decelerate():
    for speed in range(MAX_SPEED, 0, -10):
        set_motor_direction('forward', speed)
        utime.sleep_ms(SLEEP_TIME_MS)


# Main loop to demonstrate functionality
while True:
    
    set_motor_direction('forward', 10000)
    utime.sleep_ms(3000)
    stop()
