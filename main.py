import RockyBorg
import time
import math

rudolf = RockyBorg.RockyBorg()
rudolf.Init()

rudolf.v = 2*2*math.pi*0.035


def longt(richtung, speed: float):
    rudolf.SetMotorsEnabled(True)
    rudolf.SetMotor1(-1)
    rudolf.SetMotor2(1)
    input()
    rudolf.SetMotors(0)


longt(1, 0.5)
