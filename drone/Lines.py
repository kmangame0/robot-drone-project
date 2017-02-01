import numpy as np
import cv2

cap = cv2.VideoCapture(0)
while(True):
	ret, frame = cap.read()
	img = cv2.Canny(frame,100,200)
	cv2.imshow('frame',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()