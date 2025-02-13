
# Motor Controller (mini L298N)

<img alt="L298N Motor Controller" src="/lessons/images/motor_controller.PNG" width="500"/>

The mini L298N is a small DC motor controller that allows you to use a microcontroller to control the speed and direction of up to 2 attached motors.

It does this by having paired inputs (labeled `IN1`, `IN2`, `IN3`, and `IN4`).  `IN1` and `IN2` are used to control `MOTOR-A`.  And `IN3` and `IN4` are used to control `MOTOR-B`.
Adding power to one of the pins in a pair (e.g. `IN1`) would cause the motor connected to `MOTOR-A` to move in a direction.  Cutting power to `IN1` and adding power to `IN2` would cause the motor connected to `MOTOR-A` to move in the opposite direction.
The same applies to the second pair `IN3` & `IN4`, just that it controls the motor on `MOTOR-B`.  If you want a pin to move the motor in a different direction, either switch the connections on the motor or the `IN*` pins.

You should only put a signal/power to one of the paired pins at a time.  Meaning you'd never want to put power to both `IN1` and `IN2` as that would not make sense.  You'd want power to go to one or the other in order to control the direction.
You can put power to one of the first pairs and one of the second pairs at the same time.  Just not power to both pins in a pair.

# Wire it up!

Wire the Pico to the motor controller and wire one motor to the `MOTOR-A` connector.  How you connect the motor wires to the `MOTOR-A` pins doesn't matter.  That is, there isn't a right or wrong way to connect the motor wires.  If you reverse the wires it will just cause the motor to spin in the opposite direction.

Note that the Pico is upside down, with the pins sticking straight up.  The diagram has the Pico in this orientation as well.  That is, the Pico in the diagram is showing you the correct pins if it is upside down with the pins up and the USB connection at the top. Also note that the two wires connecting the motor to the motor controller need to be connected from the **bottom** of the controller, instead of from the top (the diagramming program we use does not allow us to show this).

<img alt="L298N Motor Controller" src="/lessons/images/motor_controller_bb.png" width="500"/>

# Code

Here is the code that simply sends full power to `IN1` or `IN2` at a time.  It loops continuously and turns the motor forward, then stops, and then backward.  "Forward" and "backward" are really relative at this point and don't really matter.  The motor should turn in different directions when `forwardFull()` is called versus when `backwardFull()` is called.

```Python
from machine import Pin, PWM
import utime

print("Running Simple Motor Test")

in1 = Pin(16, Pin.OUT)
in2 = Pin(17, Pin.OUT)

def forwardFull():
    print("in forward full")
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
```