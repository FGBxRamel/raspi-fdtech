import RockyBorg
import time

rudolf = RockyBorg.RockyBorg()
rudolf.Init()
rudolf.SetMotorsEnabled(True)
rudolf.SetMotors(0.5)
time.sleep(1)
rudolf.SetMotors(0)
