import time, sys
import ps_drone                                                               # Import PS-Drone-API
import zbar
from Pillow import Image

drone = ps_drone.Drone()                                                      # Start using drone                   
drone.startup()                                                               # Connects to drone and starts subprocesses

# Start main

drone.reset()
# Prepare the drone
drone.setSpeed(0.1)            # Sets default moving speed to 1.0 (=100%)
while (drone.getBattery()[0] == -1):  time.sleep(0.1)                         # Wait the drone
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]) # Gives a battery-status
drone.useDemoMode(False)
drone.takeoff()
time.sleep(2)
drone.hover()
time.sleep(10)

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
drone.stop


while land == False:
    drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"])       # Info needed
    #print "Altitude [X,Y,Z] :            "+str(drone.NavData["demo"][3])
    #print "Altitude [X,Y,Z] :            "+str(drone.NavData["demo"][3])
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
    if key==" ":
        print "Yes"
    elif key and key != " ":    stop =   True
    try:
        img = Image.open('img.png')
        if takeOff == True:
            takeOff = False
            drone.takeoff()
            drone.hover()
                        
        width, height = img.size
        curx = width/2
        cury = height/2
        scanner = zbar.ImageScanner()
        scanner.parse_config('enable')
        pil = Image.open('img.png').convert('L')
        raw = pil.tostring()
        image = zbar.Image(width, height, 'Y800', raw)
        scanner.scan(image)
        for symbol in image:
            print 'decoded', symbol.type, 'symbol', '"%s"' % symbol.data
        try:
            sym = iter(image).next()
            print sym.location
            qrx = sym.location[0][0]
            qry = sym.location[0][1]
            xseparation = curx - qrx
            yseparation = cury - qry

            if xseparation > 0 and yseparation > 0:
                    print "Top Left"
                    drone.moveDown()
                    drone.land()
            elif xseparation < 0 and yseparation > 0:
                    print "Top Right"
                    drone.moveLeft() 
            elif xseparation > 0 and yseparation < 0:
                    print "Bottom Left"
                    drone.moveForward()
            elif xseparation < 0 and yseparation < 0:
                    print "Bottom Right"
                    drone.moveForward()
                    drone.moveLeft()
        except:
                print "Can't get location"
    except:
        print "I don't know what to do."


    
    if alt > 50 and land == False:
        if land == False:
            drone.moveDown(150)
            time.sleep(0.3)
        if land == False:
            drone.hover()
    else:
        land = True
        drone.land()
        exit(0)

