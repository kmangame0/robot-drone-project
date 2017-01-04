import cv2
import numpy as np
import imutils
import SimpleCV as cv

Camera = SimpleCV.Camera(prop_set={'width':350,'height':150})
Display = cv.Display()
img = cv2.imread('red.png', 1)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([150, 100, 50], dtype=np.uint8)
upper_range = np.array([200, 255, 255], dtype=np.uint8)

mask = cv2.inRange(hsv, lower_range, upper_range)

contours, hierarchy = cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

# draw the white paper and eliminate the small pieces (less than 1000000 px). This px count is the same as the QR code dectection
for cnt in contours:
    if cv2.contourArea(cnt)>1000000:
        cv2.drawContours(mask,[cnt],0,255,-1) # the [] around cnt and 3rd argument 0 mean only the particular contour is drawn

        # Build a ROI to crop the QR
        x,y,w,h = cv2.boundingRect(cnt)
        roi=mask[y:y+h,x:x+w]
        # crop the original QR based on the ROI
        #QR_crop = QR_orig[y:y+h,x:x+w]
        # use cropped mask image (roi) to get rid of all small pieces
        #QR_final = QR_crop * (roi/255)
cv2.imshow('mask',mask)
cv2.waitKey(0)
