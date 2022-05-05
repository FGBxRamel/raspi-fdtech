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
    #time.sleep(timeslp)
    #rudolf.SetMotors(0)
    #rudolf.SetServoPosition(0)


#timeslp = input("timesteps:")
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
        c = 0.65 #"""Abstand zu Gerade a+b"""

        alpha = math.asin(math.sin(a/(c^2 + a^2)^(1/2)))
        beta = math.asin(math.sin(b/(c^2 + b^2)^(1/2)))

        
        #2464 pixel breite auf a+b eingeteilt
        #--> doppelte if Bedingung danach Anteil an Pixelmasse und dadurch Winkel zu berechnen
        
        pixelmengea = (128 / 0.68) * a
        pixelmengeb = (128 / 0.68) * b

        nullpunkt = int(128 - pixelmengea)

        if x < nullpunkt:
            anteilanwinkel = beta / pixelmengeb
            zielwinkel = (x - nullpunkt) * anteilanwinkel
            lenkennötig = True

        elif x > nullpunkt:
            anteilanwinkel = alpha / pixelmengea
            zielwinkel = (x - nullpunkt) * anteilanwinkel
            lenkennötig = True

        elif x == nullpunkt:
            lenkennötig = False
            drive(0)

        if lenkennötig:
            if zielwinkel < 0:
                drive(0.2)
                g = -   1
            elif zielwinkel > 0:
                drive(-0.2)
                g = 1

    elif x == None:
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)
        rudolf.SetMotor1(-0.1)
        rudolf.SetMotor2(0.1)
        rudolf.SetServoPosition(g *0.25)
        time.sleep(1)
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)

