import time, sys
import ps_drone

def run():
    drone = ps_drone.Drone()                                                      # Start using drone                   
    drone.startup()
    drone.reset()

    while (drone.getBattery()[0] == -1):  time.sleep(0.1)                         # Wait the drone
    print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]) # Gives a battery-status
    drone.useDemoMode(False)
    time.sleep(.5)
    drone.setSpeed(0.1)

    time.sleep(12)
    drone.takeoff()
    time.sleep(10)

    drone.hover()
    time.sleep(1)

    drone.moveRight()
    time.sleep(1)
    drone.stop()

    drone.moveDown(1)
    time.sleep(3)
    

    drone.land()


