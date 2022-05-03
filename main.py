import RockyBorg
import time
import math

rudolf = RockyBorg.RockyBorg()
rudolf.Init()

rudolf.v = 2*2*math.pi*0.035


def longt(richtung, speed: float):
    rudolf.SetMotorsEnabled(True)
    rudolf.SetMotor1(-0.5)
    rudolf.SetMotor2(0)


longt(1, 0.5)
