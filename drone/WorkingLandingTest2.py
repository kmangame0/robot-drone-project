import time, sys
import ps_drone                                                               # Import PS-Drone-API

drone = ps_drone.Drone()                                                      # Start using drone                   
drone.startup()                                                               # Connects to drone and starts subprocesses

# Start main

drone.reset()                                                                 # Prepare the drone
while (drone.getBattery()[0] == -1):  time.sleep(0.1)                         # Wait the drone
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]) # Gives a battery-status
drone.useDemoMode(False)
drone.takeoff()
time.sleep(10)
forward = True

land = False
time.sleep(4) # Stop for 10 seconds in order to acquire data

while land == False:
    drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"])       # Info needed
    alt = drone.NavData["demo"][3]
    if alt > 40 and land == False:
        if land == False:
            drone.moveDown(.1)
            time.sleep(0.1)
        if land == False:
            drone.hover()
            time.sleep(0.1)
    else:
        if forward == True:
            drone.moveForward()
            time.sleep(1.5)
            forward = False
            land = True
            drone.hover()
            time.sleep(1)
        else:
            land = True
            drone.land()
            exit(0)
            
##    else:
##        land = True
##        drone.land()
##        exit(0)

