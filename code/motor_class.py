from machine import Pin, PWM
import utime
import math

class MotorController:
    MAX_SPEED = 65000 # Hard limit
    MIN_SPEED = 10000
    SLEEP_TIME_MS = 1
    SPIN_LOCK_TIME = 2.5

    def __init__(self):
        
        # A max speed that can be changed based on game mode or other factors
        self.max_speed = self.MAX_SPEED
        
        # Define motor pins
        self.left_motor_forward = PWM(Pin(10))
        self.left_motor_backward = PWM(Pin(11))
        self.right_motor_forward = PWM(Pin(12))
        self.right_motor_backward = PWM(Pin(13))

        # Set PWM frequency
        self.left_motor_forward.freq(1000)
        self.left_motor_backward.freq(1000)
        self.right_motor_forward.freq(1000)
        self.right_motor_backward.freq(1000)
        # Trim factor
        self.trim_factor = 0

    def setMaxSpeed(self, speed):
        self.max_speed = speed
        
    def setTrim(self, trim):
        self.trim_factor = trim

    ### x values turn and y values are for forward and reverse
    def move(self, x: float, y: float):
        """ Move the car based on x and y values """
        
        # Calculate speed based on y value
        speed = int(self.MIN_SPEED + ((abs(x) + abs(y)) * (self.max_speed - self.MIN_SPEED)))
        if speed > self.MAX_SPEED:
            speed = self.MAX_SPEED
        #print(f"Speed: {speed}")
        
        left_speed = speed
        right_speed = speed
        if y > 0 or y < 0 : # moving forward or backwards
            # calculate speed based on trim
            # decrease baseline speed by factor based on trim
            trim_adjusted_speed =  speed - (speed * (abs(self.trim_factor) * .05))
            #print(f"trim adjusted speed:{trim_adjusted_speed}")
            
            # find the difference in the speed and the trim adjusted
            speed_diff = speed - trim_adjusted_speed
            #print(f"speed diff:{speed_diff}")
            
            # add speed_diff to one or the other motor to bring that motor up to current speed
            left_speed = trim_adjusted_speed if (self.trim_factor > 0) else (trim_adjusted_speed + speed_diff)
            right_speed = trim_adjusted_speed if (self.trim_factor < 0) else (trim_adjusted_speed + speed_diff)
            left_speed = int(left_speed)
            right_speed = int(right_speed)
            #print(f"leflt speed:{left_speed}")
            #print(f"right speed:{right_speed}")

        self.left_motor_forward.duty_u16(left_speed if (x > 0 or y > 0) else 0)
        self.left_motor_backward.duty_u16(left_speed if (x < 0 or y < 0) else 0)
        self.right_motor_forward.duty_u16(right_speed if (x < 0 or y > 0) else 0)
        self.right_motor_backward.duty_u16(right_speed if (x > 0 or y < 0) else 0)
        
    ### Execute a spinning manuever and stop anything else from happening.
    def spin_lock(self):
        print("in Spin lock")
        self.stop()
        self.left_motor_forward.duty_u16(self.MAX_SPEED)
        ## Sleep the bad way to keep this thread from doing anything else
        utime.sleep(self.SPIN_LOCK_TIME)
        

    def stop(self):
        """Stop all motors."""
        self.left_motor_forward.duty_u16(0)
        self.left_motor_backward.duty_u16(0)
        self.right_motor_forward.duty_u16(0)
        self.right_motor_backward.duty_u16(0)

