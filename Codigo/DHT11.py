import dht
import machine
import time

def rutine_DHT11(DHT11_PIN):
    # Initialize the DHT11 sensor and connect it to pin 14
    sensor = dht.DHT11(machine.Pin(DHT11_PIN))

    # Enter a 5 seg loop loop
    time1 = time.ticks_us()
    during = 0
    while during <= 5000000:
        time2 = time.ticks_us()
        during = time.ticks_diff(time2, time1)
        try:
            # Measure temperature and humidity
            sensor.measure()

            # Get temperature and humidity values
            temp = sensor.temperature()
            humi = sensor.humidity()

            # Print temperature and humidity
            print("Temperature: {}, Humidity: {}".format(temp, humi))

            # Wait for 0.25 second between measurements
            time.sleep(0.25)
        except Exception as e:
            print("Error: ", e)
            time.sleep(0.25)
