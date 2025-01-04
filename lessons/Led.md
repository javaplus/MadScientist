# LED

An LED is a Light Emitting Diode.  A diode only allows electricity to flow in one direction.  So, there is a positive and negative side to the LED.  Typically the longer leg of the LED is the positive side.

So, for this lab, we will simply hook our LED to the Pico to see it light up. 

## What to do

For this lab, we are going to start by just using the Pico as a power source to light up our LED.  

## Orientation

It will be easiest if you orient your Pico as seen below in the [wiring diagram](#wiring-diagram).   
The USB connection should be at the top, but touching the table and the pins should be sticking straight up.

## Wiring Diagram

Plug a red wire from the longer leg on the LED to the 3.3V pin on the Pico. And a black wire from the other leg to a GND (Ground) pin on the pico.  

NOTE: Technically the color of the wires you use doesn't matter (internally they are the same), but the color does make it easier to know their purpose.  Usually, red wires indicate positive(+) and black or white wires indicate ground/negative(-). 

See Diagram:

![LED Wiring Diagram](/lessons/images/simple_led_bb.png)

When you plug the wires into the LED you should see it light up.  If you accidentally plug the wires in backwards (long leg to ground), then that shouldn't hurt anything, but the LED won't light up because a diode only allows electricity to flow in one direction.

## Voltage Considerations 

![LED Specification](/lessons/images/led_specs.png)

LEDs (like most electronics) have voltage ranges in which they are designed to run. As mentioned above, we are currently running off 3.3V (Volts), but if we look at the specifications for the LEDs, we will see we are actually running a little over the specified voltage range of 3.0 to 3.2V for our blue LED. This is why it's so bright. It's running slightly above max power! 

Notice that the white, blue, and green LEDs support up to 3.2V. The other LEDs (red and yellow) only support up to 2.2V.  So, if we tried to use a red or yellow LED with our current circuit we could burn them out.

Since we are barely over spec with our blue LED we most likely won't have an issue, but it would be safer for the lifespan of the LED to run at a lower voltage. 


## Resistors

 One simple way to lower the voltage in a circuit is to use a resistor.  A resistor simply resists (or restricts) the flow of electricity. You could use a resistor to lower the voltage to safer levels, but we are going to be lazy and try a different approach when we use the 2 Volt LEDs.

 ![Resistor](/lessons/images/resistor.png)

For now we will continue using the blue LED which can handle the 3 Volts from the Pico and NOT use a resistor.

# Controlling LED with PICO

Now we will look at how to use code on the Pico to control an LED.

Grab your blue LED or any LED rated for 3 Volts.  Take a red wire and connect the long leg of the LED into the GP16 pin on the Pico.  "GP " stands for General Purpose Input Output.  Connect the short leg of the LED to a GND pin on the Pico.

![Blink Diagram](/lessons/images/simple_led2_bb.png)

With the LED in place and connected to the Pico and to ground, we just need to write the code. 

``` Python
from machine import Pin
import utime

led = Pin(16, Pin.OUT)

while True:
    led.toggle()
    utime.sleep_ms(1000)
```

Enter the code above into the editor and then click the Play button.
If everything works, you should see the LED flash about once a second.

If it works, blink twice!

## Other Pin functions

Another way to turn the LED off and on is to use the [value() function](https://docs.micropython.org/en/latest/library/machine.Pin.html#machine.Pin.value).

Here is that code:

``` Python
from machine import Pin
import utime

led = Pin(16, Pin.OUT)

while True:
    led.value(1)
    utime.sleep_ms(1000)
    led.value(0)
    utime.sleep_ms(1000)
```

Try this out.  If you want it to blink faster change the time it sleeps.

