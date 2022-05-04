
import RockyBorg
import time
import math

rudolf = RockyBorg.RockyBorg()
rudolf.Init()

speed = 0.1
timesleep = 3
direction = 0.5
speed2 = 0.2
timesleep2 = 2

rudolf.SetMotorsEnabled(True)
rudolf.SetMotor1(speed * (-1))
rudolf.SetMotor2(speed)
time.sleep(timesleep)
rudolf.SetServoPosition(direction)
rudolf.SetMotor1(speed2 * -1)
rudolf.SetMotor2(speed2)
time.sleep(timesleep2)
rudolf.SetMotors(0)
rudolf.SetServoPosition(0)


