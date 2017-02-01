import numpy as np
import cv2

webcam = cv2.VideoCapture(0)
while True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray,(25,25),0)
    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=30,param2=30,minRadius=15,maxRadius=500)
    nx = 0
    ny = 0
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        bestRed = 0
        bestX = 0
        bestY = 0
        for (x, y, r) in circles:		
            try:
            	redTotal = 0
            	roi = im[y-10:y+10, x-10:x+10]
            	h, w = roi.shape[:2]
            	for x1 in range(0,w):
            		for y1 in range(0,h):
            			redTotal = redTotal + roi[x1,y1][2]
            	if redTotal > bestRed:
            		bestRed = redTotal
            		bestX = x
            		bestY = y
            except:
            	continue
            if bestRed > 2500:
            	cv2.circle(im, (bestX, bestY), r, (0, 255, 0), 4)
            	cv2.circle(im,(bestX,bestY),2,(0,0,255),3)
    cv2.imshow('OpenCV', im)

    
    key = cv2.waitKey(1)
