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
time.sleep(12)
forward = True
land = False
drone.setSpeed(0.2) 
time.sleep(0.5)
drone.hover()
time.sleep(1)

drone.moveLeft()
time.sleep(1)
drone.stop()
time.sleep(2)

drone.moveForward()
time.sleep(1)
drone.stop()
time.sleep(2)

drone.moveRight()
time.sleep(1)
drone.stop()
time.sleep(2)

drone.moveBackward()
time.sleep(1)
drone.stop()
time.sleep(2)

drone.moveLeft()
time.sleep(1)
drone.stop()
time.sleep(2)


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
        land = True
        drone.land()
        exit(0)
        
