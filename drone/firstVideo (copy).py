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
drone.groundCam()                                             
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001) 
drone.startVideo()                                           
drone.showVideo()                                            

print "Use <space> to toggle front- and groundcamera, any other key to stop"
IMC =    drone.VideoImageCount                               
stop =   False
ground = False
redLower = (29, 86, 6)
redUpper = (64, 255, 255)
currentWhiteTotal = 0
quadrantWithMostWhite = 0
previousWhiteTotal = 0
while not stop:
    while drone.VideoImageCount == IMC: 
    	time.sleep(0.01)

    IMC = drone.VideoImageCount
    key = drone.getKey()
    img = drone.VideoImage
    img = cv2.GaussianBlur(img,(5,5),0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower_range = np.array([150, 100, 50], dtype=np.uint8)
    upper_range = np.array([200, 255, 255], dtype=np.uint8)
    img = cv2.inRange(hsv, lower_range, upper_range)
    #cv2.imshow('image',mask)
	#cv2.waitKey(0)

    currentWhiteTotal = 0
    previousWhiteTotal = 0
	#Top Left

    for x in range (0,213):
        for y in range (0,120):
            color = img[x][y]
            if color < 5:
                currentWhiteTotal = currentWhiteTotal + 1
            if currentWhiteTotal > previousWhiteTotal:
                quadrantWithMostWhite = 1
	        previousWhiteTotal = currentWhiteTotal 
	#Top Center
    for x in range (213,426):
        for y in range (0,120):
            color = img[x][y]
            if color > 100:
                currentWhiteTotal = currentWhiteTotal + 1
            if currentWhiteTotal > previousWhiteTotal:
                quadrantWithMostWhite = 2
            previousWhiteTotal = currentWhiteTotal
	#Top Right
    for x in range (426,639):
    	for y in range (0,120):
            color = img[x][y]
            if color > 100:
            	currentWhiteTotal = currentWhiteTotal + 1
            if currentWhiteTotal > previousWhiteTotal:
            	quadrantWithMostWhite = 3
            previousWhiteTotal = currentWhiteTotal  
	#Left
    for x in range (0,213):
    	for y in range (120,240):
            color = img[x][y]
            if color > 100:
            	currentWhiteTotal = currentWhiteTotal + 1
            if currentWhiteTotal > previousWhiteTotal:
            	quadrantWithMostWhite = 4
            previousWhiteTotal = currentWhiteTotal    
	#Center
    for x in range (213,426):
    	for y in range (120,240):
            color = img[x][y]
            if color > 100:
            	currentWhiteTotal = currentWhiteTotal + 1
            if currentWhiteTotal > previousWhiteTotal:
            	quadrantWithMostWhite = 5
            previousWhiteTotal = currentWhiteTotal   
	#Right
    for x in range (426,639):
    	for y in range (120,240):
            color = img[x][y]
            if color > 100:
            	currentWhiteTotal = currentWhiteTotal + 1
            if currentWhiteTotal > previousWhiteTotal:
            	quadrantWithMostWhite = 6
            previousWhiteTotal = currentWhiteTotal  
	#Bottom Left
    for x in range (0,213):
    	for y in range (240,359):
            color = img[x][y]
            if color > 100:
            	currentWhiteTotal = currentWhiteTotal + 1
            if currentWhiteTotal > previousWhiteTotal:
            	quadrantWithMostWhite = 7
            previousWhiteTotal = currentWhiteTotal
	#Bottom Center
    for x in range (213,426):
    	for y in range (240,359):
            color = img[x][y]
            if color > 100:
            	currentWhiteTotal = currentWhiteTotal + 1
            if currentWhiteTotal > previousWhiteTotal:
            	quadrantWithMostWhite = 8
            previousWhiteTotal = currentWhiteTotal  
	#Bottom Right
    for x in range (426,639):
    	for y in range (240,359):
            color = img[x][y]
            if color > 100:
            	currentWhiteTotal = currentWhiteTotal + 1
            if currentWhiteTotal > previousWhiteTotal:
            	quadrantWithMostWhite = 9
            previousWhiteTotal = currentWhiteTotal
    if previousWhiteTotal > 1000:
	    print "Most White: " + str(quadrantWithMostWhite)          	
    if key==" ":
        if ground:              
		ground = False
        else:
                ground = True
        	drone.groundVideo(ground)       
    elif key and key != " ":    stop =   True
