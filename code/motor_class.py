from machine import Pin, PWM
import utime

class MotorController:
    MAX_SPEED = 45000
    MIN_SPEED = 5000
    SLEEP_TIME_MS = 1
    SPEED_CHANGE_STEP = 1000  # Change speed by this amount

    def __init__(self):
        # Define motor pins
        print("init MotorController")
        self.left_motor_forward = PWM(Pin(19))
        self.left_motor_backward = PWM(Pin(18))
        self.right_motor_forward = PWM(Pin(16))
        self.right_motor_backward = PWM(Pin(17))

        # Set PWM frequency
        self.left_motor_forward.freq(1000)
        self.left_motor_backward.freq(1000)
        self.right_motor_forward.freq(1000)
        self.right_motor_backward.freq(1000)

        # Initialize current speed and direction
        self.current_speed = 0
        self.current_direction = None

    def set_motor_direction(self, direction):
        """Set the motors' direction based on the given command."""
        if direction == 'forward':
            print(f"setting power to forward at speed:{self.current_speed}")
            self.left_motor_forward.duty_u16(self.current_speed)
            self.left_motor_backward.duty_u16(0)
            self.right_motor_forward.duty_u16(self.current_speed)
            self.right_motor_backward.duty_u16(0)
        elif direction == 'backward':
            self.left_motor_forward.duty_u16(0)
            self.left_motor_backward.duty_u16(self.current_speed)
            self.right_motor_forward.duty_u16(0)
            self.right_motor_backward.duty_u16(self.current_speed)
        elif direction == 'left':
            self.left_motor_forward.duty_u16(self.current_speed)
            self.left_motor_backward.duty_u16(0)
            self.right_motor_forward.duty_u16(0)
            self.right_motor_backward.duty_u16(0)
        elif direction == 'right':
            self.left_motor_forward.duty_u16(0)
            self.left_motor_backward.duty_u16(0)
            self.right_motor_forward.duty_u16(self.current_speed)
            self.right_motor_backward.duty_u16(0)
        else:
            self.stop()

    def stop(self):
        """Stop all motors."""
        print("Stopping")
        self.left_motor_forward.duty_u16(0)
        self.left_motor_backward.duty_u16(0)
        self.right_motor_forward.duty_u16(0)
        self.right_motor_backward.duty_u16(0)
        self.current_speed = 0
        self.current_direction = None

    def change_speed_and_direction(self, new_direction):
        
        print(f"change speed and direction with:{new_direction}")
        
        """Adjust the current speed and direction based on input."""
        if new_direction not in ['forward', 'backward', 'left', 'right']:
            print("Invalid direction. Stopping motors.")
            self.stop()
            return

        if self.current_direction is None:
            # Set initial direction and speed
            self.current_direction = new_direction
            self.current_speed = self.MIN_SPEED
            self.set_motor_direction(self.current_direction)
            return

        # Adjust speed based on current direction and new direction
        if new_direction == self.current_direction:
            if self.current_speed < self.MAX_SPEED:
                self.current_speed = min(self.current_speed + self.SPEED_CHANGE_STEP, self.MAX_SPEED)
        else:
            if new_direction == 'backward':
                if self.current_direction == 'forward':
                    self.current_speed = max(self.current_speed - self.SPEED_CHANGE_STEP, 0)
                    if self.current_speed == 0:
                        self.current_direction = 'backward'
                        self.current_speed = self.MIN_SPEED
            else:
                # For left or right turns, we can just stop the opposing motor
                self.set_motor_direction(new_direction)
                return

        self.set_motor_direction(self.current_direction)

