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

def Movement():
    landed = False
    NDC =   drone.NavDataCount
    while landed == False:
        #while drone.NavDataCount==NDC:      time.sleep(0.001)
        #print landed
        #try:
        alt = 151
        print "Here"
        if drone.NavDataCount-NDC <1:
              print "Lost "+str(drone.NavDataCount-NDC-1)+" NavData"
        else:
            drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"])
            #try:
            
            alt = drone.NavData["altitude"][3]
            print "Altitude: "+str(drone.NavData["altitude"][3])
            #except:
               
            if alt > 350 : ##Altitude in cm
                #try:
                drone.moveDown(10)
                drone.hover()
                #except:
            else:
                landed = True
                drone.land()
                exit(0)
            #except:
                #print "Corrupt Data"
                #continue
        NDC = drone.NavDataCount
        print "Here2"

Movement()

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
