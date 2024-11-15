import RGB, cinta_RGB, display_7_seg, LCD_I2C
import button_LED, potenciometro
import HCSR04, DHT11, sensor_IR, fotoresistor, receptor_IR
import buzzer

import os
exec(open("pines.py").read())

# LCD
print("Rutina LCD I2C")
LCD_I2C.rutine_LCD()
# RGB
print("Rutina LED RGB")
RGB.rutine_RGB(RGB_R,RGB_G,RGB_B)
# CINTA RGB
print("Rutina 1 Cinta RGB")
cinta_RGB.rutine_cinta1(CINTA_RGB)
print("Rutina 2 Cinta RGB")
cinta_RGB.rutine_cinta2(CINTA_RGB)
# BUZZER
print("Rutina 1 Buzzer")
buzzer.rutine_buzzer1(BUZZER)
print("Rutina 2 Buzzer")
buzzer.rutine_buzzer2(BUZZER)
# BOTON Y LED
print("Rutina Botones-LED")
button_LED.rutine_button(BUTTON1,BUTTON2,RGB_R,RGB_G,RGB_B)
# SENSOR INFRAROJO
print("Rutina Sensor IR")
sensor_IR.rutine_IR(SENSOR_IR)
# FOTORESISTOR
print("Rutina Fotoresistor")
fotoresistor.rutine_photoresistor(FOTORESISTOR)
# POTENCIOMETRO
print("Rutina Potenciometro")
potenciometro.rutine_potenciometro(POTENCIOMETRO,RGB_R)
# SENSOR ULTRASONIDO HC-SR04
print("Rutina Ultrasonido")
HCSR04.rutine_HCSR04(HCSR04_TRIG,HCSR04_ECHO)
# SENSOR TEMP-HUMI DHT11
print("Rutina DHT-11")
DHT11.rutine_DHT11(SENSOR_DHT11)
# SENSOR RECEPTOR IR
print("Rutina Receptor IR")
receptor_IR.rutine_receptor(VS1838B)