import RGB, cinta_RGB, display_7_seg, LCD_I2C
import button_LED, potenciometro
import HCSR04, DHT11, sensor_IR, fotoresistor, receptor_IR
import buzzer

import os
exec(open("pines.py").read())

# SENSOR INFRAROJO
print("Rutina Sensor IR")
sensor_IR.rutine_IR(SENSOR_IR)
