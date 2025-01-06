# RGB Leds

![RGBLED](https://th.bing.com/th/id/R.75cc7295833e3bf067561afbf0628a7f?rik=kZSBtVtLXsYVmA&riu=http%3a%2f%2fupload.wikimedia.org%2fwikipedia%2fcommons%2ff%2ff1%2fRGB_LED.jpg&ehk=sN9J9UFC17Ux4jgZQOREVca1aKfBsLfXcGljFElUorw%3d&risl=&pid=ImgRaw&r=0)

First, what does RGB mean? well it stands for red, green and blue. This will allow LED to turn multiple colors.  
The diagram below shows what each pin does when powered.

![LEDdia](https://microcontrollerslab.com/wp-content/uploads/2018/05/RGB-LED-pinout.png)


Now let's write some code to give the LED some color!


![LEDFritz](https://github.com/javaplus/MadScientist/blob/main/lessons/images/RGBled.png?raw=true)
  
  First plug in the RGB led into pico as shown in the picture above.

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
this code will give power to each pin one at a time, making the led flash different colors!

Now lets have the led fade into different colors. In this code we will be using the library PMW(pulse width modulation)
  allowing us to change the values of the brightness/color.     
  
  [Learn more about PWM!](https://github.com/javaplus/MadScientist/blob/main/lessons/led_pwm.md)

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

Here we make a function called alt_colors allowing us to easily call a color change command.  








