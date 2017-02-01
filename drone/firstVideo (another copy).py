import time, sys, ps_drone, cv2, math
import numpy as np 
import cv2.cv as cv                                         

drone = ps_drone.Drone()                                     
drone.startup()                                              

drone.reset()                                                
while (drone.getBattery()[0] == -1):      time.sleep(0.1)    
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	
drone.useDemoMode(False)                                     

drone.setConfigAllID()                                       
drone.sdVideo()                                              
drone.groundCam()
drone.setConfig("control:altitude max", "990")
drone.setConfig("control:altitude min", "300")
                                       
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001) 
drone.startVideo()                                           
drone.showVideo()                                            

print "Taking off..."
time.sleep(1)
drone.takeoff()
time.sleep(10)
drone.setSpeed(0.1)
print "Ready..."
drone.getNDpackage(["demo"])

IMC =    drone.VideoImageCount                               
stop =   False
ground = False
redLower = (29, 86, 6)
redUpper = (64, 255, 255)
threshold = 100
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
    best_cnt = 0
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > max_area:
            max_area = area
            best_cnt = cnt
    try:
        M = cv2.moments(best_cnt)
        cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
        #cv2.circle(img,(cx,cy),5,255,-1)
    except:
        continue
    alt = drone.NavData["demo"][3]
    #print "X: " + str(cx) + " Y: " + str(cy)

    if alt > 80:
        drone.moveDown(0.5)
    if alt < 15:
        drone.land()
        exit(0)

    if abs(320 - cx) < 200 and abs(180 - cy) < 100:
        print "Center"
        drone.moveDown(0.5)
        time.sleep(0.25)
        if alt < 25:
            drone.land()
    else:
        if 320 - cx > 0 and 180 - cy > 0:
            print "Quad 1"
            drone.relMove(-0.1,0.1, 0.0,0.0,0.0,0.0)
            time.sleep(0.1)
        elif 320 - cx < 0 and 180 - cy > 0:
            print "Quad 2"
            drone.relMove(0.1,0.1, 0.0,0.0,0.0,0.0)
            time.sleep(0.1)
        elif 320 - cx > 0 and 180 - cy < 0:
            print "Quad 3"
            drone.relMove(-0.1,-0.1, 0.0,0.0,0.0,0.0)
            time.sleep(0.1)
        elif 320 - cx < 0 and 180 - cy < 0:
            print "Quad 4"
            drone.relMove(0.1,-0.1, 0.0,0.0,0.0,0.0)
            time.sleep(0.1)

    if key==" ":
        drone.land()
        time.sleep(1)
        exit(0)
        if ground:              
		ground = False
        else:
                ground = True
        	drone.groundVideo(ground)       
    elif key and key != " ":    stop =   True

    drone.hover()
