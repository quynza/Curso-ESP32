import machine
import time

# Calculate the distance using the ultrasonic sensor
def distance(TRIG,ECHO):
    # Ensure trigger is off initially
    TRIG.off()
    time.sleep_us(2)  # Wait for 2 microseconds

    # Send a 10-microsecond pulse to the trigger pin
    TRIG.on()
    time.sleep_us(10)
    TRIG.off()

    # Wait for the echo pin to go high
    while not ECHO.value():
        pass

    # Record the time when the echo pin goes high
    time1 = time.ticks_us()

    # Wait for the echo pin to go low
    while ECHO.value():
        pass

    # Record the time when the echo pin goes low
    time2 = time.ticks_us()

    # Calculate the time difference between the two recorded times
    during = time.ticks_diff(time2, time1)

    # Calculate and return the distance (in cm) using the speed of sound (340 m/s)
    return during * 340 / 2 / 10000

def rutine_HCSR04(trig_pin,echo_pin):
    # Define the trigger and echo pins for the distance sensor
    TRIG_ = machine.Pin(trig_pin, machine.Pin.OUT)
    ECHO_ = machine.Pin(echo_pin, machine.Pin.IN)
    
    # Enter a 5 seg loop loop
    time1 = time.ticks_us()
    during = 0
    while during <= 5000000:
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        dis = distance(TRIG_,ECHO_)
        print('Distance: %.2f' % dis)
        time.sleep_ms(300)  # Wait for 300 milliseconds before repeating

