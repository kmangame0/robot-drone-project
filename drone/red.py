import cv2
import numpy as np
import imutils
import math

img = cv2.imread('red.png', 1)
height = np.size(img, 0)
width = np.size(img, 1)
print width
print height
centerWidth = int(width/2)
centerHeight = int(height/2)
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
    print x
    print y
    cv2.circle(mask, (int(x), int(y)), 2, (150, 50, 50), 2)
    distanceToCenterWidth = centerWidth - int(x)
    distanceToCenterHeight = centerHeight - int(y)
    print distanceToCenterWidth
    print distanceToCenterHeight

cv2.imshow('mask',mask)
cv2.waitKey(0)
