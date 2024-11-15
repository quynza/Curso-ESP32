import machine
import time

def rutine_button(BUTTON1,BUTTON2,RGB_R,RGB_G,RGB_B):
    button1 = machine.Pin(BUTTON1, machine.Pin.IN) # Button pin
    button2 = machine.Pin(BUTTON2, machine.Pin.IN) # Button pin
    led_R = machine.Pin(RGB_R, machine.Pin.OUT) # LED pin
    led_G = machine.Pin(RGB_G, machine.Pin.OUT) # LED pin
    led_B = machine.Pin(RGB_B, machine.Pin.OUT) # LED pin

    # Enter a 5 seg loop loop
    time1 = time.ticks_us()
    during = 0
    while during <= 5000000:
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        
        # If the button is pressed by reading its value
        if button1.value() and not button2.value():
            # Turn on the LED by setting its value to 1
            led_R.value(1)
            led_G.value(0)
            led_B.value(0)
            time.sleep(0.5)
        elif not button1.value() and button2.value():
            led_R.value(0)
            led_G.value(1)
            led_B.value(0)
            time.sleep(0.5)
        elif button1.value() and button2.value():
            led_R.value(0)
            led_G.value(0)
            led_B.value(1)
            time.sleep(0.5)
        else:
            # Turn off the LED
            led_R.value(0)
            led_G.value(0)
            led_B.value(0)
            time.sleep(0.5)
    
    led_R.value(0)
    led_G.value(0)
    led_B.value(0)
