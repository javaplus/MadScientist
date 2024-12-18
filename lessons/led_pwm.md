# PWM(Pulse Width Modulation)

## Overview

Now we will look at how to use PWM (Pulse Width Modulation) with the RaspberryPi Pico.  If you aren't familiar with PWM just think of it as a way to send a pulse of power at regular intervals.  PWM is a more efficient way of powering electronics like motors or even LEDs.  Instead of having constant power to a device you can send pulses of electricity to keep a motor running or light up an LED. That is you can specify a frequency at which to send pulses of electricity and then fluctuate the amount of time that signal or power is on during each pulse.  The amount of time the power is on during each signal/pulse is called the **Duty Cycle**.  The image below from [circuitdigest.com](https://circuitdigest.com/tutorial/what-is-pwm-pulse-width-modulation) illustrates PWM signals using various Duty Cycles. **NOTE** The frequency rate isn't shown below, but it doesn't matter, the duty cycle is independent of the frequency.

![PWM](/lessons/images/Pulse-Width-Modulation.jpg)


If powering a motor with PWM, the higher the duty cycle the faster the motor would spin.  
If powering an LED with PWM, the higher the duty cycle the brighter the LED will be.
This is caused by an increase in the average output voltage. (You will see this happen during this lab!)


 ## What to do

In this lab, we will use PWM in via the code on the Pico to dim and brighten an LED. Compared to the earlier lab when we lit an LED, we will be making several changes.
The first change we will make are to slightly alter the way we are interacting with the GPIO pin connecting to our LED. In the previous lab, the GPIO pin was configured as a simple output pin and where we would set the value to 1(or high) to turn the light on or set the value to 0 (or low) to turn the LED off.  So, in our previous implementation it was strictly a binary operation.

With PWM, we will be able to change the frequency and the duty cycle.  That is how many pulses per second(frequency) we send and how long the power will be high during each pulse(duty cycle).  However, initially we will just make a few tiny changes to keep the functionality of LED toggling off and on, but it will use PWM to light up the LED.

The wiring diagram is the same as the previous LED lab:
![Wiring Diagram](/lessons/images/simple_led2_bb.png)

## The Code

So, to start we need import [PWM](https://docs.micropython.org/en/latest/library/machine.PWM.html?highlight=pwm) from the machine library.  So, alter the first import by adding "PWM" alongside the existing "Pin".  The altered import line should look like this:  

```Python
from machine import Pin, PWM
```
Next we will alter the initiation of the "led" variable to use PWM.  To do this, we simply create a Pin with our pin number and wrap that with "PWM()".  
Alter the "led" initialization line like this:
```Python
led = PWM(Pin(16))
led.freq(1000)
```
Here we define the Pin #16 as our pin to use for PWM signals.  We also set the frequency to 1000Hz. That's 1000 pulses per second.  

Since our `"led"` variable now is a PWM object, the `value()` function is invalid.  So, we need to update each place we were calling the `value()` function, to use the [duty_u16()](https://docs.micropython.org/en/latest/library/machine.PWM.html?highlight=pwm#machine.PWM.duty_u16) function.  

This function allows us to set the duty cycle.  

The lowest possible value is **0** ... but we can also use 0%.

The highest possible value is **65535** ... but we can also use 100%. 

Therefore, if we want our LED to be at the brightest level, replace `led.value(1)` to `led.duty_u16(65535)` 
To turn the LED completely off, replace `led.value(0)` to `led.duty_u16(0)`

Here's the full code:

```Python
from machine import Pin, PWM
import utime

led = PWM(Pin(16))
led.freq(1000)

led.duty_u16(0) # init led to off


while True:
    # Turn LED on full
    led.duty_u16(65535) 
    utime.sleep_ms(500)
    
    # turn LED off
    led.duty_u16(0)
    utime.sleep_ms(500)

```
After updating the code click the STOP button to reset and then click the Play button to run the new code.

If everything is working, then you should see the led flash on and off, but now using PWM.

Not super exciting yet, but wait there's more!

## See the Power of PWM!

To see some difference with PWM verses the pure binary on and off, try playing with the value passed to the `led.duty_16(65535)` method.  Replace **65535** with a lower value so that when the LED comes on, it's not as bright.  Something like this:  
```Python
    led.duty_u16(5000) # 65535 is max
```

Retest with different values to see how it affects the brightness of the LED.

After you are bored with that, let's make some cool affects with PWM.

What we'll do now is make pressing the button slowly increase the brightness to max and then pressing it again slowly dim it till it's off.

To do this, we will simply add a for loop in the block of code that turns on or off the LED to slowly adjust the duty cycle up or down.  Here's an example for loop to slowly increase in brightness:

```Python
       for duty in range(0,65535,1):
            led.duty_u16(duty) # 65535 is max
```
**NOTE** The 3rd parameter of the for loop is the step.  That is how much to count by.  If you want to could by 5's, then change the 1 to 5.

Here's an example for loop to slowly decrease in brightness:

```Python
       for duty in range(65535,0,-1):
            led.duty_u16(duty) # 65535 is max
```

You can swap out the code that turns the LED on and off with these loops to see the LED more slowly light up and turn off.  These for loops may still cause it to light up and dim quickly.  Can you think how you could slow the light up or dimming down?

Here's the full code:

```Python
from machine import Pin, PWM


led = PWM(Pin(16))
led.freq(1000)

led.duty_u16(0) # init led to off


while True:
    # Slowly brighten
    for duty in range(0,65535,1):
        led.duty_u16(duty) # 65535 is max
        

    # Slowly dim
    for duty in range(65535,0,-1):
        led.duty_u16(duty) # 65535 is max

```

If you got this to work, eat some gummies!

## Stretch Goal

Play with the for loops and optionally some sleeping in your for loop to get the LEDs to light up slowly or dim slowly.

