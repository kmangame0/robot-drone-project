import time, sys
import ps_drone                                                               # Import PS-Drone-API
import zbar
from PIL import Image

drone = ps_drone.Drone()                                                      # Start using drone                   
drone.startup()                                                               # Connects to drone and starts subprocesses

# Start main

drone.reset()
# Prepare the drone
drone.setSpeed(0.1)            # Sets default moving speed to 1.0 (=100%)
while (drone.getBattery()[0] == -1):  time.sleep(0.1)                         # Wait the drone
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]) # Gives a battery-status
drone.useDemoMode(False)
##### Mainprogram begin #####
drone.setConfigAllID()                                       # Go to multiconfiguration-mode
drone.sdVideo()                                              # Choose lower resolution (hdVideo() for...well, guess it)                                            # Choose front view
drone.videoFPS(5)
#drone.midVideo()
ground = True
drone.groundVideo(ground)
CDC = drone.ConfigDataCount
while CDC == drone.ConfigDataCount:       time.sleep(0.0001) # Wait until it is done (after resync is done)
drone.startVideo()                                           # Start video-function
drone.showVideo()                                            # Display the video
##### And action !
IMC =    drone.VideoImageCount                               # Number of encoded videoframes
stop =   False
NDC = drone.NavDataCount
movement = True
takeOff = True
##drone.takeoff()
##time.sleep(2)
##drone.hover()
##time.sleep(10)

##
##drone.moveForward()            # Drone flies forward...
##time.sleep(2)                  # ... for two seconds
##drone.stop()                   # Drone stops...
##time.sleep(1)
##drone.hover()
##time.sleep(1)
####
##drone.moveRight()       
##time.sleep(1)                
##drone.stop()                   
##time.sleep(1)
####
##drone.moveBackward()       
##time.sleep(4)                
##drone.stop()                   
##time.sleep(2)	
####
##drone.moveLeft()       
##time.sleep(1)                
##drone.stop()                   
##time.sleep(1)
####
##
##drone.moveForward()            # Drone flies forward...
##time.sleep(2)                  # ... for two seconds
##drone.stop()                   # Drone stops...
##time.sleep(1)
##drone.hover()
##time.sleep(1)
##drone.hover()
##time.sleep(1)

"""
drone.moveForward()
time.sleep(2)
"""
land = False
done = True

while land == False:
    ground = True
    drone.groundVideo(ground)
    drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"])       # Info needed
    #print "Altitude [X,Y,Z] :            "+str(drone.NavData["demo"][3])
    #print "Altitude [X,Y,Z] :            "+str(drone.NavData["demo"][3])
    print "Here"
    alt = drone.NavData["demo"][3]
##    x = drone.NavData["demo"][4][0]
##    y = drone.NavData["demo"][4][1]
##    z = drone.NavData["demo"][4][2]
##    print "x: " + str(x)
##    print "y: " + str(y)
##    print "z: " + str(z)
    ##yaw = drone.NavData["demo"][2][2]
   ## print str(yaw)
##    if drone.NavData["demo"][2][2] <10:
##        drone.turnAngle(2,0.5)
##    if drone.NavData["demo"][2][2] >10:
##        drone.turnAngle(-2,0.5)

    while drone.VideoImageCount == IMC: time.sleep(0.01)     # Wait until the next video-frame
    IMC = drone.VideoImageCount
    key = drone.getKey()                                     # Gets a pressed key
##    if key==" ":
##        print "Yes"
##    elif key and key != " ":    stop =   True
    try:
        ground = True
        drone.groundVideo(ground)
        print "Here2"
        if done == True:
            done = False
            img = Image.open('img.png')
            if takeOff == True:
                takeOff = False
                drone.takeoff()
                drone.hover()
                time.sleep(15)
        if alt > 25 and land == False:
            if land == False:
                drone.moveDown(150)
                time.sleep(0.3)
            if land == False:
                drone.hover()
        else:            
            print "Here3"                
            width, height = img.size
            curx = width/2
            cury = height/2
            print "Here4"
            scanner = zbar.ImageScanner()
            scanner.parse_config('enable')
            pil = Image.open('img.png').convert('L')
            raw = pil.tostring()
            image = zbar.Image(width, height, 'Y800', raw)
            scanner.scan(image)
            print "Here5"
            for symbol in image:
                print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
            try:
                print "Here6"
                sym = iter(image).next()
                print sym.location
                qrx = sym.location[0][0]
                qry = sym.location[0][1]
                xseparation = curx - qrx
                yseparation = cury - qry
                print "Here7"
                if xseparation > 0 and yseparation > 0:
                    print "Top Left"              
                    if alt > 40 and land == False:
                        if land == False:
                            drone.moveDown(150)
                            time.sleep(0.3)
                        if land == False:
                            drone.hover()
                    else:
                        land = True
                        drone.land()
                        exit(0)
                elif xseparation < 0 and yseparation > 0:
                        print "Top Right"
                        drone.moveLeft() 
                elif xseparation > 0 and yseparation < 0:
                        print "Bottom Left"
                        drone.moveForward()
                elif xseparation < 0 and yseparation < 0:
                        print "Bottom Right"
                        drone.moveForward()
                        time.sleep(0.3)
                        drone.moveLeft()
                done = True
            except:
                    print "Can't get location"
    except:
        print "I don't know what to do."
        ground = True
        drone.groundVideo(ground)
