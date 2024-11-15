from machine import ADC,Pin
import time

def rutine_photoresistor(PHOTORESISTOR):
    # create an ADC object acting on a pin
    photoresistor = ADC(Pin(PHOTORESISTOR))
    # Configure the ADC attenuation to 11dB for full range
    photoresistor.atten(photoresistor.ATTN_11DB)

    # Enter a 5 seg loop loop
    time1 = time.ticks_us()
    during = 0
    while during <= 5000000:
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        # read a raw analog value in the range 0-4095
        value = photoresistor.read()
        print(value)
        time.sleep(0.05)
