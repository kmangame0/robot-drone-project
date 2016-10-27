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
time.sleep(2)

"""
drone.moveForward()
time.sleep(2)
"""
land = False
drone.stop
time.sleep(4) # Stop for 10 seconds in order to acquire data

while land == False:
    drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"])       # Info needed
    #print "Altitude [X,Y,Z] :            "+str(drone.NavData["demo"][3])
    #print "Altitude [X,Y,Z] :            "+str(drone.NavData["demo"][3])
    alt = drone.NavData["demo"][3]
    if alt > 40 and land == False:
        if land == False:
            drone.moveDown(5)
            time.sleep(1)
        if land == False:
            drone.hover()
    else:
        land = True
        drone.land()
        exit(0)

