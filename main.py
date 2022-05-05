import RockyBorg
import time
import math
import pic

rudolf = RockyBorg.RockyBorg()
rudolf.Init()
run = True
g = -1

def drive(direction:float):
    rudolf.SetMotorsEnabled(True)
    rudolf.SetMotor1(speed * -1)
    rudolf.SetMotor2(speed)
    rudolf.SetServoPosition(direction)
    #time.sleep(timeslp)
    #rudolf.SetMotors(0)
    #rudolf.SetServoPosition(0)


#timeslp = input("timesteps:")
speed = float(input("speed:"))
resolution = int(input("resolution:"))
redv = int(input("redvalue:"))
greenv = int(input("greenvalue:"))
bluev = int(input("bluevalue:"))
rangev = int(input("value-range:"))
colorcode = [redv, greenv, bluev]
color = pic.Color(colorcode, rangev, resolution)

while run == True:
    
    x = color.getY()  

    if not x == None:
        #68 cm Breite des Bildes bei 65 cm Abstand (41cm nach links / 27 cm nach rechts)
        #sin = Gegenkatete/Hypotenuse, Hypotenuse =  (65^2 + (41oder27)^2)^1/2
        
        a = 0.27 #"""Länge: Mittelpunkt bis rechter äußerer Rand"""
        b = 0.41 #"""Länge: Mittelpunkt bis linker äußerer Rand""""
        #c = 0.65 #"""Abstand zu Gerade a+b"""

        #alpha = math.asin(math.sin(a/(c^2 + a^2)^(1/2)))
        #beta = math.asin(math.sin(b/(c^2 + b^2)^(1/2)))

        
        #2464 pixel breite auf a+b eingeteilt
        #--> doppelte if Bedingung danach Anteil an Pixelmasse und dadurch Winkel zu berechnen
        
        pixelmengea = (resolution / 0.68) * a
        pixelmengeb = (resolution / 0.68) * b

        nullpunkt = int(resolution - pixelmengea)

        if x < nullpunkt:
            dir = (x - nullpunkt) / pixelmengeb
            drive(dir)
            g = dir * -1
            print("links")

        elif x > nullpunkt:
            dir = (x - nullpunkt) / pixelmengea 
            drive(dir)
            g = dir *-1
            print("rechts")
        elif x == nullpunkt:
            drive(0)
            g = 0.001
            print("mitte")

    elif x == None:
        rudolf.SetMotorsEnabled(True)
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)
        rudolf.SetMotor1(-1)
        rudolf.SetMotor2(1)
        rudolf.SetServoPosition(g * 1)
        time.sleep(2)
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)
        print("nicht gefunden")

