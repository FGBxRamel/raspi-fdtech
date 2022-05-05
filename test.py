from copyreg import dispatch_table
from xmlrpc.server import _DispatchArity1
import ultrasonic_sensor
stopdist = 10

#returns distance in cm's
dist = ultrasonic_sensor.distance
    
#stopps if distance is to low
if dist < stopdist:
    run = False



