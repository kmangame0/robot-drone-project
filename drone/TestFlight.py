import time, sys, ps_drone, cv2, math
import numpy as np 
import cv2.cv as cv                                         

import time
import ps_drone

drone = ps_drone.Drone()								# Start using drone					
drone.printBlue("Battery: ")

drone.startup()											# Connects to drone and starts subprocesses
drone.reset()											# Always good, at start

while drone.getBattery()[0] == -1:	time.sleep(0.1)		# Waits until the drone has done its reset
time.sleep(0.5)											# Give it some time to fully awake 

drone.printBlue("Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]))	# Gives a battery-status

print "Taking off..."
time.sleep(1)
drone.takeoff()
time.sleep(6)

print "Hovering..."
drone.hover()
time.sleep(2)


#Quadrant One

# angle = 0.0
# print "Testing with 2 decimal place precision"
# print "Moving at: " + str(angle) + " degrees for 1.5 seconds..."

# x = -round((angle/900.0),2)
# y = round(((90.0-angle)/900.0),2)

# drone.relMove(x,y, 0.0,0.0,0.0,0.0)
# time.sleep(1.5)

# print "Stopping"
# drone.stop()
# time.sleep(2)

# print "Landing"
# drone.land()


#Quadrant Two

# angle = abs(37.0)
# print "Testing with 2 decimal place precision"
# print "Moving at: " + str(angle) + " degrees for 1.5 seconds..."

# x = round((angle/900.0),2)
# y = round(((90.0-angle)/900.0),2)

# drone.relMove(x,y, 0.0,0.0,0.0,0.0)
# time.sleep(1.5)

# print "Stopping"
# drone.stop()
# time.sleep(2)

# print "Landing"


#Quadrant Three

# angle = abs(37.0)
# print "Testing with 2 decimal place precision"
# print "Moving at: " + str(angle) + " degrees for 1.5 seconds..."

# x = -round((angle/900.0),2)
# y = -round(((90.0-angle)/900.0),2)

# drone.relMove(x,y, 0.0,0.0,0.0,0.0)
# time.sleep(1.5)

# print "Stopping"
# drone.stop()
# time.sleep(2)

# print "Landing"


#Quadrant Four

angle = abs(37.0)
print "Testing with 2 decimal place precision"
print "Moving at: " + str(angle) + " degrees for 1.5 seconds..."

x = round((angle/900.0),2)
y = -round(((90.0-angle)/900.0),2)

drone.relMove(x,y, 0.0,0.0,0.0,0.0)
time.sleep(1.5)

print "Stopping"
drone.stop()
time.sleep(2)

print "Landing"