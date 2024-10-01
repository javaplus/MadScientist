
# Motor Controller (mini L298N)

The mini L298N is a small DC motor controller that allows you to use PWM signals to control the speed and direction of upto 2 attached motors.

It does this by having paired inputs (labeled `IN1, IN2, IN3, and N4`).  `IN1` and `IN2` are used to control `MOTOR-A`.  And `IN3` and `IN4` are used to control `MOTOR-B`
Adding power to on of the pins in a pair (e.g. `IN1`) would cause the motor connected to `MOTOR-A` to move in a direction.  Cutting power to `IN1` and adding power to `IN2`, would cause the motor connected to `MOTOR-A` to move in the opposite direction.
The same applies to the second pair `IN3` & `IN4`, just that it controls the motor on `MOTOR-B`.  If you want a pin to move the motor in a different direction that it is, either switch the connections on the motor or the `IN*` pins.

You should only put a signal/power to one of the paired pins at a time.  Meaning you'd never want to put power to both `IN1` and `IN2`as that would not make sense.  You'd want power to go to one or the other in order to control the direction.
You can have power to one of the first pairs and one of the second pairs at the same time.  Just not power to both pins in a pair. (Maybe need a diagram here saying valid power options).

https://www.aliexpress.us/item/2251832826330994.html?spm=a2g0o.order_detail.order_detail_item.11.896cf19cEFLkKq&gatewayAdapt=glo2usa
