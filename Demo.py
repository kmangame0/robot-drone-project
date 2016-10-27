import time, sys
import ps_drone                                                               # Import PS-Drone-API

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
time.sleep(5)


drone.moveForward()            # Drone flies forward...
time.sleep(2)                  # ... for two seconds
drone.stop()                   # Drone stops...
time.sleep(1)
drone.hover()
time.sleep(1)
##
drone.moveRight()       
time.sleep(1)                
drone.stop()                   
time.sleep(1)
##
drone.moveBackward()       
time.sleep(4)                
drone.stop()                   
time.sleep(2)	
##
drone.moveLeft()       
time.sleep(1)                
drone.stop()                   
time.sleep(1)
##

drone.moveForward()            # Drone flies forward...
time.sleep(2)                  # ... for two seconds
drone.stop()                   # Drone stops...
time.sleep(1)
drone.hover()
time.sleep(1)
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

