import cv2, time, ps_drone
import numpy as np
from PIL import Image, ImageTk
import math
import sys

drone = ps_drone.Drone()
drone.startup()                                              
drone.reset()   
drone.trim()
time.sleep(2)                                             
while (drone.getBattery()[0] == -1):      time.sleep(0.1)    
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	
drone.useDemoMode(True) 
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001) 
print "Taking off..."
#drone.takeoff()
t = 0
while True:
	key = drone.getKey()
	print t
	if key == " ":
		if t < 255:
			t = t+1
		drone.thrust(t,t,t,t)