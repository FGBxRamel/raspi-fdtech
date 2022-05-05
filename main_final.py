#libary import
import RockyBorg
import time
import pic
import ultrasonic_sensor

#class definition
rudolf = RockyBorg.RockyBorg()

#sets up Rockyborg
rudolf.Init()

#drive function
def drive(direction:float):
    rudolf.SetMotorsEnabled(True)
    rudolf.SetMotor1(speed * -1)
    rudolf.SetMotor2(speed)
    rudolf.SetServoPosition(direction)

#set standart values
stopdist = float(input("stopping-disatance:"))
speed = float(input("speed:"))
resolution = int(input("resolution:"))
redv = int(input("redvalue:"))
greenv = int(input("greenvalue:"))
bluev = int(input("bluevalue:"))
rangev = int(input("value-range:"))
colorcode = [redv, greenv, bluev]
color = pic.Color(colorcode, rangev, resolution)
run = True
g = -1

#loop to search 
while run == True:
    
    x = color.getY()  

    if not x == None:
        
        #Länge: Mittelpunkt bis rechter äußerer Rand (68 cm Breite des Bildes bei 65 cm Abstand (41cm nach links / 27 cm nach rechts)
        a = 0.27
        #Länge: Mittelpunkt bis linker äußerer Rand (68 cm Breite des Bildes bei 65 cm Abstand (41cm nach links / 27 cm nach rechts)
        b = 0.41 
        
        #2464 pixel breite auf a+b eingeteilt --> doppelte if Bedingung danach Anteil an Pixelmasse und dadurch Winkel zu berechnen
        pixelmengea = (resolution / 0.68) * a
        pixelmengeb = (resolution / 0.68) * b

        #defining median
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

    #no color found --> driving in circle to find object again
    elif x == None:
        rudolf.SetMotorsEnabled(True)
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)
        rudolf.SetMotor1(-1)
        rudolf.SetMotor2(1)
        rudolf.SetServoPosition(g * 1)
        time.sleep(1)
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)
        print("nicht gefunden")
