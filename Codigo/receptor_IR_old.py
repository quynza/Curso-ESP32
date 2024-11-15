import time
from machine import Pin, freq
from ir_rx.print_error import print_error
from ir_rx.nec import NEC_8

# Decode the received data and return the corresponding key name
def decodeKeyValue(data):
    if data == 0x19:
        return "0"
    if data == 0x45:
        return "1"
    if data == 0x46:
        return "2"
    if data == 0x47:
        return "3"
    if data == 0x44:
        return "4"
    if data == 0x40:
        return "5"
    if data == 0x43:
        return "6"
    if data == 0x07:
        return "7"
    if data == 0x15:
        return "8"
    if data == 0x9:
        return "9"
    if data == 0x16:
        return "*"
    if data == 0x0D:
        return "#"
    if data == 0x18:
        return "UP"
    if data == 0x08:
        return "LEFT"
    if data == 0x5A:
        return "RIGHT"
    if data == 0x52:
        return "DOWN"
    if data == 0x1C:
        return "OK"
    return data

# User callback
def callback(data, addr, ctrl):
    if data < 0:  # NEC protocol sends repeat codes.
        pass
    else:
        print(decodeKeyValue(data))

def rutine_receptor(RECEPTOR_PIN):
    pin_ir = Pin(RECEPTOR_PIN, Pin.IN) # IR receiver
    ir = NEC_8(pin_ir, callback) # Instantiate the NEC_8 receiver
    # Show debug information
    ir.error_function(print_error)
    
    try:
        # Enter a 5 seg loop loop
        time1 = time.ticks_us()
        during = 0
        while during <= 10000000:
            time2 = time.ticks_us()
            during = time.ticks_diff(time2, time1)
            pass
    except KeyboardInterrupt:
        ir.close()  # Close the receiver
