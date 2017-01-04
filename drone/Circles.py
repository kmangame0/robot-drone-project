import numpy as np
import cv2

webcam = cv2.VideoCapture(0)
while True:
    (_, im) = webcam.read()
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT, 1.2, 100)
 
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:		
            cv2.circle(im, (x, y), r, (0, 255, 0), 4)
    cv2.imshow('OpenCV', im)
    key = cv2.waitKey(1)
