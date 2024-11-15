from machine import Pin
from neopixel import NeoPixel
import time
import random

def rutine_cinta1(CINTA_PIN):
    pin = Pin(CINTA_PIN, Pin.OUT)   # set a pin to output to drive NeoPixels
    pixels = NeoPixel(pin, 8)   # create NeoPixel driver on pin for 8 pixels

    for i in range(3):
        pixels[0] = [64,154,227]    # set the pixel
        pixels[1] = [128,0,128]
        pixels[2] = [50,150,50]
        pixels[3] = [255,30,30]
        pixels[4] = [0,128,255]
        pixels[5] = [99,199,0]
        pixels[6] = [128,128,128]
        pixels[7] = [255,100,0]
        pixels.write()              # write data to all pixels
        time.sleep(2)
        
        pixels[0] = [0,0,0]
        pixels[1] = [0,0,0]
        pixels[2] = [0,0,0]
        pixels[3] = [0,0,0]
        pixels[4] = [0,0,0]
        pixels[5] = [0,0,0]
        pixels[6] = [0,0,0]
        pixels[7] = [0,0,0]
        pixels.write()              # write data to all pixels

def rutine_cinta2(CINTA_PIN):
    pin = Pin(CINTA_PIN, Pin.OUT)   # set a pin to output to drive NeoPixels
    pixels = NeoPixel(pin, 8)   # create NeoPixel driver on pin for 8 pixels
    
    time1 = time.ticks_us()
    during = 0
    while during <= 5000000:
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        
        for i in range(8):
            # Generate a random color for the current pixel
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            # Turn on the current pixel with the random color
            pixels[i] = color

            # Update the RGB LED strip display
            pixels.write()

            # Turn off the current pixel
            pixels[i] = (0, 0, 0)

            # Wait for a period of time to control the speed of the running light
            time.sleep_ms(100)
    
    pixels[0] = [0,0,0]
    pixels[1] = [0,0,0]
    pixels[2] = [0,0,0]
    pixels[3] = [0,0,0]
    pixels[4] = [0,0,0]
    pixels[5] = [0,0,0]
    pixels[6] = [0,0,0]
    pixels[7] = [0,0,0]
    pixels.write()              # write data to all pixels
