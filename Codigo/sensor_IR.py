import machine
import time

def rutine_IR(IR_PIN):
    ir_avoid = machine.Pin(IR_PIN, machine.Pin.IN, machine.Pin.PULL_UP) # avoid module pin

    # Enter a 5 seg loop loop
    time1 = time.ticks_us()
    during = 0
    while during <= 5000000:
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        # Print values of the obstacle avoidance module
        print(ir_avoid.value())
        time.sleep(0.2)
