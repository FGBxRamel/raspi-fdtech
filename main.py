import RockyBorg
import time

rudolf = RockyBorg.RockyBorg()
print("Init")
rudolf.Init()
print("Init done")
rudolf.SetMotorsEnabled(True)
print("Enabled Motors")
rudolf.SetMotors(0.5)
print("Set Motors 0,5")
time.sleep(1)
print("Seting Motors 0")
rudolf.SetMotors(0)
print("Set Motors 0")