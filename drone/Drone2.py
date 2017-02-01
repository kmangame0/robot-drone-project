# -*- coding: utf-8 -*-
import Tkinter as tk
import cv2, time, ps_drone
import numpy as np
from PIL import Image, ImageTk
import math
import sys

def basic_movements():
	# drone.move(0.0,0.05, 0.0,0.0)
	# time.sleep(1)
	# drone.stop()
	# time.sleep(2)
	# drone.move(0.05,0.0, 0.0,0.0)
	# time.sleep(1)
	# drone.stop()
	# time.sleep(2)
	# drone.move(0.0,-0.05, 0.0,0.0)
	# time.sleep(1)
	# drone.stop()
	# time.sleep(2)
	# drone.move(-0.05,0.0, 0.0,0.0)
	# time.sleep(1)
	# drone.stop()
	# time.sleep(2)
	drone.move(0.0,0.0,0.5,0.0)
	time.sleep(.2)

def setup(drone):
	drone.startup()                                              
	drone.reset()   
	drone.trim()
	time.sleep(1)                                             
	while (drone.getBattery()[0] == -1):      time.sleep(0.1)    
	print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	
	drone.useDemoMode(True)  
	drone.setConfigAllID()                                       
	drone.sdVideo()                                              
	drone.frontCam()
	CDC = drone.ConfigDataCount
	while CDC == drone.ConfigDataCount:       time.sleep(0.0001) 
	print "Taking off..."
	drone.takeoff()
	time.sleep(10)
	#basic_movements()
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
	#key = drone.getKey()
	frame = drone.VideoImage
	#frame = blur_and_dilate(frame)
	#frame = find_blobs(frame)
	img = frame
	area,cx,cy,r = detect_red(frame, img)
	alt = drone.NavData["demo"][3]

	if cx != -1:
		cv2.line(frame,(320,180),(cx,cy),(0,255,255),2)
		#frame,img = find_contours(frame,img)
		#frame = img
		#frame = cv2.flip(frame, 1)
		cv2.line(frame,(310,180),(330,180),(0,0,0),2)
		cv2.line(frame,(320,170),(320,190),(0,0,0),2)

		if cx < 240 or cx > 400:
			cv2.line(frame,(240,0),(240,360),(0,0,0),1)
			cv2.line(frame,(400,0),(400,360),(0,0,0),1)
		else:
			cv2.line(frame,(240,0),(240,360),(0,255,0),1)
			cv2.line(frame,(400,0),(400,360),(0,255,0),1)
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
			dy = cy - 180.0
			dx = cx - 320.0
			theta = math.atan(dy/dx)
			theta *= 180.0/math.pi
			theta = int(theta)
			dia = int(r*2)
			movement = 0
			direction = "Down"
			if cx < 250:
				direction = "Left"
				drone.move(-0.05,0.0, 0.0,0.0)
				#time.sleep(0.3)
				#drone.stop()
				#time.sleep(0.3)
			elif cx > 390:
				direction = "Right"
				drone.move(0.05,0.0, 0.0,0.0)
				#time.sleep(0.3)
				#drone.stop()
				#time.sleep(0.3)
			else:
				direction = "Down"
				drone.move(0.0,0.0, -1.0,0.0)
				#time.sleep(0.3)
				print "Alt: " + str(alt)
				if alt < 25:
					print "Landing..."
				 	drone.land()
				  	sys.exit()
			cv2.rectangle(frame,(cx+75,cy-15),(cx+280,cy+135),(255,255,255),-1)
			cv2.putText(frame,"Angle: " + str(theta), (cx+85,cy+90), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
			cv2.putText(frame,"Diameter: " + str(dia), (cx+85,cy+70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
			cv2.putText(frame,"From Center: " + str(c), (cx+85,cy+50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
			cv2.putText(frame,"X: " + str(cx), (cx+85,cy+30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
			cv2.putText(frame,"Y: " + str(cy), (cx+165,cy+30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
			cv2.putText(frame,"Centered: " + str(centered), (cx+85,cy+10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
			cv2.putText(frame,"Move: " + direction, (cx+85,cy+110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, 0)
			try:
				cv2.circle(frame, (cx, cy), r, (0, 255, 0), 4)
			except:
				pass

		except:
			pass
	else:
		drone.hover()
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(5, show_frame)

#def find_blobs():

def basic_movements():
	drone.move(0.0,0.1, 0.0,0.0)
	time.sleep(2)
	drone.stop()
	time.sleep(2)
	drone.move(0.1,0.0, 0.0,0.0)
	time.sleep(2)
	drone.stop()
	time.sleep(2)
	drone.move(0.0,-0.1, 0.0,0.0)
	time.sleep(2)
	drone.stop()
	time.sleep(2)
	drone.move(-0.1,0.0, 0.0,0.0)
	time.sleep(2)
	drone.stop()
	time.sleep(2)

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
	try:
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray,(25,25),0)
		circles = cv2.HoughCircles(gray, cv2.cv.CV_HOUGH_GRADIENT,1,20,param1=30,param2=30,minRadius=15,maxRadius=500)
		nx = 0
		ny = 0
		if circles is not None:
			circles = np.round(circles[0, :]).astype("int")
			bestRed = 0
			bestX = 0
			bestY = 0
			bestR = 0
			for (x, y, r) in circles:		
				try:
					redTotal = 0
					if y - 10 > 0 and y - 10 < 320 and x - 10 > 0 and x - 10 < 640:
						roi = img[y-10:y+10, x-10:x+10]
					else:
						pass
					h, w = roi.shape[:2]
					for x1 in range(0,w):
						for y1 in range(0,h):
							if roi[x1,y1][0] < 80 and roi[x1,y1][1] < 70:
								redTotal = redTotal + roi[x1,y1][2]
					if redTotal > bestRed:
						bestRed = redTotal
						bestX = x
						bestY = y
						bestR = r
				except:
					return -1,-1,-1,-1
			if bestRed > 5000:
						return bestRed,bestX,bestY,bestR
			else:
				return -1,-1,-1,-1
		else:
			return -1,-1,-1,-1
	except:
		return -1,-1,-1,-1
	# img = cv2.GaussianBlur(img,(5,5),0)
	# #img = cv2.medianBlur(frame,15)
	# #img = cv2.dilate(img, np.ones((25, 25)))
	# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	# lower_range = np.array([0, 100, 100], dtype=np.uint8)
	# upper_range = np.array([8, 255, 255], dtype=np.uint8)
	# #lower_range = np.array([150, 100, 50], dtype=np.uint8)
	# #upper_range = np.array([255, 255, 255], dtype=np.uint8)
	# img = cv2.inRange(hsv, lower_range, upper_range)
	
	# contours,hierarchy = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	# max_area = 0
	# best_cnt = 0
	# angle = 0
	# for cnt in contours:
	# 	area = cv2.contourArea(cnt)
	# 	if area > max_area:
	# 		max_area = area
	# 		best_cnt = cnt
	# if max_area > 250:
	# 	try:
	# 		M = cv2.moments(best_cnt)
	# 		cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
	# 		return max_area,cx,cy
	# 	except:
	# 		return -1,-1,-1
	# else:
	# 	return -1,-1,-1

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