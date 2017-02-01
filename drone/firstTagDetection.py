import time, sys
import ps_drone                                                # Import PS-Drone

drone = ps_drone.Drone()                                       # Start using drone
drone.startup()                                                # Connects to drone and starts subprocesses

drone.reset()                                                  # Sets the drone's status to good (LEDs turn green when red)
while (drone.getBattery()[0] == - 1):   time.sleep(0.1)        # Wait until the drone has done its reset
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1])    # Gives a battery-status
drone.useDemoMode(False)                                        # Just give me 15 basic dataset per second (is default anyway)
drone.getNDpackage(["demo","vision_detect"])                   # Packets, which shall be decoded
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
#drone.groundCam()                                    # Choose front view
CDC = drone.ConfigDataCount
                                # Display the video
while CDC == drone.ConfigDataCount:    time.sleep(0.01)        # Wait until configuration has been set
#drone.startVideo()                                  # Start video-function
#drone.showVideo()                                   # Display the video
# Get detections
print "Taking off..."
time.sleep(1)
#drone.takeoff()
time.sleep(10)
#drone.setSpeed(0.1)
print "Ready..."
stop = False
#IMC =    drone.VideoImageCount # Number of encoded videoframes
quad = 0
prevX = 0
prevY = 0
while not stop:
    #while drone.VideoImageCount==IMC: time.sleep(0.01) # Wait until the next video-frame
    #IMC = drone.VideoImageCount
    NDC = drone.NavDataCount
    while NDC == drone.NavDataCount:   time.sleep(0.01)
    if drone.getKey():                 stop = True
    # Loop ends when key was pressed
    tagNum = drone.NavData["vision_detect"][0]                 # Number of found tags
    tagX =   drone.NavData["vision_detect"][2]                 # Horizontal position(s)
    tagY =   drone.NavData["vision_detect"][3]                 # Vertical position(s)
    tagZ =   drone.NavData["vision_detect"][6]                 # Distance(s)
    tagRot = drone.NavData["vision_detect"][7]
    alt = drone.NavData["demo"][3]
    print "tagX: " + str(tagX)
    print "tagY: " + str(tagY)
    # if tagNum:
    #     if abs(420 - tagX[0]) < 150 and abs(320 - tagY[0]) < 150:
    #         quad = 5
    #         #drone.moveDown(1.0)
    #         time.sleep(0.50)
    #         if tagZ[0] < 50:
    #             print "Landing"
    #             #drone.land()
    #     else:    
    #         if 420 - tagX[0] > 0 and 320 - tagY[0] > 0:
    #             #drone.relMove(0.01,0.01, 0.0,0.0,0.0,0.0)
    #             quad = 1
    #         elif 420 - tagX[0] < 0 and 320 - tagY[0] > 0:
    #             #drone.relMove(-0.01,0.01, 0.0,0.0,0.0,0.0)
    #             quad = 2
    #         elif 420 - tagX[0] > 0 and 320 - tagY[0] < 0:
    #             #drone.relMove(-0.01,-0.01, 0.0,0.0,0.0,0.0)
    #             quad = 3
    #         elif 420 - tagX[0]  < 0 and 320 - tagY[0] < 0:
    #             #drone.relMove(0.01,-0.01, 0.0,0.0,0.0,0.0)
    #             quad = 4
    #     prevX = tagX[0]
    #     prevY = tagY[0]
    # else:
    #     #drone.hover()
    #     if quad == 5 and alt > 40:
    #         #drone.moveDown(1.0)
    #         time.sleep(0.50)
    #         if tagZ[0] < 50:
    #             print "Landing"
    #             #drone.land()
    #     else: 
    #         #drone.land()
    #         pass
    #     if quad == 1:
    #         #drone.relMove(0.01,-0.01, 0.0,0.0,0.0,0.0)
    #     elif quad == 2:
    #         #drone.relMove(-0.01,-0.01, 0.0,0.0,0.0,0.0)
    #     elif quad == 3:
    #         #drone.relMove(-0.01,0.01, 0.0,0.0,0.0,0.0)
    #     elif quad == 4:
    #         #drone.relMove(0.01,0.01, 0.0,0.0,0.0,0.0)





    # Show detections
    #if tagNum:
        #for i in range (0,tagNum):
            #print "Tag no "+str(i)+" : X= "+str(tagX[i])+"  Y= "+str(tagY[i])+"  Dist= "+str(tagZ[i])+"  Orientation= "+str(tagRot[i])
    #else:   #print "No tag detected"
