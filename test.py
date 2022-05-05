import ultrasonic_sensor
import time
stopdist = 10

#returns distance in cm's
while True:
    time.sleep(1)
    print(ultrasonic_sensor.distance())
"""#stopps if distance is to low
if dist < stopdist:
    run = False
"""


