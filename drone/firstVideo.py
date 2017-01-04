import time, sys
import ps_drone
import numpy as np
import cv2   
import cv2.cv as cv                                           

drone = ps_drone.Drone()                                     
drone.startup()                                              

drone.reset()                                                
while (drone.getBattery()[0] == -1):      time.sleep(0.1)    
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	
drone.useDemoMode(True)                                     

drone.setConfigAllID()                                       
drone.sdVideo()                                              
drone.frontCam()                                             
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001) 
drone.startVideo()                                           
drone.showVideo()                                            

print "Use <space> to toggle front- and groundcamera, any other key to stop"
IMC =    drone.VideoImageCount                               
stop =   False
ground = False
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)
while not stop:
    while drone.VideoImageCount == IMC: time.sleep(0.01)     
    IMC = drone.VideoImageCount
    key = drone.getKey()  

    #BGR
    img = IMC
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
 
	
    if len(cnts) > 0:
        c = max(cnts, key=cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
	center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
 
		
	if radius > 10:
	    cv2.circle(img, (int(x), int(y)), int(radius),
				(0, 255, 255), 2)
	    cv2.circle(img, center, 5, (0, 0, 255), -1)

	for i in xrange(1, len(pts)):
	    if pts[i - 1] is None or pts[i] is None:
		continue

	    thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
	    cv2.line(img, pts[i - 1], pts[i], (0, 0, 255), thickness)
 
	cv2.imshow("Frame", img)
	key = cv2.waitKey(1)
    if key==" ":	
        if ground:              ground = False
        else:                   ground = True
        drone.groundVideo(ground)                           
    elif key and key != " ":    stop =   True
