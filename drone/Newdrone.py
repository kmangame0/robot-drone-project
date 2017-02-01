import cv2, time, ps_drone, math, sys
import numpy as numpy
from PIL import Image, ImageTk

drone = ps_drone.Drone()
IMC =    drone.VideoImageCount 
drone.startup()                                              
drone.reset()   
drone.trim()
time.sleep(2) 

centered = False
average = 0
counter = 0    
prevAngle = 0
landed = False

def loop():
	global IMC
	global counter
	global average
	global centered
	global prevAngle
	global landed

	while landed == False:
		while drone.VideoImageCount == IMC: 
			time.sleep(0.01)
		IMC = drone.VideoImageCount
		frame = drone.VideoImage
		alt = drone.NavData["demo"][3]
		cx = 0
		cy = 0
		r = 0
		area = 0

		area, x , y, radius = circle_detect(frame)

		if x != -1

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
	drone.startVideo()                                           
	drone.getNDpackage(["demo"])
	loop()


