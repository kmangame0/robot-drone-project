import time, sys
import ps_drone
from PIL import Image

drone = ps_drone.Drone()
drone.startup()

drone.reset()
while (drone.getBattery()[0] == -1):      time.sleep(0.1)
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])
drone.useDemoMode(True)

##### Mainprogram begin #####
drone.setConfigAllID()
drone.sdVideo()
drone.groundCam()
drone.videoFPS(5)
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001)
drone.startVideo()
drone.showVideo()

IMC =    drone.VideoImageCount
stop =   False
ground = True
takeOff = True

x = time.localtime()
xSeconds = x[5]
while not stop:
    y = time.localtime()
    ySeconds = y[5]
    if ySeconds - xSeconds > 20:
        drone.land()
        exit(0)
    while drone.VideoImageCount == IMC: time.sleep(0.01)
    IMC = drone.VideoImageCount
    try:
        img = Image.open('img.png')
        if takeOff == True:
            takeOff = False
            drone.takeoff()
            time.sleep(10)
    except:
        print "Error"
    
