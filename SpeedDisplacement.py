import time
import ps_drone
import numpy as np
import matplotlib.pyplot as pit

drone = ps_drone.Drone()       
drone.startup()
drone.reset()

while (drone.getBattery()[0] == -1):   time.sleep(0.1)
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])

drone.useDemoMode(False)
drone.takeoff()                
time.sleep(12)

land = False
forward = True
drone.setSpeed(0.1)
print drone.setSpeed()
count = 0

x=[0]
y=[0]
while land == False:
    drone.getNDpackage(["demo"])
    alt = drone.NavData["demo"][3]
    xSpeed = drone.NavData["demo"][4][0]/25.4
    ySpeed = drone.NavData["demo"][4][1]/25.4
    zSpeed = drone.NavData["demo"][4][1]/25.4
    print "X speed: " + str(xSpeed) + "in/s"
    print "Y speed: " + str(ySpeed) + "in/s"
    print "Z speed: " + str(zSpeed) + "in/s"
   
    if forward == True:
        print "Forward!"
        x.append(xSpeed)
        y.append(ySpeed)
        drone.moveForward()
        time.sleep(2)
        forward = False
        drone.hover()
    print "Done!"
    count = count + 1
    print count
    if count > 10000:
        land = True
##      
drone.land()
pit.plot(x,y)
pit.show()
