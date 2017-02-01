# -*- coding: utf-8 -*-
import Tkinter as tk
import cv2, time, ps_drone
import numpy as np
from PIL import Image, ImageTk
import math
import sys

def basic_movements():
	# print "up"
	# drone.move(0.0,0.0,0.1,0.0)
	# time.sleep(.3)
	# print "forward"
	# drone.move(0.0,0.05, 0.0,0.0)
	# time.sleep(2)
	# drone.hover()
	# time.sleep(2)
	# drone.move(0.05,0.0, 0.0,0.0)
	# print "right"
	# time.sleep(2)
	# drone.hover()
	# time.sleep(2)
	# drone.move(0.0,-0.05, 0.0,0.0)
	# print "backward"
	# time.sleep(2)
	# drone.hover()
	# time.sleep(2)
	# drone.move(-0.05,0.0, 0.0,0.0)
	print "left"
	time.sleep(1)
	drone.hover()
	time.sleep(2)
	

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

	cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
	img = Image.fromarray(cv2image)
	imgtk = ImageTk.PhotoImage(image=img)
	lmain.imgtk = imgtk
	lmain.configure(image=imgtk)
	lmain.after(5, show_frame)

def move(frame,img):
	global landing
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
		if cx > 160 and cx < 480 and cy > 90 and cy < 270 and area > 5000:
			print "In center"
			drone.move(0.0,0.0,-0.5,0.0)
			if area > 75000 and alt < 30:
				#Also check if alt is less than 30 when flying
				landing = True
				drone.land()
				print "landing"

		elif cx < 320 and cx > 0 and cy < 180 and cy > 0:
			cx = 320 - cx
			cy = 160 - cy
			fx = -0.01*cx/320.0
			fy = 0.01*cy/160.0
			drone.move(fx,fy,0.0,0.0)
			print "Q1"

		elif cx > 320 and cx < 640 and cy < 180 and cy > 0:
			cx = cx - 320
			cy = 160 - cy
			fx = 0.01*cx/320.0
			fy = 0.01*cy/160.0
			drone.move(fx,fy,0.0,0.0)
			print "Q2"
		elif cx < 320 and cx > 0 and cy < 360 and cy > 180:
			cx = 320-cx
			cy = cy - 160
			fx = -0.01*cx/320.0
			fy = -0.01*cy/160.0
			drone.move(fx,fy,0.0,0.0)
			print "Q3"
		elif cx > 320 and cx < 640 and cy < 360 and cy > 180:
			cx = cx - 320
			cy = cy - 160
			fx = 0.01*cx/320.0
			fy = -0.01*cy/160.0
			drone.move(fx,fy,0.0,0.0)
			print "Q4"
		else:
			print "Not found - Rise!"
			drone.move(0.0,0.0,0.1,0.0)
		 	time.sleep(.25)

def find_contours(frame,img):
	img = cv2.GaussianBlur(img,(25,25),0)
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	lower_range = np.array([150, 50, 50], dtype=np.uint8)
	upper_range = np.array([255, 255, 255], dtype=np.uint8)
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
	#print "Max_Area: " + str(max_area)
	if max_area > 250:
		try:
			M = cv2.moments(best_cnt)
			cx,cy = int(M['m10']/M['m00']), int(M['m01']/M['m00'])
			return max_area,cx,cy,-1
		except:
			return -1,-1,-1,-1
	else:
		return -1,-1,-1,-1
    
show_frame()
root.mainloop()