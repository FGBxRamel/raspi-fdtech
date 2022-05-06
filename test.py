import ultrasonic_sensor
import time
stopdist = 10
n = 0
while n < 5:
    print(30/ultrasonic_sensor.distance())
    time.sleep(1)
    n += 1

