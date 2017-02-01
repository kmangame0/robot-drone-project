# -*- coding: utf-8 -*-
import Tkinter as tk
import cv2, time, ps_drone
import numpy as np
from PIL import Image, ImageTk
import math
import sys
import time

prevError = 0
lastTime = 0
prevCX = 0
prevCY = 0
lastKnownQuad = -1
circleDetected = False
def basic_movements():
	move = True
	xPos = 0.0
	yPos = 0.25
	while(move == True):
		for i in range(0,5):
			xPos = xPos + 0.05
			yPos = yPos - 0.05
			drone.move(xPos,yPos,0.0,0.0)
			time.sleep(.1)
			#x: .5
			#y: 0.0
		for i in range(0,5):
			xPos = xPos - 0.05
			yPos = yPos - 0.05
			drone.move(xPos,yPos,0.0,0.0)
			time.sleep(.1)
			#x: 0.0
			#y: -.5
		for i in range(0,5):
			xPos = xPos - 0.05
			yPos = yPos + 0.05
			drone.move(xPos,yPos,0.0,0.0)
			time.sleep(.19)
			#x: -.5
			#y: 0.0
		for i in range(0,5):
			xPos = xPos + 0.05
			yPos = yPos + 0.05
			drone.move(xPos,yPos,0.0,0.0)
			time.sleep(.22)
		move = False
		print "Done!"
		drone.hover()
		time.sleep(1)

def setup(drone):
	drone.startup()                                              
	drone.reset()   
	drone.trim()
	time.sleep(2)                                             
	while (drone.getBattery()[0] == -1):      time.sleep(0.1)    
	print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	
	drone.useDemoMode(True)  
	drone.setConfigAllID()                                       
	drone.sdVideo()                                              
	drone.groundCam()
	CDC = drone.ConfigDataCount
	while CDC == drone.ConfigDataCount:       time.sleep(0.0001) 
	print "Taking off..."
	drone.takeoff()
	time.sleep(5)
	drone.hover()
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
centeredOverRedCircle = True
landing = False

def show_frame():
	global lmain
	global IMC
	global counter
	global average
	global centered
	global prevAngle
	global centeredOverRedCircle
	global landing
	while drone.VideoImageCount == IMC: 
		time.sleep(0.01)
	IMC = drone.VideoImageCount
	key = drone.getKey()
	frame = drone.VideoImage
	img = frame

	move(frame,img)
	cv2.rectangle(frame,(160,90),(480,270),(255,255,255),2)
	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(5, show_frame)

def move(frame,img):
	global landing
	global prevCX
	global prevCY
	global lastKnownQuad
	global circleDetected
	cx = 0
	cy = 0
	r = 0
	area = 0

	area, cx,cy,r = find_contours(frame,img)
	try:
		cv2.circle(frame, (cx, cy), 1, (0, 255, 0), 4)
	except:
		pass
	if landing == False:
		alt = drone.NavData["demo"][3]
		print "CX: " + str(cx)
		print "CY: " + str(cy)
		print "Area: " + str(area)
		if cx > 160 and cx < 480 and cy > 90 and cy < 270:
			print "In center"
			drone.move(0.0,0.0,-0.25,0.0)
			time.sleep(.25)
			if area > 50000 and alt < 35:
				#Also check if alt is less than 35 when flying
				landing = True
				drone.land()
				print "landing"

		elif cx < 320 and cx > 0 and cy < 180 and cy > 0:
			cx = 320 - cx
			cy = 160 - cy
			fx = -0.025*cx/320.0
			fy = 0.025*cy/160.0
			drone.move(fx,fy,0.0,0.0)
			prevCX = cx
			prevCY = cy
			lastKnownQuad = 1
			print "Q1"

		elif cx > 320 and cx < 640 and cy < 180 and cy > 0:
			cx = cx - 320
			cy = 160 - cy
			fx = 0.025*cx/320.0
			fy = 0.025*cy/160.0
			drone.move(fx,fy,0.0,0.0)
			prevCX = cx
			prevCY = cy
			lastKnownQuad = 2
			print "Q2"
		elif cx < 320 and cx > 0 and cy < 360 and cy > 180:
			cx = 320-cx
			cy = cy - 160
			fx = -0.025*cx/320.0
			fy = -0.025*cy/160.0
			drone.move(fx,fy,0.0,0.0)
			prevCX = cx
			prevCY = cy
			lastKnownQuad = 3
			print "Q3"
		elif cx > 320 and cx < 640 and cy < 360 and cy > 180:
			cx = cx - 320
			cy = cy - 160
			fx = 0.025*cx/320.0
			fy = -0.025*cy/160.0
			drone.move(fx,fy,0.0,0.0)
			prevCX = cx
			prevCY = cy
			lastKnownQuad = 4
			print "Q4"
		else:
			print "Not found - Rise!"
			drone.move(0.0,0.0,0.1,0.0)
			time.sleep(.25)

def find_contours(frame,img):
	global circleDetected
	img = cv2.GaussianBlur(img,(25,25),0)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower_range = np.array([125, 50, 50], dtype=np.uint8)
	upper_range = np.array([255, 255, 255], dtype=np.uint8)
	img = cv2.inRange(hsv, lower_range, upper_range)
	contours,hierarchy = cv2.findContours(img,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
	max_area = 0
	best_cnt = 0
	for cnt in contours:
		area = cv2.contourArea(cnt)
		if area > max_area:
			max_area = area
			best_cnt = cnt
	if max_area > 250:
		try:
			M = cv2.moments(best_cnt)
			cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
			circleDetected = True
			print "Area inside find_Contours: " + str(max_area) 
			return max_area,cx,cy,-1
		except:
			return -1,-1,-1,-1
	else:
		return -1,-1,-1,-1

show_frame()
root.mainloop()