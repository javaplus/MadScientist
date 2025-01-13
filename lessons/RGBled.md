# RGB Leds

![RGBLED](https://th.bing.com/th/id/R.75cc7295833e3bf067561afbf0628a7f?rik=kZSBtVtLXsYVmA&riu=http%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2ff%2ff1%2fRGB_LED.jpg&ehk=sN9J9UFC17Ux4jgZQOREVca1aKfBsLfXcGljFElUorw%3d&risl=&pid=ImgRaw&r=0)

First, what does RGB mean? well it stands for red, green and blue. This will allow LED to turn multiple colors.  
The diagram below shows what each pin does when powered.

![LEDdia](https://microcontrollerslab.com/wp-content/uploads/2018/05/RGB-LED-pinout.png)


First plug in the RGB led into pico as shown in the picture below using four female to female wires. Note the orientation of the Pico in the picture is with the pins still up in the air.  
The black wire in the picture below connects to the longest pin, which is the ground  pin.  The pin on the edge next to it is connected to the red wire.  Again wire color doesn't really matter, but it does help you keep straight what is connected to what.  

![LEDFritz](https://github.com/javaplus/MadScientist/blob/main/lessons/images/RGBled.png?raw=true)
  

Now let's write some code to give the LED some color!

```python
from machine import Pin
import utime

red = Pin(22, Pin.OUT)

green = Pin(21, Pin.OUT)

blue = Pin(20, Pin.OUT)

def alt_colors (color, cooldown):
    color.value(1)
    utime.sleep_ms(cooldown)
    color.value(0)
    
    
while True:
    alt_colors(red, 1000)
    
    alt_colors(green, 1000)
    
    alt_colors(blue, 1000)
```
this code will give power to each pin one at a time, making the led flash the 3 primay colors!

Now lets have the led fade into different colors. In this code we will be using the library PMW(pulse width modulation)
  allowing us to change the values of the brightness/color.     
  
  [Learn more about PWM!](https://github.com/javaplus/MadScientist/blob/main/lessons/led_pwm.md)

Here we will make a function called alt_colors() passing in the different pins to cycle through different duty cycle values to control the brightness of the LED.

```python
from machine import Pin, PWM
from time import sleep

red = PWM(Pin(22))

green = PWM(Pin(21))

blue = PWM(Pin(20))

def alt_colors(color):
    
    for duty in range(0,65535,1):
        color.duty_u16(duty) # 65535 is max color brightness
        

    for duty in range(65535,0,-1):
        color.duty_u16(duty) # 65535 is max color brightness

while True:
    alt_colors(red)

    alt_colors(green)

    alt_colors(blue)
# you can change colors by alt_colors(red, green or blue)
```

Up to this point, we've only ever had power going to a single pin at a time and therefore only producing one of 3 colors: Red, Green, or Blue.

However, the power of the RGB LED is that it can produce any color you want by mixing Red, Green, and Blue.  You can control how much of each color based on the duty cycle of the appropriate pin.

Let's mix the colors now with some new code!  

```python
from machine import Pin, PWM
from time import sleep

red = PWM(Pin(22))

green = PWM(Pin(21))

blue = PWM(Pin(20))

# Function to turn completely off
def off():
    blue.duty_u16(0)
    red.duty_u16(0)
    green.duty_u16(0)

# Full blue
blue.duty_u16(65534) # 65534 is the max color brightness
# Mix in half red
red.duty_u16(35565)
# this makes purple

sleep(0.5)

off()

sleep(0.5)

# a little blue
blue.duty_u16(25545)
# a lot of red
red.duty_u16(65534)
# this makes pink

sleep(0.5)

off()
```

You can change the duty value which is the brightness of the color.  
the max value is 65534 and 0 means off. get creative here mix all the colors  
or just two colors by using or changing (color).duty_u16(color value)






