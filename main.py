import RockyBorg
import time

rudolf = RockyBorg.RockyBorg()
rudolf.Init()
rudolf.SetMotorsEnabled(True)
print("Enabled Motots")
rudolf.SetMotors(0.5)
print("Set Motors 0,5")
time.sleep(1)
print("Set Motors 0")
rudolf.SetMotors(0)
