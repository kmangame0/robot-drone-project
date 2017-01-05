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
    contours,hierarchy = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    max_area = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt
    M = cv2.moments(best_cnt)
    cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
    cv2.circle(img,(cx,cy),5,255,-1)
    #cv2.imshow('image',mask)
	#cv2.waitKey(0)
    print "X: " + str(cx) + " Y: " + str(cy)

    if key==" ":
        if ground:              
		ground = False
        else:
                ground = True
        	drone.groundVideo(ground)       
    elif key and key != " ":    stop =   True
