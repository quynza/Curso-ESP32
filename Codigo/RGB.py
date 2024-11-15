from machine import Pin, PWM
import time

def set_color1(red,green,blue,r, g, b):
    red.duty(r)
    green.duty(g)
    blue.duty(b)

def rutine_RGB(RED_PIN,GREEN_PIN,BLUE_PIN):
    # Set up the PWM channels
    red = PWM(Pin(RED_PIN))
    green = PWM(Pin(GREEN_PIN))
    blue = PWM(Pin(BLUE_PIN))

    # Set the PWM frequency
    red.freq(1000)
    green.freq(1000)
    blue.freq(1000)

    # Enter a 5 seg loop loop
    time1 = time.ticks_us()
    during = 0
    while during <= 5000000:
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        set_color1(red,green,blue,1023,0,0) # Red
        time.sleep(1)
        set_color1(red,green,blue,0,1023,0) # Green
        time.sleep(1)
        set_color1(red,green,blue,0,0,1023) # Blue
        time.sleep(1)
        set_color1(red,green,blue,1023,0,1023) # Purple
        time.sleep(1)
    
    set_color1(red,green,blue,0,0,0) # Off
    time.sleep(1)
