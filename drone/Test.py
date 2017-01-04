import time, sys
import ps_drone 
import cv2                                            
import math
import imutils
import numpy as np

drone = ps_drone.Drone()                                     
drone.startup()                                              

drone.reset()                                                
while (drone.getBattery()[0] == -1):      time.sleep(0.1)    
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	
drone.useDemoMode(False)                                      

drone.setConfigAllID()                                       
drone.sdVideo()                                              
drone.groundCam()                                             
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001) 
drone.startVideo()                                          
drone.showVideo()                                            

drone.takeoff()
time.sleep(5)
drone.setSpeed(0.1)
print "Use <space> to toggle front- and groundcamera, any other key to stop"
IMC =    drone.VideoImageCount

stop =   False
ground = True
width = 640
height = 360
centerWidth = 320
centerHeight = 180
while not stop:
    drone.getNDpackage(["demo"])      
    alt = drone.NavData["demo"][3]
    while drone.VideoImageCount == IMC: time.sleep(0.01)     
    IMC = drone.VideoImageCount
    key = drone.getKey()  
    img = drone.VideoImage
    try:
        img = cv2.blur(img,(5,5))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_range = np.array([150, 100, 50], dtype=np.uint8)
        upper_range = np.array([200, 255, 255], dtype=np.uint8)
        mask = cv2.inRange(hsv, lower_range, upper_range)
        moments = cv2.moments(mask, 0)
        area = moments['m00'] 
        if(area > 10000): 
            x = moments['m10'] / area
            y = moments['m01'] / area
            #cv2.circle(img, (int(x), int(y)), 2, (150, 50, 50), 2)
            distanceToCenterWidth = centerWidth - int(x)
            distanceToCenterHeight = centerHeight - int(y)
            print distanceToCenterWidth
            print distanceToCenterHeight
	    
	    if distanceToCenterWidth < 75 and distanceToCenterHeight < 75:
		drone.moveDown(0.1)
		time.sleep(50/1000)
 		if alt < 40:
		    drone.land()
		    exit(0)
	    else:
	        if (centerWidth - int(x)) > 0 and (centerHeight - int(y)) > 0:
	            drone.moveRight()
		    time.sleep(25/1000)
		    drone.stop()
		    drone.moveBackward()
		    time.sleep(25/1000)
		    drone.stop()	
	        if (centerWidth - int(x)) < 0 and (centerHeight - int(y)) > 0:
	            drone.moveLeft()
		    time.sleep(25/1000)
		    drone.stop()
		    drone.moveBackward()
		    time.sleep(25/1000)
		    drone.stop()
	        if (centerWidth - int(x)) > 0 and (centerHeight - int(y)) < 0:
	            drone.moveRight()
		    time.sleep(25/1000)
		    drone.stop()
		    drone.moveForward()
		    time.sleep(25/1000)
	 	    drone.stop()
	        if (centerWidth - int(x)) < 0 and (centerHeight - int(y)) < 0:
	            drone.moveLeft()
		    time.sleep(25/1000)
		    drone.stop()
		    drone.moveForward()
		    time.sleep(25/1000)
	   	    drone.stop()
	 
    except:
	drone.hover()
        continue                               
    if key==" ":
	drone.land() 
 	exit(0)  
                         
    elif key and key != " ":    stop =   True
