# -*- coding: utf-8 -*-
import Tkinter as tk
import cv2, time, ps_drone
import numpy as np
from PIL import Image, ImageTk
import math

def setup(drone):
	drone.startup()                                              
	drone.reset()                                                
	while (drone.getBattery()[0] == -1):      time.sleep(0.1)    
	print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	
	drone.useDemoMode(False)  
	drone.setConfigAllID()                                       
	drone.sdVideo()                                              
	drone.frontCam()
	CDC = drone.ConfigDataCount
	while CDC == drone.ConfigDataCount:       time.sleep(0.0001) 
	drone.startVideo()                                           
	#drone.showVideo() 
	drone.getNDpackage(["demo"])
	root.title("Autonomous Flight Control Center")
	root.geometry("650x365")

drone = ps_drone.Drone()
root = tk.Tk()                                                                                    
setup(drone)
lmain = tk.Label(root)
lmain.pack()
IMC =    drone.VideoImageCount 
centered = False
average = 0
counter = 0    
prevAngle = 0                            

def show_frame():
	global lmain
	global IMC
	global counter
	global average
	global centered
	global prevAngle
	while drone.VideoImageCount == IMC: 
		time.sleep(0.01)

	IMC = drone.VideoImageCount
	key = drone.getKey()
	if key == " ":
		drone.land()
		exit(0)
	frame = drone.VideoImage
	#frame = blur_and_dilate(frame)
	#frame = find_blobs(frame)
	img = frame
	area,cx,cy = detect_red(frame, img)
	if cx != -1:
		cv2.line(frame,(320,180),(cx,cy),(0,255,255),2)
	#frame,img = find_contours(frame,img)
	#frame = img
	#frame = cv2.flip(frame, 1)
	cv2.line(frame,(310,180),(330,180),(0,0,0),2)
	cv2.line(frame,(320,170),(320,190),(0,0,0),2)
	try:
		a = abs(320-(cx))
		b = abs(180-(cy))
		a = a**2
		b = b**2
		c = a + b
		c = math.sqrt(c)
		c = int(c)
		if c < 25:
			centered = True
		else:
			centered = False
		angle = int(math.atan((180.0-cy)/(370.0-cx))*180.0/math.pi)
		counter = counter + 1
		if counter > 5:
			average = average / counter
			average = int(average)
			prevAngle = average
			counter = 0
		else:
			average = average + angle
		cv2.putText(frame,"Angle: " + str(prevAngle), (370,180), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
		cv2.putText(frame,"Area: " + str(area), (370,160), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
		cv2.putText(frame,"From Center: " + str(c), (370,140), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
		cv2.putText(frame,"X: " + str(cx), (370,120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
		cv2.putText(frame,"Y: " + str(cy), (450,120), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
		cv2.putText(frame,"Centered: " + str(centered), (370,100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
	except:
		pass
	#angle = int(math.atan((cx-cy),(320-180))*180/math‌​.pi)
	#angle = int(math.atan((cx-cy),(320-180))*(180/math.pi))
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(10, show_frame)

#def find_blobs():

def blur_and_dilate(frame):
	frame = cv2.medianBlur(frame,15)
	frame = cv2.dilate(frame, np.ones((25, 25)))
	return frame

def find_blobs(frame):
	params = cv2.SimpleBlobDetector_Params()
	params.filterByArea = True
	params.minArea = 150
	params.filterByCircularity = False
	params.filterByConvexity = False
	params.filterByInertia = False
	detector = cv2.SimpleBlobDetector(params)
	keypoints = detector.detect(frame)
	counter = 0
	for keyPoint in keypoints:
		counter = counter + 1
		x = keyPoint.pt[0]
		y = keyPoint.pt[1]
		cv2.putText(frame,str(counter), (int(x),int(y+25)), cv2.FONT_HERSHEY_SIMPLEX, 1, 150)
		s = keyPoint.size
		#print x,y,s
	im_with_keypoints = cv2.drawKeypoints(frame, keypoints, np.array([]), (255,0,0), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
	return im_with_keypoints

def detect_red(frame,img):
	img = cv2.GaussianBlur(img,(5,5),0)
	#img = cv2.medianBlur(frame,15)
	#img = cv2.dilate(img, np.ones((25, 25)))
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower_range = np.array([0, 100, 100], dtype=np.uint8)
	upper_range = np.array([8, 255, 255], dtype=np.uint8)
	#lower_range = np.array([150, 100, 50], dtype=np.uint8)
	#upper_range = np.array([255, 255, 255], dtype=np.uint8)
	img = cv2.inRange(hsv, lower_range, upper_range)
	
	contours,hierarchy = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	max_area = 0
	best_cnt = 0
	angle = 0
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area > max_area:
			max_area = area
			best_cnt = cnt
	if max_area > 250:
		try:
			M = cv2.moments(best_cnt)
			cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
			return max_area,cx,cy
		except:
			return -1,-1,-1
	else:
		return -1,-1,-1

def find_contours(frame,img):
	#frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	#contours, _ = cv2.findContours(frame, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
	# for c in contours:
	# 	rect = cv2.boundingRect(c)
	# 	if rect[2] < 300 or rect[3] < 200: continue
	# 	#print cv2.contourArea(c)
	# 	x,y,w,h = rect
	# 	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
	# 	cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)


	#We want to detect areas of similar pixels (in a box essentially)
	#We want to find colors we can lock onto in the real world and remember their position


	return frame, img
    
show_frame()
root.mainloop()