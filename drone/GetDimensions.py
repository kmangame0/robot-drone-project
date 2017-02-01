import time, sys, ps_drone, cv2, math
import numpy as np 
import cv2.cv as cv                                         

drone = ps_drone.Drone()                                     
drone.startup()                                              

drone.reset()                                                
while (drone.getBattery()[0] == -1):      time.sleep(0.1)    
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	

#Cannot get altitute without setting to false
drone.useDemoMode(False)                                     

drone.setConfig("control:altitude max", "990")
drone.setConfig("control:altitude min", "300")
drone.setConfigAllID()                                       
drone.sdVideo()                                              
drone.groundCam()
                                       
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001) 
drone.startVideo()                                           
drone.showVideo()                                            

print "Taking off..."
time.sleep(1)
#drone.takeoff()
time.sleep(6)
#drone.setSpeed(0.1)
print "Ready..."
drone.getNDpackage(["demo"])

IMC =    drone.VideoImageCount                               
stop =   False
ground = False
threshold = 100
while not stop:
    while drone.VideoImageCount == IMC: 
    	time.sleep(0.01)
    IMC = drone.VideoImageCount
    key = drone.getKey()
    alt = drone.NavData["demo"][3]
    print alt
