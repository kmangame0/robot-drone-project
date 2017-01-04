import time, sys
import ps_drone 
import cv2                                             # Import PS-Drone

drone = ps_drone.Drone()                                     # Start using drone
drone.startup()                                              # Connects to drone and starts subprocesses

drone.reset()                                                # Sets drone's status to good (LEDs turn green when red)
while (drone.getBattery()[0] == -1):      time.sleep(0.1)    # Waits until drone has done its reset
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])	# Gives a battery-status
drone.useDemoMode(True)                                      # Just give me 15 basic dataset per second (is default anyway)

##### Mainprogram begin #####
drone.setConfigAllID()                                       # Go to multiconfiguration-mode
drone.sdVideo()                                              # Choose lower resolution (hdVideo() for...well, guess it)
drone.groundCam()                                             # Choose front view
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001) # Wait until it is done (after resync is done)
drone.startVideo()                                           # Start video-function
drone.showVideo()                                            # Display the video

##### And action !
print "Use <space> to toggle front- and groundcamera, any other key to stop"
IMC =    drone.VideoImageCount
                             # Number of encoded videoframes
stop =   False
ground = True

while not stop:
    while drone.VideoImageCount == IMC: time.sleep(0.01)     # Wait until the next video-frame
    IMC = drone.VideoImageCount
    key = drone.getKey()                                     # Gets a pressed key
    if key==" ":
	img = drone.VideoImage	
        drone.groundVideo(True) 
	picName = 'red.png'
	cv2.imwrite(picName, img)  
 	exit(0)  
                         # Toggle between front- and groundcamera. Hint: options work for all videocommands
    elif key and key != " ":    stop =   True
