import time, sys, ps_drone 

drone = ps_drone.Drone()                                                                   
drone.startup()                                                              
drone.reset() 
                                                                
while (drone.getBattery()[0] == -1):  time.sleep(0.1)                         
print "Battery: "+str(drone.getBattery()[0])+"%  "+str(drone.getBattery()[1]) 
drone.useDemoMode(False)
drone.takeoff()
time.sleep(10)
land = False
time.sleep(4) 

while True:
    drone.getNDpackage(["demo","pressure_raw","altitude","magneto","wifi"])      
    alt = drone.NavData["demo"][3]
    if alt > 40 and land == False:
        drone.moveDown(.1)
        time.sleep(0.1)
        drone.hover()
    else:
        land = True
        drone.land()
        break

exit(0)

