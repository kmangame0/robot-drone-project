import time
import ps_drone                # Imports the PS-Drone-API

drone = ps_drone.Drone()       # Initializes the PS-Drone-API
drone.startup()                # Connects to the drone and starts subprocesses

drone.takeoff()                # Drone starts
time.sleep(7.5)                # Gives the drone time to start

##drone.moveForward()            # Drone flies forward...
##time.sleep(2)                  # ... for two seconds
##drone.stop()                   # Drone stops...
##time.sleep(2)                  # ... needs, like a car, time to stop
##
##drone.moveBackward(0.25)       # Drone flies backward with a quarter speed...
##time.sleep(1.5)                # ... for one and a half seconds
##drone.stop()                   # Drone stops
##time.sleep(2)	

drone.setSpeed(0.1)            # Sets default moving speed to 1.0 (=100%)
print drone.setSpeed()         # Shows the default moving speed

##drone.turnLeft()               # Drone moves full speed to the left...
##time.sleep(2)                  # ... for two seconds
##drone.stop()                   # Drone stops
##time.sleep(2)
time.sleep(10)
drone.land()                   # Drone lands
