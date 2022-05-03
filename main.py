import RockyBorg
import os

rudolf = RockyBorg.RockyBorg()
rudolf.Init()
rudolf.SetMotorsEnabled(True)
rudolf.SetMotors(0.5)
os.sleep(1)
rudolf.SetMotors(0)
