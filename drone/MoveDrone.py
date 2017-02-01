import time, sys
import ps_drone                                                # Import PS-Drone

drone = ps_drone.Drone()                                       # Start using drone
drone.startup()                                                # Connects to drone and starts subprocesses

drone.reset() 
drone.trim()                                                 # Sets the drone's status to good (LEDs turn green when red)
while (drone.getBattery()[0] == - 1):   time.sleep(0.1)        # Wait until the drone has done its reset
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])    # Gives a battery-status
drone.useDemoMode(True)                                        # Just give me 15 basic dataset per second (is default anyway)
drone.getNDpackage(["demo"])                   # Packets, which shall be decoded
time.sleep(0.5)                                                # Give it some time to awake fully after reset

##### Mainprogram begin #####
# Setting up detection...
# Shell-Tag=1, Roundel=2, Black Roundel=4, Stripe=8, Cap=16, Shell-Tag V2=32, Tower Side=64, Oriented Roundel=128
drone.setConfig("detect:detect_type", "3")                     # Enable universal detection
drone.setConfig("detect:detections_select_h", "0")           # Detect "Oriented Roundel" with front-camera
drone.setConfig("detect:detections_select_v", "128")             # No detection with ground cam
#The above configuration must be 128 or 0
#drone.setConfigAllID()                              # Go to multiconfiguration-mode
#drone.sdVideo()                                     # Choose lower resolution (try hdVideo())

Kp = 1
Ki = 1
Kd = 1
lastXError = 0.001
lastXTime = 1.0
errorXSum = 0.001
lastYError = 0.001
lastYTime = 1.0
errorYSum = 0.001
xOutput = 0.0
yOutput = 0.0

#drone.groundCam()                                    # Choose front view
CDC = drone.ConfigDataCount
                                # Display the video
while CDC == drone.ConfigDataCount:    time.sleep(0.01)        # Wait until configuration has been set

drone.takeoff()
time.sleep(5)

def XPID(xSpeed):
	global Kp
	global Ki
	global Kd
	global lastXTime
	global lastXError
	global errorXSum
	global xOutput
	now = time.localtime()
	now = float(now[5])
	timeChange = (float)(now-lastXTime)
	if timeChange > 1:
		error = 0 - xSpeed
		errorXSum += error*timeChange
		dError = (error-lastXError)/timeChange
		output = Kp*error + Ki*errorXSum + Kd*dError
		lastXError = error
		lastXTime = now
		xOutput = output
		return output
	else:
		return xOutput

def YPID(ySpeed):
	global Kp
	global Ki
	global Kd
	global lastYTime
	global lastYError
	global errorYSum
	global yOutput
	now = time.localtime()
	now = now[5]
	timeChange = (float)(now-lastYTime)
	if timeChange > 1:
		error = 0 - ySpeed
		errorYSum += error*timeChange
		dError = (error-lastYError)/timeChange
		output = Kp*error + Ki*errorYSum + Kd*dError
		lastYError = error
		lastYTime = now
		yOutput = output
		return output
	else:
		return yOutput

while True:
	key = drone.getKey()
	if key == " ":
		drone.land()
	xSpeed = drone.NavData["demo"][4][0]
	ySpeed = drone.NavData["demo"][4][1]
	xOut = XPID(xSpeed)
	yOut = YPID(ySpeed)
	drone.move(xOut,yOut,0.0,0.0)