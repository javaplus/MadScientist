from machine import Pin, PWM
import utime

led1 = PWM(Pin(26))
led1.freq(1000)

led2 = PWM(Pin(27))
led2.freq(1000)


while True:
    for i in range(100,10000,20):
        led1.duty_u16(i)
        led2.duty_u16(i)
        utime.sleep_ms(5)
    
    for y in range(10000,100,-20):
        led1.duty_u16(y)
        led2.duty_u16(y)
        utime.sleep_ms(5)
        