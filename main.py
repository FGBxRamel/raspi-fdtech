import RockyBorg
import time
import math

rudolf = RockyBorg.RockyBorg()
rudolf.Init()

rudolf.v = 2*2*math.pi*0.035


def drive(speed: float, direction: float = 0, timesleep: float = 1):
    rudolf.SetMotorsEnabled(True)
    rudolf.SetMotor1(speed * (-1))
    rudolf.SetMotor2(speed)
    time.sleep(timesleep)
    rudolf.SetMotors(0)
    rudolf.SetServoPosition(direction)


drive(1,1,2)
