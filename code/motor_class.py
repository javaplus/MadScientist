from machine import Pin, PWM

class MotorController:
    MAX_SPEED = 45000
    MIN_SPEED = 10000
    SLEEP_TIME_MS = 1

    def __init__(self):
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

    def move(self, x: float, y: float):
        """ Move the car based on x and y values """

        # Calculate speed based on y value
        speed = int(self.MIN_SPEED + ((abs(x) + abs(y)) * (self.MAX_SPEED - self.MIN_SPEED)))
        # print(f"Speed: {speed}")

        self.left_motor_forward.duty_u16(speed if (x > 0 or y > 0) else 0)
        self.left_motor_backward.duty_u16(speed if (x < 0 or y < 0) else 0)
        self.right_motor_forward.duty_u16(speed if (x < 0 or y > 0) else 0)
        self.right_motor_backward.duty_u16(speed if (x > 0 or y < 0) else 0)

    def stop(self):
        """Stop all motors."""
        self.left_motor_forward.duty_u16(0)
        self.left_motor_backward.duty_u16(0)
        self.right_motor_forward.duty_u16(0)
        self.right_motor_backward.duty_u16(0)
