import ultrasonic_sensor
import time
import math
stopdist = 10
n = 0
while n < 5:
    print(math.asin(30/ultrasonic_sensor.distance()))
    time.sleep(1)
    n += 1

