import RockyBorg
import time
import math
import pic

rudolf = RockyBorg.RockyBorg()
rudolf.Init()
run = True

def drive(direction:float):
    rudolf.SetMotor1(speed * -1)
    rudolf.SetMotor2(speed)
    rudolf.SetServoPosition(direction)

speed = input("speed:")
resolution = input("resolution:")
redv = input("redvalue:")
greenv = input("greenvalue:")
bluev = input("bluevalue:")
rangev = input("value-range:")
colorcode = [redv, greenv, bluev]
color = pic.Color(colorcode, rangev, resolution)

while run == True:
    
    x = color.getY()  

    if not x == None:
        #68 cm Breite des Bildes bei 65 cm Abstand (41cm nach links / 27 cm nach rechts)
        #sin = Gegenkatete/Hypotenuse, Hypotenuse =  (65^2 + (41oder27)^2)^1/2
        
        a = 0.27 #"""Länge: Mittelpunkt bis rechter äußerer Rand"""
        b = 0.41 #"""Länge: Mittelpunkt bis linker äußerer Rand""""
        
        pixelmengea = (resolution / 0.68) * a
        pixelmengeb = (resolution / 0.68) * b

        nullpunkt = int(resolution - pixelmengea)

        if x < nullpunkt:
            dir = (x - nullpunkt) / pixelmengeb
            drive(dir)
            g = dir * -1

        elif x > nullpunkt:
            dir = (x - nullpunkt) / pixelmengea 
            drive(dir)
            g = dir *-1

        elif x == nullpunkt:
            drive(0)
            g = 0.001

    elif x == None:
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)
        rudolf.SetMotor1(-0.1)
        rudolf.SetMotor2(0.1)
        rudolf.SetServoPosition(g *0.25)
        time.sleep(1)
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)