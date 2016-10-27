import time
import ps_drone                # Imports the PS-Drone-API
drone = ps_drone.Drone()       # Initializes the PS-Drone-API
drone.startup()                # Connects to the drone and starts subprocesses
time.sleep(1)
drone.reset()
NDC = drone.NavDataCount
drone.takeoff()                # Drone starts
time.sleep(10)                # Gives the drone time to start

landed = False
drone.setSpeed(0.1)            # Sets default moving speed to 1.0 (=100%)
drone.useDemoMode(False)
##drone.moveForward()            # Drone flies forward...
##time.sleep(1)                  # ... for two seconds
##drone.stop()                   # Drone stops...
##time.sleep(2)                  # ... needs, like a car, time to stop

while landed == False:
    while drone.NavDataCount==NDC:      time.sleep(0.001)
    print landed
    try:
        drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"])
        #print "Altitude: "+str(abs(drone.NavData["altitude"][3]))
        alt = abs(drone.NavData["altitude"][3])
        if alt > 200 : ##Altitude in cm
            drone.moveDown(10)
            drone.hover()
        else:
            landed = True
            drone.land()
    except:
        print "Corrupt Data"
        continue

##
##drone.moveBackward()       
##time.sleep(1)                
##drone.stop()                   
##time.sleep(2)	
##
##drone.moveLeft()       
##time.sleep(1)                
##drone.stop()                   
##time.sleep(2)
##
##drone.moveRight()       
##time.sleep(2)                
##drone.stop()                   
##time.sleep(2)
##
##drone.hover()
##time.sleep(1)

##print drone.setSpeed()         # Shows the default moving speed

##drone.turnLeft()               # Drone moves full speed to the left...
##time.sleep(2)                  # ... for two seconds
##drone.stop()                   # Drone stops
##time.sleep(2)

##drone.land()                   # Drone lands
