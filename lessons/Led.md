# LED

An LED is a Light Emitting Diode.  A Diode only allows electricity to flow in one direction.  So, there is a positive and negative side to the LED.  Typically the longer leg of the LED is the positive side.


So, for this lab, we will simply hook LED to the Pico to see it light up. 

## What to do:

For this lab, we are going to use the Pico only as a power source.  

We will now connect the LED to the Raspberry Pi Pico.  

NOTE: Technically the color of wires you use don't matter (internally they are the same), but the color does make it easier to know the purpose.  Usually, red wires indicate positive(+) and black or white wires indicate ground/negative(-).   line indicates the positive side.

##### Orientation

It will be easiest if you orient your Pico as seen below in the [wiring diagram](#wiring-diagram).   
The USB connection should be at the top, but touching the table and the pins sticking straight up.

## Wiring Diagram

![LED Wiring Diagram](/lessons/images/simple_led_bb.png)


# Voltage Considerations (Maybe move to talk next one and talk about PWM)

LED's (like most electronics) have voltage ranges in which they are designed to run. As mentioned above, we are currently running off 3.3Volts, but if we look again at the specifciations for the LEDs, we will see we are actually running a little over the specified voltage range of 3.0 to 3.2V for our Blue LED. This is why it's so bright. It's running slightly above max power!

![LED Specification](/lessons/images/led_specs.png)



