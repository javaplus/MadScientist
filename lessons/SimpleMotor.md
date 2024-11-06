# Electric Motor


Electric motors are great for adding movement to your projects.  Simple electric motors like the ones we will be using simply have two connections.  Connect these wires to a power source and you'll get movement.  Be careful though to know what power they can work with.  

## N20 Electric Motor

![N20 Electric Motor](/lessons/images/motor.PNG)

We are using the GA12-N20 Motor.  They are metal geared high torque motors and can typically support from 3V up to 12V of power.  At 3 volts, our motors can turn about 100RPM(revolutions per minute).  The Raspberry Pi Pico GPIO pins output 3.3volts and can be controlled programmatically, but the VBus pin outputs a steady 5volts. However, the pins on the Pico are for very low power devices like LEDs or sensors and are not recommended to run electric motors.  So, caution needs to be taken when using electric motors with the pico to not draw too much power through the board.  A small motor with little load (no resistance) should be fine for our quick test, but we will show you the correct way to power a motor using the pico later.  For now, let's focus on understanding how simple electric motors work.

## Try it out
To test our electric motor, we will simply plug our Pico in via USB which will immediately provide a steady 5volts of power on the VBus pin and we can use this to temporarily test out motor.

At this point, we are just using the pico as simple battery source.  So, connect one wire from the motor to the VBUS pin and the other to a ground pin.  It doesn't matter which wire you connect to what. You are just providing a flow of electricity through the motor.  It can spin in either direction depending on the way the power flows.

![Wiring Diagram for Motor](/lessons/images/simple_motor_bb.png)

As soon as you connect the wires of the motor to the Pico, you should see the motor spinning.  If you reverse the wires, you should see them spin in the opposite direction.  
