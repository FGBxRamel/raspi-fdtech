
import RockyBorg
import time
import math

rudolf = RockyBorg.RockyBorg()
rudolf.Init()

speed = 1
timesleep = 3
direction = 1

rudolf.SetMotorsEnabled(True)
rudolf.SetMotor1(speed * (-1))
rudolf.SetMotor2(speed)
time.sleep(timesleep)
rudolf.SetMotors(0)
rudolf.SetServoPosition(direction)


