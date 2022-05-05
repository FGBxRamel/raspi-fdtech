# libary import
import RockyBorg
import time
import pic
import ultrasonic_sensor

# class definition
rudolf = RockyBorg.RockyBorg()

# sets up Rockyborg
rudolf.Init()

# drive function
def drive(direction: float):
    """

    """
    rudolf.SetMotorsEnabled(True)
    rudolf.SetMotor1(speed * -1)
    rudolf.SetMotor2(speed)
    rudolf.SetServoPosition(direction)


# set standart values
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

# loop to search
while run == True:

    # gets x-coordniate of aim (pixel with nearest value to given values)
    x = color.getY()

    # runs when x is definied
    if not x == None:

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
            drive(dir)
            g = dir * -1
            print("links")

        # drives right if x-value is higher then range around center
        elif x > (nullpunkt+10):
            dir = (x - nullpunkt) / pixelmengea
            drive(dir)
            g = dir * -1
            print("rechts")

        # drives straigt if x-value is equal to center
        # TODO Set offset
        elif x < (nullpunkt + 10) and x > (nullpunkt - 10):
            drive(0)
            g = 0.001
            print("mitte")

    # no color found --> driving in circle to find object again
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
