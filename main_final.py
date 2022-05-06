# libary import
import configparser as cp
import time

import pic
import RockyBorg
import ultrasonic_sensor


def drive(direction: float) -> None:
    """
    lets the vehicle drive with predefined speed and given direction

    direction: value betwenn -1 and 1 describing in wich direction the vehicle drives
    """
    rudolf.SetMotorsEnabled(True)
    rudolf.SetMotor1(speed * -1)
    rudolf.SetMotor2(speed)
    rudolf.SetServoPosition(direction)


def reset() -> None:
    """Helper function to stop/reset the Rocky so it stops."""
    rudolf.MotorsOff()
    rudolf.SetMotorsEnabled(False)
    rudolf.SetServoPosition(0)

config = cp.ConfigParser()
config.read("config.ini")
presets = config["PRESETS"]

rudolf = RockyBorg.RockyBorg()
rudolf.Init()


# set standart values
if input("Preset values? (y/n):").lower() == "y":
    resolution = presets.getint("Resolution")
    speed = presets.getfloat("Speed")
    stopdist = presets.getfloat("StopDistance")
    valueRange = presets.getint("ValueRange")
    color = pic.Color(tolerance=valueRange, length=resolution)
else:
    stopdist = float(input("stopping-distance:"))
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
found = False
notFound = 0
input("Press Enter to start.")

# loop to search
while run == True:

    # set for straight image
    rudolf.SetMotors(0)
    rudolf.SetServoPosition(0)

    # gets x-coordniate of aim (pixel with nearest value to given values)
    x = color.getY()

    # runs when x is definied
    if not x == None:
        found = True
        notFound = 0
        # distance from center to right picture-end on x-axis (individual for every camera, needs to be measured)
        a = 0.27

        # distance from center to left picture-end on the x-axis (individual for every camera, needs to be measured)
        b = 0.41

        # distance from measuring device (individual for every camera, needs to be measured)
        c = 0.68

        # amount of pixels on the x-axis for each part (left and right of the center)
        pixelmengea = (resolution / c) * a
        pixelmengeb = (resolution / c) * b

        # defining center of the x-axis
        nullpunkt = int(resolution - pixelmengea)

        # drives left if x-value is lower then range around center
        if x < (nullpunkt-10):
            dir = (x - nullpunkt) / pixelmengeb
            print("links")
            drive(dir)
            g = dir * -1

        # drives right if x-value is higher then range around center
        elif x > (nullpunkt+10):
            dir = (x - nullpunkt) / pixelmengea
            print("rechts")
            drive(dir)
            g = dir * -1

        # drives straigt if x-value is equal to range in center
        elif x < (nullpunkt + 10) and x > (nullpunkt - 10):
            print("mitte")
            drive(0)
            g = 0.001

    # no color found --> driving in circle to find object again
    elif x == None:
        if found and notFound >= 2:
            reset()
            break
        notFound += 1
        print("nicht gefunden")
        rudolf.SetMotorsEnabled(True)
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)
        rudolf.SetMotor1(-0.25)
        rudolf.SetMotor2(0.25)
        rudolf.SetServoPosition(g * 1)
        time.sleep(1)
        rudolf.SetMotors(0)
        rudolf.SetServoPosition(0)

    # timesleep when resolution is to high, to protct the raspberry pi from crashing
    if resolution > 128:
        time.sleep((resolution^2/128^2)/4)

    """#Neigungswinkel des Ultraschallsensorss in Grad
    alpha = 10

    distact = 
  
    if distact < stopdist:
        reset()
        break"""
reset()
print("Prozess beendet.")