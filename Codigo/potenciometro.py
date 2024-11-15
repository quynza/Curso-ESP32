from machine import ADC, Pin, PWM
import time

def rutine_potenciometro(POTENCIOMETRO,LCD_R):
    pot = ADC(Pin(POTENCIOMETRO, Pin.IN)) # create an ADC object acting on a pin

    # Configure the ADC attenuation to 11dB for full range
    pot.atten(pot.ATTN_11DB)

    # Create a PWM object
    led = PWM(Pin(LCD_R), freq=1000)

    # Enter a 5 seg loop loop
    time1 = time.ticks_us()
    during = 0
    while during <= 5000000:
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        # Read a raw analog value in the range of 0-4095
        value = pot.read()

        # Scale the value to the range of 0-1023 for ESP32 PWM duty cycle
        pwm_value = int(value * 1023 / 4095)

        # Update the LED brightness based on the potentiometer value
        led.duty(pwm_value)
        
        # Print the raw value and the voltage
        print(f"value: {value}")

        # Wait for 0.5 seconds before taking the next reading
        time.sleep(0.2)
    led.duty(0)